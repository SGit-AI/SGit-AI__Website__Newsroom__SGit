<!-- generated from survivability/self-audit.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/survivability/self-audit.html*

> The Change-of-Control Stress Test run against the sgit estate itself, with the same four legs and the same evidence rules: the result on each leg, what changing it would actually take, and which changes are planned.

---

# We run the test on our own estate

A tool whose author will not apply it to themselves is a marketing asset. One who does is a standard. So here is [the Change-of-Control Stress Test](stress-test.md) run against this project's own estate, with the same four legs and the same evidence rules — the result on each, what changing it would take, and which changes are planned.

> **The short version.****The estate's copyright is held by one company** — the single-holder pattern the [survivability argument](index.md#mechanism) identifies as the mechanism behind every catalogued relicensing between 2018 and 2024. Applied to us, the test says so, for the same structural reason it says so of the projects we cite. That is the result a single-founder company with no external contributors should expect, and the useful part of this page is the second half: what each leg would take to change, and which of those changes are on the build order.

## The four legs

| Leg | Result | The evidence, and what it means |
|---|---|---|
| **1 · Copyright structure** | Fails | Copyright is held by **a single company**. There is no distributed-copyright structure and no DCO regime with independent contributors behind it — which is partly a consequence of [the position that open source is right even with zero contributions](../views/index.md#zero-contributions). That position is coherent, and this is its structural cost: a project with no external contributors has, by construction, no distributed copyright. **One party could ship the next release under different terms.** Nothing structural prevents it. |
| **2 · Trademark holder** | Fails | Held by the operating company, transferable with the company. There is no neutral foundation and no charter-level restriction on transfer. A fork could take the code and could not take the name — the same asymmetry the test asks you to check for in anyone else. |
| **3 · Schema licence** | Partial | The stated position is unambiguous — *"The customer's schemas can be closed, a lot of their data is closed, **but our schemas are open**"* — and [the argument that schemas matter as much as code is ours](../views/sovereignty.md#step2). What is missing is the artefact: the schemas are not **separately licensed** with their own declared terms in the way leg three asks for. The intent passes; the paperwork does not yet exist. This is the cheapest of the three to fix and it is not fixed. |
| **4 · Fork capacity** | Fails | There is no named party with the headcount and mandate to run a fork. Honestly: there is no community to be the unnamed party either, so this is not even the *"the community would fork it"* answer the test flags as failing — it is the answer below that one. The code is Apache-2.0 and genuinely forkable; **nobody is standing by to fork it**. |

> **Result, by our own tool: single-party dependent.** Three legs against, one partial. This is the pattern every relicensing in the 2018–2024 wave followed. It does not mean this project will be relicensed. It means **nothing structural would stop it**, and that an acquisition would carry the standing along with the company — which is exactly what we say about everyone else, and it is exactly as true here. The code already published is Apache-2.0 and stays that way whatever happens; the result is about the terms of the *next* release.

## Why publish this

Three reasons, in order of how much they matter.

**Because the test would be worthless otherwise.** The whole proposition of a four-leg test answerable from public artefacts is that it does not depend on the assessor's goodwill. An assessor who exempts themselves has demonstrated that the test is a marketing instrument dressed as a diagnostic, and every reader is right to discount it accordingly.

**Because it is the same discipline the author already applies elsewhere.** His own listed tension about publishing security reviews reads: *"It is unusually transparent and **it publishes your own weaknesses to an audience that includes people looking for them**."* That cost is real. It is also the reason the transparency claim is worth anything at all.

**Because the honest answer to "will you fix it?" may be no** — and that is still publishable, and still more useful than silence.

## What would have to change, and whether we intend to

| Leg | What fixing it actually requires | Position |
|---|---|---|
| **1 · Copyright** | Either move copyright to a neutral entity, or adopt a DCO with inbound=outbound and accumulate enough independent contribution that no single party retains standing. The first is a legal step available now; the second cannot be done unilaterally and is **years of other people's work**. | **Not resolved.** A single-founder company with no external contributors cannot distribute copyright by deciding to. Moving it to a foundation is possible and has costs — governance, control, the ability to relicense for a customer, which is [an existing commercial mechanism](../views/open-core.md). **No decision has been taken, and pretending one has would be worse than saying so.** |
| **2 · Trademark** | Transfer to a neutral holder, or publish a trademark policy that states what a fork may and may not call itself. | **Not done.** The second half — **publishing a policy** — costs almost nothing and removes the worst of the ambiguity even while the holder stays the same. It is the clearest unforced gap on this page. |
| **3 · Schemas** | Declare the schemas under their own licence (CC0 or CC BY), separately from the code, in the repositories that define them. | **Should be done, and is the cheapest.** The position is already stated; the artefact is missing. It is on [the build order](../roadmap/index.md), and there is no good argument for its not being done. |
| **4 · Fork capacity** | A named third party with engineers and a mandate. | **Not in our gift**, and worth being blunt about: **this leg is not fixable by the project it is about**. It is a fact about the world outside the project. Any vendor claiming to pass leg four on its own say-so should be treated with suspicion — including us. |

## What this does not concede

Failing the test is not a confession that the model is wrong; it is the model working. The four legs describe **exposure**, and the exposure described here is real, priced, and now public. What a reader should take from it:

- The code is **Apache-2.0 and already published**. The licence you have cannot be withdrawn — [that is what the licence file genuinely guarantees](index.md#mechanism), and it is not nothing.
- What is not guaranteed is the terms of the *next* release, and no assurance from us changes that. **Structure is what changes it**, and the structure is what this page is about.
- Every argument on this site about the risk of single-holder projects **applies to this one**. Readers should discount accordingly, and the discount is the honest price of the argument.

> **What this page does not yet cover.** It audits *structure*. An SBOM of the estate, a licence-scan result and an upstream-contribution record — the things the site argues companies should publish — are [first on the build order](../roadmap/index.md#supply-chain), and will be linked from here when they ship.

[← The stress test](stress-test.md)[The history →](../history/index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
