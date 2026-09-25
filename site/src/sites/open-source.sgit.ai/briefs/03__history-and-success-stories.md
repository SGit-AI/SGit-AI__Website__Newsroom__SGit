# 03 — The history, and how to use it

**The corpus contains no history of open source.** Not thin — absent. Zero occurrences of *free software*, *copyleft*, *Stallman*, *GNU* as a movement, *Netscape*, *SourceForge*, *FSF*. Nothing before 2001. The GPL appears twice, both as litigation precedent.

So it was researched from scratch. **`research__history-and-success-stories.md` ships in this pack: 18,000 words, compiled 24 August 2026, WebSearch and WebFetch only, with every fetch failure reported inline rather than worked around.** It contains a sourced timeline 1955→2026, fourteen success stories, two instructive failures, an evidence table, seven both-sides arguments, seventeen corrected myths, and a source list separating what was fetched from what was only search-derived.

This document is the editorial guidance for turning that into pages.

---

## 1. Do not build a conventional timeline page

Everyone has one. The site's advantage is that **the accurate history supports your thesis better than the romantic one does** — and almost nobody publishes the accurate version. Lead with the corrections; use the timeline as supporting material behind them.

**Six findings to open with:**

**Unix circulated because it was illegal to sell it.** The 1956 AT&T consent decree barred Bell Labs from any business but common-carrier communications. Unix shipped for the cost of media and postage as a *compliance artefact*, not an act of generosity. The decree lifted in 1982; AT&T commercialised System V immediately. **The founding act of the sharing culture was regulatory, not ideological.**

**BSD lost to litigation risk, not to its licence.** USL v. BSDi ran April 1992 – February 1994 and clouded free Unix during exactly the window Linux needed. The settlement removed **three files out of eighteen thousand** and added copyright notices to seventy. The claim was nearly empty; the two years of *uncertainty* were decisive. Linux's victory is partly a litigation artefact.

**Netscape's source release was a six-year near-failure.** Announced 22 January 1998, released 31 March 1998 — and the codebase was so degraded the team threw it away and rewrote from scratch. Netscape 6 shipped November 2000; **Firefox 1.0 did not arrive until November 2004**, by which time IE had won. The founding case study of the open source movement is a cautionary tale about the bazaar.

**Eric Raymond did not coin "open source."** **Christine Peterson** of the Foresight Institute did, in the first week of February 1998 — and deliberately had Todd Anderson, who had more credibility as a Linux programmer, introduce it so it would spread memetically. Sources disagree on the exact date: OSI says 3 February; Peterson's account describes 2 and 5 February.

**"Given enough eyeballs, all bugs are shallow" is not a security property.** Heartbleed survived two years in the most security-critical library on the internet. Jim Zemlin, running the Linux Foundation, said of 2014: *"In these cases, the eyeballs weren't really looking."* And **xz was engineered by the maintainer specifically to survive review** — then caught by one engineer, Andres Freund, who was *benchmarking SSH latency*, not doing a security review. Robert Glass called the law a fallacy in 2003 on evidence that useful reviewers cap out at two to four.

**Two of the four relicensings reversed.** Elastic added AGPLv3 in August 2024; Redis 8 shipped under AGPLv3 around 1 May 2025. MongoDB remains SSPL; Terraform remains BUSL and HashiCorp is now inside IBM (closed 27 February 2025). And note the precision: none of them went *closed source* — they went **source-available**.

Every one of those supports your framing — that the model succeeds on **economics and structure**, not on virtue and not on eyeballs.

---

## 2. The success stories — pick six, not fourteen

Fourteen are researched. A site that publishes all fourteen at equal weight is a listicle. **Pick the six that carry an argument you are making elsewhere on the site**, and link the rest.

The recommended six, each chosen for what it proves:

| Story | What it proves | The number |
|---|---|---|
| **Linux** | Copyleft turned competitors into co-maintainers — no vendor could privately fork and out-develop the commons, so upstreaming was cheaper | Kernel 6.18 (30 Nov 2025): **2,134 developers, the most in its history**, 333 first-timers, 13,710 commits. Intel 10.4%, Google 7.9%, Red Hat 6.3% |
| **Let's Encrypt** | **The most measurable civilisational impact in the list.** And the mechanism was not price — it was removing the transaction. Free was necessary; **automated was sufficient** | HTTPS page loads: **under 30% globally in 2015 → ~80% globally, ~95% US**. From 1M certs (Mar 2016) to **~10M per day** (Sept 2025) |
| **SQLite** | **Inverts almost everything else.** Public domain, not open-source-licensed, and explicitly **not open-contribution** — it refuses patches from anyone who has not signed a public-domain affidavit, and the originals are kept **in a firesafe** | Estimated **1 trillion databases in active use**; plausibly the second most-deployed library after zlib |
| **PostgreSQL** | **The control case for the whole relicensing wave.** No company owns it, so no company can relicense it — exactly `04__` §1's argument, demonstrated | **55.6% of developers** use it, the most-used database (SO 2025, n=49,063) |
| **cURL** | **The most important open-source story of 2025–26**, and it is about AI destroying a funding mechanism. See §3 | **~30 billion installations**; seven volunteers on the security team |
| **Blender** | A community literally **bought its own freedom** out of bankruptcy | €100,000 raised in seven weeks, July–Sept 2002. *Flow* (2024), made entirely in Blender, won the Academy Award for Best Animated Feature |

