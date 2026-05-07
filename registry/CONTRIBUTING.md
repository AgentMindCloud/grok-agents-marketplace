# Contributing

Thanks for helping build the Grok agent ecosystem.

## Adding a new template

1. Fork this repo.
2. Copy `templates/hello-grok/` as a starting point.
3. Follow the structure in [docs/template-anatomy.md](docs/template-anatomy.md).
4. Add your entry to [featured-agents.json](featured-agents.json).
5. Open a PR. CI will run `grok-install validate`, `grok-install scan`, a mock
   run of your template, and `yamllint`. All four must pass.

## Quality bar

Every template must:

- Run end-to-end (CI enforced)
- Have a README with a 60-second demo gif
- Declare permissions explicitly in `.grok/grok-security.yaml`
- Set `safety_profile` appropriately for the blast radius
- Provide full JSON schemas for every custom tool
- Gate any X-writing tool behind an approval step
- Declare rate limits
- Contain zero hardcoded credentials (use `.env.example`)
- Stay under 150 lines of YAML total

If your template can't meet the bar, it can still land — just set
`certified: false` in `featured-agents.json` and the gallery will show it
without the badge.

## Style

- YAML: 2-space indent, lowercase keys, no trailing whitespace. `yamllint`
  config is at the repo root.
- Python tools: type-hinted, one tool per function, docstring becomes the
  tool description.
- Prompts: plain text in `.grok/grok-prompts.yaml`, not inlined in agent
  definitions.

## Reviews

Two approvals required for new templates. One approval for fixes or doc
changes.

## Code of conduct

Be kind. Assume good faith. We're building the Grok ecosystem together.
