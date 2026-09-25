<!-- generated from history/numbers.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/history/numbers.html*

> The $8.8 trillion figure and what it actually measures, the 70–90% claim that is really a presence figure, and the statistics the research could not source — listed as unverified rather than published as established.

---

# The numbers, and the ones we refuse to publish

This site's credibility position is that it corrects other people's unsourced figures. That only works if it does not accumulate its own — so this page states what the load-bearing numbers actually measure, and lists the ones the research **could not source** and which therefore do not appear anywhere else on this site.

> **The standing warning, in the author's own words:***"the figures circulating are largely recycled from a smaller set of studies through commercial blogs, so **the direction is well supported and the precision is not**."* That is the right way to hold nearly every number in this field, including the ones below that survive scrutiny.

## "Open source is worth $8.8 trillion" — no

This is the most-repeated figure in the field and it is almost always cited without the thing that makes it meaningful. It comes from a Harvard Business School working paper (24-038), and it is a **demand-side replacement cost**: what it would cost *if every firm using open source independently recreated the software it uses*, priced at global average developer wages.

> **The source, linked — because this page asks other people to cite theirs.**[↗ Revealing Value: The Economic Power of Open Source Software](https://aiinstitute.hbs.edu/revealing-value-the-economic-power-of-open-source-software/), the HBS AI Institute's own summary of working paper 24-038 by **Manuel Hoffmann** (Harvard LISH), **Frank Nagle** (HBS Strategy Unit) and **Yanuo Zhou** (Rotman Toronto). It is worth reading rather than citing second-hand for one reason: it carries **both** figures, in the same table, which is exactly the context that falls off in transmission. It ends where this site does — on the *tragedy of the commons*, the risk that something free and ubiquitous is overused and underfunded, with the remedy framed as treating open source as critical infrastructure rather than as goodwill.
>
> **And two findings in it travel better than the trillion does.** Six languages — JavaScript, Java, Go, TypeScript, C, Python — account for **84% of the demand-side value**, and roughly **5% of developers** create the bulk of it. Those are *concentration* figures rather than valuation ones, they are measured rather than counterfactual, and concentration is [a survivability question](../survivability/index.md). The headline is the least useful number in the paper.

| Measure | Figure | What it means |
|---|---|---|
| **Demand-side replacement** | **$8.8 trillion** | Every firm rebuilds everything it uses, separately. Counts the same library once per user. |
| **Supply-side replacement** | **$4.15 billion** | Recreate everything *once*. Three orders of magnitude smaller, and the same paper's own figure. |
| **Goods-market model** | **~$177 million** | A substantive published critique argues the paper's own alternative model — the realistic counterfactual, in which firms would have bought or substituted rather than rebuilt — yields this. **Four orders of magnitude below the headline.** |

**The rule this site applies:** publish $8.8tn only with its definition and the critique attached, or do not publish it. It is not a fabrication — it is a real calculation of a specific counterfactual, and the counterfactual is unrealistic in a way that matters. Quoted bare, it functions as a claim about market value, which is not what it measures.

> **The author's own earlier writing cited it bare, and this page is the correction.** Stated rather than quietly fixed, because a site that holds others to a citation standard should be seen applying it to itself first.

## "70–90% of a modern codebase is open source" — a different measurement

The underlying finding, from Black Duck's OSSRA report, is that **98% of 947 audited codebases *contain* open source**. That is a **presence** figure, not a share-of-lines figure. "Does this codebase contain any open source at all?" and "what proportion of these lines are open source?" are different questions with very different answers.

And the population matters: OSSRA's audit sample is **skewed toward M&A due diligence** — codebases being examined because someone is buying the company. That is not a random sample of software, and there is no particular reason to think its composition matches the industry's.

**The direction is not in dispute.** Modern applications rest heavily on open source; that is obvious to anyone who has read a lockfile. The precision is what is unsupported, and quoting "70–90% of the code" as though it were measured lends a rhetorical exactness the evidence does not carry.

## The numbers that hold up

These appear elsewhere on the site, with their source, date and caveat:

| Number | Source and date | Caveat |
|---|---|---|
| **2,134 developers** on Linux kernel 6.18, the most in its history; 333 first-timers, 13,710 commits | Kernel release, 30 Nov 2025 | Counts contributors to one release, not the maintainer population. |
| **55.6% of developers** use PostgreSQL — the most-used database | Stack Overflow Developer Survey 2025, n=49,063 | Self-selected respondents. Reliable for direction, not a census. |
| **HTTPS page loads: <30% (2015) → ~80% globally, ~95% US**; ~10M certificates/day by Sept 2025 | Let's Encrypt / browser telemetry, 2015–2025 | Telemetry measures the browsers reporting it. |
| **~30 billion cURL installations; seven volunteers on the security team** | Project statements, 2025–26 | Installations are an estimate by the project; the security-team figure is a headcount. |
| **81 genuine reports, >$90,000 paid** since 2019; ~20% of 2025 submissions AI slop vs ~5% genuine; bounty closed **31 Jan 2026** | curl's own published figures, Jan 2026 | First-party, from the programme that ran it. [The full story →](../funding/curl.md) |
| **€100,000 in seven weeks** to free Blender, Jul–Sep 2002 | Contemporary records | — |
| **Three files out of eighteen thousand** removed in the USL v. BSDi settlement | Settlement, Feb 1994 | — |
| **Licence conflicts in 68% of audited codebases**, up 12 points — the highest in the report's history | OSSRA 2026 | Same skewed audit population as above. Use for direction. [Relevant to the compliance argument →](../agents/index.md#compliance) |
| **Mean vulnerabilities per codebase up 107% year on year**, attributed to AI-accelerated code creation | OSSRA 2026 | **Correlation, not demonstrated causation** — and the report's attribution is its own interpretation. [Cited that way on the agents page →](../agents/index.md) |

## The claims this site will not publish

These were investigated and **could not be established from a primary source**. They do not appear anywhere else on this site, and this list is the reason.

| The claim | Why it is not published |
|---|---|
| **"Linux runs 90% of the cloud"** | **No primary source found.** Every result traced back to SEO content citing other SEO content. The number may well be roughly right; there is nothing behind it to cite. |
| **"All 500 of the TOP500 supercomputers run Linux"** | TOP500's OS-family table could not be fetched, so this is **unverified** — though the top five on the June 2026 list are all Linux-derived, which is stated as what it is. |
| **Wikipedia's traffic figures** ("18 billion views, 500M uniques") | Traces to a **February 2014** New York Times report. `stats.wikimedia.org` is cache-only and could not be fetched. A twelve-year-old number presented as current. |
| **GitHub's scale figures** | **They do not reconcile with each other.** Octoverse 2025 reports 630M repositories and 180M+ developers; GitHub separately announced its billionth repository in June 2025; Wikipedia carries "150 million users, May 2025". Cite Octoverse and say which measure you mean — or say nothing. |
| **CNCF's 2025 headline** that Kubernetes is "the de facto operating system for AI" | The survey **published no sample size and no field dates.** And its own data shows **44% of organisations run no AI/ML workloads on Kubernetes at all** — which is difficult to reconcile with the headline. |

> **Why publish a list of things you are not saying?** Because the absence is otherwise invisible, and because these are figures a reader will encounter everywhere else. Naming them is more useful than silently omitting them — and it is the same reasoning that puts [the site's own open questions](../roadmap/index.md#open) on a page rather than in a footnote.

[← Six success stories](stories.md)[The practice →](../practice/index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
