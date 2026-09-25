<!-- generated from history/timeline.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/history/timeline.html*

> A sourced timeline of open source from the 1956 AT&T consent decree to the relicensing wave and its partial reversals — placed behind the corrections rather than in front of them, because the corrections are the part worth reading first.

---

# The timeline, 1955 → 2026

Deliberately the second page in this section rather than the first. [The six corrections lead](index.md), because a timeline is a shape everyone already has and the corrections are the part that changes what you think. This is the supporting material — with a column for what each moment is *evidence of*, since a date on its own argues nothing.

## Before there was a name (1955–1991)

| When | What happened | What it is evidence of |
|---|---|---|
| **1955–56** | SHARE, the IBM user group, forms and circulates code between installations. The **AT&T consent decree** (1956) bars Bell Labs from any business but common-carrier communications. | Sharing preceded ideology. The decree is the structural fact that made the next twenty-five years possible. |
| **1969–1975** | Unix is written at Bell Labs and distributed to universities **for media and postage** — the only lawful channel available. | [Correction 1.](index.md#unix) A compliance artefact, not a gift. |
| **1977–1980s** | Berkeley builds BSD on top of it; the Berkeley licence emerges as the permissive model. | Permissive licensing predates the debate about it by a decade. |
| **1982** | **The consent decree is lifted.** AT&T commercialises System V immediately. | The control experiment. Remove the constraint and the behaviour reverses within months. |
| **1983–1991** | The GNU project begins (1983); the GPL formalises copyleft (1989, v2 1991); the FSF is founded (1985). | Copyleft as a deliberate legal invention — a licence designed to make a structural guarantee the BSD licence does not attempt. |
| **1991** | **Linux 0.01.** Relicensed to GPLv2 in 1992. | Arrives at the exact moment the alternative becomes legally uncertain. |

## The window that decided it (1992–1998)

| When | What happened | What it is evidence of |
|---|---|---|
| **Apr 1992 – Feb 1994** | **USL v. BSDi.** Free Unix is clouded by litigation for two years. The settlement removes **three files out of eighteen thousand** and adds copyright notices to about seventy. | [Correction 2.](index.md#bsd) Litigation risk, not licence design, is what moved adoption. |
| **1995** | Apache httpd released; the Apache Group forms (Foundation, 1999). | The first large-scale demonstration of **neutral-foundation governance** — which is [leg two of the stress test](../survivability/stress-test.md#leg2), working, thirty years before anyone needed the test. |
| **Feb 1998** | **Christine Peterson coins "open source"** and has Todd Anderson introduce it. OSI founded shortly after; the Open Source Definition published. | [Correction 4.](index.md#peterson) |
| **22 Jan / 31 Mar 1998** | Netscape announces, then releases, the Communicator source. The code is so degraded the team eventually rewrites from scratch. | [Correction 3.](index.md#netscape) Opening a codebase is the start of the engineering, not the end. |

## The commons becomes infrastructure (1999–2013)

| When | What happened | What it is evidence of |
|---|---|---|
| **2000** | SQLite begins — public domain, and explicitly **not open-contribution**. | The case that inverts nearly every assumption on this page. [See the story →](stories.md#sqlite) |
| **Jul–Sep 2002** | **Blender's community buys its freedom** out of bankruptcy: €100,000 in seven weeks. | The one case where the romantic version is simply true. [See the story →](stories.md#blender) |
| **Nov 2004** | **Firefox 1.0.** Six and a half years after the Netscape release. | The other half of correction 3, and the reason to state the interval rather than the outcome. |
| **2005** | Git is written to replace BitKeeper after its licence terms are withdrawn. | A licence withdrawal by a single holder producing, by accident, the most widely used developer tool in the world. **An early instance of the pattern the survivability argument describes** — and of what fork capacity looks like when it exists. |
| **2008** | GitHub launches; the OWASP European Summit runs in the Algarve. | Distribution stops being the problem. [The summit thread starts here →](../owasp/index.md) |
| **2010** | **Oracle acquires Sun. OpenSolaris is killed.** illumos forks and survives. | The counter-case for [survivability](../survivability/index.md#cases): an OSI-approved licence did not save it; a named fork party did. |

## Eyeballs, foundations, and the wave (2014–2026)

| When | What happened | What it is evidence of |
|---|---|---|
| **Apr 2014** | **Heartbleed.** Two years undetected in OpenSSL. The Core Infrastructure Initiative follows. | [Correction 5](index.md#eyeballs), and the first industry-scale admission that critical infrastructure was unfunded. |
| **2014–2015** | **Kubernetes** released by Google; CNCF founded 2015. | The clearest strategic use of open source in the industry's history: commoditise the layer below your business. [See the story →](stories.md#kubernetes) |
| **Dec 2015 – 2025** | **Let's Encrypt** enters public beta. HTTPS page loads go from under 30% globally to roughly 80%, and to around 95% in the US; issuance reaches ~10 million certificates a day by September 2025. | The largest measurable civilisational impact on the list — and the mechanism was **automation, not price**. [See the story →](stories.md#letsencrypt) |
| **2018–2024** | **The relicensing wave.** MongoDB → SSPL (2018); Elastic → SSPL/ELv2 (2021); Terraform → BUSL (Aug 2023); Redis → RSAL/SSPL (Mar 2024). OpenTofu and Valkey fork within weeks. | The event the whole [survivability argument](../survivability/index.md) is built from. Every one: **a single corporate copyright holder with the standing to move.** |
| **Aug 2024 – May 2025** | **Elastic adds AGPLv3; Redis 8 ships AGPLv3.** IBM's acquisition of HashiCorp closes 27 Feb 2025 — **and Terraform stays BUSL.** | [Correction 6.](index.md#reversals) Structure works in both directions, and acquisition entrenches rather than reverses. |
| **Mar 2024** | **The xz backdoor** — engineered by the maintainer to survive review, found by one engineer benchmarking SSH latency. | The strongest single refutation of the eyeballs claim, and of social-trust models generally. |
| **Jan 2026** | **cURL announces its bug bounty will close** on 31 January, after ~20% of 2025 submissions were AI-generated slop against ~5% genuine. | The story that belongs to this site more than any other. [Read it →](../funding/curl.md) |

> **On sourcing.** This timeline is compiled from [the research document published with this site](../documents/index.md), which reports its fetch failures inline rather than working around them. Where dates are contested — the coining of "open source" is the clearest case — [the disagreement is stated](index.md#peterson) rather than resolved by picking one. Items the research could not verify from a primary source are **not on this page at all**; [they are listed as unverified](numbers.md#unverified).

[← Six corrections](index.md)[Six success stories →](stories.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
