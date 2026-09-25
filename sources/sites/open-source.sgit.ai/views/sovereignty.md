<!-- generated from views/sovereignty.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/views/sovereignty.html*

> A four-step argument: open source is the only structure under which independence is possible; the data schemas matter as much as the code; without ownership you are one SLA away from losing access; and company nationality is not sovereignty, because acquisitions move it.

---

# Sovereignty requires open source

Four steps, each one a claim you can disagree with separately. The argument is tight and it is **not** a claim that open source guarantees sovereignty — the site is careful about that distinction throughout, and the fourth step is where it connects to [the survivability argument](../survivability/index.md) and becomes the same argument at a different scale.

## Step 1 — Only open source makes independence possible at all

> "it is only when the code is open source that there is a possibility and the ability to have independence and sovereignty. Because **if you suddenly get cut off from the service, at least you have a chance**. That is why you have to have open source in order to have sovereignty."

Note the modesty of "at least you have a chance". The claim is about *possibility*, not outcome. Having the source does not mean you can run it, maintain it, or afford the people who could — it means the option exists rather than not existing. Every stronger version of this claim is wrong, and the author does not make one.

## Step 2 — The schemas matter as much as the code, and access is not control

> "**the data schemas are as important as the code.** Sometimes you say the data is open, you have access to the data, but you do not have access to the code or the schemas. And by access I mean you need to be able to **control** it, to **own** it."

This is the original move in the argument and the one most often missed. "Data portability" regimes generally guarantee that you can *get* your data — as an export, in a format the vendor chose, with a structure documented to whatever degree the vendor found convenient. That is access. It is not control. A schema you did not define and cannot change is a dependency exactly as binding as a binary you cannot recompile, and it is the one nobody audits.

The practical consequence is a question worth asking any vendor: *is the schema separately licensed, and under what?* It is the third leg of [the stress test](../survivability/stress-test.md) for precisely this reason.

## Step 3 — Without ownership you are one SLA away from losing access

> "without owning it you are dependent on service-level agreements, so **you are one SLA away from losing access**. And… whichever government has jurisdiction and control over the company that controls the code controls the other countries. It is literally that simple."

The second sentence is the one that has stopped being abstract. Jurisdiction over a supplier is jurisdiction over everyone downstream of that supplier, and this is now a live procurement consideration rather than a thought experiment. The argument does not require any particular geopolitical view to work — it only requires that jurisdictions can act, which is not in dispute.

## Step 4 — Company nationality is not sovereignty

> "who owns a company is already very fuzzy… especially with acquisitions you lose control. **A European company gets acquired by a US company and the sovereignty moves, you lose it.**"

> **This step is the survivability argument.** "A European company gets acquired and the sovereignty moves" and "a single copyright holder gets acquired and the licence changes" are the same mechanism at two scales — one about a country, one about a project. Saying so makes both stronger, and it is why the [stress test's four legs](../survivability/stress-test.md) are the practical form of a sovereignty question. **Buying from a company incorporated in your jurisdiction protects you exactly until someone buys the company.**

## The standard objection, and the answer

The reflexive objection to any of this is that it will stifle innovation. The answer given is not a defence of open source so much as a reframing of what is actually being protected:

> "I do not buy that this will stifle innovation, because the work is there. It is a question of whether there is a **rent-extraction process** happening, which is what proprietary software provides."

The work — the engineering, the invention, the people — does not disappear when the rent does. What disappears is the rent. Whether that reduces the incentive to do the work is the real question, and it is an empirical one that this argument asserts rather than settles.

## Where this argument is weak

| The objection | How much it lands |
|---|---|
| **Open source is necessary but nowhere near sufficient.** Having the source of a system you cannot operate, on infrastructure you do not own, with no one on staff who can read it, is sovereignty on paper only. | **It lands fully** — and the author concedes it. This is why [the villagers argument](villagers.md) exists: the capacity to read and repair is the part that actually has to be bought, and nobody is currently funding it. [Sovereignty bounties are the proposed answer →](../funding/index.md#bounties) |
| **The exit is theoretical unless someone has walked it.** "You have the source" is not a migration plan, and no organisation has budget for one they might never use. | **It lands**, and it is the strongest single idea on this site's response list — [fund the substitution side, not the supply side](../funding/index.md#bounties). Nobody currently does. |
| **Sovereignty arguments are often protectionism with better vocabulary.** | **Sometimes true, and worth watching for.** The test is whether the argument would accept a foreign-owned open-source stack over a domestic proprietary one. This one would — the criterion is structural, not national, which is exactly what step 4 says. |
| **Open source has its own single points of failure.** A commons maintained by seven volunteers is not obviously more sovereign than a vendor with a support contract. | **It lands hard**, and [cURL is the case in point](../funding/curl.md). The answer is not that the commons is safe; it is that its failure mode is visible and fixable by anyone, where a vendor's is neither. |

[← The position](index.md)[Open core, or packaging? →](open-core.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