Two more worth a paragraph each because they complicate the picture honestly: **Kubernetes** (Google commoditising the layer below its business — the clearest strategic use of open source in the industry's history, and a direct illustration of your Wardley framing) and **VS Code** (MIT core, proprietary shipped binary, licence-restricted marketplace — *"a textbook open core structure, executed so smoothly that most of its 75.9% user base does not know it is running proprietary software"*).

---

## 3. cURL is your page — build it properly

It belongs to this site more than any other story, because it is your arguments colliding in one project.

**The facts:** ~30 billion installations. One project lead, Daniel Stenberg, since 1998. Seven volunteers on the security team. In July 2025 he reported that **~20% of all bug-bounty submissions that year were AI-generated slop while only ~5% were genuine vulnerabilities**, each report consuming three or four people for thirty minutes to three hours. Over the programme's life since 2019: **81 genuine reports, over $90,000 paid**. On **22 January 2026** curl announced the HackerOne bounty would close on 31 January, moving to unpaid GitHub reporting. Stenberg: *"The main goal with shutting down the bounty is to remove the incentive for people to submit crap."*

**Why it is your page.** It is OS20 (*"open source is not free, somebody is always paying"*) as a measured fact. It is the AI-slop finding from your own corpus with a named casualty. It is the strongest possible argument for OS26–OS29 — that charity does not fix this and market forces must. And it is a live externality: **thirty billion installations, and the funding mechanism was destroyed by costs nobody was paying for.**

---

## 4. The evidence table — and one number to handle carefully

`research__history-and-success-stories.md` Part 3 has the full table with sources, dates and caveats. **Use it as the site's fact base and cite from it.**

The one that needs care, because your corpus already cites it:

> **"Open source is worth $8.8 trillion"** — **no.** $8.8tn is the **demand-side replacement cost**: what it would cost if every firm using OSS independently recreated it, priced at global average developer wages. The **supply-side** figure — recreate everything once — is **$4.15 billion**. And a substantive critique argues the paper's own alternative "goods market" model, which is the realistic counterfactual, yields **$177 million** — four orders of magnitude lower.

**Publish the $8.8tn only with its definition and the critique attached.** The corpus already cites it without either. That correction is itself a good short page, and it is exactly the discipline the site holds others to.

Same treatment for **"70–90% of a modern codebase is open source"** — the real OSSRA finding is that **98% of 947 audited codebases *contain* open source**, which is a presence figure, not a share-of-lines figure, from an audit population skewed toward M&A due diligence.

---

## 5. What the research could not verify — say so

The house style is to publish what is unresolved. Carry these forward:

- **"Linux runs 90% of the cloud"** — no primary source found; every result was SEO content citing other SEO content. **Do not publish it.** TOP500's OS-family table could not be fetched, so "all 500 run Linux" is unverified — though the top five on the June 2026 list are all Linux-derived.
- **Wikipedia's traffic figures.** The circulating "18 billion views, 500M uniques" is from a **February 2014** New York Times report. `stats.wikimedia.org` is cache-only and could not be fetched.
- **GitHub's own numbers do not reconcile** — Octoverse 2025 reports 630M repositories and 180M+ developers; GitHub separately announced its "1 billionth repository" in June 2025; Wikipedia carries "150 million users, May 2025". Cite Octoverse and say which measure you mean.
- **CNCF's 2025 survey published no sample size or field dates.** Its headline is that Kubernetes is *"the de facto operating system for AI"* — while **44% of organisations run no AI/ML workloads on Kubernetes at all.**
- Several success-story founding dates and licences are marked *not verified this session* in the research file. **Check them before publishing.**

---

## 6. Two failures, and why they belong on the site

The research covers two in detail. Publish at least one; a history of open source with no failures is marketing.

**OpenSolaris** — open-sourced under a licence deliberately incompatible with the GPL, under governance Sun retained control of, then killed by Oracle after acquisition. It is the clearest illustration of `04__` §1: **the licence was not the problem, the copyright holder was.** Illumos survives as the fork, which is also the point — fork capacity mattered and a named party existed.

The second is in the research file. Between them they make the argument that **structure, not licence, determines survival** — which is the site's best original idea, and it is much stronger demonstrated than asserted.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
