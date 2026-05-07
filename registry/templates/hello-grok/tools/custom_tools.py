"""Single tool: return the current UTC timestamp."""

from datetime import datetime, timezone


def now() -> str:
    """Return the current UTC time as an ISO-8601 string."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds")
