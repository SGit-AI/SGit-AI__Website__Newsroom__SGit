---
title: The sgit network, dated by its own records
date: 2026-09-24
desk: Cartographer
standfirst: A timeline of when the sgit network's sites and major releases appeared, from riskmandate.ai's first reconstructed version in June to the day sgit.ai briefed riskmandate.ai and riskmandate.ai built the page. Every date is one a source states; a site whose first date no source gives is left off.
sources:
  - src:history/sgit.ai-version-log.json
  - src:history/sgit.ai-git-log.txt
  - https://riskmandate.ai/versions.md
  - src:sites/store.sgit.ai/ledger/index.md
  - https://graphs.sgit.ai/llms.txt
  - https://infographics.sgit.ai/llms.txt
  - https://subscriptions.sgit.ai/llms.txt
  - https://twins.sgit.ai/llms.txt
  - https://skills.sgit.ai/llms.txt
  - https://games.sgit.ai/llms.txt
  - https://what-can-it-do.games.sgit.ai/llms.txt
  - https://threat-modeling.sgit.ai/llms.txt
  - https://chrome-extensions.sgit.ai/llms.txt
  - src:sites/abp.sgit.ai/versions/v0.1.0.json
reviewed_by:
reviewed_on:
---

This timeline puts the network's dated events in one line: the sites as they first appeared, and the releases that changed what the network is. The dates come from three kinds of record: sgit.ai's [version log](src:history/sgit.ai-version-log.json) and [git log](src:history/sgit.ai-git-log.txt), riskmandate.ai's [version record](https://riskmandate.ai/versions.md), and the first version each sibling site states about itself.

Two cautions. riskmandate.ai's releases before v1.0.0 are marked "reconstructed" in its record: their notes are a record, and the builds they describe are not in its repository ([version record](https://riskmandate.ai/versions.md)). And a sibling site's "v0.1.0" date is the date the site gives for its first version, not a date we saw it go live. Sites that give no first date (nhi.sgit.ai, pki.sgit.ai and several more) appear only where sgit.ai's log dates them.

### June to 19 August: before the network, and the first vaults

```mermaid
timeline
    title Before the network, and sgit.ai's first vaults
    29 June : riskmandate.ai v0.1.0, baseline, reconstructed
    4 July : riskmandate.ai v0.6.0, a pricing page and RAMM, reconstructed
    11 August : sgit.ai v0.1.1, the first vault app : sgit.ai v0.1.2, the MVP site
    16 August : sgit.ai v0.2.19 starts publishing vaults
    17 August : sgit.ai v0.2.25, the Risk Mandate vault joins the catalogue
    19 August : sgit.ai v0.2.36, a network section, with nhi.sgit.ai and pki.sgit.ai
```

### 20 to 26 August: the sibling sites arrive

```mermaid
timeline
    title The sibling sites arrive
    20 August : sg-sentinel.sgit.ai, the third site : riskmandate.ai v0.11.0, the grant is not the mandate
    21 August : graphs.sgit.ai v0.1.0, the fourth site
    23 August : infographics.sgit.ai v0.1.0
    25 August : subscriptions.sgit.ai v0.1.0 : twins.sgit.ai v0.1.0 : riskmandate.ai v0.12.0, the insurability layer
    26 August : skills.sgit.ai v0.1.0 : sgit.ai v0.2.44, the network becomes a directory
```

### 6 to 17 September: briefs, games, the ABP and the store

```mermaid
timeline
    title Briefs, games, the ABP and the store
    6 September : sgit.ai v0.2.55, briefs become a section
    8 September : games.sgit.ai v0.1.0 : what-can-it-do.games.sgit.ai v0.1.0 : threat-modeling.sgit.ai v0.1.0
    9 September : chrome-extensions.sgit.ai v0.1.0 : sgit.ai v0.2.74, the network list catches up with the organisation
    11 September : abp.sgit.ai v0.1.0, its first version : riskmandate.ai v1.0.0, the site becomes the repository
    15 September : riskmandate.ai v1.19.0, the store linked and pricing as four levels
    17 September : store.sgit.ai, a payment link for level one
```

### 20 to 24 September: the week the newsroom began

```mermaid
timeline
    title The week the newsroom began
    20 September : sgit.ai v0.3.0, the em-dash leaves the prose
    21 September : sgit.ai v0.4.0, a startups section
    23 September : sgit.ai v0.5.7, a partnerships section : sgit.ai v0.6.0, the first business plan for somebody else to run
    24 September : sgit.ai v0.6.7, the interview-page brief : riskmandate.ai v1.34.2 builds it : riskmandate.ai v1.34.3 takes it live : sgit.ai v0.6.8, Company X-Ray
```

## Where each date comes from

