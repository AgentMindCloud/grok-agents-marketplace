"""Tools for the reply engagement bot."""

from __future__ import annotations

import os
from typing import Literal, TypedDict

from grok_install.runtime import x_client  # provided by grok-install


class Mention(TypedDict):
    id: str
    author: str
    text: str
    created_at: str


class Classification(TypedDict):
    mention_id: str
    worth_replying: bool
    reason: str


class Draft(TypedDict):
    mention_id: str
    in_reply_to: str
    text: str
    approved: bool


def fetch_mentions(since: str = "1h", limit: int = 25) -> list[Mention]:
    """Fetch recent mentions of the authenticated user from X.

    Args:
        since: ISO-8601 timestamp or relative window like '1h', '30m'.
        limit: max mentions to return (1-100).
    """
    client = x_client.from_env()
    return client.mentions(since=since, limit=limit)


def classify_mention(
    mention_id: str,
    worth_replying: bool,
    reason: Literal["question", "critique", "appreciation", "spam", "other"],
) -> Classification:
    """Record whether a mention is worth replying to and why."""
    return {"mention_id": mention_id, "worth_replying": worth_replying, "reason": reason}


def draft_reply(mention_id: str, in_reply_to: str, text: str) -> Draft:
    """Create a reply draft for human review. Never posts."""
    if len(text) > 280:
        raise ValueError("reply exceeds 280 chars")
    return {"mention_id": mention_id, "in_reply_to": in_reply_to, "text": text, "approved": False}


def post_reply(approval_token: str, in_reply_to: str, text: str) -> dict:
    """Post an approved reply to X. Requires a valid approval token."""
    if not approval_token or not approval_token.startswith("appr_"):
        raise PermissionError("missing or invalid approval token")
    if os.getenv("REPLY_BOT_DISABLED") == "1":
        raise RuntimeError("kill switch engaged")
    client = x_client.from_env()
    return client.reply(in_reply_to=in_reply_to, text=text)
