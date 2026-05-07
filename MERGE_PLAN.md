# MERGE_PLAN

The ledger of repository consolidations into `grok-agents-marketplace`.

The mono-repo strategy folds related satellite repos into this one so the data
layer, the rendering layer, and the tooling layer ship together. Each merge is
performed with `git subtree --squash`, which preserves the upstream commit SHA
in this repo's history without dragging in every upstream commit.

---

## Phase 15 — `awesome-grok-agents` → `/registry/`

**Status:** ✅ COMPLETE — 2026-05-07

| Field | Value |
| --- | --- |
| Source repo | `https://github.com/AgentMindCloud/awesome-grok-agents` |
| Source ref | `main` (HEAD `05a8166`) |
| Destination | `./registry/` |
| Mechanism | `git subtree add --prefix=registry <url> main --squash` |
| Branch | `claude/merge-grok-agents-registry-KwJfA` |
| History preservation | Squash commit retains the upstream SHA in its message |

### What this is

The full `awesome-grok-agents` catalog (agent manifests, schemas, templates,
`featured-agents.json`, docs) is now mirrored in this repo at `./registry/`.
This is the **final major merge before Tier 4 polish**.

### What this is NOT

Application code is **not** rewired in this phase. The marketplace site still
fetches the catalog over HTTPS from `raw.githubusercontent.com/.../awesome-grok-agents/...`
exactly as before — see `README.md` "Data Sources" and the architecture diagram.

Repointing `src/lib/...` catalog loaders at `./registry/` and updating the
architecture diagram are deliberately deferred to **Tier 4 polish**.

### Re-running / refreshing the registry

To pull a newer snapshot of `awesome-grok-agents` into `./registry/` later:

```bash
git subtree pull --prefix=registry https://github.com/AgentMindCloud/awesome-grok-agents.git main --squash
```

---

## Prior phases (1 – 14)

Not ledgered here. See the repo's `git log` for the historical record — those
phases predate this document and are not retro-fitted (inventing a backfill
ledger would be inaccurate).

---

## Next up — Tier 4 polish

- Repoint catalog loaders (`src/lib/...`) to read from `./registry/`
- Update the README architecture diagram's data-source arrow
- Update the `## ✦ Data Sources` README copy to reflect the in-repo source
