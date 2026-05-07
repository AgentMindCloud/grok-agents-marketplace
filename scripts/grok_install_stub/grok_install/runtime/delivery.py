"""Stub message delivery (email/slack/stdout)."""

from __future__ import annotations

from typing import Any


def send(channel: str, to: str, payload: Any) -> dict[str, Any]:
    return {"channel": channel, "to": to, "delivered": True}
