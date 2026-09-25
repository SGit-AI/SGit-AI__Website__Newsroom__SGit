# 00 — The Brief: `open-source.sgit.ai`

**Version** v0.33.62 · 24 August 2026
**From** Dinis Cruz, via the SG/Send Librarian
**To** the agent commissioned to build `open-source.sgit.ai`
**Licence** CC BY 4.0 — and see `07__` §2, because **the estate's own licensing is inconsistent and nobody has noticed**

---

## 1. The commission

> *"a pack for `open-source.sgit.ai` which is focused on explaining my views on Open Source, how I use it, and the history of Open Source (and its massive success stories). I should have a number of documents that cover this topic in detail (check `__Send` and `docs.diniscruz.ai`)."*

Three things: **the views**, **the practice**, **the history**. The first two are richly documented. The third is not, and that is the finding that shapes the whole pack.

---

## 2. The honest split, up front

You were right that there are a number of documents. There are about forty substantive ones, roughly 70,000 words, and **1,593 files carry at least one open-source or licence term**. But they are not evenly distributed across your three asks:

| Ask | State | What this pack did |
|---|---|---|
| **Your views** | **Very rich.** 56 distinct concepts catalogued — **24 of them original arguments**, not restatements | `01__`, `04__` |
| **How you use it** | **Rich, and partly undocumented even to you.** Three licences across three layers, a real publish-the-source practice, published packages | `02__` |
| **The history** | **Absent. Not thin — absent.** | `03__` — researched from scratch, 18,000 words |

On that last row, precisely: **zero occurrences of "free software", "copyleft", "Stallman", "GNU" as a movement, "Netscape", "SourceForge", or "FSF"** anywhere in the corpus. Nothing before 2001. **The GPL appears exactly twice, both times as litigation precedent, never as a philosophy.** There is no licence taxonomy at all — no GPL-vs-Apache-vs-MIT discussion, no copyleft-vs-permissive argument — yet the entire estate runs on Apache-2.0, CC BY 4.0 and CC0, and **the reasons for those choices are written down nowhere.**

That is not a criticism. It is a clean division of labour for the site: **you supply the argument, the research supplies the ground under it.**

---

## 3. The thesis

Your own sentence, and it should be the first thing on the front page:

> ***"the power of open source is not for the community, it is not because it is nice for others, and it is not to give back."***

Paired with the one that makes it land:

> ***"open source is not free, somebody is always paying for it. What you get from open source is freedom, that is different… We play the game of empowering the user and being the reputable source of trust. We are selling trust."***

That is a position most open-source sites do not take, and it is defensible, and you have 70,000 words behind it. The history in `03__` supports it far better than the usual telling does — see §5.

---

## 4. The five pages only you can write

Ranked. These are the reason to build the site rather than link to someone else's.

| # | Page | The claim | Source |
|---|---|---|---|
| **1** | **Survivability is not a licence property** | ***"Survivable is not a property of the licence file. It is a property of the copyright and trademark structure."*** With the mechanism: *"Every catalogued relicensing between 2018 and 2024 followed the same legal pattern: a single corporate copyright holder, having aggregated contributor copyright via a CLA, exercised the right to change terms going forward. Distributed-copyright projects could not be moved the same way, because no single party had standing."* And the kicker: *"HashiCorp went BUSL, IBM acquired it, and the licence stayed."* | 24 Jul 2026 · 3,459 w |
| **2** | **The Change-of-Control Stress Test** | A four-leg, publicly answerable test — copyright structure, trademark holder, schema licence, named fork capacity. ***"The stress test is a query, not an interview. 'Show me the CLA' and 'show me who holds the trademark' are answerable from public artefacts, and a vendor that cannot answer them has answered them."*** Ships as a tool, not an essay | same |
| **3** | **Sovereignty bounties — fund the exit, not the supply** | *"Every one of those programmes funds the supply side… None of them funds the **substitution side**… on present evidence nobody is funding it."* Plus bounty size as a **published lock-in metric**, and vendor-sponsored proof of no lock-in | 24 Jul 2026 · 4,205 w |
| **4** | **Open source is a strategy, not charity** | The whole OS7–OS11 cluster: technology is not the moat; ***"the lock-in is not on the technology, the lock-in is in the quality and the services and the new versions and the maintainability and the certification of versions"***; open source as a *workflow* | 17 Jul 2026 · 2,378 w |
| **5** | **Somebody has to be the villagers** | NFR maintenance as a market, and ***"the ability to read and repair code somebody else wrote"*** as the appreciating scarce asset. *"Demand for a specific skill is rising sharply while the mechanism that produces that skill is being dismantled"* | 31 Jul 2026 · 3,059 w |

Two more that carry a section each rather than a page: **lock-in degrades your own architecture** (*"you introduce attrition, and by introducing attrition you create much worse architectures"*) and **open source frees you to cannibalise your own code** (*"the code does not particularly have value"*).

---

## 5. The history research changes the standard story — use it

`03__` is 18,000 words of freshly-sourced history, and several findings cut directly toward your thesis rather than the usual romantic one. The site should lead with these, because they are true, checkable, and almost nobody publishes them:

