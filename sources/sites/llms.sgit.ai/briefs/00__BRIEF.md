# 00 — The Brief: `llms.sgit.ai`

**Version** v0.33.62 · 24 August 2026
**From** Dinis Cruz, via the SG/Send Librarian
**To** the agent commissioned to build `llms.sgit.ai`
**Licence** CC BY 4.0

---

## 1. The commission

> *"focused on my work about LLMs, which should include **the work and code samples of how to add an LLM chat pane to websites and vaults** (this will be `llms.sgit.ai`)."*

The chat-pane half is the strongest thing here and it is **already built, already documented, and already shipping** — but the documentation lives in an agent authoring contract that no human reader will ever find. The wider LLM work is broad and scattered.

---

## 2. The headline: there are three chat-pane surfaces, not one

This is the thing to get right on page one, because they differ in **who holds the key** and **who needs permission** — and most people assume there is only one.

| Surface | Where | App involvement | Permission needed |
|---|---|---|---|
| **1. The vault chat panel** | `/vault` → **✨ AI Chat** | none | **none** |
| **2. The same panel, beside a running app** | `/en-gb/app/` → **✨ AI** | **none** | **none** |
| **3. AI inside your own app** | your vault app's UI | you build it | **`permissions.llm.chat`** |

Surfaces 1 and 2 are **no-code**. The panel runs on **host chrome at the real origin**, so it holds the vault key and the microphone directly; the sandboxed app frame sees neither and cannot read the conversation.

> ***"Every existing vault app gets this without being changed."***

Surface 3 is the one that needs code, and it is the one the commission asked for samples of. `01__` covers all three; `02__` is the API; **`code__chat-pane-samples.md` ships runnable samples.**

---

## 3. The idea worth leading with

> **Your app calls a language model without ever holding an API key.**

The key lives in `.vault/llm/config.json`, **inside the permission floor** — the app cannot read it. The host makes the call. You send messages and receive text.

That single sentence is the site's thesis, and it is unusual enough to be the front page. Everything else — the grants, the consent HUD, the budget caps, the streaming contract, the cost ledger — follows from deciding that **the credential and the code that spends it should not be in the same trust boundary**.

---

## 4. What is actually shipped

Verbatim from the 2 August capability brief:

> **Shipped:** the shared engine (`SGLlm`), vault key/policy resolution (`SGLlmVault`), the admin settings panel, the host-native chat panel (multi-file, params, ledger, **voice**, **pasted screenshots**) on **both** `/vault` and `/en-gb/app/`, and the `sg.llm.*` bridge with permission + consent + budget + streaming + cancel + `listen` + `imagePart`.

That is a lot, and it is unusually complete for something with no public documentation.

---

## 5. ⚠️ The honesty constraint — and one item on it is load-bearing

The same brief's **Not built** list, and the first item is not a nice-to-have:

> **CSP egress lockdown.** *App frames are not yet served with a `connect-src` that blocks direct network access, so a malicious app could still call an LLM provider itself with its own key.* **"The bridge protects *your* key; it is not yet a boundary that prevents all egress. This is the gap that turns the current design from a convenience into a guarantee."**

**Publish that sentence.** A site whose thesis is *"your app never holds the key"* must say plainly that the mechanism currently protects the vault's key rather than preventing all egress. It is the difference between a convenience and a guarantee, the corpus says so itself, and a reader will find it either way.

Also not built:

- **Phase 4 minted credentials** — short-lived, budget-capped tokens so the vault holds a *reference*, not a key. Described as *"the commercially load-bearing piece"*, and the thing that would make vault-sharing safe with AI configured.
- **ViV kernel parity** — nested vault-in-vault kernels do not relay `sg.llm.*` yet.
- **A per-vault audio model setting** — the transcription model is a constant.

And the standing warning from Part 1 of the how-to, which belongs on every page about configuration:

> *"**Know what you are storing.** With a key configured, the vault contains a credential. Sharing the vault key shares the ability to spend it."*

---

## 6. The wider LLM work — broad, and unevenly developed

Beyond the chat pane, measured across the corpus:

| Thread | Files | State |
|---|---:|---|
| **Provenance / determinism** | 431 mention provenance, 421 determinism | **The oldest thread** — the earliest dated artefact in the whole estate is *Deterministic GenAI Outputs with Provenance*, OWASP AppSec Lisbon, 28 June 2024 |
| **RAG and graph grounding** | 2,095 | Pervasive, and mostly *about* graphs rather than about retrieval |
| **Prompt injection** | 92 | Real, concentrated in the agent-to-agent and sentinel clusters |
| **OpenRouter as the provider layer** | 442 | The estate's actual model access path — BYOK, model globs, generation-id reconciliation |
| **Local LLMs / Ollama** | 144 | Offline chat, the Docker dev environment, and two sg-compute specs (`ollama`, `local_claude`) |
| **Structured output** | 41 | Underdeveloped relative to how much the estate depends on it |
| **Hallucination** | 45 | Mostly framed as a grounding problem, not a model problem |
| **Cost per token / model routing** | 2 / 1 | **Almost nothing written**, despite the ledger being built |

**The shape to publish:** this estate's LLM position is not about models. It is about **provenance, grounding, and keeping the credential away from the code** — and that has been consistent since June 2024.

---

## 7. The numbers

| | |
|---|---|
| **The API** | `sg.llm.available` · `chat` · `cancel` · `usage` · `models` · `imagePart` · `listen` · `listenStop` · `listenCancel` · `listening` |
| **Grants** | `chat` · `models` · `usage` · `listen` — **default-deny**, and `listen` is never implied by `chat` |
| **Error codes** | 9 — `EPERM` `ECONSENT` `ENOKEY` `EREADONLY` `EBUDGET` `EMODEL` `EABORT` `EIMGSIZE` `EPROTO` |
| **Chat panel** | 24,000-char shared file budget · streaming coalesced on a ~50 ms timer · CSV/JSON ledger export with OpenRouter generation ids |
| **Images** | png/jpeg/webp/gif · downscaled to 1568px · **base64 chunked at 8190, not 8192** |
| **Voice** | host-held microphone · `google/gemini-3.5-flash` by default · consent every time |
| **Canonical docs** | `AUTHORING.md` §"Calling an LLM" · the `create-vault-apps` skill · the 2 Aug how-to brief |
| **This pack** | 9 documents + a runnable code-samples file · manifest of 24 rows |

---

## 8. Build order

1. **`/chat-pane/`** — the three surfaces, the decision table, and the samples. **This is the commission.** `01__` + `code__chat-pane-samples.md`.
2. **`/api/`** — the full `sg.llm.*` reference. `02__`. It exists today only inside a 9,487-word agent authoring contract; extracting it is the single highest-value publishing act available.
3. **`/security/`** — the key-never-in-the-frame model, the grant ladder, consent, budgets, **and the CSP gap stated plainly**. `03__`.
4. **`/websites/`** — what changes when there is no vault. `04__`. **This is the half of the commission with the least existing material** — see `08__` G1.
5. **`/provenance/`** — the oldest and most distinctive thread, from the 2024 OWASP talk forward. `05__`.
6. **`/local/`** — Ollama, the offline Docker chat, and the two sg-compute specs.
7. **`/shipped/`** — §5, unsoftened, with the CSP sentence quoted.

Publish the build order unresolved with `08__`'s open questions and tensions visible.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
