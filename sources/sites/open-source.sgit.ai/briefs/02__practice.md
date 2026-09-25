# 02 — How he actually uses open source

The views are well documented. The **practice** is documented in fragments, and one significant part of it appears to be accidental. This is the page that makes the site credible — anyone can hold a position; showing the licence file is different.

---

## 1. ⚠️ Resolve this before writing the page: the estate runs three licences and nobody has noticed

| Layer | Licence | Evidence |
|---|---|---|
| **Code** — `SGraph-AI__App__Send`, all seven Issues-FS repos | **Apache-2.0** | `LICENSE` files; `license = "Apache 2.0"` in every `pyproject.toml` |
| **Briefs / corpus documents** | **CC BY 4.0** — footer on ~1,100+ files | *"This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0)."* |
| **Published articles** — `docs.diniscruz.ai` | **CC0 1.0 Universal** | `/root/docs.diniscruz.ai/LICENSE` |

**The briefs assume CC BY is the site-wide answer. The published-articles repo is actually public domain.** No document anywhere in the corpus mentions CC0 or reconciles it with the CC BY rule.

This is either a **deliberate maximal-openness choice worth a page** — CC0 on the essays, CC BY on the working corpus, Apache-2.0 on the code, each chosen for its layer — or an **inconsistency to fix before the new site inherits it**. It cannot be neither. Decide, then write it up; the reasoning is genuinely interesting either way, and the site loses credibility if a reader finds the mismatch first.

**And a second, larger gap:** there is no discussion anywhere in the corpus of **why Apache-2.0 rather than MIT**. The patent grant? The NOTICE file? Defensive termination? For a site about open source, written by someone whose entire estate is Apache-2.0, that is the most conspicuous unwritten page in the pack.

---

## 2. The CC BY reasoning, which *is* documented

Four distinct arguments, all quotable:

**Alignment, not compliance.** *"**The Creative Commons licence aligns with our zero-lock-in principle.** We are already committed to zero lock-in and open standards. A project released entirely under CC BY 4.0, using open source tools, with no proprietary components — this is the natural extension of our existing values."*

**It is a hard rule, not a preference.** Rule 2 of the corpus discipline: *"**CC BY 4.0 licence** at the bottom of every document."* Every day-index brief closes with it.

**BY vs BY-SA was actively considered, and BY won.** *"CC BY-SA 4.0 or CC BY 4.0 for the licence? | BY-SA encourages derivatives to stay open; BY is more permissive."* He chose permissive. **That is a real decision with a real reason and it deserves its own section** — especially since the survivability argument in `04__` §1 is, in effect, an argument that licences are the *weakest* of the structural protections.

**Openness is a credibility asset, and it is backed.** *"The transparency claim is credible because it is **backed** (the CC BY 4.0 corpus, the public briefs, rendering from a public vault)."*

**Downstream licences are respected.** *"CC BY 4.0 for the article and most contents; original source materials retain their own licences."* Wardley-map briefs carry a bespoke footer crediting Simon Wardley's own CC licence — a small discipline worth showing as an example.

---

## 3. The line: everything open, except at the customer

The stated position, verbatim:

> *"The line is very simple: **everything is open source**, so you do not even have that conversation. It is a key pillar. It is not for everybody, some investors will not like it, but you find the ones who do, and it is a good match. You can always commercial-license or relicense everything for a customer who wants it, but the core is all open source. **No part of the company or the ecosystem is not open source.**"*

And the single boundary:

> *"The moment you have closed repos is the moment you do customisations for the customer, the moment you hit customer data… that becomes the natural place for proprietary, non-public information, because at that point it is the customer's data and their strategy."*

With the commercial hook explicitly **not** being the code:

> *"We do not have that lock-in on technology, and that is fundamental. The natural line is a business line, and that is okay: that is when you charge to maintain it. It is the hook, but a hook based on value… The customer's schemas can be closed, a lot of their data is closed, **but our schemas are open**."*

The mechanism, historically: **selling access to private GitHub repos** — *"the repo is what you sell access to, it is how you communicate with the customer, and the customer simply clones or pulls to get all the scripts and everything needed to run it."*

**⚠️ This section and `04__` §2 must be written together.** Five weeks after the "nothing proprietary" statement, the corpus says customers get a subset — and calls it open-core itself.

---

## 4. What has actually been published

Verified against the reality document, not the briefs:

