# Submitting your own template

Got a Grok agent that might help others? Here's the path from idea to merged
PR.

## 1. Build locally

Start from `templates/hello-grok` — it has the minimum viable structure.

```bash
cp -r templates/hello-grok templates/my-awesome-agent
cd templates/my-awesome-agent
```

Edit `grok-install.yaml`, the files in `.grok/`, and `tools/custom_tools.py`.
Keep YAML under 150 lines total. If you need more, your agent is probably
doing two jobs — split it.

## 2. Validate locally

```bash
pip install grok-install yamllint
grok-install validate .
grok-install scan . --fail-on warning
yamllint -c ../../.yamllint.yml .
```

Then do a real run against your own X or GitHub credentials to confirm the
agent actually works.

## 3. Write the README

Use the structure in [template-anatomy.md](template-anatomy.md). The demo
gif should be short (≤60s) and show the end-to-end flow — install, configure,
first useful output.

## 4. Register it

Add an entry to the root `featured-agents.json`. The CI registry check
validates the path, the required files, and the safety profile.

Set `certified: false` if you're not yet meeting the full quality bar —
your template can still land, it just won't carry the certified badge.

## 5. Open a PR

CI will run four checks:

1. `yamllint` on every YAML file
2. `grok-install validate` on your template
3. `grok-install scan --fail-on warning`
4. A mock run (no real API calls)

Two reviewer approvals land a new template; one lands doc or fix PRs.

## Design tips

- **One job per agent.** If your template description needs the word "and",
  you probably want two templates.
- **Gate every external write.** Anything that posts to X, comments on a
  PR, or sends a message belongs under `requires_approval`.
- **Name your permissions tightly.** `x.post` is better than `x.*`. Least
  privilege keeps the safety scan green.
- **Reference prompts by key.** Inline prompts make the agent file hard to
  read. Put them in `grok-prompts.yaml`.
- **Don't fake outputs in the mock.** `GROK_INSTALL_MODE=mock` should
  exercise the same code path, just with stub API clients.

Questions? Open a discussion before you open the PR — happy to help shape
the idea.

## Optional: v2.14 visuals

Starting with `grok-install/v2.14`, a template can declare an optional
`visuals:` block. It's purely additive — templates that leave it out
still ship and still certify. Templates that include it get a richer
preview card in the gallery and in any downstream renderer that
understands v2.14.

Minimal stub:

```yaml
spec: grok-install/v2.14
version: "2.14"
# ...existing keys...
visuals:
  accent_color: "#7c5cff"      # any 6-digit hex
  preview_card:
    style: minimal             # minimal | futuristic | premium
    title: my-awesome-agent
    subtitle: One-line pitch.
    poster: docs/posters/my-awesome-agent.svg
```

Richer blocks can also set `theme`, `palette`, `typography`, `gradient`,
`glow`, `animation`, `haptics`, `accessibility`, and `auto_generate`.
See the 5 reference templates for worked examples:

- `templates/hello-grok` — minimal
- `templates/trend-to-thread` — futuristic + auto-generated demo media
- `templates/voice-agent-x` — futuristic + haptics + a11y
- `templates/thread-ghostwriter` — premium (serif, gold trim)
- `templates/code-reviewer` — minimal developer / terminal card

Each has a companion write-up under `docs/visuals/<template>.md`
explaining the design choice.

If you add visuals, also set `has_visuals: true` and `accent_color:
"#..."` on your `featured-agents.json` entry so the registry schema
passes.

## First-good-PR rubric

New to the repo? These are the highest-leverage first PRs. Any of
them is mergeable on its own.

1. **Fix a typo.** README, any docs page, any template README. One
   reviewer approval lands it.
2. **Add a demo GIF.** Every template is missing one (see
   `docs/gifs/README.md` for dimensions and length rules). Ship one
   short clip and link it from that template's README.
3. **Add a translation.** Port any template README to another
   language. File it as `README.<lang>.md` beside the original.
4. **Add v2.14 visuals to an existing template.** Pick any of the 5
   templates still on `grok-install/v2.12` (e.g. `reply-engagement-bot`,
   `research-swarm`, `personal-knowledge`, `scientific-discovery`,
   `live-event-commentator`), add a `visuals:` block modelled on the
   5 reference templates, and flip `has_visuals: true` in the registry.
5. **Improve a validator.** The scripts under `scripts/` are pure
   Python. A single targeted improvement (better error message,
   extra check, fixture) is welcome.

All five are reviewed against the same quality bar as a new template —
just with a much smaller surface area.
