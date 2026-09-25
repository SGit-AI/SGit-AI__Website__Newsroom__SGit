<!-- generated from practice/publish-the-source.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/practice/publish-the-source.html*

> Every page available as markdown at the same path with the extension swapped, and the links inside the markdown pointing at markdown — the practice, how it was actually built with edge functions, and how this site implements it.

---

# Publish the source next to the render

This is the strongest practice page available, because it is **a mechanism rather than an intention**. It is also the one this site implements on itself — [this page has a markdown twin](publish-the-source.md), generated in CI, and the build fails if it is stale.

## The markdown twin at every URL

> "**every page is available as markdown at the same path with the extension swapped, and links inside the markdown point at markdown, so a traversing agent never has to parse HTML.**"

The second clause is the one that makes it work, and it is the one usually left out. Publishing a markdown version of a page is common. Publishing a markdown version **whose internal links also point at markdown** means an agent that arrives at one `.md` never has to return to the HTML surface — it can traverse the entire site without a parser, and without ever needing to guess that a twin exists for the next page.

## Why it is load-bearing rather than decorative

An agent-access report run against this estate in August 2026 found the failure precisely, and it is not the failure people expect:

> "many agents can only fetch URLs that a search engine has already returned to them… **A link listed inside a fetched document did not count as having been seen.** … **It can read the map and cannot walk it.**"

> "**The markdown is exemplary and the discovery layer is what stops agents using it.**"

And the consequence, which should worry anyone publishing technical material:

> "the package registry page, which is a summary written for a different purpose, **becomes the authoritative source by default because it is the only one that ranks**."

That is the real failure mode. Not that your documentation is bad — that **a worse summary of it becomes canonical** because it is the only version an agent can reach. Publishing excellent markdown that nothing can discover is a solved problem that stays unsolved.

## The mitigation ladder, and what this site ships

| Rung | What it does | Status here |
|---|---|---|
| **Get indexed** | **The real fix**, and the only one that addresses the root cause: agents that can only fetch what a search engine returned need the search engine to have returned it. | **In progress** — the site is new. Not in our gift on any particular timescale, and [on the build order](../roadmap/index.md) rather than quietly hoped for. |
| **Make `llms.txt` self-sufficient** | **The cheap fix.** If a link inside a document does not count as seen, then a file that is *only* links is the failure mode restated. It has to carry the substance. | **Shipped.**[llms.txt](../llms.txt) states the thesis, the central claim and its mechanism in the file itself. |
| **Ship `llms-full.txt`** | **Removes link-following entirely.** Every page, one file, one fetch. | **Shipped.**[llms-full.txt](../llms-full.txt), generated from the pages themselves. |
| **The markdown twin at every URL** | Keeps a traversing agent on the markdown surface once it arrives anywhere. | **Shipped, and enforced.**`validate.js` fails the build if any page lacks a twin, and CI regenerates and fails if a committed twin is stale. |

> **The mechanism is published with the site.**`admin/build/gen_markdown.py` converts each hand-written page, rewrites internal `.html` links to `.md`, and concatenates the result into `llms-full.txt`. It is about 400 lines with no dependencies, so it runs in CI with nothing installed. [The build tooling is documented →](../admin/index.md) — which is itself the practice this page is about.

## How the original was built — the part that is actually hard

> "we added native support to the library for serving `llms.txt` and `.md` files… The way it was done is important: it was done using **edge functions**. These are static files, the browser will not run any JavaScript on them, so we couldn't render encrypted data. What we did was add a little bit of JavaScript on the Lambda@Edge function that does the rendering of the file."

That detail is worth preserving because it names the genuine obstacle. The whole point of a markdown twin is that it is served as **plain text to a client that will not execute anything** — which is exactly what makes it useful to an agent, and exactly what rules out any client-side rendering strategy. If the content needs any transformation at all, the transformation has to happen *before* the bytes leave the server. An edge function is the smallest place that can be true.

This site takes the simpler road available to it: the twins are **generated at build time and committed**, so GitHub Pages serves static files and there is no runtime component at all. Same contract, no edge function — and CI is what keeps the two surfaces from diverging.

## The ambition beyond markdown

> for every page on the website, serve not just the content but **the semantic knowledge graph of that content (and the references)**, alongside the LLM-friendly text.

Not implemented here, and named as an ambition rather than a feature. [graphs.sgit.ai owns the how](https://graphs.sgit.ai); what this site would own is the argument for why a publisher should do it — and that argument is not yet written.

## And the version nobody has shipped

> publish **"not just the article text but the full body of evidence, the semantic graph, the source materials, the multilingual versions, the agentic workflow provenance, and **every prompt and decision that went into the finished piece**."**

That is a genuinely radical openness claim and it is barely stated anywhere public. It is worth taking seriously because of what it would prove: **in a world where a great deal of published text is machine-assisted, provenance is the only thing that distinguishes a considered document from a generated one** — and provenance is checkable if you publish it and unfalsifiable if you do not.

This site ships part of it and should be precise about which part. **The source materials are published verbatim** — [the briefs this site was built from are in the repository](../documents/index.md), in full, as the source of truth for anything the pages summarise. The evidence trail is partial: [every number carries its source, date and caveat, and the unverifiable ones are listed as unpublished](../history/numbers.md). **The workflow provenance and the prompts are not published**, and claiming otherwise would be exactly the kind of thing this page argues against.

> **The cost of this practice, in the author's own words.** He lists it as a tension: *"Publishing security reviews — it is unusually transparent and **it publishes your own weaknesses to an audience that includes people looking for them**."* That is real, it is the argument against everything on this page, and it is disclosed rather than glossed. It is also the reason the transparency is worth anything: [a self-audit that could not fail would not be evidence of anything](../survivability/self-audit.md).

## One place the openness stops, and why

The practice is not openness for its own sake, and the boundary is instructive. A public vault's **read key is published by definition**, so cataloguing read keys adds convenience and no exposure. A central list of **write** keys would be *"a single artefact whose compromise hands over write access to everything"* — and the estate has already had a key exposure, which it also documents.

The sharper rule comes from the irreversibility: *"**Nothing published can be corrected.** If a frozen sample vault turns out to contain something it should not, there is no edit available."* Hence the discipline — **escrow the write key before publishing, not after.** Publishing is a one-way door, and the time to think about it is before you walk through, which is a general principle rather than a vault-specific one.

[← Why Apache-2.0, not MIT](apache-vs-mit.md)[Agents and open source →](../agents/index.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
