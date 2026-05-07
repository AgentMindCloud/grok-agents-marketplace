---
title: viral-thread-architect
description: Multi-agent swarm that turns a rough idea into a viral X thread.
image: /docs/posters/viral-thread-architect.png
permalink: /agents/viral-thread-architect/
---

<div align="center">

# Viral Thread Architect

**Turn any idea into a fire X thread in seconds — with images, voice version, and perfect formatting.**

![Grok-Native Certified](https://img.shields.io/badge/Grok--Native-Certified-00F0FF?style=for-the-badge&labelColor=0A0A0A)
![Safety: strict](https://img.shields.io/badge/Safety-Strict-00FF9D?style=for-the-badge&labelColor=0A0A0A)
![Pattern: swarm](https://img.shields.io/badge/Pattern-Swarm-00F0FF?style=for-the-badge&labelColor=0A0A0A)
![Runtime: grok--4.20--multi--agent](https://img.shields.io/badge/Runtime-grok--4.20--multi--agent-00F0FF?style=for-the-badge&labelColor=0A0A0A)

[Install on X](https://x.com/intent/post?text=%40grok%20install%20github.com%2Fagentmindcloud%2Fawesome-grok-agents%2Fagents%2Fviral-thread-architect) · [Example output](demo/EXAMPLE_THREAD.md) · [Demo script](demo/SCRIPT.md)

</div>

---

## What it does

A 3-agent swarm produces one polished X thread end-to-end:

1. **Coordinator** pulls live X + web context for the topic.
2. **Lucas** (creative) writes a cold, scroll-stopping hook and requests a hero image.
3. **Benjamin** (logic) structures the body into 8–12 posts, one beat per post, image slots at the start, middle, and close.
4. The coordinator assembles the final thread, runs the safety + cost gates, and optionally synthesizes a voice-narrated version.
5. Human approval token is required before anything is posted.

## Install on X

Mention Grok on X with the install command:

```
@grok install github.com/agentmindcloud/awesome-grok-agents/agents/viral-thread-architect
```

Or via CLI:

```bash
pip install grok-install
grok-install install github.com/agentmindcloud/awesome-grok-agents/agents/viral-thread-architect
```

## Quick start (3 steps)

```bash
# 1. Install
grok-install install github.com/agentmindcloud/awesome-grok-agents/agents/viral-thread-architect

# 2. Configure — fill XAI_API_KEY and X_OAUTH_TOKEN
cd viral-thread-architect
cp .env.example .env

# 3. Run with your idea
grok-install run --input idea="what I learned shipping a multi-agent swarm"
```

Or, trigger it from inside X by replying to any post with:

```
@VirtualThreadArchitect thread: <your idea>
```

## Features

| Feature | Notes |
|---|---|
| Multi-agent reasoning | Coordinator + Lucas + Benjamin running in parallel where possible (`max_parallel_calls: 4`). |
| Image generation | Hero + inline visuals, style-locked to the brand palette (`#0A0A0A` bg, `#00F0FF` accent). |
| Voice version | Optional MP3 narration, 165 wpm, 420 ms pacing between posts. |
| Safety gates | Human approval on every post. Banned category block. Daily + per-thread rate limits. |
| Cost ceiling | Hard-capped at $5/day, $0.50/thread. Halts with alert on ceiling hit. |
| Observability | Every event logged to `grok-analytics://viral-thread-architect`. |

## YAML highlight — `grok-swarm.yaml`

The multi-agent shape is defined in one file:

```yaml
swarm:
  id: thread-architect-swarm
  version: 2.0
  agents:
    - id: coordinator
      role: orchestrator
      model: grok-4.20-multi-agent
      tools: [x_search, web_search]
      prompt_ref: coordinator
    - id: creative        # Lucas — writes hooks
      role: lucas
      model: grok-4.20
      tools: [image_generation]
      prompt_ref: hook_writer
    - id: logic           # Benjamin — structures body
      role: benjamin
      model: grok-4.20
      prompt_ref: thread_structure
  state:
    encrypted: true
    persistence: session-only
  orchestration:
    timeout_seconds: 60
    max_parallel_calls: 4
    strategy: coordinator_delegates
```

## Customization

| Change | Edit this |
|---|---|
| Persona / writing voice | `.grok/agent.yaml` → `persona` |
| Prompt wording | `.grok/prompts.yaml` |
| Thread length bounds | `.grok/prompts.yaml` (`thread_structure.8 to 12 posts`) + `.grok/safety.yaml` (`max_posts_per_thread`) |
| Image style hints | `.grok/tools.yaml` → `image_generation.style_hints` |
| Voice on/off | `.grok/grok-voice.yaml` → `enabled` |
| Banned categories | `.grok/safety.yaml` → `banned_categories` |
| Daily cap | `.grok/safety.yaml` → `rate_limits.max_threads_per_day` |
| Cost ceiling | `.grok/deployment.yaml` → `cost_controls` |

## Safety

- **Profile:** `strict`
- **Approval required:** `post:thread` — a human signs off on every thread before it publishes
- **Human review trigger:** any topic mentioning real named people, brands/trademarks, or market/election predictions
- **Banned:** election misinformation, medical advice, financial advice, explicit content, minors, harassment, self-harm
- **Rate limits:** 10 threads/day, 12 posts/thread max, 5-minute cooldown between threads
- **Kill switch:** `VIRAL_THREAD_DISABLED=1` halts all posting immediately
- **Audit log:** every post recorded, 30-day retention

Full self-check: [SAFETY-REPORT.md](SAFETY-REPORT.md) → **100/100**.

## Demo

- 30-second walkthrough script: [demo/SCRIPT.md](demo/SCRIPT.md)
- Example output thread: [demo/EXAMPLE_THREAD.md](demo/EXAMPLE_THREAD.md)
- Thumbnail generation prompt (brand-locked): [demo/THUMBNAIL_PROMPT.md](demo/THUMBNAIL_PROMPT.md)

---

<div align="center">

Built with **GrokInstall** · Built for Grok on X

_GrokInstall is an independent community project. Not affiliated with xAI, Grok, or X._

</div>
