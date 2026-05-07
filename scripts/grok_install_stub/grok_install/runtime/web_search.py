"""Stub web search."""

from __future__ import annotations

from typing import Any


def search(query: str, limit: int = 8) -> list[dict[str, Any]]:
    return [
        {"url": f"https://example.com/{i}", "title": f"Result {i}", "snippet": f"Snippet about {query}"}
        for i in range(min(limit, 2))
    ]
