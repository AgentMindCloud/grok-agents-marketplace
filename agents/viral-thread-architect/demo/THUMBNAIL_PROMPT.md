# Thumbnail Generation Prompt

> **LOCKED BRAND SPEC — do not deviate.** Whoever renders this thumbnail (human designer, Claude Design, or any AI image tool) must follow every item below. The brand is locked. Approximations are not accepted.

## Brand spec (non-negotiable)

- **Background:** pure black `#0A0A0A`. No other background, no gradient to any other hue.
- **Accent:** cyan `#00F0FF` only. No purple, no orange, no pastels, no secondary accent.
- **Motif:** animated-feeling circuit traces — thin, 1 px strokes, threading across the canvas like a neural-circuit map. No stock tech imagery, no abstract blobs.
- **Typography:** Space Grotesk or JetBrains Mono feel. Uppercase or technical styling. Tracking tight (-2 px) on display lettering.
- **Composition:** the word **"THREAD"** rendered large and centered, with neon-glow edges (1 to 2 px cyan halo at 30% opacity). The glow is on hero lettering only — not on decoration.
- **Feel:** Apple polish meets Blade Runner 2049. Premium, calm, confident. Quiet, not loud.
- **Never include:** mascots, people, emojis, stock photography, drop shadows, light mode, gradients between unrelated hues, generic AI-art aesthetics.
- **Visual reference:** `grok-install-brand/banners/awesome-grok-agents-banner.svg`. Match that banner's treatment of circuit traces, node dots, and neon glow.

## Composition prompt

```
A premium 1280x720 thumbnail, pure black #0A0A0A background.
The word THREAD in uppercase condensed sans-serif, centered slightly
above middle, filling roughly 55 percent of the frame width. The
lettering is rendered in cyan #00F0FF with a thin 1-2 px neon glow
at 30 percent opacity — confident, calm, surgical.

Behind the lettering: thin 1 px cyan circuit traces branching
across the full canvas like a sparse neural map. Tiny round cyan
nodes at trace junctions, some slightly brighter than others to
imply signal flow. No motion blur. Crisp edges.

Below the wordmark, in JetBrains Mono at 1/6 the size of THREAD,
the subtitle: VIRAL THREAD ARCHITECT — BUILT FOR GROK ON X

Bottom edge, 12 px from the margin, in 10 pt JetBrains Mono at
50 percent opacity: grokinstall — independent, not affiliated
with xAI, Grok, or X.

No people. No mascots. No emojis. No stock photography. No drop
shadows. No gradients other than the subtle radial falloff from
the glow. Dark mode only.
```

## Technical specs

| Field | Value |
|---|---|
| Dimensions | 1280×720 (16:9 thumbnail) and 1920×1080 export |
| Format | PNG preferred, SVG acceptable |
| Color space | sRGB |
| Background | `#0A0A0A` solid |
| Accent | `#00F0FF` only |
| File size target | under 400 KB |

## Disclaimer placement

The independence disclaimer must be present on the thumbnail itself at bottom-center, small (~10 pt equivalent), 50% opacity:

> GrokInstall is an independent community project. Not affiliated with xAI, Grok, or X.

## Output path

Save generated asset to:

```
agents/viral-thread-architect/demo/thumbnail.png
```

Do not check in sub-resolutions unless explicitly requested — the 1920×1080 master is the single source.
