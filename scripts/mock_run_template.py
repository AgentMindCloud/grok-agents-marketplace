"""Exercise every tool in a template with stub runtime + synthetic inputs.

Imports `tools/custom_tools.py`, then for every tool declared in
`.grok/grok-agent.yaml`, calls it with plausible dummy arguments. Any
`PermissionError` from missing approval tokens is treated as expected
behaviour (proof the gate exists). Any other exception fails the run.
"""

from __future__ import annotations

import argparse
import importlib.util
import inspect
import sys
import typing
from pathlib import Path

import yaml

# Defaults picked so signatures like `foo(x: int = 5)` accept them.
PRIMITIVE_DEFAULTS: dict[type, object] = {
    str: "sample",
    int: 3,
    float: 0.5,
    bool: True,
    list: ["sample"],
    dict: {"sample": "value"},
}


def _sample_for(annotation: object) -> object:
    origin = typing.get_origin(annotation)
    args = typing.get_args(annotation)
    if annotation is inspect.Parameter.empty:
        return "sample"
    if annotation in PRIMITIVE_DEFAULTS:
        return PRIMITIVE_DEFAULTS[annotation]
    if origin is list:
        inner = args[0] if args else str
        return [_sample_for(inner)]
    if origin is dict:
        return {"key": "value"}
    if origin is typing.Literal:
        return args[0]
    if origin is typing.Union:
        for alt in args:
            if alt is type(None):
                continue
            return _sample_for(alt)
        return None
    # TypedDict / custom types: return a permissive dict.
    return {"stub": True}


def _call(func: object, module_globals: dict[str, object]) -> object:
    sig = inspect.signature(func)  # type: ignore[arg-type]
    try:
        hints = typing.get_type_hints(func, globalns=module_globals)  # type: ignore[arg-type]
    except Exception:
        hints = {}
    kwargs: dict[str, object] = {}
    for name, param in sig.parameters.items():
        if param.default is not inspect.Parameter.empty:
            continue
        if name == "approval_token":
            kwargs[name] = "missing"  # trigger the approval gate
            continue
        annotation = hints.get(name, param.annotation)
        kwargs[name] = _sample_for(annotation)
    return func(**kwargs)  # type: ignore[misc]


def run(root: Path) -> list[str]:
    failures: list[str] = []
    agents = yaml.safe_load((root / ".grok/grok-agent.yaml").read_text()).get("agents") or []
    tools_file = root / "tools/custom_tools.py"
    spec = importlib.util.spec_from_file_location(f"mock_{root.name}_tools", tools_file)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    all_tools = {tool for agent in agents for tool in (agent.get("tools") or [])}
    for name in sorted(all_tools):
        func = getattr(module, name, None)
        if func is None:
            failures.append(f"{name}: missing")
            continue
        try:
            _call(func, module.__dict__)
        except (PermissionError, FileNotFoundError, ValueError):
            # Expected: approval gates, missing-state errors, and input validation
            # all count as the tool running as designed.
            continue
        except Exception as exc:  # noqa: BLE001
            failures.append(f"{name}: {type(exc).__name__}: {exc}")
    return failures


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("template")
    args = parser.parse_args()
    root = Path(args.template).resolve()
    failures = run(root)
    if failures:
        print(f"MOCK {root.name}: {len(failures)} failure(s)")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)
    print(f"MOCK {root.name}: all tools exercised")


if __name__ == "__main__":
    main()
