---
title: Two risk acceptance ladders, and a plan that has already chosen between them
date: 2026-09-24
desk: Architect
from_site: risks.sgit.ai
to_site: riskmandate.ai
status: new
action: give riskmandate.ai's team the Risk Acceptance Office plan's open question on which ladder, with risks.sgit.ai's ladder beside it
sources:
  - https://risks.sgit.ai/llms-full.txt
  - https://sgit.ai/demos/vaults/risk-acceptance/index.md
  - src:vaults/risk-acceptance/plan/02-the-method.md
  - src:vaults/risk-acceptance/plan/10-open-questions.md
  - https://riskmandate.ai/acceptable.md
reviewed_by:
reviewed_on:
---

**risks.sgit.ai publishes a six-rung acceptance interval ladder, and sgit.ai's Risk Acceptance Office plan has adopted it. riskmandate.ai's "Accepted is not acceptable" page frames the intervals differently, and nothing on riskmandate.ai shows that the plan has named the difference as an open question.**

## Side A: risks.sgit.ai, and the plan that follows it

[risks.sgit.ai](https://risks.sgit.ai/llms-full.txt), concept C3, "The acceptance interval ladder":

> "Six rungs: 1h, 4h, 1d, 1w, 1m, 6m, default one month."

The same entry also describes the rungs in bands ("Under 24 hours means pull the plug; a day to a week is a lower-grade incident"), so risks.sgit.ai itself carries both framings side by side.

The [Risk Acceptance Office plan](https://sgit.ai/demos/vaults/risk-acceptance/index.md), published on sgit.ai on 24 September 2026, says its research found that "The published method disagrees with itself in four places: two different interval ladders, ..." Its method file, [02-the-method.md](src:vaults/risk-acceptance/plan/02-the-method.md), tabulates the six rungs "As published on risks.sgit.ai" and then says:

> "RiskMandate.ai's "Accepted is not acceptable" page publishes different bands (1 to 24 hours, 1 day to 1 week, 1 week to 1 month as the default, 1 to 3 months, over 3 months). The plan uses the risks.sgit.ai ladder and lists the reconciliation as an open question."

The first of its [open questions](src:vaults/risk-acceptance/plan/10-open-questions.md) is "Which ladder?", ending "a single published ladder would help every client conversation."

## Side B: riskmandate.ai

[riskmandate.ai's "Accepted is not acceptable" page](https://riskmandate.ai/acceptable.md) states the rule in its own terms: "Anything under a week is an incident", and, on when a risk should come back, "roughly a month far above, three months mid, six months at or near the line."

## What we checked

- The markdown copy of riskmandate.ai's page in the snapshot does not carry the band labels the plan quotes ("1 to 24 hours" and so on); they may be on the rendered HTML page, which is not in the snapshot. The two phrasings above are what the markdown copy says.
- riskmandate.ai's acceptable and acceptance pages do not link risks.sgit.ai. Across the whole riskmandate.ai snapshot, risks.sgit.ai appears once, in the v1.4.0 release note.
- No riskmandate.ai file mentions the Risk Acceptance Office plan.
- Whether one ladder should win is not for this newsroom to say. The signal is that the question has been asked on one site and not yet reached the other.
