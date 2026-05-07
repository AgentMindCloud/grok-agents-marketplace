"""Tools for the live event commentator."""

from __future__ import annotations

import os
import time
from typing import Literal, TypedDict

from grok_install.runtime import storage, x_client

MIN_GAP_SECONDS = 120


class Sample(TypedDict):
    query: str
    window_seconds: int
    volume: int
    top_posts: list[dict]
    sentiment: float


class Moment(TypedDict):
    kind: Literal["volume_spike", "sentiment_flip", "notable_post"]
    summary: str
    source_post_url: str | None


class Reaction(TypedDict):
    moment: Moment
    text: str
    approved: bool


def sample_event_stream(query: str, window_seconds: int = 30) -> Sample:
    """Sample the X stream for the event query over a short window."""
    return x_client.from_env().stream_sample(query=query, window_seconds=window_seconds)


def detect_moment(kind: str, summary: str, source_post_url: str | None = None) -> Moment:
    """Record a detected moment worth commenting on."""
    if kind not in ("volume_spike", "sentiment_flip", "notable_post"):
        raise ValueError(f"unknown moment kind: {kind}")
    return {"kind": kind, "summary": summary, "source_post_url": source_post_url}


def draft_reaction(moment: Moment, text: str) -> Reaction:
    """Draft a single reaction post for approval."""
    if len(text) > 280:
        raise ValueError("reaction exceeds 280 chars")
    return {"moment": moment, "text": text, "approved": False}


def post_single(approval_token: str, text: str) -> dict:
    """Post an approved reaction. Enforces the cooldown and kill switch."""
    if not approval_token or not approval_token.startswith("appr_"):
        raise PermissionError("missing or invalid approval token")
    if os.getenv("COMMENTATOR_DISABLED") == "1":
        raise RuntimeError("kill switch engaged")
    last = storage.get("last_post_at") or 0
    now = time.time()
    if now - last < MIN_GAP_SECONDS:
        return {"skipped": True, "reason": "cooldown"}
    result = x_client.from_env().post(text=text)
    storage.put("last_post_at", now)
    return result
