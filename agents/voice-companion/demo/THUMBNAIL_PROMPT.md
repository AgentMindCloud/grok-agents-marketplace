# Thumbnail Generation Prompt

> **LOCKED BRAND SPEC — do not deviate.** Whoever renders this thumbnail must follow every item below. The brand is locked. Approximations are not accepted.

## Brand spec (non-negotiable)

- **Background:** pure black `#0A0A0A`. No other background, no gradient to any other hue.
- **Accent:** cyan `#00F0FF` only. No purple, no orange, no pastels, no secondary accent.
- **Motif:** an animated-feeling voice waveform — a clean, thin, horizontal waveform rendered as 1–2 px cyan strokes. The waveform threads across the canvas like a heartbeat, not like a speaker EQ bar. Subtle circuit trace fragments at the edges to tie it to the GrokInstall family.
- **Typography:** Space Grotesk or JetBrains Mono feel. Uppercase, tight tracking (-2 px on display lettering).
- **Composition:** the word **"VOICE"** rendered large, centered slightly above the midline, with a 1–2 px neon-glow edge at 30% opacity. The waveform passes horizontally through the lettering so the glow on the word and the glow on the waveform share one light source.
- **Feel:** Apple polish meets Blade Runner 2049. Calm. Confident. Quietly present — the way a good voice agent feels.
- **Never include:** mascots, people, faces, emojis, microphones as icons, stock photography, drop shadows, light mode, gradients between unrelated hues, generic AI aesthetics.
- **Visual reference:** `grok-install-brand/banners/awesome-grok-agents-banner.svg` — match its restraint and glow treatment.

## Composition prompt

```
A premium 1280x720 thumbnail, pure black #0A0A0A background.

Centered slightly above middle, the word VOICE in uppercase
condensed sans-serif, filling roughly 55 percent of the frame width.
The lettering is cyan #00F0FF with a thin 1-2 px neon-glow edge at
30 percent opacity — surgical, not bloomy.

A single horizontal voice waveform, 1-2 px stroke, cyan #00F0FF,
runs edge-to-edge across the canvas and passes through the middle
of the lettering. The waveform is organic, not symmetric — like a
real utterance captured in a soft moment.

At the left and right thirds, thin fragments of circuit traces
extend off-canvas, tying this to the GrokInstall family.

Below the wordmark, in JetBrains Mono at 1/6 the size of VOICE,
the subtitle: VOICE COMPANION — BUILT FOR GROK ON X

Bottom edge, 12 px from the margin, in 10 pt JetBrains Mono at
50 percent opacity: grokinstall — independent, not affiliated
with xAI, Grok, or X.

No people. No faces. No microphones as icons. No mascots. No
emojis. No stock photography. No drop shadows. No gradients other
than the radial falloff from the glow. Dark mode only.
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

```
agents/voice-companion/demo/thumbnail.png
```

Do not check in sub-resolutions unless explicitly requested — the 1920×1080 master is the single source.
