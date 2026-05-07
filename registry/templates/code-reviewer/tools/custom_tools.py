"""Tools for the GitHub PR code reviewer."""

from __future__ import annotations

import os
from typing import Literal, TypedDict

from grok_install.runtime import github as gh


class PullRequest(TypedDict):
    number: int
    title: str
    body: str
    base: str
    head: str
    labels: list[str]


class InlineComment(TypedDict):
    path: str
    line: int
    body: str


class ReviewPayload(TypedDict):
    verdict: Literal["approve", "request_changes", "comment"]
    summary: str
    comments: list[InlineComment]
    approved: bool


def fetch_pr(repo: str, pr_number: int) -> PullRequest:
    """Fetch a pull request's metadata."""
    return gh.from_env().pull_request(repo=repo, number=pr_number)


def fetch_diff(repo: str, pr_number: int) -> str:
    """Return the unified diff for the PR."""
    return gh.from_env().pull_request_diff(repo=repo, number=pr_number)


def fetch_file(repo: str, path: str, ref: str) -> str:
    """Return the contents of a file at a specific ref."""
    return gh.from_env().file_contents(repo=repo, path=path, ref=ref)


def draft_inline_comment(path: str, line: int, body: str) -> InlineComment:
    """Draft one inline comment anchored to a file:line."""
    if line <= 0:
        raise ValueError("line must be positive")
    if len(body) > 1500:
        raise ValueError("inline comment too long")
    return {"path": path, "line": line, "body": body}


def draft_summary(
    verdict: Literal["approve", "request_changes", "comment"],
    summary: str,
    comments: list[InlineComment],
) -> ReviewPayload:
    """Assemble the full review payload for human approval."""
    return {"verdict": verdict, "summary": summary, "comments": comments, "approved": False}


def post_review(approval_token: str, repo: str, pr_number: int, payload: ReviewPayload) -> dict:
    """Post the approved review to GitHub."""
    if not approval_token or not approval_token.startswith("appr_"):
        raise PermissionError("missing or invalid approval token")
    if os.getenv("CODE_REVIEWER_DISABLED") == "1":
        raise RuntimeError("kill switch engaged")
    return gh.from_env().post_review(repo=repo, number=pr_number, payload=payload)
