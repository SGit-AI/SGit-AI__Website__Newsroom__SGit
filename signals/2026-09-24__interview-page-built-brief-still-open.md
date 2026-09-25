---
title: riskmandate.ai built the interview page; sgit.ai's briefs index still lists the ask as open
date: 2026-09-24
desk: Cartographer
standfirst: riskmandate.ai has built the interview page sgit.ai asked for, the same day it was asked; sgit.ai's briefs index, in the snapshot taken late that night, still carries the ask as open.
from_site: riskmandate.ai
to_site: sgit.ai
status: new
action: give sgit.ai's team riskmandate.ai's v1.34.2 release note, so the ask can be marked acted on
sources:
  - https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.md
  - https://sgit.ai/docs/briefs/index.md
  - https://riskmandate.ai/versions/1.34.2.md
  - https://riskmandate.ai/versions/1.34.3.md
  - https://riskmandate.ai/interview-founder-marketing.md
  - https://riskmandate.ai/briefs.md
reviewed_by:
reviewed_on:
---

**riskmandate.ai has built the interview page sgit.ai asked for, the same day it was asked; sgit.ai's briefs index, in the snapshot taken late that night, still carries the ask as open.**

## Side A: riskmandate.ai built it

The [v1.34.2 release note](https://riskmandate.ai/versions/1.34.2.md), dated 24 September 2026, is titled "Twenty minutes of your advice, by voice" and opens: "A build brief from the sgit.ai site team". It says the first interview page "is for founders who are good at UK events, marketing and content that spreads", that "The page has the brief's six parts in its order", and that "The pattern is a template": the next page "is one JSON file and one command".

The page is [interview-founder-marketing](https://riskmandate.ai/interview-founder-marketing.md). The [v1.34.3 note](https://riskmandate.ai/versions/1.34.3.md) explains that v1.32.2 to v1.34.2 had not deployed because CI failed, and that "With this release, the UK support page, the two articles, the business cases, the OWASP graph and the interview page reach riskmandate.ai for the first time."

[riskmandate.ai's brief register](https://riskmandate.ai/briefs.md) lists the brief with its sha256 and marks what was not done: a run of the prompt in voice mode, which "the lead runs", and "Sending the summary back into a vault. The brief marks it as later".

## Side B: sgit.ai still says open

The [brief itself](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.md) says "Status: open. Written 24 September 2026." The [briefs index](https://sgit.ai/docs/briefs/index.md), under "Cross-team asks addressed, and status-tracked", has the entry "To the RiskMandate.ai team: an interview page pattern, and the first page on it" with status open.

Both files are stamped site v0.6.8. sgit.ai's git log puts v0.6.7 (the brief) at 20:55 and v0.6.8 at 23:26 on 24 September. riskmandate.ai's notes give dates, not times, so we cannot say which came first; what we can say is that the snapshot of both sites, taken around 23:40 UTC that night, has the page built on one and the ask open on the other.

## What we checked

- The index's other entries show how a closed ask is written: "acted on", with the release that did it. This one has neither.
- The ask is closed in substance by riskmandate.ai; two named parts remain with riskmandate.ai's lead. Both are recorded in [the loose ends](nr:loose-ends).
- A brief written on one site and built on another the same day is the loop the briefs index exists for. The index is the only part that has not caught up.
