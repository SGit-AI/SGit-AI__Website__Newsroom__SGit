---
title: riskmandate.ai asks how to restore an edited calendar event; sgit.ai's Connector Twin answers it the same day
date: 2026-09-24
desk: Architect
from_site: sgit.ai
to_site: riskmandate.ai
status: new
action: give riskmandate.ai's team the Connector Twin article, as a control that answers the question its calendar article ends on
sources:
  - https://sgit.ai/articles/connector-twin-before-you-deploy-an-agent.md
  - https://sgit.ai/demos/vaults/connector-twin/index.md
  - https://riskmandate.ai/article-calendar-edits-cannot-be-undone.md
  - https://riskmandate.ai/versions.md
reviewed_by:
reviewed_on:
---

**On 24 September both sites published an article on the same fact: an agent that edits a calendar event leaves nothing a user can restore. riskmandate.ai ends by asking readers for a way to restore an edited event. sgit.ai's article proposes one, a twin of the connector that captures the event's before-state, and neither article links the other.**

## Side A: sgit.ai's Connector Twin

[Before you give an agent a connector, give the connector a twin](https://sgit.ai/articles/connector-twin-before-you-deploy-an-agent.md), sgit.ai v0.6.3, 24 September 2026. It checks Google's pages the same day and reaches the same finding: "A moved calendar event has no version history a user can open."

Its answer is a journal of every connector call, appended to a write-only lane and replayed "with a before and after for every change and a revert plan for each one." In its table of what the twin can put back, the row "Move or edit an event" reads "Yes, exactly, from the captured before-state", and what it cannot undo is "The notifications already sent, and a second round when it is moved back".

The same idea is a published business plan, the [Connector Twin vault](https://sgit.ai/demos/vaults/connector-twin/index.md).

## Side B: riskmandate.ai's calendar article

[A deleted meeting comes back. An edited one does not.](https://riskmandate.ai/article-calendar-edits-cannot-be-undone.md), released in riskmandate.ai v1.32.3 on 24 September 2026 (see the [version record](https://riskmandate.ai/versions.md)), says an agent allowed to edit a calendar can leave "fifty meetings moved, re-titled or stripped of their guests, each still looking like a real meeting, with nothing to restore them from." It ends:

> "If you know a way to restore an edited Calendar event that Google’s pages do not mention, tell us and we will correct this page with a date."

## What we checked

- Searched the riskmandate.ai article for "twin", "journal", "replay", "revert" and "sgit": none.
- The sgit.ai article mentions RiskMandate.ai and the Licence to Operate vault, but not the calendar article.
- The twin does not contradict riskmandate.ai: it restores from its own capture, not from anything Google keeps, so the article's claim about Google's pages still stands. What the twin offers is a control to put against the risk, which is the grammar riskmandate.ai already uses: a control that leaves a smaller residual risk.
- The Connector Twin is a business plan whose replay runs on an invented scheduling assistant, not a running service; the vault page says so.
