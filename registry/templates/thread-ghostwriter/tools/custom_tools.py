"""Tools for the thread ghostwriter."""

from __future__ import annotations

import os
from typing import TypedDict

from grok_install.runtime import storage, x_client


class VoiceProfile(TypedDict):
    avg_chars: int
    sentence_shape: str
    punctuation: list[str]
    topics: list[str]
    hook_patterns: list[str]


class Thread(TypedDict):
    topic: str
    tweets: list[str]
    approved: bool


def load_recent_posts(limit: int = 200) -> list[dict]:
    """Load the user's recent X posts for voice analysis."""
    return x_client.from_env().user_timeline(limit=max(10, min(limit, 400)))


def store_voice_profile(profile: VoiceProfile) -> VoiceProfile:
    """Persist the inferred voice profile."""
    storage.put("voice_profile", profile)
    return profile


def load_voice_profile() -> VoiceProfile:
    """Return the stored voice profile, or raise if none exists."""
    profile = storage.get("voice_profile")
    if profile is None:
        raise FileNotFoundError("no voice profile yet — run profile step first")
    return profile


def draft_thread(topic: str, tweets: list[str]) -> Thread:
    """Create a thread draft for human review."""
    if not 3 <= len(tweets) <= 12:
        raise ValueError("thread must be 3-12 tweets")
    for i, t in enumerate(tweets):
        if len(t) > 280:
            raise ValueError(f"tweet {i} exceeds 280 chars")
    return {"topic": topic, "tweets": tweets, "approved": False}


def post_thread(approval_token: str, tweets: list[str]) -> dict:
    """Post an approved thread to X."""
    if not approval_token or not approval_token.startswith("appr_"):
        raise PermissionError("missing or invalid approval token")
    if os.getenv("GHOSTWRITER_DISABLED") == "1":
        raise RuntimeError("kill switch engaged")
    return x_client.from_env().post_thread(tweets=tweets)
