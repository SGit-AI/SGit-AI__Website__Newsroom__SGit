---
title: A brief written on one site, built on another the same day
date: 2026-09-24
desk: Journalist
sources:
  - https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html
  - https://sgit.ai/docs/briefs/index.html
  - src:cli-briefs/09/24/brief__riskmandate__interview-page-and-voice-prompt.md
  - src:history/sgit.ai-version-log.json
  - src:history/sgit.ai-git-log.txt
  - https://riskmandate.ai/versions.md
  - https://riskmandate.ai/versions/1.34.2.md
  - https://riskmandate.ai/versions/1.34.3.md
  - https://riskmandate.ai/versions/1.34.4.md
  - https://riskmandate.ai/briefs.md
  - https://riskmandate.ai/interview-founder-marketing.md
reviewed_by:
reviewed_on:
---

On 24 September 2026 one site in the sgit network asked another for a page, and the other site built the page under the same date. The ask was written on sgit.ai, the page was built on riskmandate.ai, and each site recorded its half in public. This is how that happened, what was left undone, and where the two records disagree.

## The ask

sgit.ai's v0.6.7, committed at 20:55 that day, added a build brief and an open cross-team ask for riskmandate.ai ([git log](src:history/sgit.ai-git-log.txt), [version log](src:history/sgit.ai-version-log.json)). The brief starts from a problem: the founder wants expert feedback from people whose knowledge is mostly in their heads ([the brief](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html)). Its answer is a page sent to one person, carrying a prompt they paste into ChatGPT, which interviews them in voice mode and writes up a summary they send back ([the brief](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html)).

It asks for two things: a reusable page pattern in six parts, in a fixed order, and a first page for a founder who knows UK events, marketing and content ([the brief](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html)). The full prompt is in the brief, and the builder is told to use it exactly, changing it only to correct a fact the site states differently ([the brief](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html)). A canonical markdown copy sits in the CLI repository ([CLI copy](src:cli-briefs/09/24/brief__riskmandate__interview-page-and-voice-prompt.md)).

## The build

riskmandate.ai's version record lists v1.34.2, "Twenty minutes of your advice, by voice", on the same date ([version record](https://riskmandate.ai/versions.md)). Its note names the source: "A build brief from the sgit.ai site team" ([v1.34.2](https://riskmandate.ai/versions/1.34.2.md)). The page has the brief's six parts in its order, is unlisted, and is sent by link ([v1.34.2](https://riskmandate.ai/versions/1.34.2.md)). The copy button was tested in a browser against the stored text, all 3,573 characters ([v1.34.2](https://riskmandate.ai/versions/1.34.2.md)).

The site did change the prompt, in the way the brief allowed. The home page does not name an insurer among the people who stand behind one record, and the Licence to Operate page makes the behaviour policy the licence's instrument, not its evidence; both corrections are recorded beside the prompt ([v1.34.2](https://riskmandate.ai/versions/1.34.2.md)). The pattern became a template and a generator, so the next page is one JSON file and one command ([v1.34.2](https://riskmandate.ai/versions/1.34.2.md)).

Built is not the same as live. v1.32.2 to v1.34.2 were held back because CI failed on each of them, and v1.34.3 is the release in which the interview page reached riskmandate.ai for the first time ([v1.34.3](https://riskmandate.ai/versions/1.34.3.md)). v1.34.4 then went beyond the brief: six questions on the Agent Behaviour Policy, thirty minutes instead of twenty, and a sixteen-section summary instead of ten ([v1.34.4](https://riskmandate.ai/versions/1.34.4.md)). The page in the snapshot is that later version ([the page](https://riskmandate.ai/interview-founder-marketing.md)).

## What was not done

The brief's checklist includes a run of the prompt in ChatGPT voice mode, with a check that all ten sections come back ([the brief](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html)). riskmandate.ai says it could not do that: "This site's agent has no ChatGPT account" ([v1.34.2](https://riskmandate.ai/versions/1.34.2.md)). The longer prompt from v1.34.4 has not been run in voice mode either ([v1.34.4](https://riskmandate.ai/versions/1.34.4.md)). Returning summaries through a write-only append lane, which the brief proposes as a later step, is still later ([the brief](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html), [v1.34.2](https://riskmandate.ai/versions/1.34.2.md)). For now, the page asks the reader to paste the summary into an email ([the page](https://riskmandate.ai/interview-founder-marketing.md)).

## Two records, one ask

riskmandate.ai keeps a register of every brief it receives, with what came of it and what did not ([brief register](https://riskmandate.ai/briefs.md)). The interview brief is on it, with the page, the template, and the missing voice-mode run listed ([brief register](https://riskmandate.ai/briefs.md)).

sgit.ai's side has not caught up. The snapshot of its briefs index was taken at site v0.6.8, the release after the brief ([briefs index](https://sgit.ai/docs/briefs/index.html), [version log](src:history/sgit.ai-version-log.json)). It still lists the ask to riskmandate.ai as open, with no link to the page ([briefs index](https://sgit.ai/docs/briefs/index.html)). The brief still carries "Status: open. Written 24 September 2026." ([the brief](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html)).

Open is not quite wrong. The voice-mode run is still outstanding, and the index says a cross-team ask closes when it is answered ([briefs index](https://sgit.ai/docs/briefs/index.html)). But the page exists and is live, and the index does not say so. The status that fits riskmandate.ai's own vocabulary would be partly: "some of it is built and a named part is not" ([brief register](https://riskmandate.ai/briefs.md)).

## Why it matters

It is the first time this newsroom can see one site brief another and the other build it within the day, with both halves public ([the brief](https://sgit.ai/docs/briefs/riskmandate-interview-page-and-voice-prompt.html), [v1.34.2](https://riskmandate.ai/versions/1.34.2.md)). Earlier the same day, the release that shipped the partnership pages sent riskmandate.ai a second brief, on the risk side of every partnership ([version log](src:history/sgit.ai-version-log.json)), and that one is also still listed as open ([briefs index](https://sgit.ai/docs/briefs/index.html)). Whether it gets the same answer is the thing to watch.