| Package | Where | Note |
|---|---|---|
| **`sgit-ai`** | PyPI · `SGit-AI/SGit-AI__CLI` | Name chosen because *"`sgit` was already taken"*. CI: push to `main` → tests → deploy to qa → **PyPI publish** |
| `sg-send-cli` | PyPI | **Deprecated 20 March 2026**, superseded by `sgit-ai` |
| **`issues-fs`** + six siblings | `owasp-sbot` org | `issues_fs_cli`, `issues_fs_service`, `issues_fs_service_ui`, `issues_fs_service_client_python`, `issues_fs_dev_utils`, `issues_fs_docs` — all Apache-2.0 |
| **The `osbot-*` / `mgraph-*` family** | PyPI · `owasp-sbot` | `osbot-utils` (885 mentions across the corpus), `osbot-aws`, `osbot-fast-api`, `osbot-fast-api-serverless`, `memory_fs`, `mgraph-db`, `mgraph-ai-service-cache`. Described internally as *"2 years of open source infrastructure"* |

**`MGraph-DB` is publicly credited to OWASP** — *"an open source, serverless graph database… published by the OWASP community… available in the OWASP SBot GitHub repositories (within `owasp-sbot/MGraph-DB`)"*. And the whole Issues-FS estate lives under **`owasp-sbot`**, tying the current work to the OWASP identity. See `06__`.

**Not documented anywhere:** why any of these was open-sourced, what the licence decision was for each, or what happened afterwards. Five real published projects and not one retrospective. The O2 Platform article is the honourable exception — and it is written *about* him, not *by* him in the first person.

---

## 5. "Publish the source next to the render" — a real, implemented practice

This is the strongest practice page available, because it is a mechanism rather than an intention.

**The markdown twin at every URL:**

> *"**every page is available as markdown at the same path with the extension swapped, and links inside the markdown point at markdown, so a traversing agent never has to parse HTML.**"*

**How it was built** — and this detail matters, because it is the hard part:

> *"we added native support to the library for serving `llms.txt` and `.md` files… The way it was done is important: it was done using **edge functions**. These are static files, the browser will not run any JavaScript on them, so we couldn't render encrypted data. What we did was add a little bit of JavaScript on the Lambda@Edge function that does the rendering of the file."*

**The ambition beyond markdown:**

> *"for every page on the website, serve not just the content but **the semantic knowledge graph of that content (and the references)**, alongside the LLM-friendly text."*

**And publishing the working, not just the output:**

> publish *"not just the article text but the full body of evidence, the semantic graph, the source materials, the multilingual versions, the agentic workflow provenance, and **every prompt and decision that went into the finished piece**."*

That last one is a genuinely radical openness claim and it is barely stated anywhere public. It belongs on the front page of this site.

---

## 6. Read keys, write keys, and openness applied to itself

> *"**A public vault's read key is published by definition**, so cataloguing read keys adds convenience and no exposure."*

versus the hard rule — a central list of write keys *"would be a single artefact whose compromise hands over write access to everything, and this site already documents the time a key exposure happened to it."*

And the irreversibility, which is the interesting part for an open-source site:

> *"**Nothing published can be corrected.** If a frozen sample vault turns out to contain something it should not, there is no edit available."* → *"**escrow the write key before publishing, not after.**"*

The self-applied version, listed by the corpus as an honest tension: *"Publishing security reviews | It is unusually transparent and **it publishes your own weaknesses to an audience that includes people looking for them**."*

**Use that as the page's closing argument.** It is openness costing something real, disclosed rather than glossed — which is exactly the standard the site holds others to in `04__`.

---

## 7. Licence compliance in practice — one artefact, and it is honest about being manual

The only worked compliance document in the corpus (25 Feb 2026, 761 words): one line, `fastapi-mcp = "*"`, pulled in **17 transitive dependencies**. The review tabulates each with its SPDX identifier against the project's Apache-2.0 licence and concludes: ***"License verdict: No compliance issues. All MIT, BSD-3-Clause, or Apache-2.0."*** It also flags a non-licence concern — Pydantic entering the tree against an architectural rule.

**That is one manual review, once, eighteen months ago.** There is no SBOM of the estate, no automated licence scanning, no policy document, and no upstream-contribution record. The corpus argues that companies should *"declare your supply chain"* and there is no evidence of doing so.

**Two honest options for the page.** Publish the gap as a stated intention with a date — which is consistent with the house style and costs nothing. Or close it before launch: an SBOM of the estate plus a CI licence check is a day's work, and it would make `04__`'s organic-food argument something demonstrated rather than proposed. **The second is much stronger.**

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
