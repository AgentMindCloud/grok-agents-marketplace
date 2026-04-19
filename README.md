<div align="center">

# GROKINSTALL · Agents Marketplace

### The community marketplace for Grok-native agents on X

<p>
  <img alt="Next.js" src="https://img.shields.io/badge/Next.js-15-00F0FF?style=flat-square&labelColor=0A0A0A" />
  <img alt="TypeScript" src="https://img.shields.io/badge/TypeScript-strict-00F0FF?style=flat-square&labelColor=0A0A0A" />
  <img alt="Tailwind" src="https://img.shields.io/badge/Tailwind-3-00F0FF?style=flat-square&labelColor=0A0A0A" />
  <img alt="License" src="https://img.shields.io/badge/License-Apache%202.0-00F0FF?style=flat-square&labelColor=0A0A0A" />
</p>

</div>

---

`grok-agents-marketplace` is the public-facing marketplace at **grokagents.dev**
— where anyone can discover, compare, and install Grok-native agents with a
single click. Part of the GrokInstall ecosystem alongside `grok-install`,
`grok-yaml-standards`, `vscode-grok-yaml`, and `grok-install-action`.

## Stack

- **Next.js 15** App Router · React Server Components · Turbopack dev
- **TypeScript** strict, `noUncheckedIndexedAccess` on
- **Tailwind CSS** with locked GrokInstall brand tokens
- **Octokit** for live GitHub star counts (authenticated when `GITHUB_TOKEN` set)
- **Shiki** for YAML syntax highlighting on agent detail pages
- **Biome** for lint + format (no ESLint/Prettier)

## Local dev

```bash
# 1. Install
npm install

# 2. (optional) raise the GitHub API rate limit
cp .env.example .env.local
# edit .env.local and paste a GITHUB_TOKEN — no scopes required

# 3. Run
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

## Data sources

- **Catalog**: `raw.githubusercontent.com/AgentMindCloud/awesome-grok-agents/main/featured-agents.json`,
  revalidated every 10 minutes. On fetch failure the app serves `src/data/featured-agents.mock.json`
  so dev works offline.
- **Stars**: GitHub REST via Octokit, 1-hour in-memory cache, stale-on-error.
  Anonymous works (60 req/hr); setting `GITHUB_TOKEN` raises it to 5000 req/hr.

## Deployment

Target is Vercel. Deploy is wired up in Session 11 — for now, the project
builds fully locally:

```bash
npm run build && npm run start
```

Required env:

- `GITHUB_TOKEN` — recommended, not required. No scopes.
- `NEXT_PUBLIC_SITE_URL` — defaults to `https://grokagents.dev`.

## Project structure

```
src/
├── app/                      App Router
│   ├── layout.tsx            root, loads fonts + theme
│   ├── page.tsx              homepage (hero + featured + latest)
│   ├── globals.css           brand tokens (@tailwind + CSS vars)
│   ├── marketplace/
│   │   ├── page.tsx          search + filter + grid
│   │   └── [id]/page.tsx     agent detail (YAML + install tabs)
│   ├── not-found.tsx         branded 404
│   ├── robots.ts / sitemap.ts
├── components/
│   ├── layout/               Header, Footer, SkipToContent, ThemeProvider
│   ├── ui/                   GlassCard, NeonButton, CertificationBadge,
│   │                         StatPill, CircuitTrace, Skeleton, Section
│   ├── marketplace/          AgentCard, SearchBar, FilterPills,
│   │                         MarketplaceGrid, InstallOnX, InstallTabs,
│   │                         YamlSnippet, CreatorProfile
│   └── home/                 Hero, StatsTeaser, FeaturedCarousel, LatestGrid
├── lib/
│   ├── agents.ts             fetch featured-agents.json + ISR + mock fallback
│   ├── github.ts             Octokit star-count fetcher with cache
│   ├── constants.ts          nav items, cert/category labels, site URLs
│   ├── types.ts              Agent, Certification, Category, SortKey
│   └── utils.ts              cn, formatCount, fuzzyMatch, debounce
└── data/
    └── featured-agents.mock.json   6-agent offline fallback
```

## Brand system

All colors, radii, shadows, blur, and fonts live in `tailwind.config.ts` and
`src/app/globals.css` — nowhere else. No hardcoded hex in components.

| token          | value                       |
| -------------- | --------------------------- |
| `bg`           | `#0A0A0A`                   |
| `cyan`         | `#00F0FF`                   |
| `green`        | `#00FF9D`                   |
| `danger`       | `#FF2D55` (safety only)     |
| `surface`      | `rgba(255,255,255,0.04)`    |
| `border-subtle`| `rgba(0,240,255,0.15)`      |
| `border-focus` | `rgba(0,240,255,0.40)`      |
| `shadow-cyanGlow` | `0 0 24px rgba(0,240,255,0.30)` |
| `backdrop-blur-gi` | `20px`                 |

## Disclaimer

GrokInstall is an independent community project. Not affiliated with xAI,
Grok, or X.

## License

Apache 2.0 — see [LICENSE](./LICENSE).
