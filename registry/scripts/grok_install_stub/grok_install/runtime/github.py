"""Stub GitHub client."""

from __future__ import annotations

from typing import Any


class _Client:
    def pull_request(self, repo: str, number: int) -> dict[str, Any]:
        return {
            "number": number,
            "title": "Sample PR",
            "body": "body",
            "base": "main",
            "head": "feature",
            "labels": [],
        }

    def pull_request_diff(self, repo: str, number: int) -> str:
        return "diff --git a/foo b/foo\n+added line\n"

    def file_contents(self, repo: str, path: str, ref: str) -> str:
        return f"# stub contents for {path}@{ref}\n"

    def post_review(self, repo: str, number: int, payload: dict[str, Any]) -> dict[str, Any]:
        return {"repo": repo, "number": number, "posted": True}


def from_env() -> _Client:
    return _Client()
