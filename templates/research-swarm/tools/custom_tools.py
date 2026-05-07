"""Tools for the research-swarm multi-agent pipeline."""

from __future__ import annotations

from typing import TypedDict

from grok_install.runtime import http, web_search as ws


class Source(TypedDict):
    url: str
    title: str
    author: str
    date: str
    extract: str


class Critique(TypedDict):
    claim: str
    counter_argument: str
    weak: bool


def web_search(query: str, limit: int = 8) -> list[dict]:
    """Run a web search and return result URLs + snippets."""
    return ws.search(query=query, limit=max(1, min(limit, 15)))


def fetch_page(url: str) -> str:
    """Fetch a URL and return readable text (stripped of nav/footers)."""
    return http.readable(url)


def add_source(url: str, title: str, author: str, date: str, extract: str) -> Source:
    """Register a source for the publisher to cite."""
    return {"url": url, "title": title, "author": author, "date": date, "extract": extract}


def challenge_claim(claim: str, counter_argument: str, weak: bool) -> Critique:
    """Record a counter-argument against a claim."""
    return {"claim": claim, "counter_argument": counter_argument, "weak": weak}


def score_evidence(claim: str, score: float) -> dict:
    """Score the evidence strength for a claim on a 0-1 scale."""
    if not 0 <= score <= 1:
        raise ValueError("score must be between 0 and 1")
    return {"claim": claim, "score": score}


def compile_brief(question: str, tldr: str, findings: list[str], sources: list[Source]) -> dict:
    """Produce the final brief object returned to the caller."""
    if len(tldr.split()) > 60:
        raise ValueError("TL;DR must be under 60 words")
    if not 3 <= len(findings) <= 5:
        raise ValueError("brief must have 3-5 key findings")
    return {"question": question, "tldr": tldr, "findings": findings, "sources": sources}
