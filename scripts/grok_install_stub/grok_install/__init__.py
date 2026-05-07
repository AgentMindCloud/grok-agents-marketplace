"""Minimal stand-in for the `grok_install` runtime.

The real `grok-install` CLI isn't on PyPI yet. This package lets every
template's `custom_tools.py` import from `grok_install.runtime` so we can
statically analyse and mock-run them in CI without reaching any network.

Every exported module follows the same shape the templates expect. Every
function returns a safely-typed fake value — no network calls, no secrets
needed.
"""

__version__ = "0.0.0-stub"
