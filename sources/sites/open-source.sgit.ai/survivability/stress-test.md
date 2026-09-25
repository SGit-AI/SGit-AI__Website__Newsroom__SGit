<!-- generated from survivability/stress-test.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/survivability/stress-test.html*

> Four legs — copyright structure, trademark holder, schema licence, named fork capacity — every one answerable from public artefacts without the vendor's cooperation. Answer them here and keep the result. A vendor that cannot answer them has answered them.

---

# The Change-of-Control Stress Test

Four questions to ask about any open-source dependency you are betting on. Every one is answerable from **public artefacts** — a repository, a licence file, a trademark register, a foundation charter — which means you can run this without the vendor's cooperation, without a procurement process, and without telling anyone you are doing it.

> "The stress test is a query, not an interview. 'Show me the CLA' and 'show me who holds the trademark' are answerable from public artefacts, and **a vendor that cannot answer them has answered them.**"

> **This runs entirely in your browser.** Nothing is sent anywhere — there is no server, no analytics on your answers, and no account. Your answers are kept in this browser's local storage so the page remembers them if you come back, and the **Copy the result** button gives you a markdown summary to paste into your own notes. Clearing the form removes them.

**What are you assessing?**

1. ### Leg 1 Copyright structure

   Who holds copyright in the code, and could one party relicense the next release?

   PassesDCO / inbound=outbound, copyright distributed across contributors. No single party has standing to change the terms.

   FailsA single-entity CLA aggregating contributor copyright — or one company simply wrote it all.

   UnclearYou could not find out from public artefacts.

   **Where to look:**`CONTRIBUTING.md`, a `CLA.md` or CLA-bot check on pull requests, `Signed-off-by:` lines in the commit log (a DCO signal), and the copyright headers in source files. **Unclear is not neutral** — see the verdict note below.
2. ### Leg 2 Trademark holder

   Who owns the name, and what would stop them using it against a fork?

   PassesHeld by a neutral foundation, with charter-level restrictions on transferring it.

   FailsHeld by the operating company, transferable with the company.

   UnclearNo trademark policy published, or the holder is not stated.

   **Why it is a separate leg:** a fork can take the code and cannot take the name. Losing the name means losing the search results, the documentation people have bookmarked, the package identifier, and the recognition a new user needs to find you at all. **Trademark is how a fork is made expensive even when it is legally permitted.**
3. ### Leg 3 Schema licence

   Are the data schemas and formats licensed separately, and openly?

   PassesCC0 or CC BY, licensed *separately* from the code.

   FailsUndeclared, or silently bundled with the code licence.

   UnclearYou could not establish what governs the schemas.

   **The leg everyone skips.**[The schemas matter as much as the code](../views/sovereignty.md#step2): your data is only portable to the extent that its structure is something you may reimplement. A schema bundled with a code licence that later changes moves with it — and an undeclared schema is a dependency with no terms at all.
4. ### Leg 4 Fork capacity

   If the terms changed tomorrow, who would actually run the fork?

   PassesA **named party** with the headcount and the mandate to run it. You can say who.

   Fails"The community would fork it" — with no named party.

   UnclearThere are candidates, but none with a stated mandate.

   **The test is whether you can name them.** illumos existed and OpenSolaris users had somewhere to go; OpenTofu and Valkey existed within weeks because organisations with engineers decided to fund them. A fork is not a right that gets exercised automatically — **it is a payroll**, and if nobody's payroll is available, the right is theoretical.

Answer the four legs to see the verdict.

Copied.

## How to read the verdict

**This is not a score.** Four passes does not mean "safe" and one fail does not mean "avoid" — plenty of excellent software fails legs one and two, including software you should absolutely keep using. What the four legs tell you is **what kind of exposure you are carrying**, so you can price it, plan for it, or decide it does not matter for this dependency.

A single-holder project you use for something easily replaced is a fine risk. The same structure under something with your data in it, five years of integration around it, and no named fork capacity is a different proposition entirely — and the point of the test is that you find that out *before* the announcement rather than during it.

> **"Unclear" is an answer.** Every one of these legs is answerable from public artefacts. When a project's own materials do not let you determine who holds copyright, who owns the name, or what governs the schemas, that opacity is itself the finding — and it is the finding for a project whose whole proposition is openness. *A vendor that cannot answer them has answered them.*

## Why we do not publish scores for named vendors

We ship the test; you run it. Publishing a scorecard about named commercial projects would turn a diagnostic into a weapon, and it would be a weapon wielded by [a participant in the same market](../about/index.md#interests) — which is exactly the conflict the test is designed to let you route around. The four legs work without us.

The one exception is running it on our own estate, in public. [That is the self-audit →](self-audit.md)

[← Survivability](index.md)[The self-audit →](self-audit.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
