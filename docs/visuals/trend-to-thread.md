# trend-to-thread — visual design notes

`trend-to-thread` is the gallery's most dynamic agent: it runs on a
30-minute schedule, pulls live X trends, and drafts threaded output.
The visuals lean into that motion.

## Design choice: full futuristic

```yaml
visuals:
  accent_color: "#22d3ee"
  theme: futuristic
  preview_card:
    style: futuristic
    gradient: { from: "#0b0f17", to: "#0e3a49", angle: 135 }
    glow: { enabled: true, color: "#22d3ee", intensity: 0.45 }
    animation: { type: pulse, duration_ms: 2400, respect_reduced_motion: true }
  auto_generate:
    demo_media: true
    demo_length_seconds: 45
```

- **`accent_color: #22d3ee`** — electric cyan. Signals freshness and
  live data, distinct from the default violet. Pairs with the dark
  canvas for high contrast on both light and dark site themes.
- **`gradient` + `glow`** — the card radiates outward, echoing the
  "radar sweep" metaphor of trend monitoring. Glow intensity is held
  at `0.45` so it reads as ambient, not loud.
- **`animation: pulse`** — a slow 2.4s pulse implies the 30-minute
  polling heartbeat. `respect_reduced_motion: true` is non-negotiable:
  any viewer with `prefers-reduced-motion: reduce` gets a static card.
- **`auto_generate.demo_media: true`** — the runtime is allowed to
  produce a 45s preview clip on first install. For a scheduled
  workflow, a static poster undersells the experience; motion sells
  the loop.

## Why cyan, not violet

`hello-grok` claims the canonical violet. Every downstream hero
template differentiates itself with a neighbouring hue in the same
luminance band, so the gallery reads as a cohesive family rather than
ten unrelated brands. Cyan is adjacent to violet on the cool side and
evokes data / network, which fits the template's job.
