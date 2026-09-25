# 08 — Gaps, open questions and honest tensions

---

## 1. Must be written fresh

| # | Item | Why |
|---|---|---|
| **G1** | **Why Apache-2.0 rather than MIT** | The entire estate is Apache-2.0 and the reasoning exists **nowhere**. For a site about open source, the most conspicuous unwritten page in the pack |
| **G2** | **The CC0 / CC BY reconciliation** | `docs.diniscruz.ai` is CC0; every brief footer says CC BY 4.0. Nobody has noticed. **Blocks `/practice/`** |
| **G3** | **A licence taxonomy** | No page's worth of material on GPL vs Apache vs MIT vs BSD, permissive vs copyleft, or licence compatibility. `copyleft` appears **zero** times with context; AGPL and LGPL zero; GPL twice, both as litigation precedent. `03__`'s research supplies the ground; the *position* has to be written |
| **G4** | **The first-person OWASP account** | `06__` §4. Not researchable — it is not on the public record. **Blocks `/owasp/`** |
| **G5** | **The Open Security Summit story** | Exists as a two-sentence lineage note plus three session URLs. Founding date, motivation, what changed when it left the OWASP umbrella, whether it still runs — all missing |
| **G6** | **Retrospectives on his own projects** | O2 Platform, MGraph-DB, OSBot, memory_fs, sgit-ai, Issues-FS. **Five real published projects and not one document explaining why any was open-sourced.** The O2 article is the exception and is written *about* him |
| **G7** | **The self-audit** | Run the Change-of-Control Stress Test on SGraph and publish it. **The most credible page available**, and it currently fails on leg one |
| **G8** | **An SBOM of the estate** | `04__` argues companies should *"declare your supply chain"*. One manual review exists, from February 2026. A day's work, and it converts an argument into a demonstration |
| **G9** | **Visual assets** | No timeline, no licence-family diagram, no map of the estate, no Wardley map of the open-source landscape. Everything is prose. A real production gap for a site |
| **G10** | **The four agent-era theses** | `05__` §5 — licence compliance at machine speed, provenance of AI-generated code, training-data licensing, and what CC0 means for machine reuse. **This is the most original writing still available** |

---

## 2. Open questions worth publishing unresolved

| # | Question | Where it stands |
|---|---|---|
| **Q1** | **Is the customer subset open core or packaging?** | `04__` §3 proposes the test: does the customer build contain anything the public repo does not? The corpus contradicts itself five weeks apart and diagnoses itself. **Needs a decision** |
| **Q2** | **Which funding model?** | Three proposals — labelling, a maintainer platform, exit bounties — none costed, none piloted, none compared. The corpus admits *"the sustainable funding question is unsettled"* |
| **Q3** | **Does the junior pipeline restructure or break?** | March says the density of learning per hour increases; July says work shifted to seniors and the pipeline is being disrupted. Four months, opposite directions |
| **Q4** | **Would SGraph pass its own stress test — and if not, will it change?** | Single-company copyright is exactly the failure pattern. The honest answer may be *"no, and here is why that is an accepted risk"* — which is still publishable, and better than silence |
| **Q5** | **Was CC0 on the articles deliberate?** | Nobody has said. And in an era of model training, choosing CC0 over CC BY is a decision about *machine* reuse, not human reuse |
| **Q6** | **Do agents help or harm open-source sustainability?** | Current evidence says harm — cURL's bounty closed 31 Jan 2026, OSSRA reports vulnerabilities up 107%. Is that a transition cost or the steady state? |
| **Q7** | **Is "open source AI" coherent without training data?** | The OSI's OSAID exists and drew heavy criticism. The corpus has one 2025 paragraph and has not followed the argument. `research__` Part 4 §6 has both sides |
| **Q8** | **What does the site owe a community it does not have?** | The position is that open source is right *"even if there are no contributions."* Coherent — and it leaves the site with nothing to say about governance, PR review, or codes of conduct, **despite the survivability argument turning on DCO-vs-CLA in practice** |

---

## 3. Honest tensions

1. **Arguing that open source is a strategy, not charity — while depending on a commons built by people who thought it was charity.** The position is defensible and the tension is real. Naming it is stronger than resolving it.

2. **The site's best idea would fail on its author.** Single-company copyright, single-company trademark. Publishing that is uncomfortable and is the whole point of a stress test.

3. **No community, by design.** Intellectually coherent, commercially sensible, and it means this site can say nothing credible about the part of open source most people mean when they say the words.

4. **Telling companies to declare their supply chain without having declared one.** One manual review, eighteen months old, no SBOM, no scanning, no policy. Either state it as intention with a date, or close it before launch.

5. **Correcting other people's numbers while the corpus carries uncorrected ones.** The $8.8 trillion figure appears without its definition; the OSSRA percentage is cited as share-of-code when it is presence-of-any. `03__` fixes both — and the site must not accumulate new ones.

6. **The strongest human asset is undocumented and only he can document it.** No amount of research substitutes for the interview.

7. **Three funding proposals is thinking; three funding proposals presented as a position is indecision.** And cURL just supplied evidence that arrived after all three were written.

8. **Publishing your own weaknesses to an audience that includes people looking for them** — the corpus's own listed tension about publishing security reviews. It applies to this site more than any other, and it is the reason to trust it.

---

## 4. Loose ends worth an hour each

- **Verify the marked-unverified facts** in `research__history-and-success-stories.md` — several founding dates and licences are flagged, and the site's credibility depends on not shipping them as established.
- **Decide the CC0 question**, then stamp consistently.
- **Book the interview.** `06__` §4 has thirteen questions ready.
- **Run `licence-audit.py --check`** across the estate before launch and publish the coverage number.
- **Get one SBOM generated** for the largest repo. It converts `04__` §4 from proposal to practice.
- **Check whether the Open Security Summit still runs**, and what its current state is. It is cited three times and never described.
- **Ask whether `owasp-sbot` hosting was deliberate.** If it was, it is a page. If it was convenience, that is worth knowing before the site claims otherwise.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
