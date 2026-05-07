"""Structural validation for a single template directory.

Checks:
  - Required files exist.
  - `grok-install.yaml` has required keys and a sane spec version.
  - `.grok/grok-agent.yaml` declares at least one agent with tools.
  - `.grok/grok-security.yaml` declares `safety_profile` and `permissions`.
  - `.grok/grok-prompts.yaml` contains every `prompt_ref` used by agents.
  - `tools/custom_tools.py` imports cleanly and exposes every tool named
    by an agent.
"""

from __future__ import annotations

import argparse
import importlib.util
import sys
from pathlib import Path

import yaml

REQUIRED_FILES = [
    "grok-install.yaml",
    "README.md",
    ".env.example",
    ".grok/grok-agent.yaml",
    ".grok/grok-security.yaml",
    ".grok/grok-prompts.yaml",
    "tools/custom_tools.py",
]

VALID_SAFETY = {"strict", "standard", "permissive"}


class ValidationError(Exception):
    pass


def _load_yaml(path: Path) -> dict:
    try:
        return yaml.safe_load(path.read_text()) or {}
    except yaml.YAMLError as exc:
        raise ValidationError(f"{path}: invalid YAML — {exc}") from exc


def _check_required_files(root: Path) -> None:
    for rel in REQUIRED_FILES:
        if not (root / rel).exists():
            raise ValidationError(f"missing required file: {rel}")


def _check_grok_install(root: Path) -> None:
    data = _load_yaml(root / "grok-install.yaml")
    for key in ("spec", "name", "description", "entrypoint", "model"):
        if key not in data:
            raise ValidationError(f"grok-install.yaml: missing key '{key}'")
    if not str(data["spec"]).startswith("grok-install/v"):
        raise ValidationError(f"grok-install.yaml: bad spec {data['spec']!r}")


def _check_agents(root: Path) -> tuple[list[dict], set[str], set[str]]:
    data = _load_yaml(root / ".grok/grok-agent.yaml")
    agents = data.get("agents") or []
    if not agents:
        raise ValidationError(".grok/grok-agent.yaml: no agents declared")
    tool_names: set[str] = set()
    prompt_refs: set[str] = set()
    for agent in agents:
        for key in ("id", "model", "prompt_ref", "tools"):
            if key not in agent:
                raise ValidationError(f"agent {agent.get('id', '?')}: missing '{key}'")
        prompt_refs.add(agent["prompt_ref"])
        tool_names.update(agent["tools"])
    return agents, tool_names, prompt_refs


def _check_prompts(root: Path, refs: set[str]) -> None:
    data = _load_yaml(root / ".grok/grok-prompts.yaml")
    prompts = data.get("prompts") or {}
    missing = refs - set(prompts)
    if missing:
        raise ValidationError(f"prompts missing for refs: {sorted(missing)}")


def _check_security(root: Path, tool_names: set[str]) -> None:
    data = _load_yaml(root / ".grok/grok-security.yaml")
    if data.get("safety_profile") not in VALID_SAFETY:
        raise ValidationError(f"security: bad safety_profile {data.get('safety_profile')!r}")
    perms = data.get("permissions") or []
    if not perms:
        raise ValidationError("security: permissions list is empty")
    perm_tools = {p.split(":", 1)[1] for p in perms if isinstance(p, str) and p.startswith("tool:")}
    missing = tool_names - perm_tools
    if missing:
        raise ValidationError(f"security: tools used by agents but not permitted: {sorted(missing)}")


def _check_python_tools(root: Path, tool_names: set[str]) -> None:
    path = root / "tools/custom_tools.py"
    spec = importlib.util.spec_from_file_location(f"tpl_{root.name}_tools", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:
        raise ValidationError(f"tools/custom_tools.py: import failed — {exc}") from exc
    missing = [name for name in tool_names if not callable(getattr(module, name, None))]
    if missing:
        raise ValidationError(f"tools/custom_tools.py: missing callables {sorted(missing)}")


def validate(root: Path) -> None:
    _check_required_files(root)
    _check_grok_install(root)
    _, tool_names, prompt_refs = _check_agents(root)
    _check_prompts(root, prompt_refs)
    _check_security(root, tool_names)
    _check_python_tools(root, tool_names)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("template")
    args = parser.parse_args()
    root = Path(args.template).resolve()
    if not root.is_dir():
        print(f"not a directory: {root}", file=sys.stderr)
        sys.exit(2)
    try:
        validate(root)
    except ValidationError as exc:
        print(f"FAIL {root.name}: {exc}", file=sys.stderr)
        sys.exit(1)
    print(f"OK   {root.name}: template valid")


if __name__ == "__main__":
    main()