| Date | Event | Source |
|---|---|---|
| 29 June, 4 July | riskmandate.ai v0.1.0 "Baseline"; v0.6.0 "new Pricing page; new RAMM page" | [version record](https://riskmandate.ai/versions.md), both marked reconstructed |
| 11 August | sgit.ai v0.1.1 "Initial vault app"; v0.1.2 "the sgit.ai MVP site" | [version log](src:history/sgit.ai-version-log.json) |
| 16 August | v0.2.19: "The site starts doing the thing it was building toward: publishing vaults" | [version log](src:history/sgit.ai-version-log.json) |
| 17 August | v0.2.25: "Risk Mandate joins the catalogue" | [version log](src:history/sgit.ai-version-log.json) |
| 19 August | v0.2.36: "A NETWORK section for the sibling *.sgit.ai sites", covering nhi.sgit.ai and pki.sgit.ai | [version log](src:history/sgit.ai-version-log.json) |
| 20 August | v0.2.38: "Third site in the network: SG-SENTINEL.SGIT.AI"; riskmandate.ai v0.11.0 "New homepage: the grant is not the mandate" (reconstructed) | [version log](src:history/sgit.ai-version-log.json), [version record](https://riskmandate.ai/versions.md) |
| 21 August | v0.2.39: "Fourth site in the network: GRAPHS.SGIT.AI"; graphs.sgit.ai's own record starts at "v0.1.0 (21 August 2026)" | [version log](src:history/sgit.ai-version-log.json), [graphs.sgit.ai](https://graphs.sgit.ai/llms.txt) |
| 23 to 26 August | infographics.sgit.ai (23 August), subscriptions.sgit.ai and twins.sgit.ai (25 August), skills.sgit.ai (26 August), each at v0.1.0 | [infographics](https://infographics.sgit.ai/llms.txt), [subscriptions](https://subscriptions.sgit.ai/llms.txt), [twins](https://twins.sgit.ai/llms.txt), [skills](https://skills.sgit.ai/llms.txt) |
| 25 August | riskmandate.ai v0.12.0 "New homepage: the insurability layer" (reconstructed) | [version record](https://riskmandate.ai/versions.md) |
| 26 August | v0.2.44: "THE NETWORK BECOMES A DIRECTORY" | [version log](src:history/sgit.ai-version-log.json) |
| 6 September | v0.2.55: "BRIEFS BECOMES A SECTION WITH TWO KINDS IN IT" | [version log](src:history/sgit.ai-version-log.json) |
| 8 and 9 September | games.sgit.ai and what-can-it-do.games.sgit.ai "First publish" (8 September), threat-modeling.sgit.ai v0.1.0 (8 September), chrome-extensions.sgit.ai v0.1.0 (9 September) | [games](https://games.sgit.ai/llms.txt), [what-can-it-do](https://what-can-it-do.games.sgit.ai/llms.txt), [threat-modeling](https://threat-modeling.sgit.ai/llms.txt), [chrome-extensions](https://chrome-extensions.sgit.ai/llms.txt) |
| 9 September | v0.2.74: "THE NETWORK LIST WAS EIGHT SITES BEHIND", checked against the organisation's repositories | [version log](src:history/sgit.ai-version-log.json) |
| 11 September | abp.sgit.ai v0.1.0, "The first version of abp.sgit.ai"; riskmandate.ai v1.0.0 "The site becomes the repository" | [abp.sgit.ai v0.1.0](src:sites/abp.sgit.ai/versions/v0.1.0.json), [version record](https://riskmandate.ai/versions.md) |
| 15 September | riskmandate.ai v1.19.0 "View a policy, buy a policy: the store linked, pricing as the four levels" | [version record](https://riskmandate.ai/versions.md) |
| 17 September | "Level one carries a payment link, created on 17 September 2026" | [store ledger](src:sites/store.sgit.ai/ledger/index.md) |
| 20 September | v0.3.0: "THE EM-DASH IS GONE FROM PROSE" | [version log](src:history/sgit.ai-version-log.json) |
| 21 September | v0.4.0: "A STARTUPS SECTION" | [version log](src:history/sgit.ai-version-log.json) |
| 23 September | v0.5.7: "NEW SECTION: PARTNERSHIPS"; v0.6.0: "THE FIRST BUSINESS PLAN PUBLISHED FOR SOMEBODY ELSE TO RUN" | [version log](src:history/sgit.ai-version-log.json) |
| 24 September | sgit.ai v0.6.7 at 20:55 and v0.6.8 at 23:26 ([git log](src:history/sgit.ai-git-log.txt)); riskmandate.ai v1.34.2 and v1.34.3, dated but not timed | [version record](https://riskmandate.ai/versions.md); the day is drawn in [brief to build](nr:maps/brief-to-build) |

store.sgit.ai, newsroom.sgit.ai and the other sites in the snapshot state a current version but, in the files we hold, no first date, so they are not on the line. The [network map](nr:maps/network) shows them all by their links.
