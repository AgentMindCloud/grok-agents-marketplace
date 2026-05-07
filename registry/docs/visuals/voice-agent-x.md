# voice-agent-x — visual design notes

`voice-agent-x` is voice-first: the user speaks, the agent transcribes,
humans approve, then it publishes. Visual design has to support users
who may be driving, walking, or using a screen reader — accessibility
is the primary constraint, aesthetics second.

## Design choice: futuristic + haptics + accessibility

```yaml
visuals:
  accent_color: "#f472b6"
  theme: futuristic
  preview_card:
    style: futuristic
    animation: { type: waveform, duration_ms: 1800, respect_reduced_motion: true }
  haptics: { on_record_start: light, on_approval_required: heavy, ... }
  accessibility:
    high_contrast: true
    captions_required: true
    minimum_contrast_ratio: 7.0
    reduced_motion_fallback: static_poster
```

### Accent: pink `#f472b6`

Pink sits opposite cyan on the palette wheel, giving this template its
own lane in the gallery. It's also the highest-signal colour for
"voice / audio" in most design systems.

### Futuristic card with a waveform

The `animation.type: waveform` renders a stylised audio oscilloscope
as the card's background motion. It tells the user at a glance what
this agent does before they read a single word — and it snaps to a
static poster when `prefers-reduced-motion: reduce` is set.

### Haptics block (new in v2.14)

Voice agents are often used hands-busy. Haptics give the user
confirmation without demanding a glance at the screen:

| Event | Strength |
|-------|----------|
| record start | light |
| transcript ready | medium |
| approval required | heavy |
| publish success | success |

`respect_system_preferences: true` — any OS-level "reduce haptics"
setting turns the whole block into a no-op.

### Accessibility, loudly

- **`minimum_contrast_ratio: 7.0`** — WCAG AAA, not AA. Voice-first
  users often have the screen at arm's length; AA isn't enough.
- **`captions_required: true`** — any generated demo media must ship
  with captions. No exceptions.
- **`reduced_motion_fallback: static_poster`** — the poster is the
  ground truth. Motion is a progressive enhancement.
- **`voice_feedback: true`** — state changes (record / review /
  publish) are also announced via the system speech stack for users
  who can't see the waveform.

## Why this template sets the a11y bar

If any template in the gallery deserves a loud a11y block, it's the
voice one. Its presence here also serves as the reference example
other templates can copy when they add visuals.
