# GitHub repo metadata

Set these in **Settings → General → About** after the PR merges.
They make the repo discoverable and set the right first impression.

## Description

```
10 production-ready Grok agent templates. One command to install.
```

## Website

Leave blank for now (or point to the future GitHub Pages URL once enabled).

## Topics

Add these tags in the **Topics** field (comma-separated in the UI):

```
grok  xai  agents  ai-agents  llm  x-api  agent-templates  grok-install
awesome-list  twitter-api
```

## Social preview

Upload `docs/posters/research-swarm.svg` (or any of the other poster cards)
as the social preview image in **Settings → General → Social preview**.
GitHub will use this for link unfurls on X/LinkedIn/Slack.

## Features to enable

| Feature | Action |
|---------|--------|
| Discussions | Settings → General → Features → Discussions ✓ |
| Dependabot alerts | Security → Dependabot → Enable |
| Pages (optional) | Settings → Pages → Source: `main` / `docs` if a Pages site is added |

## Release

After the v0.1.0 PR merges to `main`, create the release via:

1. **Releases → Draft a new release**
2. Tag: `v0.1.0`
3. Title: `v0.1.0 — Initial gallery (10 templates)`
4. Body: paste the `[0.1.0]` section from `CHANGELOG.md`
5. Check **Set as the latest release**
