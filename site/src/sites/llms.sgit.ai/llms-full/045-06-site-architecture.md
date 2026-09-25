# 06 — Site Architecture

## The house pattern, plus one obligation

Copy `pki.sgit.ai`; add the `/llms-full.txt` it lacks.

And note the obligation this site carries that no sibling does: **a site called `llms.sgit.ai` will be read by more agents than any other page in the estate.** The agent-access report's finding — *"it can read the map and cannot walk it"* — is not a topic here, it is an acceptance criterion. `/llms.txt` must be **self-sufficient** rather than a link list, `/llms-full.txt` must exist, and the markdown twin must work at every path.

---

## Page by page

### `/` — the front page

The thesis in one sentence: **"Your app calls a language model without ever holding an API key."**

Then, immediately and on the same page, the qualification from `03__` §5 — the bridge protects the vault's key, and is **not yet** an egress boundary. A front page that makes the claim without the caveat is one click from being contradicted by the project's own brief.

Then the three-surface decision table, because most readers will discover they need no code at all.

### `/chat-pane/` — **build first**

`01__`. The decision table, the three surfaces, the honesty mechanisms as decisions-with-reasons, and the vault setup with its key tiers. **The one sentence to feature: *"Every existing vault app gets this without being changed."***

### `/chat-pane/samples/`

`code__chat-pane-samples.md`, verbatim. Eight samples plus the pre-ship checklist. **These must be runnable and kept runnable** — see §3.

### `/api/`

`02__`. The full `sg.llm.*` reference: one page per call with signature, grant, errors and a sample. **And a `/api/traps/` page** — the 8190 chunking, `available()` before rendering, images clearing after one turn, estimates never shown as bills, `listen` never implied by `chat`. That page will be the most visited on the site.

### `/security/`

`03__`. The four-layer ladder, the key tiers, the unfakeable recording indicator, cost integrity, **and the CSP gap in full**. Name Phase 4 as the fix and be clear it is not shipped.

### `/websites/`

`04__`. The three options, honestly compared, with the recommendation and the `sg-llm-chat` component as the concrete deliverable. **Label this section as the thin half** — it is a gap to fill, not an asset to publish.

### `/provenance/`, `/openrouter/`, `/local/`

`05__`. The 2024 OWASP talk forward; the provider-layer position; Ollama and offline. Three pages, in that order.

### `/agents/`

The dual surface: the API as machine-readable JSON, **and** the estate's own agent-readability practice — `llms.txt`, the markdown twin, `for_llms` filenames, the Lambda@Edge mechanism. Cross-link `coding.sgit.ai` `05__` §5.

### `/shipped/`

`00__` §5 unsoftened — the CSP gap, Phase 4, ViV parity, the audio-model constant — plus `05__` §6's table of what has not been built: **no evals, no structured-output spec, no model routing, no cost analysis despite a full ledger.**

### `/network/`, `/admin/`

House pattern. Build order published unresolved with `08__`'s questions and tensions visible.

---

## 3. What must be generated, not written

| Content | Source |
|---|---|
| The API reference | **generated from `AUTHORING.md`** — see `08__` Q1 |
| Error-code table | generated from the same |
| Code samples | **tested, not just published** — see below |
| Corpus counts (442 OpenRouter files, 92 injection, etc.) | generated or dated |
| Shipped / not-built | from the capability brief, with its date |

**The samples need a test.** A code sample that has drifted from the API is worse than no sample, and this API is eight months old and still moving (`listen` and `imagePart` landed a day after the rest). The cheapest mechanism: **ship the samples as a real vault app** — one that exercises `available`, `chat`, streaming, `cancel`, `usage`, `models`, `imagePart` and `listen` — and publish it as both the demo and the test. It would also be the best possible demonstration of surface 3.

---

## 4. The demo the site should ship

Everything above argues for one artefact: **a vault app that is the documentation.**

- It exercises every call, so the samples are tested by existing.
- It is openable by anyone with a read key, so the docs are runnable rather than readable.
- It demonstrates surface 3 while the reader is one click from surfaces 1 and 2.
- It is the estate's own pattern — *"the maps live in the source and are reviewable in a diff"* applied to an API reference.

⚠️ **With one condition, from `03__` §6:** a vault with an LLM key configured **carries a credential**, and publishing its read key shares the ability to spend it. So the demo vault needs a **`shared`-tier key with hard `maxCostPerSession` and `maxCallsPerSession` caps**, deliberately chosen for publication — or it needs to ask the visitor for their own key, which is the BYOK precedent from the Article 9 Lab and probably the right answer for a public demo.

**Decide that before publishing the vault, not after.** `08__` Q4.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
/briefs/07__boundaries-and-licensing.md
==============================================================================
