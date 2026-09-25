---
title: The story so far: the sgit network, 29 June to 24 September 2026
date: 2026-09-24
desk: Historian
covers: 2026-06-29 to 2026-09-24
standfirst: Three months of two version logs, read end to end: a risk site that began inside a vault, a vault site that began six weeks later, and the ideas that travelled between them until both were selling the same thing from different ends. The eras, the turning points, the gotchas and the pattern, each with its source.
sources:
  - src:history/sgit.ai-version-log.json
  - https://sgit.ai/admin/versions.html
  - https://riskmandate.ai/versions.md
  - https://riskmandate.ai/versions/0.1.0.md
  - https://riskmandate.ai/versions/0.5.0.md
  - https://riskmandate.ai/versions/0.11.0.md
  - https://riskmandate.ai/versions/1.0.0.md
  - https://riskmandate.ai/versions/1.11.0.md
  - https://riskmandate.ai/versions/1.22.0.md
  - https://riskmandate.ai/versions/1.28.0.md
  - https://risks.sgit.ai/llms.txt
  - https://abp.sgit.ai/versions/index.md
  - https://abp.sgit.ai/versions/v0.1.0/index.md
  - https://abp.sgit.ai/versions/v0.4.4/index.md
  - https://store.sgit.ai/llms.txt
  - https://graphs.sgit.ai/llms.txt
  - https://twins.sgit.ai/llms.txt
reviewed_by:
reviewed_on:
---

The Journalist's editions say what happened on each day from 20 September. This piece looks back over the whole record the newsroom holds, and asks what it adds up to. It uses two logs above all. sgit.ai's [version log](src:history/sgit.ai-version-log.json) has 166 entries, from v0.1.1 on 11 August to v0.6.8 on 24 September. riskmandate.ai's [version record](https://riskmandate.ai/versions.md) has 106 releases, from v0.1.0 on 29 June to v1.34.8 on 24 September; the 35 before v1.0.0 are marked *reconstructed*, because they were built inside a vault and their builds are not in the site's repository. Both counts are this desk's, taken from those two files. Around them sit the llms.txt files of the sibling sites and the [network map](nr:maps/network), which counts 32 sites and 152 site-to-site links in the snapshot.

## Before sgit.ai: a risk site inside a vault

