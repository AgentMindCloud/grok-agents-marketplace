"""Stub vector store."""

from __future__ import annotations

from typing import Any

_INDEXES: dict[str, list[dict[str, Any]]] = {}


def upsert(name: str, documents: list[dict[str, Any]]) -> None:
    _INDEXES.setdefault(name, []).extend(documents)


def search(name: str, query: str, k: int = 8) -> list[dict[str, Any]]:
    docs = _INDEXES.get(name, [])
    return docs[:k]
