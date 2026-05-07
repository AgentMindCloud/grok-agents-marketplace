# Security Policy

## Scope

This repo ships **agent templates** and a **stub runtime** for local
development. The in-scope surface is:

| In scope | Examples |
|----------|---------|
| Template safety-gate bypasses | Approval token checks that can be skipped without a token |
| Secret leakage in templates | Hardcoded API keys, non-empty `.env.example` defaults |
| Stub runtime vulnerabilities | Code in `scripts/grok_install_stub/` that could execute arbitrary commands |
| CI / validation script issues | Validators that silently pass malformed templates |

| Out of scope | Why |
|-------------|-----|
| The `grok-install` CLI itself | Published separately by xAI; report to them directly |
| xAI's Grok API | Report via xAI's disclosure channel |
| Third-party dependencies | Report upstream; open a tracking issue here if it affects templates |

## Reporting

Please **do not** open a public GitHub issue for security vulnerabilities.

Email **security@agentmindcloud.com** with:

1. A description of the vulnerability and its impact
2. Steps to reproduce
3. Any relevant file paths or code snippets

We will respond within **72 hours** and aim to ship a fix within **7 days**
for critical issues.

## Supported versions

Only the `main` branch is actively maintained. Fixes are not backported to
feature branches.
