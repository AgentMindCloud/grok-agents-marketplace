"""Stub arXiv client."""

from __future__ import annotations

from typing import Any


def latest(categories: list[str], limit: int = 6) -> list[dict[str, Any]]:
    return [
        {
            "id": f"2604.{i:05d}",
            "title": f"Paper {i}",
            "authors": ["A. Researcher"],
            "abstract": "Stub abstract.",
            "url": f"https://arxiv.org/abs/2604.{i:05d}",
            "categories": list(categories),
        }
        for i in range(min(limit, 2))
    ]
