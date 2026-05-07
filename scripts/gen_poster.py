"""Generate an SVG "poster" for every template listed in featured-agents.json.

Each poster is a static 1280x360 card showing the template name, a one-line
description, safety + pattern badges, the agent/tool roster parsed from
`.grok/grok-agent.yaml`, and the install one-liner. They act as placeholders
until real screen recordings exist, and stay useful alongside real gifs.
"""

from __future__ import annotations

import html
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "featured-agents.json"
POSTERS = ROOT / "docs" / "posters"

BG = "#0b0f17"
PANEL = "#121826"
ACCENT = "#7c5cff"
ACCENT_SOFT = "#2a1f55"
TEXT = "#e6e8ef"
MUTED = "#8b93a7"
OK = "#22c55e"
WARN = "#f59e0b"
DANGER = "#ef4444"

SAFETY_COLOR = {"strict": DANGER, "standard": WARN, "permissive": OK}


def pattern_label(agents: list[dict]) -> str:
    n = len(agents)
    if n <= 1:
        return "single-agent"
    if n == 2:
        return "multi-step"
    return "swarm"


def _wrap(text: str, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if len(candidate) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def _badge(x: int, y: int, label: str, fill: str, text_fill: str = "#0b0f17") -> str:
    width = 10 * len(label) + 22
    return (
        f'<g>'
        f'<rect x="{x}" y="{y}" width="{width}" height="26" rx="13" fill="{fill}"/>'
        f'<text x="{x + width / 2}" y="{y + 18}" text-anchor="middle" '
        f'font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-size="12" '
        f'font-weight="700" fill="{text_fill}">{html.escape(label)}</text>'
        f'</g>'
    ), width


def render(agent_meta: dict, agent_yaml: dict) -> str:
    name = agent_meta["name"]
    description = agent_meta["description"]
    safety = agent_meta["safety_profile"]
    install = agent_meta["install_command"]
    agents = agent_yaml.get("agents") or []
    pattern = pattern_label(agents)

    desc_lines = _wrap(description, 78)[:2]

    agent_rows = []
    for a in agents[:4]:
        tools = a.get("tools") or []
        rendered_tools = ", ".join(tools[:4])
        if len(tools) > 4:
            rendered_tools += f", +{len(tools) - 4}"
        agent_rows.append((a.get("id", "?"), rendered_tools))

    header = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1280 360" '
        f'role="img" aria-label="{html.escape(name)} poster">'
        f'<defs>'
        f'<linearGradient id="grad" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="{BG}"/>'
        f'<stop offset="1" stop-color="#1a1030"/>'
        f'</linearGradient>'
        f'</defs>'
        f'<rect width="1280" height="360" fill="url(#grad)"/>'
        f'<rect x="0" y="0" width="6" height="360" fill="{ACCENT}"/>'
    )

    parts = [header]

    parts.append(
        f'<text x="48" y="74" font-family="ui-sans-serif, -apple-system, Segoe UI, Roboto, sans-serif" '
        f'font-size="42" font-weight="800" fill="{TEXT}">{html.escape(name)}</text>'
    )
    parts.append(
        f'<text x="48" y="104" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" '
        f'font-size="14" fill="{ACCENT}">grok-native certified</text>'
    )

    for i, line in enumerate(desc_lines):
        parts.append(
            f'<text x="48" y="{144 + i * 26}" font-family="ui-sans-serif, -apple-system, Segoe UI, sans-serif" '
            f'font-size="18" fill="{MUTED}">{html.escape(line)}</text>'
        )

    badge_x = 48
    badge_y = 210
    for label, fill in (
        (f"safety: {safety}", SAFETY_COLOR.get(safety, MUTED)),
        (f"pattern: {pattern}", ACCENT),
        (f"agents: {len(agents)}", PANEL),
    ):
        svg, width = _badge(badge_x, badge_y, label, fill,
                            text_fill="#0b0f17" if fill != PANEL else TEXT)
        parts.append(svg)
        badge_x += width + 10

    roster_x = 720
    roster_y = 56
    parts.append(
        f'<rect x="{roster_x - 16}" y="{roster_y - 16}" width="528" height="230" rx="14" '
        f'fill="{PANEL}" opacity="0.85"/>'
    )
    parts.append(
        f'<text x="{roster_x}" y="{roster_y + 8}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" '
        f'font-size="13" fill="{MUTED}">AGENTS &amp; TOOLS</text>'
    )
    for i, (agent_id, tools) in enumerate(agent_rows):
        row_y = roster_y + 38 + i * 44
        parts.append(
            f'<text x="{roster_x}" y="{row_y}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" '
            f'font-size="16" font-weight="700" fill="{TEXT}">{html.escape(agent_id)}</text>'
        )
        parts.append(
            f'<text x="{roster_x}" y="{row_y + 20}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" '
            f'font-size="12" fill="{MUTED}">{html.escape(tools)}</text>'
        )

    install_y = 308
    parts.append(
        f'<rect x="48" y="{install_y - 22}" width="1184" height="40" rx="8" '
        f'fill="{ACCENT_SOFT}" opacity="0.6"/>'
    )
    parts.append(
        f'<text x="64" y="{install_y + 4}" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" '
        f'font-size="14" fill="{TEXT}">$ {html.escape(install)}</text>'
    )

    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    POSTERS.mkdir(parents=True, exist_ok=True)
    registry = json.loads(REGISTRY.read_text())
    written = 0
    for agent in registry.get("agents", []):
        template_dir = ROOT / agent["path"]
        agent_yaml_path = template_dir / ".grok" / "grok-agent.yaml"
        agent_yaml = yaml.safe_load(agent_yaml_path.read_text()) or {}
        svg = render(agent, agent_yaml)
        out = POSTERS / f"{agent['name']}.svg"
        out.write_text(svg)
        written += 1
    print(f"wrote {written} posters to {POSTERS.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