- **Unix circulated because it was illegal to sell it.** The 1956 AT&T consent decree barred Bell Labs from any business but common-carrier communications. Unix shipped for media and postage as a *compliance artefact*. The decree lifted in 1982; AT&T commercialised System V immediately.
- **BSD lost to litigation risk, not to its licence.** USL v. BSDi (Apr 1992 – Feb 1994) clouded free Unix during exactly the window Linux needed. The settlement removed **3 files out of 18,000**. The claim was nearly empty; the *uncertainty* was decisive.
- **Netscape's source release was a six-year near-failure.** Released 31 March 1998; the code was so degraded the team threw it away and rewrote. **Firefox 1.0 did not ship until November 2004**, by which time IE had won. The founding case study of the open source movement is a cautionary tale.
- **Eric Raymond did not coin "open source."** **Christine Peterson** did, in the first week of February 1998 — and deliberately had someone with more community credibility introduce it so it would spread.
- **"Given enough eyeballs" is not a security property.** Heartbleed survived two years in the most security-critical library on the internet. **xz was engineered by the maintainer specifically to survive review**, and was caught by one engineer benchmarking SSH latency — not by a security review.
- **Two of the four relicensings reversed.** Elastic added AGPLv3 (Aug 2024); Redis 8 shipped AGPLv3 (May 2025). MongoDB remains SSPL; Terraform remains BUSL inside IBM.

Every one of those supports *your* framing — that the model succeeds on economics and structure, not on virtue or on eyeballs.

---

## 6. Two dated self-contradictions — publish both

The corpus argues with itself twice, in writing, with dates. Both are more interesting published than resolved.

**(a) Open core.** On **18 June**: *"There should be **nothing proprietary**. You never have the temptation of the bait model, where some of the best features are locked behind proprietary stuff, because the community always sees through it."* On **17 July**: *"more and more we want situations where the **customers only have a subset of the code that exists in the main repo**."*

And the July document names it itself: *"Open source versus the customer subset | A fuller main repo than the customer receives sits uneasily with a pure open-source claim; **this is open-core, and worth saying so plainly**."* There is a reconciliation available — the subset framed as *subtraction* (*"less attack surface, cheaper to run, maintainable"*) rather than withholding — but it is a different argument and should be made as one.

**(b) The junior pipeline.** **21 March**: *"The learning path is not eliminated. It is restructured… juniors learn by reading, evaluating, and improving code at scale. **The density of learning per hour increases.**"* **28 July**: *"apparent gains shifted work from juniors to seniors rather than removing it."* **31 July**: the pipeline *"is being disrupted at exactly the moment the maintenance need is growing."* March optimism, July evidence, four months apart.

---

## 7. The honesty constraint

`/shipped/`, per the house pattern:

- **The site has no community story, by design.** Your own position is that open source is right *"even if there are no contributions."* Intellectually coherent — and it means there is nothing in the corpus about running a project, reviewing PRs, governance, codes of conduct, or DCO-vs-CLA **in practice**, despite the whole survivability argument turning on that distinction.
- **No downstream-dependency practice.** One manual licence review exists (Feb 2026, 17 transitive deps, SPDX table, clean verdict). **No SBOM of your own estate, no automated licence scanning, no policy document, no upstream-contribution record.** You argue companies should *"declare your supply chain"*; there is no evidence you do.
- **The three funding proposals are unreconciled** — organic-food labelling, a maintainer platform, sovereignty bounties. Three answers to one question, none costed, none piloted, none compared against each other. The corpus admits it: *"the sustainable funding question is unsettled."*
- **The estate would fail its own stress test.** SGraph's copyright is held by one company. That is exactly the single-holder pattern the survivability argument identifies as the failure mode. **Publishing that self-audit would be the most credible page on the site.**
- **Every statistic needs re-verification.** The corpus warns itself: *"the figures circulating are largely recycled from a smaller set of studies through commercial blogs, so the direction is well supported and the precision is not."* `03__` has done that work — see the myths list.

---

## 8. The numbers

| | |
|---|---|
| **Corpus** | 1,593 files carry an OSS/licence term · ~40 substantive documents · ~70,000 words · **56 concepts** — 24 original **[O]**, 22 personal positions **[P]**, 10 widely-held **[C]** |
| **Absent** | "free software" · "copyleft" · "Stallman" · "Netscape" · "SourceForge" · "FSF" — **all zero** |
| **Licences in the estate** | **3** — Apache-2.0 (code), CC BY 4.0 (~1,100+ brief footers), **CC0 1.0** (`docs.diniscruz.ai`, unnoticed) |
| **History research** | **18,000 words**, 1955→2026 · 14 success stories · 17 myths corrected · 7 both-sides arguments |
| **Published prior art** | 13 articles on `docs.diniscruz.ai`, Feb 2025 – Jun 2025, all CC0 |
| **OWASP thread** | 4 summits documented (2008, 2009, 2011, 2017) · named organiser at 2011 and 2017 · Open Security Summit from 2018 |
| **This pack** | 9 documents + the 18,000-word history research · manifest of **55 rows** — 15 Tier-0, 32 Tier-1, 2 Tier-2, 6 do-not-publish; **116,841 words** of Tier-0+1 local source, every path verified on disk |

---

## 9. Build order

1. **`/views/` — the argument.** Start with `01__`'s five pages. The site's whole identity is that it takes an unfashionable position and defends it.
2. **`/survivability/` — the stress test as a tool.** Four legs, publicly answerable, applicable to any vendor. Ship it as a form or checklist, not an essay. **Include the self-audit.**
3. **`/history/` — from `03__`.** Lead with the six findings in §5, not with a conventional timeline. The timeline is the supporting material, not the hook.
4. **`/practice/` — from `02__`.** Resolve the CC0/CC BY inconsistency *before* writing this page, then explain the choices. Why Apache-2.0 over MIT is currently unwritten anywhere.
5. **`/agents/` — `05__`.** The most original writing still available, and the least written. Four theses are named and none is written.
6. **`/owasp/` — `06__`.** Needs an interview; see `06__` §4. It is the site's strongest human asset and it is currently written in the third person from public sources.
7. **`/shipped/`** — §7, unsoftened, including the self-audit.

Publish the build order unresolved, with `08__`'s open questions and tensions visible.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
