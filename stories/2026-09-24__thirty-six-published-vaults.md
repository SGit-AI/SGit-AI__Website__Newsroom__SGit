---
title: Thirty-six published vaults, and what a reader can open today
date: 2026-09-24
desk: Journalist
standfirst: By 24 September 2026 sgit.ai had published 36 vaults, each with a read key put on its page on purpose. What kinds there are, how a key gets published, and what anyone can open with nothing installed.
section: back-catalogue
sources:
  - src:vaults/published-vaults.json
  - https://sgit.ai/demos/vaults/index.html
  - https://sgit.ai/demos/vaults/publishing.html
  - https://sgit.ai/demos/vaults/company-xray/index.html
  - https://sgit.ai/demos/vaults/agent-webmaster/index.html
  - https://sgit.ai/catalogue/index.html
  - src:history/sgit.ai-version-log.json
  - https://sgit.ai/admin/versions.html
reviewed_by:
reviewed_on:
---

sgit.ai's published vaults page says: "Open any of these in your browser right now. Every read key here was published on purpose, and a read key is the whole credential: no account, nothing to install, no write capability in it." ([published vaults](https://sgit.ai/demos/vaults/index.html)). The site's vault list, as copied into this newsroom's snapshot, has 36 entries ([vault list](src:vaults/published-vaults.json)). The counts below are computed from that file unless a sentence says otherwise.

## What kinds exist

The list puts each vault in one of eight categories: 10 briefings, 7 analyses, 5 applications, 5 references, 4 records, 3 presentations, 1 gallery and 1 report ([vault list](src:vaults/published-vaults.json)). The same breakdown is printed on the site's own table ([published vaults](https://sgit.ai/demos/vaults/index.html)). The page also says "**Nine are semantic graphs**, each in its own ontology, from a regulation down to a compute instance." ([published vaults](https://sgit.ai/demos/vaults/index.html)).

Some examples, in the list's own one-line descriptions:

- A gallery: "A travel diary: twenty photographs in three sizes and an eight-chapter narrative" ([vault list](src:vaults/published-vaults.json)).
- A record: "The site's own task board as a vault, cards as files, five columns as an app, the source of truth the site renders from" ([vault list](src:vaults/published-vaults.json)).
- A reference: "The EU AI Act parsed from Formex into an evidence graph, article by article" ([vault list](src:vaults/published-vaults.json)).
- A report: "A penetration test report (fictional) with a re-test script per finding" ([vault list](src:vaults/published-vaults.json)).
- A presentation: "The Black Hat EU 2025 keynote, with its PDF exports and eight research papers" ([vault list](src:vaults/published-vaults.json)).
- An application: "Two games about grants and mandates, the first vault here that phones home" ([vault list](src:vaults/published-vaults.json)).

