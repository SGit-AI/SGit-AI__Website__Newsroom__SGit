# 05 — Agents and open source

**This is where the most original writing is still available, and it is the reason to build the site.** The economics are strong and well argued. Four theses that follow from them are named nowhere and written nowhere.

---

## 1. Code-reading as the appreciating scarce asset

The origin (21 Mar 2026) opens by refusing the easy version of the argument, which is why it is credible:

> *"Before AI agents started writing code, you could argue that **90% of the code running in production was not being read by anyone**… So let us not pretend that 'nobody reads the code anymore' is a new problem. **It is an old problem, accelerated.**"*

The three-phase answer maps onto the Wardley teams: *"**Explorers:** agents read it (scans, checks, basic quality)… **Villagers:** mid-level developers read it… **Town Planners:** senior developers really read it."*

And the philosophical core, which is the best-written passage in the corpus on this subject:

> *"I would argue that this narrative has caused more damage than people admit… **Applications with 2,000 dependencies. CI pipelines that download half the internet. Layers of abstraction where nobody on the team understands what is happening below their layer.** The answer was never 'stop abstracting.' The answer was '**someone still needs to understand what is underneath.**' Linus Torvalds reads C code."*

---

## 2. ⚠️ The March/July contradiction — publish it

**21 March, optimistic:**
> *"The learning path is not eliminated. It is restructured. Instead of learning by writing simple code from scratch, **juniors learn by reading, evaluating, and improving code at scale. The density of learning per hour increases.**"*

**28 July, evidence:**
> *"apparent gains **shifted work from juniors to seniors** rather than removing it."*

**31 July, the market claim:**
> the junior pipeline *"is being disrupted at exactly the moment the maintenance need is growing."*

Four months apart, and the July position undercuts the March one. **This is the second dated self-contradiction in the corpus** (the first is open core, `04__` §3), and like that one it is more valuable published than resolved. The honest page says: *here is what I thought in March, here is what the evidence looked like by July, here is what would settle it.*

---

## 3. Agents as maintainers — the economics are there, the thesis is not

Four load-bearing pieces exist and have never been assembled into a claim:

1. **Agentic mass-customisation replaces professional services.** *"you turn the tail around. You use agentic workflows to create mass-customised and supported versions of the product… whoever creates this will be a domain expert in all of them, but the company is unlikely to have a person who understands all those phases."*
2. **Agents change the value margin.** *"The sweet spot is to operate at that margin where it is profitable for companies to pay you versus doing it themselves. As long as you operate there, you have a valid business model, and **now with agents that is possible in ways it was not before**."*
3. **Agents make multi-level expertise affordable.** *"In the past, having people who could operate at multiple levels of abstraction was expensive and rare. **With AI agents handling the volume, it becomes economically viable.**… That is not a problem AI creates. It is a problem AI finally makes economical to solve."*
4. **But agents currently add load, not remove it.** *"**AI slop** for low-quality, auto-generated pull requests that flood maintainer queues without adding value, increasing the burden on already-stretched maintainers. So AI is, for now, **adding maintenance load** rather than only creating maintainable work. This does not refute the thesis, it sharpens it."*

**And the fourth now has a named casualty.** cURL — ~30 billion installations, seven volunteers on the security team — **shut down its bug bounty on 31 January 2026** because ~20% of 2025 submissions were AI-generated slop against ~5% genuine, each consuming three to four people for up to three hours. Stenberg: *"The main goal with shutting down the bounty is to remove the incentive for people to submit crap."*

That is the corpus's own AI-slop finding, measured, with a date and a body count. **Write the page around it.** Independent corroboration in the research file: Black Duck OSSRA 2026 reports mean vulnerabilities per codebase **up 107% year on year** and attributes it to AI-accelerated code creation — correlation, not demonstrated causation, and the site should say so.

---

## 4. Agents are the primary audience — and this is a build requirement, not a topic

The 14 Aug 2026 agent-access report is directly load-bearing for commissioning this site:

> *"**The audience is disproportionately agents**… If agents are a primary audience, the failure mode is a primary failure mode."*

