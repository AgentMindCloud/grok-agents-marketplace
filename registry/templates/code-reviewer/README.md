---
title: code-reviewer
description: Reviews GitHub PRs with Grok reasoning. Posts inline comments behind an approval gate.
image: /docs/posters/code-reviewer.png
permalink: /templates/code-reviewer/
---

# code-reviewer

Reads a GitHub PR, reviews it like a senior engineer, and posts inline
comments plus a summary — behind a human approval gate.

![code-reviewer poster](../../docs/posters/code-reviewer.svg)

## What it does

1. Triggered by `opened`, `synchronize`, or `ready_for_review` webhooks.
2. `reader` fetches the PR, the diff, and any surrounding file context it
   needs.
3. `reviewer` drafts inline comments (one per issue, no "is this
   intentional?") and a summary with an explicit verdict.
4. The draft lands in your approval queue.
5. `commenter` posts only approved reviews.

## Install

```bash
grok-install install github.com/agentmindcloud/awesome-grok-agents/templates/code-reviewer
```

## Configure

```bash
cp .env.example .env
# GITHUB_TOKEN needs pull_request:write on the target repo
```

Point GitHub at the webhook endpoint printed by `grok-install schedule`.

## Run

```bash
# One-shot against a specific PR
grok-install run --input repo=owner/repo pr_number=123

# Run the webhook listener
grok-install serve
```

## Safety

- `safety_profile: strict`
- `post_review` behind approval
- Max 1 review per PR (avoids ping-spam on synchronize storms)
- Kill switch: `CODE_REVIEWER_DISABLED=1`
