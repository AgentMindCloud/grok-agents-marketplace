# Merge Plan — grok-agents-marketplace

This file tracks the staged tier-by-tier polish passes that land on `main` for
the public storefront at [grokagents.dev](https://grokagents.dev) and the
marketplace catalog it serves.

## Tier 4 — Spectral Visual Identity (Phase 19)

**Branch:** `claude/spectral-visual-identity-6w97D`
**Goal:** Apply the ultra-premium Spectral visual system across the storefront
and registry-style marketplace surface.

### Palette landed

| Token   | Value     | Role                                |
|---------|-----------|-------------------------------------|
| Plasma  | `#FF1E70` | Primary brand accent · CTAs · hero  |
| Aurora  | `#00E0D5` | Secondary accent · eyebrows · hover |
| Bg      | `#0A0A0A` | Deep field                          |
| Cyan    | `#00F0FF` | Legacy data accent (kept)           |
| Green   | `#00FF9D` | Safety / success states (kept)      |

### What shipped

- **Foundation tokens.** `src/lib/brand.ts`, `tailwind.config.ts`, and
  `src/app/globals.css` now expose the full Spectral set (Plasma, Aurora,
  glow shadows, halftone, nebula, chromatic-aberration, spectral-divider,
  text-spectral). Inter is now the display face; Space Grotesk is a fallback
  only. JetBrains Mono retained for eyebrows + code.
- **NebulaBackdrop** (`src/components/ui/NebulaBackdrop.tsx`). Pure SVG, three
  drifting Plasma + Aurora circles + halftone dot pattern + gradient hairline.
  Used on the home Hero, marketplace hero, section pages, and submit hero.
- **Hero** — `Grok-native` word now uses `text-spectral chromatic-aberration`
  for the chromatic-print effect. Eyebrow chip switched to Plasma; primary CTA
  uses the new `plasma` NeonButton variant; secondary CTA uses Aurora.
- **Marketplace.** `AgentCard`, `MarketplaceGrid`, `FilterPills`, `SearchBar`
  all rewired to Plasma + Aurora. Avatars without an image fall back to a
  halftone-Plasma tile. The "submit your agent" CTA card grew a top
  spectral-divider hairline.
- **Submit form.** Field eyebrows in Aurora, required marker in Plasma,
  focus rings + glow in Plasma, primary submit CTA in Plasma, preview card
  with a top spectral-divider.
- **Header + Footer.** "INSTALL" wordmark now Plasma with `text-glow-plasma`;
  scrolled header border is Plasma/15; column titles in Footer in Aurora;
  bottom hairline replaced with `spectral-divider`.
- **Per-agent preview card.** Visuals schema (`parse-visuals.ts`) now accepts
  `plasma` and `aurora` alongside the legacy `cyan` and `green` accents. Two
  new vitest cases cover them. Premium variant has Plasma + Aurora corner
  glows; futuristic gets a halftone overlay.
- **OG images.** Default OG, per-agent OG, stats snapshot OG and the static
  `public/og-default.svg` all redrawn with the Spectral nebula gradient and
  Plasma wordmark.
- **Brand SVGs.** `public/brand/banner-hero-grok-install.svg`,
  `banner-hero-grok-install-brand.svg`, `wordmark.svg`, `favicon.svg`, plus
  every icon in `public/icons/` recolored to Plasma + Aurora.
- **README.** Capsule-render header + footer regrafted to the Spectral
  gradient; typing-SVG accent now Plasma; every shield-badge color updated;
  Brand System section rewritten with the full Spectral token table and the
  new utility class catalog.

### Validation

- `npm run typecheck` — passes
- `npm run lint` — passes
- `npm run test` — 17 vitest cases pass (15 existing + 2 new for plasma /
  aurora accents in the visuals schema)

### Notes for the next tier

- The `/registry/` route mentioned in Phase 15 does not exist as a separate
  route; the registry-style surface is served through `/marketplace` and
  `/marketplace/sections/*`. Spectral treatment landed on those pages.
- The legacy `cyan` and `green` accents are intentionally kept — chart series
  on `/stats`, vscode-verified badge, and safety-max badges still use them so
  data semantics stay readable.
