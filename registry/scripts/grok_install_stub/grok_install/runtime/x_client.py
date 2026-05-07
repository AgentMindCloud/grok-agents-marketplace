"""Stub X API client."""

from __future__ import annotations

from typing import Any


class _Client:
    def mentions(self, since: str = "1h", limit: int = 25) -> Any:
        item = {"id": "m1", "author": "alice", "text": "hello", "created_at": "2026-04-17T00:00:00Z"}
        return {"items": [item], "latest_cursor": "cursor-1"}

    def reply(self, in_reply_to: str, text: str) -> dict[str, Any]:
        return {"id": "r1", "in_reply_to": in_reply_to, "text": text, "posted": True}

    def post(self, text: str) -> dict[str, Any]:
        return {"id": "p1", "text": text, "posted": True}

    def post_thread(self, tweets: list[str]) -> dict[str, Any]:
        return {"ids": [f"t{i}" for i, _ in enumerate(tweets)], "posted": True}

    def trends(self, region: str = "worldwide") -> list[dict[str, Any]]:
        return [{"keyword": "#ai", "tweet_volume": 1000, "sample_posts": []}]

    def search(self, query: str, limit: int = 20) -> list[dict[str, Any]]:
        return [{"id": "s1", "text": f"sample for {query}", "author": "bob"}]

    def user_timeline(self, limit: int = 200, since: str | None = None) -> Any:
        items = [{"id": f"u{i}", "text": f"post {i}"} for i in range(min(limit, 3))]
        if since is not None:
            return {"items": items, "latest_cursor": "cursor-1"}
        return items

    def liked_posts(self, since: str | None = None) -> dict[str, Any]:
        return {"items": [{"id": "l1", "text": "liked"}], "latest_cursor": "cursor-1"}

    def stream_sample(self, query: str, window_seconds: int = 30) -> dict[str, Any]:
        return {
            "query": query,
            "window_seconds": window_seconds,
            "volume": 10,
            "top_posts": [],
            "sentiment": 0.0,
        }


def from_env() -> _Client:
    """Return a stub client; the real implementation reads env credentials."""
    return _Client()