> *"many agents can only fetch URLs that a search engine has already returned to them… **A link listed inside a fetched document did not count as having been seen.** … **It can read the map and cannot walk it.**"*

> *"**The markdown is exemplary and the discovery layer is what stops agents using it.**"*

> *"the package registry page, which is a summary written for a different purpose, **becomes the authoritative source by default because it is the only one that ranks**."*

**The mitigation ladder is a build requirement for `open-source.sgit.ai`, not an afterthought:** get indexed (the real fix), make `llms.txt` self-sufficient (the cheap fix), and publish a single-file `llms-full.txt` concatenation (removes link-following entirely). See `07__` §1.

---

## 5. The four theses that are not written

These are the site's genuinely new pages. Each is an obvious consequence of material already in the corpus, and none exists.

**(a) Licence compliance at machine speed.** The pieces: one manual SPDX review of 17 transitive dependencies (Feb 2026); the **PBOM** — *"you leverage the ideas and concepts around SBOMs, but say, this is about permissions… a bill of actions or a bill of permissions"*, with the claim that *"this mapping is more important than the SBOM, because it should impact the SBOM"*; and the OSMM's bridge, *"**SPDX identifiers are the evidence artefact**"* with a falsifiable predicate: *"Engine dependencies whose SPDX identifier is source-available rather than OSI-approved: falsifies Level 3."*

Three components of a continuous, agent-run compliance check, and **nobody has written "agents doing licence compliance continuously" as a thesis.** The external evidence makes it urgent: OSSRA 2026 reports licence conflicts in **68% of audited codebases, up 12 points, the highest in its history**, and that **only 24% of organisations check AI-generated code across security, IP/licence, quality and all four categories**.

**(b) Provenance and attribution of AI-generated code.** The **signed-licence proposal** (24 Feb 2026) is the closest thing and it explicitly extends to code:

> *"**MIT-S** adds: 'This software includes a cryptographic signature from the original author. You must preserve this signature in all copies and substantial portions of the software.'… If the code is modified (fork): → Fork must be signed by the modifier → Original signature preserved alongside → **Chain: original author → modifier**"*

It was written about **human** authorship and never applied to AI-generated code. **The bridge is unwritten and it is the obvious next move** — a signature chain is exactly what an AI-authored contribution needs and exactly what it cannot currently produce.

**(c) Training-data licensing.** One substantive passage exists, in a 2025 published article:

> *"European lawmakers and creative industries are discussing mechanisms so that **creators can be remunerated when AI uses their works**… **Open-source projects can lead the way here by openly cataloguing their training sets** and filtering out data that's proprietary or sensitive. Ultimately, an ecosystem where **both models and their training data are open and auditable** is one where users (and regulators) have far more control."*

Plus one line elsewhere: *"Training data licensing | The fact-checked graph has value as training material (with consent)."* That is the whole of it. The research file supplies the current state of the **OSI's Open Source AI Definition** fight and the fact that **almost no "open source AI" model meets it — "open weights" is the accurate term.** That argument has moved a long way since 2025 and the corpus has not followed it.

**(d) Does the CC0 corpus change how agents can use it?** Unasked anywhere. `docs.diniscruz.ai` is CC0 — public domain, no attribution obligation. In a world where models train on public text and agents synthesise from it, **choosing CC0 over CC BY is a decision about machine reuse, not human reuse.** Whether that was deliberate is `02__` §1's question; what it *means* is a page nobody has written.

---

## 6. What the site should claim, and what it should not

**Claim:** that the economics of maintaining open source have changed, that the change is measurable, and that it currently runs *against* maintainers before it runs for them. You have the argument and cURL gives you the evidence.

**Do not claim** that agents will fix the sustainability problem. Every piece of 2025–26 evidence points the other way so far, your own corpus says so (*"AI is, for now, adding maintenance load"*), and the site's credibility rests on correcting optimistic stories rather than telling new ones.

**And keep the March/July contradiction visible while doing it.** A site arguing that AI changes open-source economics, which openly shows its own position moving as evidence arrived, is far more persuasive than one that only publishes the settled view.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
