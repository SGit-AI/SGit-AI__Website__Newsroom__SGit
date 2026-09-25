# llms.sgit.ai — brief pack

**For:** the agent commissioned to build `llms.sgit.ai`
**From:** Dinis Cruz, via the SG/Send Librarian
**Version:** v0.33.62 · 24 August 2026
**Licence:** CC BY 4.0 — see `LICENSE.md`, which carries a key-handling rule specific to this site.

---

## What this is

Your LLM work, and specifically **how to add an LLM chat pane to websites and vaults**, with code samples.

The vault half is **shipped, complete, and documented in a place no human reader will find.** The website half is thin. The pack says which is which rather than levelling them.

---

## The thesis

> **Your app calls a language model without ever holding an API key.**

The key lives in `.vault/llm/config.json`, inside the permission floor — the app cannot read it. The host makes the call.

**And the qualification, which belongs on the same page** (`03__` §5): the bridge protects *the vault's* key. It is **not yet** an egress boundary — the corpus says so itself: *"This is the gap that turns the current design from a convenience into a guarantee."*

---

## The headline: three chat-pane surfaces, not one

| Surface | Code | Permission |
|---|---|---|
| **1. Vault chat panel** (`/vault` → ✨ AI Chat) | **none** | **none** |
| **2. Beside a running app** (`/en-gb/app/` → ✨ AI) | **none** | **none** |
| **3. Inside your own app** | yes | `permissions.llm.chat` |

Surfaces 1 and 2 run on **host chrome at the real origin**, so they hold the vault key and the microphone directly; the sandboxed app frame sees neither. The sentence to feature:

> ***"Every existing vault app gets this without being changed."***

It is currently buried in a debrief.

---

## Read in this order

| File | Words | What it does |
|---|---:|---|
| **`00__BRIEF.md`** | 1.2k | **Start here.** Three surfaces, the thesis, what is shipped, the CSP gap, the wider work, the build order |
| **`01__the-chat-pane.md`** | 1.4k | **The commission.** The decision table, all three surfaces, the honesty mechanisms, vault setup and key tiers |
| **`code__chat-pane-samples.md`** | 1.4k | **Runnable samples** — minimum pane, cancel, cost meter, model picker, images, voice, file grounding, and a pre-ship checklist |
| `02__the-sg-llm-api.md` | 1.3k | The full `sg.llm.*` reference, the streaming contract, 9 error codes, and the traps |
| `03__the-security-model.md` | 1.1k | The four-layer ladder, key tiers, the unfakeable recording indicator, **and the gap** |
| `04__websites-vs-vaults.md` | 1.0k | What changes with no host. Three options, honestly compared — **the thin half** |
| `05__the-wider-llm-work.md` | 1.2k | Provenance since 2024, OpenRouter, local models, injection, and what is *not* built |
| `06__site-architecture.md` | 0.8k | Page by page, what must be generated, and **the demo vault that is the documentation** |
| `07__boundaries-and-licensing.md` | 0.8k | The second-source-of-truth problem, key rules, network boundaries |
| `08__gaps-and-open-questions.md` | 1.1k | 8 build-fresh items, 8 open questions, 7 tensions |
| `09__source-manifest.csv` | 24 rows | Every source, tiered 0–3. **Every path verified on disk** |

---

## Four things to know before you write

**1. The best documentation is the hardest to find.** The complete `sg.llm.*` contract exists **only** inside `library/guides/vault-html/AUTHORING.md` — a 9,487-word agent authoring document. It is genuinely excellent (the 8190 base64 explanation, the greenlet reasoning, the labelled-cost rule) and no human reader will ever open it. **Extracting it is the single highest-value publishing act on this site** — but generate it, don't hand-copy: the corpus explicitly refused to create a competing reference *"that drifts."*

**2. The honesty mechanisms are the best work and are published nowhere.** One 24,000-char budget shared across all attached files, not one each. `TRUNCATED` written into the text **the model sees**, *"so it cannot pretend to have read the whole thing."* Estimated costs rendered with `~` and **never as a bill**. Pasted images cleared after one send, because *"an image left attached would silently re-send and re-bill on every turn."* Recording stated in words — *"● Recording — your microphone is on"* — *"not left to an icon."* **Publish them as decisions with reasons.** That page is more persuasive than any feature tour.

**3. The website half is a gap, not an asset.** No component, no documented pattern, no code. `04__` compares three options — backend proxy, BYOK-in-browser (there's a precedent in the Article 9 Lab), or embed the vault surface — and recommends shipping a `sg-llm-chat` web component with a pluggable transport, built to the estate's own component conventions.

**4. One question has no answer and it matters.** The chat panel attaches vault file contents to the model's context. Those files are untrusted. **What stops one that says "ignore previous instructions" from doing so?** The budget and the `TRUNCATED` marker are honesty mechanisms, not injection defences. `08__` Q3 — **do not publish an injection page until this is answered.**

---

## The artefact this site should ship

**A vault app that is the documentation** (`06__` §4). One app exercising `available`, `chat`, streaming, `cancel`, `usage`, `models`, `imagePart` and `listen` — published as both the demo and the test, so the samples are verified by existing rather than by review.

⚠️ With one condition: a vault with an LLM key configured **carries a credential**. Either give the demo a `shared`-tier key with hard spend caps chosen deliberately for publication, or ask the visitor for their own key. **Decide before publishing, not after.**

---

## House pattern

Copy `pki.sgit.ai`, add the `/llms-full.txt` it lacks — and note the obligation this site carries that no sibling does: **a site called `llms.sgit.ai` will be read by more agents than any page in the estate.** Your own agent-access report's finding, *"it can read the map and cannot walk it"*, is an acceptance criterion here, not a topic.

---

This file is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
/briefs/01__the-chat-pane.md
==============================================================================
