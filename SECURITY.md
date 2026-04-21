# Security Policy

This document covers the threat model, responsible disclosure process, and
hardening guarantees for **grok-agents-marketplace** (the frontend at
[grokagents.dev](https://grokagents.dev)) and its public API surface.

If you believe you've found a security issue, **do not open a public issue
or pull request**. Follow the disclosure steps in the [Reporting](#reporting-a-vulnerability)
section.

---

## Supported versions

We run a single production deployment off `main`. We do not ship versioned
releases of the website, so there are no backported security fixes: the
latest commit on `main` is the only supported version.

| branch  | supported | notes                                       |
| ------- | --------- | ------------------------------------------- |
| `main`  | ✅        | Production deployment at grokagents.dev     |
| others  | ❌        | Feature branches — do not deploy            |

---

## Reporting a vulnerability

**Private disclosure** is required for anything with security impact.

1. Use GitHub's **Private Vulnerability Reporting** form for this repo:
   <https://github.com/AgentMindCloud/grok-agents-marketplace/security/advisories/new>
2. Or email the maintainers directly at **security@grokagents.dev**
   (monitored by @JanSol0s). PGP key available on request.
3. Include:
   - A reproducible proof of concept (URL, request, or sequence of steps)
   - Impact assessment (what an attacker gains)
   - Suggested remediation, if any
4. Please **do not** run automated scanners against production — use a local
   build (`npm run build && npm run start`).

### Our response timeline

| step                      | target                         |
| ------------------------- | ------------------------------ |
| Acknowledgement           | within **72 hours**            |
| Initial triage + severity | within **7 days**              |
| Fix and deploy            | within **30 days** (critical: 7 days) |
| Public advisory           | on fix landing, credit the reporter (opt-in) |

We follow the spirit of CVD (Coordinated Vulnerability Disclosure). If the
issue is already publicly known or actively exploited, we fast-track.

### Safe harbour

Good-faith security research that:

- does not degrade service or exfiltrate data beyond what is needed to prove
  the issue,
- respects other users' privacy,
- stops at the minimum PoC,

will not be pursued legally, and we will credit your contribution in the
advisory if you wish.

---

## Threat model

This is a **public read-mostly site** with two write surfaces: install
tracking (browser-initiated) and CLI telemetry ingest (CLI-initiated).
The threat model below covers the realistic risks.

### In scope

1. **Server-side request injection** in any `/api/*` route (telemetry,
   track-install, stats).
2. **XSS / HTML injection** in agent content (names, taglines, YAML) coming
   from the upstream `awesome-grok-agents` catalog.
3. **Cookie abuse** — `gi_anon` cookie (first-party, HttpOnly, SameSite=Lax,
   1-year). It holds only an opaque random id used for de-duplicating
   install clicks. See [cookie threat model](#cookies).
4. **Telemetry surface** — see [telemetry threat model](#telemetry).
5. **Denial of service** via unbounded payloads, KV write amplification, or
   cache stampedes. The app sets `no-store` on `/api/*` and rate-limits
   `/api/telemetry` to 30 events/min per `anon_install_id`.
6. **Open redirect** via any redirect URL in an API route or middleware.
7. **Supply chain**: npm dependencies, GitHub Actions, Vercel integrations.
   Enforced via Dependabot and `dependency-review-action` in CI.

### Out of scope

- Phishing sites impersonating `grokagents.dev` (report to the registrar).
- Bugs in third-party services (Vercel, Plausible, GitHub) — report upstream.
- Hypothetical quantum attacks on TLS.
- Self-XSS requiring the victim to paste attacker-controlled code into their
  own DevTools console.
- Clickjacking on pages that only display public data.
- Rate limits that do not meaningfully affect others.
- Weaknesses in the `awesome-grok-agents` repo catalog itself — those belong
  in that repo's security policy.

---

## Cookies

The site sets exactly **one** first-party cookie:

| name      | purpose                                    | attributes                                   | lifetime |
| --------- | ------------------------------------------ | -------------------------------------------- | -------- |
| `gi_anon` | De-duplicate install clicks per browser    | `HttpOnly; SameSite=Lax; Secure; Path=/`     | 1 year   |

- **Value**: a 128-bit random id generated server-side on first
  `/api/track-install*` POST. No user data is derived from it.
- **Not used for analytics profiling**: aggregate install counts are keyed
  by agent id, not by cookie.
- **Revocable**: clearing site data erases the cookie; a fresh id is issued
  on next click. Nothing is linked across devices.
- **Never sent to third parties**: `SameSite=Lax` + first-party only.

No other cookies, localStorage, or sessionStorage entries are set by our
code. Plausible Analytics is cookieless by design.

### Cookie threats we considered

| threat                                    | mitigation                                         |
| ----------------------------------------- | -------------------------------------------------- |
| CSRF on `/api/track-install*`             | No auth side-effects; cookie is a counter key, not a session. `SameSite=Lax` blocks cross-site `POST`. |
| Cookie theft via XSS                      | `HttpOnly` prevents JS access. CSP headers (below). |
| Cookie replay across devices              | Nothing links the cookie to a user account.        |
| Supercookie / cross-site tracking         | First-party only, no third-party pixels.           |
| EU ePrivacy consent requirement           | Cookie is strictly necessary for install counting; Plausible is cookieless. No banner required. |

---

## Telemetry

The CLI (`grok-install` v2+) posts events to `POST /api/telemetry`. The
server validates every payload with Zod before storing it in Vercel KV.

### What we collect

See `/privacy` on the site and `src/lib/telemetry-schema.ts` for the full
Zod contract. Summary:

- Event name (enum: `deploy | post | call | scan | error`)
- CLI version string (regex-bounded, ≤ 32 chars)
- Agent category (enum), booleans (pro/voice/swarm), safety score bucket
- `anon_install_id` — a locally generated random id, user-rotatable
- Server-side receive time (for retention + rate limiting)

### What we refuse to collect

- IP addresses (stripped at the edge, never persisted)
- OS usernames, hostnames, file paths
- Agent YAML contents, prompts, completions, or any response bodies
- API keys, tokens, X handles, email addresses
- Timestamps below 1-second resolution

### Browser-side events (Plausible)

The browser fires cookieless events via Plausible (when configured). These
include the v2.14 `visuals_block_rendered` event with properties
`{ agent_id, accent_color, style }`. No IP, no fingerprinting, no cookies.
Full event list: `/privacy`.

### Telemetry threat model

| threat                                   | mitigation                                                     |
| ---------------------------------------- | -------------------------------------------------------------- |
| Forged telemetry inflating counters      | Zod validation + per-`anon_install_id` rate limit (30/min)     |
| Log flooding DoS                         | Fixed-size payload cap, `no-store` on `/api/*`, rate limit     |
| PII leakage via extra fields             | Zod `strict`/whitelist schema; unknown fields rejected         |
| Cross-session de-anonymisation           | `anon_install_id` is rotatable and never combined with IP/UA   |
| Retention creep                          | 90-day delete job documented on `/privacy`                     |
| Man-in-the-middle                        | HTTPS only; HSTS set by Vercel                                 |
| Browser-side event abuse                 | Plausible events are fire-and-forget; no server trust decisions hinge on them |

---

## Hardening baseline

The deployment enforces, via `vercel.json` + Next.js headers:

- `X-Content-Type-Options: nosniff`
- `Referrer-Policy: strict-origin-when-cross-origin`
- `Permissions-Policy: camera=(), microphone=(), geolocation=()`
- `Cache-Control: no-store` on every `/api/*` response
- HTTPS-only via Vercel (HSTS preloaded on the apex domain)
- `poweredByHeader: false` in `next.config.ts`
- No `dangerouslySetInnerHTML` anywhere in the codebase (grep-enforced in CI)

Additional controls planned (tracked in issues):

- Full CSP with `script-src 'self' plausible.io` and no `unsafe-inline`
- Subresource Integrity for the Plausible script
- Signed URLs for any future user-uploaded visuals assets

---

## Dependencies

- **Dependabot** (`.github/dependabot.yml`) opens weekly grouped PRs for npm
  and GitHub Actions.
- **Dependency Review Action** (`.github/workflows/dependency-review.yml`)
  blocks PRs introducing vulnerable transitive dependencies.
- **Lockfile policy**: we commit `package-lock.json`. CI uses `npm ci` only.

---

## Credits

Security researchers who help us harden the site will be listed here (opt-in)
with a link of their choice.

_No disclosures yet — be the first._
