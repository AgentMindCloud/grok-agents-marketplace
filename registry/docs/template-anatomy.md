# Template anatomy

Every template in `templates/<name>/` follows the same layout so the CLI,
the CI workflow, and readers all know exactly where to look.

```
templates/<name>/
├── grok-install.yaml         # root config (v2.12 spec)
├── .grok/
│   ├── grok-agent.yaml       # agent definitions
│   ├── grok-workflow.yaml    # multi-step flows (optional for single-agent)
│   ├── grok-security.yaml    # permissions + safety profile
│   └── grok-prompts.yaml     # system prompts
├── tools/                     # custom Python tool implementations
│   └── custom_tools.py
├── README.md                  # what it does, how to use, demo gif
├── .env.example               # required secrets, never the values
└── LICENSE                    # Apache 2.0 inherited from the root
```

## `grok-install.yaml` (root config)

The entry point the CLI reads first. Minimum fields:

```yaml
spec: grok-install/v2.12
name: <template-name>
description: <one line, shown in the gallery>
entrypoint: .grok/grok-workflow.yaml   # or a single agent file
model: grok-4
runtime:
  python: ">=3.11"
env:
  - XAI_API_KEY
```

## `.grok/grok-agent.yaml`

One agent per block. Keep system prompts in `grok-prompts.yaml` and reference
them by key — it keeps the agent file scannable.

## `.grok/grok-security.yaml`

Must declare `safety_profile` (`strict`, `standard`, or `permissive`) and an
explicit `permissions` list. Any tool that writes to the outside world
(posting to X, commenting on a PR, sending email) must be listed under
`requires_approval`.

## `.grok/grok-workflow.yaml`

Needed only when there is more than one agent or more than one step. Use
the `steps:` syntax for sequential flows, `swarm:` for peer agents.

## `tools/custom_tools.py`

Plain Python functions. Each exported function is picked up as a tool by
`grok-install`. Type hints generate the JSON schema; the docstring becomes
the tool description.

```python
def search_x_for_trend(query: str, limit: int = 20) -> list[dict]:
    """Search X for the latest posts matching a trend keyword."""
    ...
```

## README

Required sections: **What it does**, **Install**, **Configure**,
**Run**, **Demo**. The demo must be a gif under `docs/gifs/<name>.gif`.

## `.env.example`

Every secret the template reads. Never include real values; the CI scan
will fail the PR.