Five of the ten briefings are business plans, published on 23 and 24 September as vaults 32 to 36 ([vault list](src:vaults/published-vaults.json), [published vaults](https://sgit.ai/demos/vaults/index.html)).

## How big, and when

Across the 36 entries the list records 2,957 files, and its byte figures add up to about 308 MB ([vault list](src:vaults/published-vaults.json)). The largest by size is the content-transformation proxy brief at 63 MB; the largest by file count is the AIUC-1 conformance layer, with 649 files ([vault list](src:vaults/published-vaults.json)). The smallest, Field Notes and the catalogue, are 11 KB each ([vault list](src:vaults/published-vaults.json)).

The list dates 21 vaults to August and 15 to September ([vault list](src:vaults/published-vaults.json)). The first six carry the date 16 August ([vault list](src:vaults/published-vaults.json)). On that day, the site's version log says, "The site starts doing the thing it was building toward: publishing vaults" ([version log](https://sgit.ai/admin/versions.html)). The published date on the table is "NOT a date anybody typed": it is the date each vault's page first appeared in git ([version log](src:history/sgit.ai-version-log.json)).

## Read keys, published on purpose

The Company X-Ray page, the newest, shows the pattern: it prints its read key, a link that opens the vault read-only in the official interface, and an `sgit clone` command ([Company X-Ray](https://sgit.ai/demos/vaults/company-xray/index.html)). The newest pages say the key "is published on purpose, under the `sgit_public_read_` prefix" and is "**derived** one way from a vault key that is kept in the gitignored tier and never published" ([Company X-Ray](https://sgit.ai/demos/vaults/company-xray/index.html)). The Librarian's vault data for this newsroom holds a read key for each of the 36, copied from the vault pages, and every one of them carries that prefix ([the newsroom's vaults page](nr:vaults)).

The prefix has changed twice. The first vault pages, on 16 August, printed keys as "a copyable sgit_rk1_ credential" ([version log](https://sgit.ai/admin/versions.html)). On 20 September the site found it had published keys for the two AIUC-1 vaults under a prefix that declares them secret, after "an agent correctly refused to open them" ([version log](https://sgit.ai/admin/versions.html)). The same day v0.3.0 moved "102 published read keys under sgit_rk1_ and 24 bare ones" to `sgit_public_read_` ([version log](https://sgit.ai/admin/versions.html)).

## How a key gets published

The site writes down a seven-step method, and two rules that everything else serves: "Read keys yes, vault keys never" and "Audit before the key, not after" ([publishing method](https://sgit.ai/demos/vaults/publishing.html)). The reason given for the second is that "Revocation is not retroactive." ([publishing method](https://sgit.ai/demos/vaults/publishing.html)). The first step is to classify the credential, because "Credentials arrive mislabelled. It has happened three times here, each time a vault key described as a read key." ([publishing method](https://sgit.ai/demos/vaults/publishing.html)). If it is a vault key, the method derives the read key and publishes only that ([publishing method](https://sgit.ai/demos/vaults/publishing.html)).

The audit has stopped publication more than once. On 20 August the EU AI Act vault was "the first vault here whose publication the audit STOPPED rather than cleared": it held a live vault key for a different vault, and was republished into a new vault with the credentials replaced by visible markers ([version log](https://sgit.ai/admin/versions.html)). On 25 August nine credentials were submitted, seven turned out to be write keys, and three vaults were held back ([version log](https://sgit.ai/admin/versions.html)).

Each vault page ends with "The audit, honestly": what was scanned, what was found, and the write-key status ([Company X-Ray](https://sgit.ai/demos/vaults/company-xray/index.html), [publishing method](https://sgit.ai/demos/vaults/publishing.html)). For the newest vaults that includes a control clone with an all-zeros key against the same vault id, which "cloned nothing" ([Company X-Ray](https://sgit.ai/demos/vaults/company-xray/index.html)).

## What a reader can open today

On sgit.ai, all 36 rows link to a page with the vault running live inside it ([published vaults](https://sgit.ai/demos/vaults/index.html)). The page says "Every read key and the live link are on the vault's own page." ([published vaults](https://sgit.ai/demos/vaults/index.html)). The five business plans ask for nothing: each app declares `"permissions": {}`, so, in the words of one page, "a published read key in front of it costs nobody anything" ([Agent as Webmaster](https://sgit.ai/demos/vaults/agent-webmaster/index.html)).

In this newsroom, all 36 vault pages are in the snapshot and can be read offline ([the newsroom's vaults page](nr:vaults)). The contents of five vaults, the five business plans, are also copied into the snapshot, so their plans, specifications and apps can be read here without a network ([Company X-Ray README](src:vaults/company-xray/README.md), [Agent as Webmaster README](src:vaults/agent-webmaster/README.md), [Connector Twin README](src:vaults/connector-twin/README.md), [Risk Acceptance Office README](src:vaults/risk-acceptance/README.md), [Lesson Loop README](src:vaults/lesson-loop/README.md)). The other 31 can be opened from their pages on sgit.ai with the key each page prints ([published vaults](https://sgit.ai/demos/vaults/index.html)).

## Where the sources disagree

The published vaults page's own summary line says "Thirty-one vaults you can open in your browser right now", while the count on the same page says "**36 published vaults**" ([published vaults](https://sgit.ai/demos/vaults/index.html)). The catalogue, the vault that indexes vaults, carries entries "for the first nine" and "is waiting on its key holder for the rest" ([published vaults](https://sgit.ai/demos/vaults/index.html)). The catalogue page says that when it was checked on 19 September the catalogue vault held nine entries and the gallery thirty, and calls the gap "a write-key problem" ([catalogue](https://sgit.ai/catalogue/index.html)). The site names its table, not the catalogue, as "the complete list" ([published vaults](https://sgit.ai/demos/vaults/index.html)).
