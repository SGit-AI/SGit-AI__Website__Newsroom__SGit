---
title: riskmandate.ai had a voice feedback interview two weeks before sgit.ai briefed the pattern
date: 2026-09-24
desk: Developer
from_site: riskmandate.ai
to_site: sgit.ai
status: new
action: give sgit.ai's team riskmandate.ai's feedback page and its v0.12.2 note, so the interview-page brief names the pattern's first version and the two prompts can be compared
sources:
  - https://riskmandate.ai/feedback.md
  - https://riskmandate.ai/versions/0.12.2.md
  - https://riskmandate.ai/versions.md
  - https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.md
  - https://sgit.ai/docs/briefs/index.md
  - https://riskmandate.ai/versions/1.34.2.md
reviewed_by:
reviewed_on:
---

**riskmandate.ai has run a voice interview page since early September: a prompt the reader pastes into a chat assistant, which interviews them by voice and writes a debrief they send back. sgit.ai's brief of 24 September describes the same shape as a new, reusable pattern and does not mention it.**

## Side A: riskmandate.ai's feedback page

The [v0.12.2 release note](https://riskmandate.ai/versions/0.12.2.md), dated 8 September 2026 and marked reconstructed in the [version record](https://riskmandate.ai/versions.md), added `team/prompts/voice-feedback-interview.md`, a prompt to run a voice-mode "feedback interview with people who have seen a RiskMandate presentation, and produce a debrief." It "keeps turns short for voice, leads the debrief with objections rather than praise, asks consent to quote explicitly".

v0.13.0, on 9 September, added the "feedback page". [That page](https://riskmandate.ai/feedback.md) says: "Saw a RiskMandate demo?" and sets out "Six steps, about twenty minutes." Its sections include "It asks for criticism first" and "You control what we see".

## Side B: sgit.ai's brief

The [interview-page brief](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.md) asks for a page that carries a prompt, which interviews the reader by voice "for about twenty minutes" and writes up "their ideas, a thirty, sixty and ninety day action plan, and candid feedback". Its entry on [the briefs index](https://sgit.ai/docs/briefs/index.md) calls it "A reusable page pattern for getting feedback from people whose knowledge is in their heads." It lists who the pattern could serve next, "investors, CISOs, insurers and GRC practitioners", and asks that "Candour is asked for explicitly."

Neither the brief nor the index mentions riskmandate.ai's feedback page or its prompt.

## What we checked

- Searched sgit.ai and the CLI briefs for "feedback.html" and "feedback.md": no hits.
- riskmandate.ai's own [v1.34.2 note](https://riskmandate.ai/versions/1.34.2.md), which built the new interview page, does not mention the feedback page either, and the new page does not link it. So the two prompts, one for people who saw a demo and one for experts asked in advance, now live side by side on one site without reference to each other.
- The overlap is design, not code we can see: the prompts themselves are in riskmandate.ai's repository and on its pages, and we have not compared them line by line.
