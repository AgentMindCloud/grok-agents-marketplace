<!-- Thanks for contributing to awesome-grok-agents! -->

## What is this?

<!-- One line. Is this a new template, a fix, docs, or CI? -->

## If this adds a new template

- [ ] Copied the structure from `templates/hello-grok`
- [ ] `grok-install.yaml`, `.grok/grok-agent.yaml`, `.grok/grok-security.yaml`,
      `.grok/grok-prompts.yaml` all present
- [ ] Every tool has a complete type-hinted signature and docstring
- [ ] `safety_profile` set; permissions listed explicitly; writes gated under
      `requires_approval`
- [ ] Rate limits declared; kill switch env var wired for write-capable templates
- [ ] `.env.example` lists every secret — no real values
- [ ] YAML total under 150 lines
- [ ] README has **What it does / Install / Configure / Run / Safety**
- [ ] Demo gif added at `docs/gifs/<template-name>.gif`
- [ ] Added an entry to `featured-agents.json`
- [ ] Ran locally: `grok-install validate`, `grok-install scan --fail-on warning`,
      `yamllint -c .yamllint.yml .`

## If this is a fix or docs change

- [ ] Minimum scope — no drive-by refactors
- [ ] If behavior changed, the template's README reflects it

## Screenshots / demo

<!-- For new templates, inline the demo gif or a short video. -->
