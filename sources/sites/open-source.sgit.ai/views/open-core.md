<!-- generated from views/open-core.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/views/open-core.html*

> 18 June: there should be nothing proprietary. 17 July: customers only have a subset of the code that exists in the main repo. Five weeks apart, and the July document names the tension itself. Here is the one-question test that settles which one it actually is.

---

# Open core, or packaging?

The author's position on this moved between two dated documents, five weeks apart, and both are published here rather than tidied into one — because a site that shows its view moving as commercial pressure arrived is worth more than one that only publishes the settled version, and because **the July document names the tension itself**, which is the interesting part. Then the test that settles it.

## 18 June — nothing proprietary

> "my line is that everything the company does, the code, the logic, the functionality, and the schemas, is open source. **There should be nothing proprietary.** You never have the temptation of the bait model, where some of the best features are locked behind proprietary stuff, **because the community always sees through it**."

With a single, clearly-drawn boundary:

> "The moment you have closed repos is the moment you do customisations for the customer, the moment you hit customer data… that becomes the natural place for proprietary, non-public information, because at that point **it is the customer's data and their strategy**."

That is a coherent position with a defensible line: the boundary is the customer, not the feature set. Nothing that would be useful to a second customer is withheld from the first.

## 17 July — a subset of the main repo

> "more and more we want situations where the **customers only have a subset of the code that exists in the main repo**, because of security, because of maintainability, because of complexity."

And then, in the same document's own tensions table:

> "Open source versus the customer subset \| A fuller main repo than the customer receives sits uneasily with a pure open-source claim; **this is open-core, and worth saying so plainly.**"

> **Why this is worth publishing.** The July brief did not have to catch itself. It did, in its own words, in a table it wrote for the purpose — and then the position was never reconciled. That is a more useful artefact than a resolved statement would have been, because it shows the boundary moving under commercial pressure in real time, which is exactly what [2018–2024 demonstrated at industry scale](../history/index.md#reversals).

## The test that settles it

There is a real reconciliation available, and it turns on a distinction the June brief did not need to make. From 4 June, the subset is framed as **subtraction, not withholding**:

> "a company might only need 10% of them. So we create a version with only 10% of the features. It has **much less attack surface**, it is much cheaper to run" — "customisation is not only addition; it is subtraction… less attack surface… cheaper to run… maintainable."

That is a genuinely different thing from open core, and the difference is testable in one question:

> **Does the customer build contain anything the public repo does not?**
>
> **No** → it is **packaging**. A smaller build of public code, shipped for security and operability reasons. Every line the customer runs is public. Nothing is being held back; something is being left out.
>
> **Yes** → it is **open core**. And per the July brief's own instruction: *say so plainly*.

The test is deliberately blunt because the failure mode is gradual. Open core rarely arrives as a decision; it arrives as a series of individually reasonable exceptions, each one made under revenue pressure, each one moving the boundary toward the vendor. A binary test applied at each release is the only thing that catches that, and it is the same discipline [the stress test](../survivability/stress-test.md) applies to a vendor from outside.

## Both sides of open core, fairly

| The case for | The case against |
|---|---|
| It is the only model that has repeatedly funded large-scale development **without rent extraction on the core**. The core stays genuinely open, genuinely forkable, genuinely usable by people who will never pay — and somebody pays the engineers. | The boundary **always moves toward the vendor under revenue pressure**. That is not cynicism; it is what 2018–2024 recorded. The mechanism is the same every time, and no company has ever announced in advance that it intended to move the line. |
| **VS Code is the strongest live example done well** — MIT core, and an ecosystem that is real. It is difficult to argue that the world would be better off if it had not been built this way. | And it is the strongest example of the cost: a proprietary shipped binary, a licence-restricted marketplace, and **most of its very large user base does not know it is running proprietary software**. Executed smoothly enough that the boundary is invisible, which is precisely the problem. |

## Where this leaves the position

Unresolved, and marked as such. The June statement and the July statement are both on the record; the test above is the site's proposal for settling it, and applying it is a decision for the project rather than for this page. [The self-audit is where that decision will have to be made in public](../survivability/self-audit.md), because the same question — *what does the customer actually get, and how does it differ from what is published* — is leg one of a stress test we are running on ourselves.

> **Related, and next.** Whether the reconciliation holds in practice is best read against [why each of the estate's projects was open-sourced](../roadmap/index.md#interview) — six published projects, and retrospectives on the build order.

[← Sovereignty](sovereignty.md)[Somebody has to be the villagers →](villagers.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
