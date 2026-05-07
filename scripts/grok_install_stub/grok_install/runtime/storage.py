"""Stub key/value storage backed by an in-process dict."""

from __future__ import annotations

from typing import Any

_STORE: dict[str, Any] = {}


def put(key: str, value: Any) -> None:
    _STORE[key] = value


def get(key: str, default: Any = None) -> Any:
    return _STORE.get(key, default)


def reset() -> None:
    _STORE.clear()
