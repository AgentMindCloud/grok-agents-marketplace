"""Tools for turning an X trend into a drafted thread."""

from __future__ import annotations

import os
from typing import TypedDict

from grok_install.runtime import x_client


class Trend(TypedDict):
    keyword: str
    tweet_volume: int
    sample_posts: list[dict]


class ScoredTrend(Trend):
    score: float
    reason: str


class Thread(TypedDict):
    topic: str
    tweets: list[str]
    approved: bool


def fetch_trends(topics: list[str], region: str = "worldwide") -> list[Trend]:
    """Fetch current trending topics from X, filtered to an allowlist."""
    client = x_client.from_env()
    raw = client.trends(region=region)
    allow = {t.lower() for t in topics}
    return [t for t in raw if any(tag in t["keyword"].lower() for tag in allow)]


def score_trend(keyword: str, score: float, reason: str) -> ScoredTrend:
    """Attach a 0-1 score and justification to a trend."""
    if not 0 <= score <= 1:
        raise ValueError("score must be between 0 and 1")
    return {"keyword": keyword, "tweet_volume": 0, "sample_posts": [], "score": score, "reason": reason}


def search_x_for_trend(keyword: str, limit: int = 20) -> list[dict]:
    """Pull the latest posts for a trend keyword so the author can cite real context."""
    client = x_client.from_env()
    return client.search(query=keyword, limit=max(1, min(limit, 50)))


def draft_thread(topic: str, tweets: list[str]) -> Thread:
    """Produce a thread draft for human review. Never posts."""
    if not 3 <= len(tweets) <= 12:
        raise ValueError("thread must be 3-12 tweets")
    for i, t in enumerate(tweets):
        if len(t) > 280:
            raise ValueError(f"tweet {i} exceeds 280 chars")
    return {"topic": topic, "tweets": tweets, "approved": False}


def post_thread(approval_token: str, tweets: list[str]) -> dict:
    """Post an approved thread. Requires a valid approval token."""
    if not approval_token or not approval_token.startswith("appr_"):
        raise PermissionError("missing or invalid approval token")
    if os.getenv("TREND_BOT_DISABLED") == "1":
        raise RuntimeError("kill switch engaged")
    client = x_client.from_env()
    return client.post_thread(tweets=tweets)
