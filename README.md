<div align="center">

# GROKINSTALL · Agents Marketplace

### The community marketplace for Grok-native agents on X

<a href="https://grokagents.dev">
  <img
    alt="GrokInstall marketplace — grokagents.dev hero"
    src="./public/brand/banner-hero-grok-install.svg"
    width="760"
  />
</a>

<p>
  <img alt="Next.js" src="https://img.shields.io/badge/Next.js-15-00F0FF?style=flat-square&labelColor=0A0A0A" />
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-strict-00F0FF?style=flat-square&labelColor=0A0A0A" />
  <img alt="Tailwind" src="https://img.shields.io/badge/Tailwind-3-00F0FF?style=flat-square&labelColor=0A0A0A" />
  <img alt="Vercel KV" src="https://img.shields.io/badge/Vercel-KV-00F0FF?style=flat-square&labelColor=0A0A0A" />
  <img alt="License" src="https://img.shields.io/badge/License-Apache%202.0-00F0FF?style=flat-square&labelColor=0A0A0A" />
</p>

**Live:** https://grokagents.dev

</div>

---

`grok-agents-marketplace` is the public-facing marketplace at **grokagents.dev**
— where anyone can discover, compare, and install Grok-native agents with a
single click-to-tweet on X. Part of the GrokInstall ecosystem alongside
`grok-install`, `grok-yaml-standards`, `vscode-grok-yaml`, and
`grok-install-action`.

## What ships here

**Twelve routes** make up the live surface at `grokagents.dev` — nine user-
facing pages plus three dynamically rendered OG / Twitter images
(`/marketplace/[id]/opengraph-image`, `/marketplace/[id]/twitter-image`,
`/stats/snapshot/opengraph-image`).

- `/` — landing with the marketplace, section teasers, and featured agents
- `/marketplace` — searchable, filterable grid of every certified agent
- `/marketplace/[id]` — per-agent page with YAML manifest, demo, install tabs,
  and the one-click **Install on X** button
- `/marketplace/sections/{trending,voice,swarm,new,beginner}` — curated cuts
- `/hall-of-fame` — top-10 by live install count
- `/submit` — client-side form that generates a pre-filled PR on
  `awesome-grok-agents`
- `/stats` — **adoption dashboard**: live counters (agents installed, X posts
  generated, API calls saved, active agents 7d), growth chart with 7d/30d/90d
  toggle, Pro vs Standard stacked area, category breakdown, day×hour heatmap,
  inline Hall of Fame, auto-generated Impact Stories, CSV export, and a
  shareable snapshot OG image
- `/stats/agents/[id]` — per-agent deep dive (install volume, referrers,
  search queries)
- `/privacy` — what we collect, what we don't, how to opt out, 90-day
  retention pledge

## What's new in v2.14

- **Visuals Renderer**: agents can now ship a `visuals` block in their
  manifest that drives a dedicated Preview Card on `/marketplace/[id]`
  — three style variants (`futuristic`, `premium`, `minimal`), two
  accent tokens (`cyan`, `green`), and a media dispatcher that handles
  `gif` / `video` / `image` or falls back to an auto-generated, accent-
  themed inline-SVG placeholder. Source: `src/components/AgentPreviewCard/`.
- **Zod-validated schema**: every `visuals` block is parsed through
  `parseVisuals()` before render. Invalid or hex-coded accents are
  silently dropped — the page falls back to the classic demo iframe, so
  a malformed manifest never breaks a detail page. See
  `src/lib/visuals/parse-visuals.ts` and the 15 vitest cases in
  `src/lib/visuals/__tests__/`.
- **`visuals_block_rendered` event**: a cookieless Plausible custom
  event fires on each preview-card mount with `{ agent_id, accent_color,
  style }`. Documented in full on [`/privacy`](./src/app/privacy/page.tsx).
- **Adoption counter on `/stats`**: a new Sparkle card tracks how many
  catalogued agents have opted into the Visuals Renderer.
- **Brand-token discipline**: the new component surface introduces **zero**
  hardcoded hex values — every color, glow, and border flows from the
  existing tokens in `tailwind.config.ts`.

## Architecture

```mermaid
flowchart LR
  A[Browser] -->|HTML / CSS / JS| V[Vercel Edge / Node]
  V --> N[Next.js 15 App Router]
  N -->|ISR 10m| GH[raw.githubusercontent.com/awesome-grok-agents]
  N -->|Octokit 1h| API[api.github.com /repos]
  A -->|POST /api/track-install*| KV[(Vercel KV)]
  CLI[grok-install CLI v2+] -->|POST /api/telemetry| V
  V -->|zod validate + rate limit| KV
  V -->|Read install counts + events| KV
  A -.->|pageviews + custom events| P[Plausible]
  N -->|/og, /twitter-image, /stats/snapshot/og| OG[dynamic OG via @vercel/og]
  N -->|unstable_cache 30s| V
```

## Stack

- **Next.js 15** App Router · React Server Components · Turbopack dev
- **TypeScript** strict, `noUncheckedIndexedAccess` on
- **Tailwind CSS** with locked GrokInstall brand tokens
- **Octokit** for live GitHub star counts (authenticated when `GITHUB_TOKEN` set)
- **Shiki** for YAML syntax highlighting on agent detail pages
- **@vercel/kv** for install-count persistence (falls back to in-memory in dev)
- **Plausible** privacy-first analytics, opt-in via env var
- **Biome** for lint + format (no ESLint/Prettier)

## Local dev

