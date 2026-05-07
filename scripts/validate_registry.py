"""Validate featured-agents.json against the repo layout."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "featured-agents.json"
TEMPLATES = ROOT / "templates"

REQUIRED_FIELDS = {
    "name",
    "description",
    "path",
    "tags",
    "install_command",
    "safety_profile",
    "certified",
    "poster",
}
VALID_SAFETY = {"strict", "standard", "permissive"}


def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    data = json.loads(REGISTRY.read_text())

    if data.get("version") != "1.0":
        fail("registry version must be '1.0'")

    seen: set[str] = set()
    for agent in data.get("agents", []):
        missing = REQUIRED_FIELDS - agent.keys()
        if missing:
            fail(f"{agent.get('name', '?')}: missing fields {sorted(missing)}")
        name = agent["name"]
        if name in seen:
            fail(f"duplicate agent name: {name}")
        seen.add(name)

        if agent["safety_profile"] not in VALID_SAFETY:
            fail(f"{name}: invalid safety_profile {agent['safety_profile']!r}")

        template_dir = ROOT / agent["path"]
        if not template_dir.is_dir():
            fail(f"{name}: path {agent['path']} does not exist")
        for required in ("grok-install.yaml", "README.md", ".env.example"):
            if not (template_dir / required).exists():
                fail(f"{name}: missing {required}")
        if not (template_dir / ".grok").is_dir():
            fail(f"{name}: missing .grok/ directory")

        poster = ROOT / agent["poster"]
        if not poster.is_file():
            fail(f"{name}: poster {agent['poster']} does not exist")

    listed = {a["name"] for a in data["agents"]}
    on_disk = {p.name for p in TEMPLATES.iterdir() if p.is_dir()}
    orphans = on_disk - listed
    if orphans:
        fail(f"templates on disk but not in registry: {sorted(orphans)}")
    ghosts = listed - on_disk
    if ghosts:
        fail(f"registry entries with no template dir: {sorted(ghosts)}")

    print(f"registry OK: {len(seen)} agents")


if __name__ == "__main__":
    main()
