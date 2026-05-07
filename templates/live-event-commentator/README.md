---
title: live-event-commentator
description: Real-time event commentary on X with strict rate limits and a kill switch.
image: /docs/posters/live-event-commentator.png
permalink: /templates/live-event-commentator/
---

# live-event-commentator

Covers a live event on X in real time — without the usual "engagement bot"
cringe. Picky about what counts as a moment, strict about pacing, kill
switch built in.

![live-event-commentator poster](../../docs/posters/live-event-commentator.svg)

## What it does

1. `listener` samples the X stream for the event query every 20 seconds.
   Calls `detect_moment` only on meaningful shifts — volume spikes,
   sentiment flips, genuinely notable posts.
2. `commentator` drafts one reaction per moment. No hype, no "wow".
3. `fast_approval` batches drafts in a 30-second window so the human in
   the loop can tap through them.
4. `poster` enforces a 120s cooldown and a 20-posts-per-hour cap. Never
   spams.

## Install

```bash
grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/live-event-commentator
```

## Configure

```bash
cp .env.example .env
```

## Run

```bash
grok-install run --input event_query="xAI Day" duration_minutes=60
```

Stop at any time by setting `COMMENTATOR_DISABLED=1` — in-flight drafts
that haven't been posted will be dropped.

## Safety

- `safety_profile: strict`
- Approval on every post (batched for speed)
- 120s minimum gap between posts, max 20/hour
- Kill switch: `COMMENTATOR_DISABLED=1`
