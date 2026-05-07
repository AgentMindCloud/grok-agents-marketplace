"""Runtime modules used by template tools.

Each attribute is a submodule; they're re-exported here so templates can do
`from grok_install.runtime import x_client, github, ...` in one line.
"""

from . import (
    arxiv,
    audio,
    delivery,
    github,
    http,
    storage,
    vectors,
    web_search,
    x_client,
)

__all__ = [
    "arxiv",
    "audio",
    "delivery",
    "github",
    "http",
    "storage",
    "vectors",
    "web_search",
    "x_client",
]
