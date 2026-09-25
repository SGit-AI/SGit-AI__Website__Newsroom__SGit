---
title: Company X-Ray reuses RiskMandate's pricing ladder, and RiskMandate has no sign of knowing
date: 2026-09-24
desk: Architect
standfirst: sgit.ai has a business plan, Company X-Ray, that takes RiskMandate.ai's four-level pricing ladder and its delivery pattern as they stand; riskmandate.ai owns that ladder, and nothing on it mentions the X-Ray plan.
from_site: sgit.ai
to_site: riskmandate.ai
status: new
action: give riskmandate.ai's team the Company X-Ray vault page, so a change to its own ladder is made knowing another plan copies it
sources:
  - https://sgit.ai/demos/vaults/company-xray/index.md
  - src:vaults/company-xray/plan/09-reuse-from-riskmandate.md
  - https://riskmandate.ai/pricing.md
  - https://riskmandate.ai/versions/1.22.0.md
reviewed_by:
reviewed_on:
---

**sgit.ai has a business plan, Company X-Ray, that takes RiskMandate.ai's four-level pricing ladder and its delivery pattern as they stand; riskmandate.ai owns that ladder, and nothing on it mentions the X-Ray plan.**

## Side A: sgit.ai's Company X-Ray plan

The vault page, published on 24 September 2026 in sgit.ai v0.6.8, has a section headed "Four levels, the RiskMandate way". It says:

> "Each level is the level below it plus exactly one thing, as on RiskMandate.ai's pricing page."

Its table of what is reused credits [RiskMandate.ai's pricing and its reviewed level](https://sgit.ai/demos/vaults/company-xray/index.md), "reused as they stand".

The plan's own file, [09-reuse-from-riskmandate.md](src:vaults/company-xray/plan/09-reuse-from-riskmandate.md), opens:

> "The X-ray is a different product with the same shape. Most of what RiskMandate.ai has already built and published carries over as it stands."

It lists nine things taken over, among them the four levels, the rule that each level is the one below plus one thing, free published examples with read keys, standing payment links at store.sgit.ai, "Done is a commit" and the reviewer pages. Its prices differ: the X-Ray's four paid levels are £50, £150, £500 and £1,500. It ends:

> "A founder could run both from one store, with one reviewer pool and one pattern for delivery. That is a decision for the founders, not for this plan."

## Side B: riskmandate.ai, which owns the ladder

[riskmandate.ai's pricing page](https://riskmandate.ai/pricing.md) sells an Agent Behaviour Policy at four levels, "from a pack downloaded for £10 to two sessions and a security professional's signature for £1,500."

The ladder has moved more than once. The [v1.22.0 release note](https://riskmandate.ai/versions/1.22.0.md) records that "this site was saying £5 in six places, including a generator that wrote it onto eighteen vault pages." A plan that copies the ladder inherits each such change, or drifts from it.

## What we checked

- A case-insensitive search of every riskmandate.ai file in the snapshot, and of store.sgit.ai, for "x-ray", "xray", "business-plans", "Lesson Loop" and "Risk Acceptance Office" found nothing.
- The Company X-Ray page and plan both link riskmandate.ai's pricing page, so the reuse runs one way only.
- This is a design copied by a proposal: Company X-Ray is a published business plan, not a running service, and the page marks its numbers as hypotheses.
