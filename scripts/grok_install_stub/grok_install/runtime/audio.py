"""Stub audio transcription."""

from __future__ import annotations

from typing import Any


def transcribe(path: str) -> dict[str, Any]:
    return {"text": f"transcript of {path}", "duration_seconds": 12.5}
