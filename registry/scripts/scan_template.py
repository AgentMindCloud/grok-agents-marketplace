"""Security scanner for a single template.

Warnings:
  - Any write-capable tool (post_*, publish, send, email, merge, comment)
    that is NOT under `requires_approval`.
  - Templates with any `post_*`/`send_*` tool that declare safety_profile
    below `strict`.
  - `.env.example` containing a value after '=' (possible hardcoded secret).
  - Custom tools file containing obvious hardcoded secret patterns.
  - grok-install.yaml declaring a write-capable tool without a `kill_switch`
    entry in the security config.

Exit 0 if no warnings (or --fail-on never), 1 if warnings and --fail-on
warning. Always prints a summary.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

WRITE_TOOL_PREFIXES = ("post_", "publish_", "send_", "deliver_", "merge_", "comment_")
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"xoxb-[A-Za-z0-9-]{20,}"),
]


def _load(path: Path) -> dict:
    return yaml.safe_load(path.read_text()) or {}


def scan(root: Path) -> list[str]:
    warnings: list[str] = []
    agents = _load(root / ".grok/grok-agent.yaml").get("agents") or []
    security = _load(root / ".grok/grok-security.yaml")

    all_tools = {tool for agent in agents for tool in (agent.get("tools") or [])}
    write_tools = {t for t in all_tools if t.startswith(WRITE_TOOL_PREFIXES)}

    approved = {
        p.split(":", 1)[1]
        for p in (security.get("requires_approval") or [])
        if isinstance(p, str) and p.startswith("tool:")
    }
    unapproved_writes = write_tools - approved
    if unapproved_writes:
        warnings.append(
            f"write-capable tools not under requires_approval: {sorted(unapproved_writes)}"
        )

    if write_tools and security.get("safety_profile") != "strict":
        warnings.append(
            "write-capable tools present but safety_profile is not 'strict'"
        )

    if write_tools and "kill_switch" not in security:
        warnings.append("write-capable tools present but no kill_switch declared")

    env_example = root / ".env.example"
    if env_example.exists():
        for lineno, line in enumerate(env_example.read_text().splitlines(), start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, value = line.split("=", 1)
            # Allow enum-like defaults (0/1) and known non-secret keys.
            if value and value not in {"0", "1"} and not key.endswith(("_DISABLED", "_TO", "_HOST", "_USER")):
                warnings.append(f".env.example:{lineno}: {key} has a non-empty default")

    tools_src = (root / "tools/custom_tools.py").read_text(errors="ignore")
    for pattern in SECRET_PATTERNS:
        if pattern.search(tools_src):
            warnings.append(f"tools/custom_tools.py: matches secret pattern {pattern.pattern}")

    return warnings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("template")
    parser.add_argument("--fail-on", choices=["warning", "never"], default="warning")
    args = parser.parse_args()

    root = Path(args.template).resolve()
    warnings = scan(root)
    if warnings:
        print(f"SCAN {root.name}: {len(warnings)} warning(s)")
        for w in warnings:
            print(f"  - {w}")
        if args.fail_on == "warning":
            sys.exit(1)
    else:
        print(f"SCAN {root.name}: clean")


if __name__ == "__main__":
    main()
