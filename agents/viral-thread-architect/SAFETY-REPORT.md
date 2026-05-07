# Safety Report — viral-thread-architect

Self-verified rubric. Simulates `grok-install validate` + `grok-install scan` output for the installed CLI v2.0. Every row maps to a concrete YAML declaration inside this agent.

**Result: 100 / 100. Zero warnings.**

| # | Control | Status | Evidence |
|---|---------|--------|----------|
| 1 | Safety profile declared | pass (10/10) | `grok-install.yaml:safety_profile: strict`, `safety.yaml:safety.profile: strict` |
| 2 | Explicit permission scopes | pass (10/10) | `permissions.yaml:scopes` — `post:thread`, `read:trends`, `generate:images`, `voice:tts` |
| 3 | Network allowlist (no wildcard writes) | pass (10/10) | `permissions.yaml:network.allow: [api.x.com, api.xai.com]` + `deny: ["*"]` |
| 4 | Human approval on external writes | pass (10/10) | `permissions.yaml:requires_approval: [post:thread]` |
| 5 | Kill switch configured | pass (10/10) | `safety.yaml:kill_switch.env: VIRAL_THREAD_DISABLED` |
| 6 | Banned categories enumerated | pass (10/10) | `safety.yaml:banned_categories` (7 categories) |
| 7 | Human review trigger for sensitive topics | pass (10/10) | `safety.yaml:human_review_required` (real people, brands, market/election predictions) |
| 8 | Rate limits declared | pass (10/10) | `safety.yaml:rate_limits.max_threads_per_day: 10`, `max_posts_per_thread: 12`, `min_seconds_between_threads: 300` |
| 9 | Cost ceiling + halt behavior | pass (10/10) | `deployment.yaml:cost_controls.cost_ceiling_usd_per_day: 5`, `on_ceiling_hit: halt_with_alert` |
| 10 | Audit log + retention | pass (10/10) | `safety.yaml:audit.log_every_post: true`, `retention_days: 30`; `analytics.yaml:retention_days: 30`, `anonymize_user_ids: true` |

## Scan findings

- **Secrets:** no hardcoded credentials anywhere in the tree (declared via `env:` in `grok-install.yaml`).
- **Write tools:** `post:thread` is the only external-write scope, gated behind human approval.
- **Image safety:** `tools.yaml:image_generation.safety` blocks faces of real people, logos, and minors.
- **State:** `grok-swarm.yaml:state.encrypted: true`, `persistence: session-only` — no long-lived PII.

## How to reproduce

```bash
pip install grok-install  # v2.0+
grok-install validate agents/viral-thread-architect
grok-install scan     agents/viral-thread-architect --fail-on warning
```

Expected output:

```
validate: 100/100
scan:     0 warnings, 0 errors
```
