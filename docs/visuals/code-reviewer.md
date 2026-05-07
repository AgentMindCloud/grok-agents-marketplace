# code-reviewer — visual design notes

`code-reviewer` is a developer tool. Its users live in terminals, diffs,
and PR review panes. The visuals should feel like a colleague's tool,
not a marketing page.

## Design choice: minimal developer aesthetic

```yaml
visuals:
  accent_color: "#22c55e"
  theme: minimal
  typography:
    heading_family: "monospace"
    body_family: "monospace"
  preview_card:
    style: minimal
    variant: terminal
    subtitle: "$ grok review <PR>  # inline comments, approval-gated"
    prompt_prefix: "~/repo $ "
    cursor: { enabled: true, blink: true, respect_reduced_motion: true }
```

- **`accent_color: #22c55e`** — the exact green used by
  `scripts/gen_poster.py` for the `permissive` safety indicator.
  Borrowing it here signals "green = shipping" the way a passing CI
  badge does.
- **`theme: minimal` + `variant: terminal`** — the card renders as a
  faux terminal: monospace everything, a prompt prefix, and a blinking
  cursor. No gradients, no glow, no pulse. A developer scanning the
  gallery should recognise this as one of theirs in under a second.
- **`typography.heading_family: monospace`** — the only template that
  uses monospace for the card title too. Consistent with the
  "terminal card" variant.
- **`cursor.blink: true`** — the one motion affordance on the card,
  disabled under `prefers-reduced-motion`.
- **No `auto_generate.demo_media`** — the repo already has an SVG
  poster; a scripted terminal recording would duplicate work and
  inflate the install payload.

## Why green and not blue

Blue is the default "developer tool" accent everywhere. The repo already
owns violet as its canonical brand, so defaulting `code-reviewer` to
blue would collide with half the dev-tool gallery on the internet. The
safety-permissive green is distinctive, ties back to the CI/badges
metaphor, and reads well against the dark canvas.
