<!-- generated from survivability/index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/survivability/index.html*

> Every catalogued relicensing between 2018 and 2024 followed the same legal pattern: a single corporate copyright holder, having aggregated contributor copyright via a CLA, exercised the right to change terms going forward. Distributed-copyright projects could not be moved the same way.

---

# Survivability is not a property of the licence file

This is the best original idea on the site, and the most immediately useful, because it tells a buyer to stop reading the thing everyone reads and start reading the two things almost nobody does.

> "Survivable is not a property of the licence file. **It is a property of the copyright and trademark structure.**"

## The mechanism — which is what makes this a finding, not an opinion

> "An OSI licence is irrevocable for code already published, but the copyright holder may ship the next version under different terms. **Every catalogued relicensing between 2018 and 2024 followed the same legal pattern: a single corporate copyright holder, having aggregated contributor copyright via a CLA, exercised the right to change terms going forward. Distributed-copyright projects could not be moved the same way, because no single party had standing.**"

Read that carefully, because both halves matter and the first half is what people get wrong. **The licence you already have cannot be taken away.** That is real, and it is the thing the licence file genuinely guarantees. What the licence file does *not* tell you is anything at all about who can decide the terms of the *next* release — and for anyone who intends to keep using a dependency rather than freezing it at a version, that is the only question that matters.

Whoever holds the copyright decides. So the buyer's question is not "what licence is this?" It is **"who could change it, and what would stop them?"**

## Why the CLA is the mechanism

A Contributor Licence Agreement that assigns copyright — or grants a licence broad enough to relicense under — aggregates into one entity the standing that would otherwise be distributed across every contributor. That aggregation is usually presented as administrative hygiene, and it genuinely does solve real problems (provenance, the ability to defend the project, the ability to fix a licensing mistake). It also creates, as a side effect, **the single party capable of moving the project**.

A DCO — a sign-off attesting you had the right to contribute, with no assignment — does not. Under inbound=outbound, contributors licensed their work to the project under the project's licence, and nobody acquired the standing to change it for everyone. That is the whole difference, and it is visible in a repository from outside.

> **This is not an argument that CLAs are bad.** It is an argument that a CLA is a *load-bearing structural fact* that a buyer should price, and that "we use a CLA" and "we could relicense" are the same sentence. [Leg one of the stress test asks for it →](stress-test.md)

## Acquisition entrenches the closure — it does not reverse it

> "**HashiCorp went BUSL, IBM acquired it, and the licence stayed.**"

This is the kicker, and it disposes of the most common hope. The optimistic story is that a relicensing is a phase — a cash-strapped company under pressure, and a bigger, more comfortable owner will revert it. It did not happen. Terraform went BUSL in August 2023; IBM's acquisition of HashiCorp closed on 27 February 2025; the licence stayed. **Acquisition changes who holds the standing, not whether the standing exists.** Where the structure permits closure, closure survives ownership changes in both directions.

## The control case and the counter-case

|  | PostgreSQL — the control case | OpenSolaris — the counter-case |
|---|---|---|
| **Copyright structure** | **Distributed.** No company owns it | **Sun retained it**, with governance to match |
| **Could it be relicensed?** | **No party has standing** to do it | **Yes** — and the licence was deliberately chosen to be GPL-incompatible |
| **What happened** | Survived the entire relicensing wave untouched. Now **the most-used database** — 55.6% of developers | **Killed by Oracle after the acquisition.** The community forked to illumos |
| **The lesson** | **The licence was not the problem; the copyright holder was.** OpenSolaris was under an OSI-approved licence the whole time. Being open source did not save it, because being open source was never the property that decides this. |  |

And note the second half of the OpenSolaris story, because it is the point of [leg four](stress-test.md#leg4): **illumos survives.** Fork capacity mattered, and it mattered because a named party with the ability to run it actually existed. "The community would fork it" is not a plan; illumos was.

## The update that sharpens the argument

Two of the four relicensings partially reversed after the original argument was written. Elastic added AGPLv3 in August 2024; Redis 8 shipped under AGPLv3 around 1 May 2025. MongoDB remains SSPL; Terraform remains BUSL inside IBM.

> **That does not weaken the argument. It sharpens it.** The same single-holder standing that let them leave is what let them come back. Nobody had to negotiate with thousands of contributors in either direction. **Structure determines what is possible in both directions** — and a project that can be closed by one party's decision can be reopened by one party's decision, which is a description of dependence, not of safety.

One precision worth keeping: **none of the four went closed source.** They went *source-available* — SSPL, BUSL, and similar. The code remained readable; the freedoms did not remain. Conflating the two is the most common error in commentary on this period, and it makes the situation sound both better and worse than it was.

## What to do with this

### [Run the Change-of-Control Stress Test](stress-test.md)

*The tool*

Four legs, all answerable from public artefacts, requiring no cooperation from the vendor. Answer them here and keep the result — nothing is sent anywhere.

### [We run it on our own estate](self-audit.md)

*The self-audit*

A tool whose author will not apply it to themselves is a marketing asset. Here is the result on each of the four legs, what changing it would take, and which changes are planned.

### [Sovereignty, at a different scale](../views/sovereignty.md)

*The same argument*

"A European company gets acquired and the sovereignty moves" is this argument applied to a country instead of a project. Saying so makes both stronger.

[← The position](../views/index.md)[The stress test →](stress-test.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