The earliest dated release in the network is not sgit.ai's. riskmandate.ai's baseline, on 29 June, was "delivered as an encrypted SG/Vault HTML app", with a hero reading "Agents act. You own the risk." and an interactive queue where each risk could be accepted or sent back for more information ([v0.1.0](https://riskmandate.ai/versions/0.1.0.md)). Between 30 June and 3 July the site rebuilt its own versioning four times, ending in a chain of frozen deltas where a shipped version could not be edited ([v0.2.0](https://riskmandate.ai/versions/0.2.0.md) to [v0.4.5](https://riskmandate.ai/versions/0.4.5.md)). On 2 July it moved to a risk-acceptance focus, with "the signature mechanic: no deny button", and scrubbed a certification claim from every frozen version as a documented exception to that immutability ([v0.5.0](https://riskmandate.ai/versions/0.5.0.md)).

risks.sgit.ai, the research site behind the product, dates the idea itself: orthodox risk management in February 2026, an inversion in June, a formalisation in August ([risks.sgit.ai](https://risks.sgit.ai/llms.txt)). Its central claim is that a risk is underwritten rather than predicted, so "THERE IS NO DENY BUTTON" ([risks.sgit.ai](https://risks.sgit.ai/llms.txt)).

## Era one: sgit.ai builds its own proof (11 to 27 August)

sgit.ai's first entry is itself a vault app, and twelve releases went out on 11 August ([version log](src:history/sgit.ai-version-log.json)). The next day it found its own vault passphrase written into a tracked, public file as an anti-leak tripwire, removed it, and wrote: "The key must be treated as compromised and rotated." ([v0.1.13](https://sgit.ai/admin/versions.html)). The same day it published a runbook with this leak as the case study ([v0.1.14](https://sgit.ai/admin/versions.html)).

August is the era of building proof. 81 of the 166 entries fall in that month by this desk's count. The site published its first vault with a deliberately published read key on 15 August ([v0.2.6](https://sgit.ai/admin/versions.html)), a catalogue of vaults with the rule "read keys yes, vault keys never" ([v0.2.12](https://sgit.ai/admin/versions.html)), and a vaults section on 16 August ([v0.2.19](https://sgit.ai/admin/versions.html)). On 17 August the riskmandate field demo joined the catalogue as a vault app of 124 files ([v0.2.25](https://sgit.ai/admin/versions.html)). By 27 August the site had published its 24th vault, Licence to Operate, an agent's grant of 12 capabilities against a mandate of 4, with a delta of 8 ([v0.2.52](https://sgit.ai/admin/versions.html)).

In the same weeks the network appeared. A network section went up on 19 August with two sites, nhi.sgit.ai and pki.sgit.ai ([v0.2.36](https://sgit.ai/admin/versions.html)). By 26 August it listed nineteen, whose repositories were created between 11 and 26 August, "fifteen of the twenty in the final five days" ([v0.2.44, v0.2.45](https://sgit.ai/admin/versions.html)).

riskmandate.ai turned in the same month. On 20 August its home page led with "the grant is not the mandate", correcting a claim of 17 July that the two were equal, and stated the limit plainly: "we define the mandate and map the gap; we do not enforce it" ([v0.11.0](https://riskmandate.ai/versions/0.11.0.md)). It embedded three vaults sgit.ai had published, "the same technique sgit.ai uses" ([v0.11.0](https://riskmandate.ai/versions/0.11.0.md)).

## Era two: the policy gets a name (late August to 17 September)

sgit.ai's log goes quiet from 28 August to 4 September, and riskmandate.ai's from 2 to 7 September (both counted from the logs). When they resumed, the work converged on one object.

On 11 September two things happened on the same day. riskmandate.ai left its vault: "The site becomes the repository", with the host frame gone and the vault kept "as the historical record" ([v1.0.0](https://riskmandate.ai/versions/1.0.0.md)). And abp.sgit.ai published its first version, in which "the ontology is promoted out of a game" rather than authored a second time ([abp.sgit.ai v0.1.0](https://abp.sgit.ai/versions/v0.1.0/index.md)). The game was what-can-it-do.games.sgit.ai, whose pipeline the new site copied ([abp.sgit.ai v0.1.0](https://abp.sgit.ai/versions/v0.1.0/index.md)).

The next day riskmandate.ai gave the Agent Behaviour Policy a page, saying the site "had been arguing the Agent Behaviour Policy's contents for months without the artefact having a name" ([v1.1.0](https://riskmandate.ai/versions/1.1.0.md)). By 15 September its home page led with the policy, marked the first step "what we sell" and the rest "design" ([v1.12.0](https://riskmandate.ai/versions/1.12.0.md)), and store.sgit.ai had put up four levels with a price each ([v1.19.0](https://riskmandate.ai/versions/1.19.0.md)). The store's own summary now reads: "Every agent needs a licence to operate. This is where you buy one." ([store.sgit.ai](https://store.sgit.ai/llms.txt)). Between 11 and 17 September riskmandate.ai shipped 38 releases by this desk's count ([version record](https://riskmandate.ai/versions.md)).

## Era three: correcting the record, then turning outward (18 to 24 September)

The newsroom's [week piece](nr:history/week-2026-39) covers these seven days in detail. In short: sgit.ai shipped 58 entries, and spent the first half of the week correcting its own record, from the fractal definition to a mislabelled read key that another agent refused to open ([v0.2.89, v0.2.98](https://sgit.ai/admin/versions.html)). On 21 September riskmandate.ai set the phase: the offering is built, and "Nobody buys a full policy until they have made a smaller one." ([v1.28.0](https://riskmandate.ai/versions/1.28.0.md)). By 23 and 24 September sgit.ai was publishing proposed partnerships and business plans for somebody else to run ([v0.5.7 to v0.6.8](https://sgit.ai/admin/versions.html)).

## The connection lines

**Read keys.** The line runs from a published read-only key on 12 August ([v0.1.15](https://sgit.ai/admin/versions.html)), through the catalogue's rule ([v0.2.12](https://sgit.ai/admin/versions.html)), to a credential check written after a vault key was submitted as a read key ([v0.2.26](https://sgit.ai/admin/versions.html)). It ends, for now, in classification "by declaration and never by shape" ([v0.2.98](https://sgit.ai/admin/versions.html)). risks.sgit.ai carries the same standing rule, "publish read keys, NEVER write keys" ([risks.sgit.ai](https://risks.sgit.ai/llms.txt)).

**Append lanes.** pki.sgit.ai's registry rule, carried onto sgit.ai on 19 August, is "the writer owns what it writes" ([v0.2.36](https://sgit.ai/admin/versions.html)). A telemetry brief of 6 September ([v0.2.55](https://sgit.ai/admin/versions.html)) was built into a games vault by another agent, the first end-to-end test "of whether a brief written for an agent produces what it describes" ([v0.2.56](https://sgit.ai/admin/versions.html)). The team that owns the append code then found the brief wrong on both points it told builders to check ([v0.2.58](https://sgit.ai/admin/versions.html)). By 24 September write-only lanes appear in two business plans ([v0.6.3, v0.6.6](https://sgit.ai/admin/versions.html)) and, as a later step, in the interview-page brief ([v0.6.7](https://sgit.ai/admin/versions.html)); riskmandate.ai marks that step "later" ([v1.34.2](https://riskmandate.ai/versions/1.34.2.md)).

**Risk acceptance.** From riskmandate.ai's queue of 29 June, through a vault with "no deny button" on sgit.ai ([v0.2.27](https://sgit.ai/admin/versions.html)) and the six-step interval ladder on risks.sgit.ai ([risks.sgit.ai](https://risks.sgit.ai/llms.txt)), to a Risk Acceptance Office business plan on 24 September ([v0.6.5](https://sgit.ai/admin/versions.html)) and a figure in which "A control does not make a risk zero; it leaves a green one" ([v1.34.8](https://riskmandate.ai/versions/1.34.8.md)).

**Agent behaviour policies.** Grant against mandate appeared as a correction on riskmandate.ai ([v0.11.0](https://riskmandate.ai/versions/0.11.0.md)) and as a priced delta in a vault on sgit.ai ([v0.2.52](https://sgit.ai/admin/versions.html)). It became a vocabulary on abp.sgit.ai and a product on riskmandate.ai. The traffic ran both ways: on 20 September abp.sgit.ai promoted seven deployment shapes that riskmandate.ai had built and requested on 12 September ([abp.sgit.ai v0.4.4](https://abp.sgit.ai/versions/v0.4.4/index.md)).

**Vaults as the unit of publishing.** sgit.ai's home page was rebuilt on 7 September around the sentence "a vault is a unit of work: data, app, history and sources, shipped as one string" ([v0.2.60](https://sgit.ai/admin/versions.html)). In the same month both sites stopped keeping their own pages in a vault: riskmandate.ai on 11 September ([v1.0.0](https://riskmandate.ai/versions/1.0.0.md)), and sgit.ai on 19 September, when it purged a mirror that had no reader and was 91% of its repository ([v0.2.84](https://sgit.ai/admin/versions.html)). The published vaults went on growing, to thirty-six on 24 September ([v0.6.8](https://sgit.ai/admin/versions.html)).

**Business plans as vaults.** A talk ([v0.2.46](https://sgit.ai/admin/versions.html)), a pitch ([v0.2.51](https://sgit.ai/admin/versions.html)) and a job application ([v0.2.79](https://sgit.ai/admin/versions.html)) went into vaults before the first business plan written for somebody else to run, on 23 September ([v0.6.0](https://sgit.ai/admin/versions.html)). The fifth plan's four levels "reuse RiskMandate.ai's pricing pattern" ([v0.6.8](https://sgit.ai/admin/versions.html)): a pattern that began on one site became a template on the other.

## The moments

- **12 August.** A secret in sgit.ai's own tracked file ([v0.1.13](https://sgit.ai/admin/versions.html)). Much of the key discipline that follows traces back to it.
- **17 August.** A vault key submitted as a read key, caught by shape, and only the derived read key published ([v0.2.25](https://sgit.ai/admin/versions.html)). The next release turned the catch into a script, because "The catch depended on somebody looking." ([v0.2.26](https://sgit.ai/admin/versions.html)).
- **20 August.** riskmandate.ai says in public that it maps the gap and does not enforce it ([v0.11.0](https://riskmandate.ai/versions/0.11.0.md)).
- **11 September.** riskmandate.ai leaves its vault and abp.sgit.ai begins, on the same date ([v1.0.0](https://riskmandate.ai/versions/1.0.0.md), [abp.sgit.ai versions](https://abp.sgit.ai/versions/index.md)).
- **20 September.** An agent refuses a read key labelled private, and sgit.ai agrees: "It was right and our label was wrong." ([v0.2.98](https://sgit.ai/admin/versions.html)). This was the moment of the [week](nr:history/week-2026-39).
- **24 September.** A brief written on sgit.ai is built on riskmandate.ai the same day ([v0.6.7](https://sgit.ai/admin/versions.html), [v1.34.2](https://riskmandate.ai/versions/1.34.2.md)).

## The gotchas

**Green does not mean live.** On 17 August two sgit.ai releases passed every check and never reached the site, because the deploy job died on a rate limit ([v0.2.33](https://sgit.ai/admin/versions.html)). On 22 August the tag gate blocked a deploy for a day ([v0.2.40](https://sgit.ai/admin/versions.html)). On 24 September six riskmandate.ai releases, by this desk's count, were merged and never deployed, because the local check did not run what CI ran ([v1.34.3](https://riskmandate.ai/versions/1.34.3.md)).

**A scan only finds what it looks for.** A live third-party API key passed sgit.ai's first credential pass because its field name matched none of the patterns; a screenshot caught it ([v0.2.43](https://sgit.ai/admin/versions.html)). A credential test first called a leak on evidence an all-zeros key reproduced ([v0.2.56](https://sgit.ai/admin/versions.html)).

**A page can render and still be broken.** riskmandate.ai shipped a version with no stylesheet, because its own delta listed that stylesheet for removal ([v0.12.1](https://riskmandate.ai/versions/0.12.1.md)). Later, two pages threw on load while every test passed; "The only signal was an error in a console nobody was reading." ([v1.20.2](https://riskmandate.ai/versions/1.20.2.md)).

## The nuggets

- "a page nothing links to, a page the index omits, and a page the deploy never published are all equally unpublished" ([v0.2.33](https://sgit.ai/admin/versions.html)).
- "a missing tag is a bookkeeping gap, a blocked deploy is an outage" ([v0.2.40](https://sgit.ai/admin/versions.html)).
- "Any credential test that has no negative control is not a test" ([v0.2.56](https://sgit.ai/admin/versions.html)).
- "A sentence somebody can disagree with is worth more than a number nobody can argue with, because the disagreement is where the information is." ([v1.11.0](https://riskmandate.ai/versions/1.11.0.md)).
- "never publish a prohibition without publishing what enforces it in the same row." ([v1.8.0](https://riskmandate.ai/versions/1.8.0.md)).
- An idea that went upstream and came back. On 19 September sgit.ai briefed graphs.sgit.ai that its fractal test should separate grammar from ontology ([v0.2.94](https://sgit.ai/admin/versions.html)). graphs.sgit.ai's llms.txt at v0.6.22, dated 20 September, now states "the grammar survives every zoom and the ontology does not have to" ([graphs.sgit.ai](https://graphs.sgit.ai/llms.txt)).

## The pattern

Three things recur across both logs and the sibling sites.

First, corrections are published beside the thing corrected. riskmandate.ai left its v1.10.0 note standing after reversing it, because rewriting it "is the one thing the register exists to prevent" ([v1.11.0](https://riskmandate.ai/versions/1.11.0.md)). abp.sgit.ai corrected "a rule this site published nine hours earlier, applied in the open" ([abp.sgit.ai v0.2.0](https://abp.sgit.ai/versions/v0.2.0/index.md)).

Second, sites state what is built and what is not, in capitals where they judge it matters. risks.sgit.ai: "ESSENTIALLY NONE OF THIS IS IMPLEMENTED IN CODE." ([risks.sgit.ai](https://risks.sgit.ai/llms.txt)). twins.sgit.ai: "ONE TWIN IS BUILT." ([twins.sgit.ai](https://twins.sgit.ai/llms.txt)). store.sgit.ai gives every claim one of ten states ([store.sgit.ai](https://store.sgit.ai/llms.txt)).

Third, a rule arrives after a mistake, and the rule carries the mistake with it. sgit.ai's lessons page gives the reason: "a rule with no origin is only a preference" ([lessons](https://sgit.ai/lessons/index.html)). The newsroom's [decision log](nr:history/decisions) numbers the choices this record shows, oldest first, and [the open questions](nr:history/open-questions) list what the sources asked and have not yet answered.
