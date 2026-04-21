<!--
Thanks for the PR! Please fill in every section below. An empty template
means the reviewer has to do the archaeology — and that's slower for
everyone. See CONTRIBUTING.md for the full contributor guide.
-->

## Summary

<!-- 1–3 sentences: what does this change, and why? Focus on the WHY. -->

## Screenshots / videos

<!--
For any UI change, attach a before + after screenshot or a short clip.
For API-only changes, paste the request/response pair or a curl example.
-->

| before | after |
| ------ | ----- |
|        |       |

## Checklist — local verification

- [ ] `npm run typecheck` passes (strict + `noUncheckedIndexedAccess`)
- [ ] `npm run lint` passes (biome, 0 errors)
- [ ] `npm run test` passes (vitest)
- [ ] `npm run build` succeeds (`next build` — no warnings that weren't already present on `main`)
- [ ] Lighthouse on the Vercel preview: Performance ≥ 90, Accessibility ≥ 95, Best Practices ≥ 95, SEO ≥ 95
- [ ] No hardcoded hex / rgb values added (brand tokens only — see CONTRIBUTING)
- [ ] No new top-level npm dependency added (or: adding `<name>` because `<reason>`)

## Checklist — telemetry & privacy

_Skip this section if your PR does not touch telemetry, cookies, or
tracking code._

- [ ] No new PII fields collected (no IPs, handles, emails, YAML contents, prompts)
- [ ] Any new Plausible event is documented on `/privacy`
- [ ] Any new wire-contract field is Zod-validated server-side
- [ ] Event name is `snake_case`, ≤ 40 chars, property values bounded
- [ ] Retention + opt-out paths still work (90-day purge, `--no-telemetry` flag)

## Checklist — accessibility & brand

- [ ] Keyboard focus visible on every new interactive element
- [ ] Icon-only buttons have an accessible label (`aria-label` or visible text)
- [ ] New colors / shadows / radii added through `tailwind.config.ts`, not inline
- [ ] Text contrast passes WCAG AA at the declared ink token

## Rollout plan

<!-- For risky changes only: feature flag, staged rollout, or "ship it". -->

- [ ] Ship on merge (safe default)
- [ ] Gate behind env var: `NEXT_PUBLIC_...`
- [ ] Needs a data migration — see `migrations/` PR: #

## Related issues

<!-- Closes #123 / Refs #456 — GitHub auto-links these. -->

Closes #
