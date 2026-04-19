# Disclaimer

**GrokInstall** (including `grokagents.dev`, `grok-agents-marketplace`,
`grok-install`, `grok-yaml-standards`, `vscode-grok-yaml`, and
`grok-install-action`) is an independent, community-maintained open-source
project. It is **not affiliated with, endorsed by, or sponsored by** xAI
Corp., X Corp., or any of their subsidiaries, officers, or employees.

"Grok" and "X" are trademarks of their respective owners. References to
"Grok-native agents" in this project describe a community file format and
tooling convention; they do not imply any partnership, certification, or
official support from xAI or X.

## No warranty

The software and agent manifests distributed through this marketplace are
provided **"as is"**, without warranty of any kind — express or implied —
including but not limited to warranties of merchantability, fitness for a
particular purpose, and non-infringement. See [LICENSE](./LICENSE) for the
full Apache 2.0 terms.

## Third-party agents

Agents listed in the marketplace are authored and maintained by third
parties. Their presence in the catalog **does not constitute an
endorsement** by the GrokInstall maintainers. Install counts, star
counts, and safety scores are informational signals only — not a
substitute for reviewing the agent's YAML manifest, source repository,
and permissions before deploying it against your own X account or API
key.

The `grok-install` CLI surfaces a safety score derived from the
`grok-yaml-standards` linter; a high score does not guarantee an agent
is free of bugs, abuse vectors, or policy violations. **You are
responsible for the agents you install.**

## Rate limits and API usage

Installing an agent via the marketplace may issue requests against xAI's
Grok API and X's posting APIs under **your own credentials**. You are
responsible for any costs, rate-limit consumption, and terms-of-service
compliance those requests incur. GrokInstall never proxies, stores, or
sees your API keys.

## Reporting issues

Please file a GitHub issue if you:

- discover a malicious, broken, or policy-violating agent in the catalog
- find a security vulnerability in the marketplace, CLI, or action
- want an agent delisted (maintainers of the source repo can open a PR
  against `awesome-grok-agents` removing the entry)

Security disclosures: see `SECURITY.md` in `agentmindcloud/grok-install`.
