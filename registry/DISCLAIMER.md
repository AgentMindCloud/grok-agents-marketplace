# Disclaimer

`awesome-grok-agents` is a **community-maintained** collection of example
templates for the `grok-install` CLI and xAI's Grok models. It is **not** an
official xAI or Grok product, and no affiliation with or endorsement by xAI
should be inferred from the name, branding, or content of this repository.

## No warranty

The templates in this repository are provided **as-is**, without warranty of
any kind, either express or implied, including but not limited to the implied
warranties of merchantability, fitness for a particular purpose, and
non-infringement. See [LICENSE](LICENSE) for the full text.

## You are responsible for what you deploy

Each template can post to X, comment on GitHub, call the Grok API, speak
audio, or touch other external services. Before you run any template:

- Read the template's `README.md`, `.grok/grok-security.yaml`, and
  `tools/custom_tools.py`.
- Confirm the `safety_profile`, the declared `permissions`, and any
  `requires_approval` gates match what you actually want the agent to do.
- Set the documented kill-switch environment variables before enabling writes.
- Comply with the terms of service of every platform the agent touches —
  including X, GitHub, xAI, and any other third-party API.

## Rate limits, cost, and abuse

Running these agents consumes Grok API credits and third-party API quotas.
You are responsible for monitoring cost, respecting rate limits, and ensuring
your deployment does not violate anti-spam or automation policies on the
platforms it writes to. The maintainers of this repository are not liable for
charges, suspensions, or damages resulting from your use of these templates.

## Security

If you believe you have found a security issue in a template or in this
repository's tooling, please follow the disclosure process in
[SECURITY.md](SECURITY.md). Do not open a public issue.

## Trademarks

"Grok", "xAI", and "X" are trademarks of their respective owners. Use of
these names in this repository is descriptive — it identifies the platforms
the templates target — and does not imply endorsement.
