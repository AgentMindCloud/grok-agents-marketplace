"""Tools for building a personal X knowledge base."""

from __future__ import annotations

from typing import Literal, TypedDict

from grok_install.runtime import storage, vectors, x_client


class Document(TypedDict):
    id: str
    text: str
    url: str
    kind: Literal["post", "like", "mention"]
    created_at: str


def _since(key: str, default: str = "30d") -> str:
    return storage.get(f"sync_cursor:{key}") or default


def _remember(key: str, cursor: str) -> None:
    storage.put(f"sync_cursor:{key}", cursor)


def sync_posts() -> dict:
    """Pull posts created since the last sync."""
    client = x_client.from_env()
    cursor = _since("posts")
    result = client.user_timeline(since=cursor)
    _remember("posts", result["latest_cursor"])
    return {"new_items": len(result["items"]), "kind": "post"}


def sync_likes() -> dict:
    """Pull likes created since the last sync."""
    client = x_client.from_env()
    cursor = _since("likes")
    result = client.liked_posts(since=cursor)
    _remember("likes", result["latest_cursor"])
    return {"new_items": len(result["items"]), "kind": "like"}


def sync_mentions() -> dict:
    """Pull mentions since the last sync."""
    client = x_client.from_env()
    cursor = _since("mentions")
    result = client.mentions(since=cursor)
    _remember("mentions", result["latest_cursor"])
    return {"new_items": len(result["items"]), "kind": "mention"}


def index_documents(documents: list[Document]) -> dict:
    """Embed and upsert documents into the vector index."""
    vectors.upsert("personal", documents)
    return {"indexed": len(documents)}


def semantic_search(query: str, k: int = 8) -> list[Document]:
    """Search the personal index for the top-k documents."""
    return vectors.search("personal", query=query, k=max(1, min(k, 25)))


def answer_with_citations(answer: str, citations: list[str]) -> dict:
    """Return the final answer along with the permalinks it cites."""
    if not citations:
        raise ValueError("answer must include at least one citation")
    return {"answer": answer, "citations": citations}
