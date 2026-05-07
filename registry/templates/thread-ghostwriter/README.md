---
title: thread-ghostwriter
description: Turns a rough idea into a polished, tone-matched X thread ready for approval.
image: /docs/posters/thread-ghostwriter.png
permalink: /templates/thread-ghostwriter/
---

# thread-ghostwriter

You give it a rough idea. It reads your recent X posts, learns your voice,
and drafts a polished thread that sounds like you wrote it.

![thread-ghostwriter poster](../../docs/posters/thread-ghostwriter.svg)

## What it does

1. First run: `voice_profiler` loads your recent 200 posts and extracts a
   voice profile (tweet length, punctuation habits, hook patterns).
2. `ghostwriter` loads that profile and drafts a thread on your idea,
   matching the profile.
3. Draft lands in the approval queue.
4. `poster` publishes only approved drafts.

The voice profile is cached — runs after the first skip straight to
drafting.

## Install

```bash
grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/thread-ghostwriter
```

## Configure

```bash
cp .env.example .env
```

## Run

```bash
grok-install run --input idea="what I learned from shipping grok-install" length=7
```

## Safety

- `safety_profile: strict`
- Max 3 threads per day
- `post_thread` gated behind approval
- Kill switch: `GHOSTWRITER_DISABLED=1`
