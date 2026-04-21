# Contributing to grok-agents-marketplace

Thanks for helping build the public face of GrokInstall at **grokagents.dev**.
This repo is Next.js 15 + TypeScript strict + Tailwind + Biome. Every change
ships behind CI (typecheck, lint, build, Lighthouse) so the bar is "green PR +
no regressions on the brand tokens or telemetry surface."

If this is your first PR, skim the [Code of Conduct](./CODE_OF_CONDUCT.md) and
[Security policy](./SECURITY.md) before opening changes.

---

## TL;DR

```bash
git clone https://github.com/AgentMindCloud/grok-agents-marketplace
cd grok-agents-marketplace
npm install
cp .env.example .env.local   # optional — works offline with mock catalog
npm run dev                  # http://localhost:3000
```

Before pushing:

```bash
npm run typecheck   # tsc --noEmit (strict + noUncheckedIndexedAccess)
npm run lint        # biome check .
npm run test        # vitest run
npm run build       # next build — must pass
```

---

## Local development

### Requirements

- **Node.js ≥ 20** (LTS recommended)
- **npm ≥ 10** — we do not pin the package manager, but lockfile is npm
- A GitHub account for PRs

### Environment variables

All variables are optional for local dev. Copy `.env.example`:

| var                               | purpose                                               |
| --------------------------------- | ----------------------------------------------------- |
| `GITHUB_TOKEN`                    | Raises GitHub API rate limit 60 → 5000/hr. No scopes. |
| `KV_REST_API_URL` / `_TOKEN`      | Vercel KV persistence. Blank = in-memory fallback.    |
| `NEXT_PUBLIC_SITE_URL`            | Canonical URL (defaults to localhost in dev).         |
| `NEXT_PUBLIC_PLAUSIBLE_DOMAIN`    | Blank = analytics disabled. Production = grokagents.dev. |
| `NEXT_PUBLIC_PLAUSIBLE_HOST`      | Optional — self-hosted Plausible host.                |

**Never** commit `.env.local`. The `.gitignore` covers it.

### Offline dev

The catalog fetch falls back to `src/data/featured-agents.mock.json` when
`raw.githubusercontent.com` is unreachable. Install counts fall back to an
in-memory Map when KV env vars are absent. So `npm run dev` always works.

### Folder layout

```
src/
├── app/                # Next.js App Router routes (server-first)
├── components/         # Reusable UI
│   ├── ui/             # Brand primitives (GlassCard, NeonButton, CircuitTrace…)
│   ├── marketplace/    # Agent card, search, filters
│   ├── stats/          # Recharts dashboards
│   └── AgentPreviewCard/  # v2.14 Visuals Renderer
├── lib/                # Server + shared utilities
│   ├── visuals/        # Zod schema + demo media renderer
│   ├── telemetry-*.ts  # CLI telemetry pipeline
│   └── tracking.ts     # Client-side Plausible wrapper
└── types/              # Ambient TS declarations
```

---

## Code style

### Biome rules (no ESLint, no Prettier)

- `npm run lint` runs `biome check .`
- `npm run format` runs `biome format --write .`
- Line width 100, indent 2 spaces, single quotes, trailing commas
- **`noUnusedImports: error`** — unused imports fail CI
- **`noExplicitAny: warn`** — prefer `unknown` and narrow
- **`useImportType: warn`** — use `import type { … }` for type-only imports

Run Biome before you push. CI will reject any `error`-level rule violation.

### TypeScript

- `strict: true`, `noUncheckedIndexedAccess: true`, `noImplicitOverride: true`
- Use the `@/` alias (`@/lib/…`, `@/components/…`) — never relative `../../..`
- Schema validation: **always Zod** (already v4.3.6 in deps). New user-facing
  or wire-contract types go through a `z.object(…).safeParse`. See
  `src/lib/visuals/parse-visuals.ts` for the pattern.

### Tailwind — brand tokens only

**No hardcoded hex values anywhere outside `tailwind.config.ts` and
`src/app/globals.css`.** Every color, shadow, radius, blur, and animation
lives in those two files.

Allowed tokens (abridged — see `tailwind.config.ts` for full set):

| category    | tokens                                                     |
| ----------- | ---------------------------------------------------------- |
| background  | `bg`, `surface`, `surface-raised`                          |
| text        | `ink`, `ink-muted`, `ink-subtle`                           |
| accent      | `cyan`, `cyan-glow`, `green`, `green-glow`, `danger`       |
| border      | `border-subtle`, `border-focus`                            |
| shadow      | `shadow-cyanGlow`, `shadow-cyanGlowSoft`, `shadow-greenGlow` |
| blur        | `backdrop-blur-gi`                                         |
| animation   | `animate-fade-in-up`, `animate-pulse-slow`, `animate-shimmer` |
| font        | `font-display`, `font-body`, `font-mono`                   |

If you need a new token, add it to `tailwind.config.ts` **and** document it
in the README brand table. Don't introduce arbitrary `text-[#abcdef]` values.

### Component conventions

- **Server-first**: Reach for React Server Components by default. Only add
  `'use client'` when you truly need client state, effects, or browser APIs.
- **Use existing primitives**: `GlassCard`, `NeonButton`, `Section`,
  `StatPill`, `CertificationBadgeRow`, `CircuitTrace`. Don't re-implement.
- **Accessibility**: Lighthouse A11y ≥ 95 is enforced by CI. Label every
  icon-only button, keep focus rings visible, test with keyboard only.
- **No inline styles** with color/size values. If you absolutely need them,
  they must reference a CSS variable already defined in `globals.css`.

---

## Telemetry & privacy

We take telemetry seriously. The full pipeline is documented in
[`/privacy`](./src/app/privacy/page.tsx) and [`SECURITY.md`](./SECURITY.md).
When adding a new tracked event:

1. Add the emit site via `src/lib/tracking.ts` (client) or the server-side
   `/api/telemetry` receive path (CLI v2+).
2. **Document the event** on `/privacy` with its name, properties, and why
   it's collected.
3. Never collect PII. No IPs, handles, emails, prompts, or YAML contents.
4. Every custom event name must be `snake_case` and ≤ 40 chars.
5. Property values must be bounded (< 256 chars, no unbounded free text).

Failing any of the above will block the PR in review.

---

## Tests

- Framework: **Vitest** (Node env, no DOM unless needed)
- Location: colocated `__tests__/` folders next to the code under test
- Run: `npm run test` (one-shot) or `npm run test:watch`
- Add a test for **every** new parser, every new API validator, every new
  shared utility. UI snapshot tests are discouraged — they rot fast.

---

## Commit & PR workflow

- **Branches**: `feat/*`, `fix/*`, `chore/*`, `docs/*`
- **Commits**: imperative mood, ≤ 72 chars subject, explain *why* in body
- **PRs**: use the template — it covers tsc, biome, build, Lighthouse, and
  the "no hardcoded hex" checklist.
- **Reviews**: at least one approval from a CODEOWNER (see `.github/CODEOWNERS`)
  for `src/app/api/**` and `vercel.json`.
- **Squash merges only** — we keep `main` linear.

---

## Reporting issues

- Bugs → open a `bug` issue via the template
- Features → `feature` template
- Listing/agent corrections → `agent-listing-issue` template
- **Security** → do **not** open an issue. Follow [SECURITY.md](./SECURITY.md).

---

## Licensing

By contributing, you agree that your contributions are licensed under the
Apache License 2.0, same as the project.
