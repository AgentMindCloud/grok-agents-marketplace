# Changelog

All notable changes to **grok-agents-marketplace** are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and the project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- `.env.example`: `POSTGRES_URL` and `TELEMETRY_HMAC_SECRET` entries
  documenting the upcoming Vercel Postgres backend for telemetry and
  the HMAC signing secret shared with `grok-install` CLI v2.1+.
- `DISCLAIMER.md`: non-affiliation notice, no-warranty statement,
  third-party agent disclaimer, and API-usage responsibility clause.
- `.github/FUNDING.yml`: GitHub Sponsors / custom funding links for the
  repo's Sponsor button.
- `CHANGELOG.md`: this file.

### Notes
- Session 8 is **additive config + meta files only**. The Next.js app,
  API routes, and Vercel build configuration are unchanged.
- `LICENSE` (Apache 2.0) was already present; no change.

## [0.1.0] — 2026-04-19

Initial public launch of **grokagents.dev**. Shipped across sessions
10–12:

### Added
- Next.js 15 App Router scaffold with GrokInstall brand tokens
  (`tailwind.config.ts`, `src/app/globals.css`), Biome lint/format,
  strict TypeScript with `noUncheckedIndexedAccess`.
- `/` landing page with marketplace teaser and featured agents grid.
- `/marketplace` searchable, filterable grid backed by the
  `awesome-grok-agents` catalog (`featured-agents.json`, ISR 10m).
- `/marketplace/[id]` per-agent detail page with Shiki YAML
  highlighting, demo block, install tabs, and one-click **Install on X**
  button.
- `/marketplace/sections/{trending,voice,swarm,new,beginner}` curated
  cuts; trending falls back to live install counts when
  `trending.json` is absent.
- `/hall-of-fame` top-10 by Vercel KV install counts.
- `/submit` client-side form that generates a pre-filled PR body
  against `awesome-grok-agents`.
- `/stats` adoption dashboard: live counters, 7d/30d/90d growth chart,
  Pro vs Standard stacked area, category breakdown, day×hour heatmap,
  inline Hall of Fame, auto-generated Impact Stories, CSV export,
  shareable snapshot OG image.
- `/stats/agents/[id]` per-agent deep dive.
- `/privacy` page documenting what we collect, retention, and opt-out.
- `/api/agents` — catalog + merged install counts (60s SWR).
- `/api/track-install`, `/api/track-install-intent` — marketplace button
  clicks with HttpOnly `gi_anon` dedup cookie.
- `/api/telemetry` — CLI telemetry endpoint, zod-validated, rate-limited
  to 30 events/min per `anon_install_id`, CORS-open, 204 on success.
- `/api/stats/public`, `/api/stats/summary`, `/api/stats/daily/[agentId]`,
  `/api/stats/growth` — public aggregates, IP rate-limited.
- Vercel KV persistence with in-memory fallback for local dev.
- Dynamic OG routes: `/og`, `/twitter-image`, `/stats/snapshot/og`.
- Plausible analytics integration, opt-in via
  `NEXT_PUBLIC_PLAUSIBLE_DOMAIN`.
- `migrations/001_telemetry.sql` — Postgres schema for telemetry
  events (not yet wired up).
- Apache 2.0 license.
