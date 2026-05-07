"""Tools for the voice-to-X workflow."""

from __future__ import annotations

import os
from pathlib import Path
from typing import TypedDict

from grok_install.runtime import audio, x_client


class Transcript(TypedDict):
    text: str
    duration_seconds: float


class Post(TypedDict):
    text: str
    approved: bool


def transcribe_audio(path: str) -> Transcript:
    """Transcribe an audio file into text."""
    audio_path = Path(path)
    if not audio_path.is_file():
        raise FileNotFoundError(f"no such audio file: {path}")
    if audio_path.stat().st_size > 25 * 1024 * 1024:
        raise ValueError("audio file over 25MB; split it first")
    return audio.transcribe(str(audio_path))


def polish_to_post(text: str) -> Post:
    """Produce a single polished post for approval."""
    if len(text) > 280:
        raise ValueError("post exceeds 280 chars")
    return {"text": text, "approved": False}


def post_single(approval_token: str, text: str) -> dict:
    """Post the approved text to X."""
    if not approval_token or not approval_token.startswith("appr_"):
        raise PermissionError("missing or invalid approval token")
    if os.getenv("VOICE_X_DISABLED") == "1":
        raise RuntimeError("kill switch engaged")
    return x_client.from_env().post(text=text)
