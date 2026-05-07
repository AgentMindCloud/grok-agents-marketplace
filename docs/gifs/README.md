# Demo gifs

Each template links to a demo gif at `docs/gifs/<template-name>.gif`. This
directory holds those recordings.

## Standards

- **Length**: ≤ 60 seconds
- **Dimensions**: 1280×720 or 1920×1080, 30fps
- **Size**: keep under 5 MB so the README stays fast
- **Content**: show the end-to-end flow — install, configure one env var,
  first useful output. Don't show raw API keys or personal data.

## Tools

Any of these work: [vhs](https://github.com/charmbracelet/vhs) for
terminal recordings, [LICEcap](https://www.cockos.com/licecap/) for
cross-platform screen capture, or `ffmpeg` to convert a screen recording.

## Adding one

1. Record the flow.
2. Optimize: `gifsicle -O3 input.gif -o docs/gifs/<name>.gif`
3. Confirm the README's image reference matches the filename.
4. Commit the `.gif` with the template change in the same PR.

The following templates ship without a gif yet — PRs welcome:

- hello-grok
- reply-engagement-bot
- trend-to-thread
- research-swarm
- code-reviewer
- thread-ghostwriter
- personal-knowledge
- scientific-discovery
- voice-agent-x
- live-event-commentator
