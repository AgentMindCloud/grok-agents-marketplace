# thread-ghostwriter — visual design notes

`thread-ghostwriter` exists to produce polished, tone-matched long-form
writing. The visuals mirror the output: considered, quiet, a little
luxurious.

## Design choice: premium

```yaml
visuals:
  accent_color: "#a78bfa"
  theme: premium
  palette: { ..., trim: "#d4af37" }
  typography:
    heading_family: "serif"
    letter_spacing: "0.01em"
  preview_card:
    style: premium
    gradient: { from: "#141123", to: "#2a1f55", angle: 110 }
    trim: { color: "#d4af37", width_px: 1, corners: rounded }
    glow: { intensity: 0.25 }
    animation: { type: fade, duration_ms: 1200 }
```

- **`accent_color: #a78bfa`** — a softer, higher-chroma violet than
  `hello-grok`. Reads as "refined violet" rather than "default violet".
- **`theme: premium`** — a first-class theme in the v2.14 spec,
  distinct from `futuristic`. Opt-in serif headings, subtle gradient,
  low-intensity glow.
- **`trim.color: #d4af37`** — a single hairline of muted gold on the
  card edge. One pixel wide. That's all the "luxury" this template
  gets; any more and it would feel costume.
- **`typography.heading_family: serif`** — the only template that
  overrides the default sans-serif. Threads written by this agent
  lean essayistic, so the card should too.
- **`animation: fade`** — a 1.2s crossfade on hover. No motion on the
  card itself at rest. Quiet.

## Why "premium" and not "futuristic"

`trend-to-thread` and `voice-agent-x` both use `theme: futuristic` —
fast, bright, pulsing. That set of signals is wrong for a writing
agent where the user's first reaction should be trust, not urgency.
The gallery needs at least one template that demonstrates the
`premium` theme so future contributors have a working reference.