```bash
npm install

# (optional) configure env
cp .env.example .env.local
# edit .env.local:
#   GITHUB_TOKEN=ghp_...          (raises rate limit; no scopes)
#   KV_REST_API_URL=...           (leave blank for in-memory fallback)
#   NEXT_PUBLIC_PLAUSIBLE_DOMAIN= (leave blank to disable analytics)

npm run dev
# → http://localhost:3000
```

Commands:

| command             | purpose                                  |
| ------------------- | ---------------------------------------- |
| `npm run dev`       | Next.js dev server on :3000              |
| `npm run build`     | Production build (prerenders all agents) |
| `npm run start`     | Serve the production build               |
| `npm run typecheck` | `tsc --noEmit`                           |
| `npm run lint`      | `biome check .`                          |
| `npm run format`    | `biome format --write .`                 |

## Deploy (Vercel)

1. Import the repo in Vercel → new project, Next.js preset.
2. **Storage** → Create KV database, attach to the project (exposes `KV_REST_API_URL` + `KV_REST_API_TOKEN`).
3. **Environment Variables** (both Production + Preview):
   - `GITHUB_TOKEN` — no scopes needed
   - `NEXT_PUBLIC_SITE_URL=https://grokagents.dev`
   - `NEXT_PUBLIC_PLAUSIBLE_DOMAIN=grokagents.dev`
   - `NEXT_PUBLIC_PLAUSIBLE_HOST` — optional (self-hosted Plausible)
   - KV vars get injected by the integration in step 2
4. **Domain** → add `grokagents.dev` and `www.grokagents.dev`, set the
   apex as the primary.

### DNS records

Configure at your registrar:

| Host  | Type  | Value                      |
| ----- | ----- | -------------------------- |
| `@`   | A     | `76.76.21.21`              |
| `www` | CNAME | `cname.vercel-dns.com`     |

Then flip to HTTPS-everywhere in the domain settings.

## Data sources

- **Catalog**: `raw.githubusercontent.com/AgentMindCloud/awesome-grok-agents/main/featured-agents.json`,
  revalidated every 10 minutes. On fetch failure the app serves
  `src/data/featured-agents.mock.json` so dev works offline.
- **Trending**: `raw.githubusercontent.com/AgentMindCloud/awesome-grok-agents/main/trending.json`
  (optional). When absent, `/marketplace/sections/trending` sorts by live
  install counts.
- **Stars**: GitHub REST via Octokit, 1-hour in-memory cache, stale-on-error.
- **Install counts**: Vercel KV (`install:total:<agentId>` + ZSET
  `install:recent:<agentId>` for 7-day windows). In-memory fallback in dev.

## API

| route                                 | method | purpose                                                                         |
| ------------------------------------- | ------ | ------------------------------------------------------------------------------- |
| `/api/agents`                         | GET    | Catalog + merged install counts (60s SWR cache)                                 |
| `/api/track-install`                  | POST   | Marketplace button clicks: `{ agent_id, source }` → increments counts          |
| `/api/track-install-intent`           | POST   | X-intent variant (post to X without redirecting)                                |
| `/api/telemetry`                      | POST   | CLI telemetry — zod-validated payload, per-`anon_install_id` rate-limited, 204  |
| `/api/stats/public`                   | GET    | Public aggregate JSON (IP rate-limited, CORS-enabled, 30s SWR)                  |
| `/api/stats/summary`                  | GET    | Agent-level install summary, used by dashboard                                  |
| `/api/stats/daily/[agentId]`          | GET    | 30-day per-agent daily series (zero-filled, 5-min cache)                        |
| `/api/stats/growth?period=&metric=`   | GET    | Aggregate growth series (installs/posts/savings × 7d/30d/90d)                   |

Cookie-based endpoints (`/api/track-install*`) set a first-party `gi_anon`
HttpOnly cookie for anonymous de-duplication (1-year). The CLI telemetry path
uses a locally-generated, rotatable `anon_install_id` instead — see `/privacy`.

### CLI telemetry payload

```json
{
  "event": "deploy",
  "timestamp": "2026-04-19T08:15:02.341Z",
  "cli_version": "2.0.4",
  "agent_category": "voice",
  "used_pro_mode": true,
  "used_swarm": false,
  "used_voice": true,
  "safety_score": 97,
  "agent_count": 1,
  "success": true,
  "anon_install_id": "k3r9s1-abc-0af4..."
}
```

The receive endpoint is CORS-open and rate-limited to **30 events/minute per
`anon_install_id`**; excess requests return `429 { error: "rate_limited" }`
with `Retry-After`. Events persist in Vercel KV (or in-memory in dev) for
90 days; aggregated counters on `/stats` live indefinitely.

## Submitting an agent

Head to `/submit`, fill in the form, click **Open pre-filled PR** — you’ll
land on GitHub with the PR body pre-populated against
`awesome-grok-agents`. Or copy the markdown body and open a PR manually.

## Brand system

All colors, radii, shadows, blur, and fonts live in `tailwind.config.ts` and
`src/app/globals.css` — nowhere else. No hardcoded hex in components.

| token                | value                           |
| -------------------- | ------------------------------- |
| `bg`                 | `#0A0A0A`                       |
| `cyan`               | `#00F0FF`                       |
| `green`              | `#00FF9D`                       |
| `danger`             | `#FF2D55` (safety only)         |
| `surface`            | `rgba(255,255,255,0.04)`        |
| `border-subtle`      | `rgba(0,240,255,0.15)`          |
| `border-focus`       | `rgba(0,240,255,0.40)`          |
| `shadow-cyanGlow`    | `0 0 24px rgba(0,240,255,0.30)` |
| `backdrop-blur-gi`   | `20px`                          |

## Disclaimer

GrokInstall is an independent community project. Not affiliated with xAI,
Grok, or X.

## License

Apache 2.0 — see [LICENSE](./LICENSE).
