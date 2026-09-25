# Licence

## This pack

Everything in this brief pack — the nine numbered documents, `code__chat-pane-samples.md`, `09__source-manifest.csv`, this file and `README.md` — is released under the **Creative Commons Attribution 4.0 International licence (CC BY 4.0)**.

    Copyright (c) 2026 Dinis Cruz
    Licensed under CC BY 4.0 — https://creativecommons.org/licenses/by/4.0/

Attribution: **Dinis Cruz**, with AI co-authorship (Claude, Anthropic).

**In `code__chat-pane-samples.md`, the `sg.llm.*` calls are the shipped API contract; the surrounding UI code was written for this pack.** Say which half is which when publishing — a reader needs to know what is a contract and what is an example.

## The site this pack commissions

**The entire content of `llms.sgit.ai`** is CC BY 4.0, consistent with the network. Stamp every raw markdown document; gate with `licence-audit.py --check`.

**The code quoted throughout is Apache-2.0** — `SGraph-AI__App__Send` and the vault-html guides. Retain the notice where snippets run long.

---

## ⚠️ Do not create a second source of truth

The corpus already refused to, deliberately:

> *"**No — and deliberately.** It belongs in the two homes that already exist: `AUTHORING.md` — the canonical `window.sg.*` contract. **Adding a competing document would create a second source of truth that drifts.**"*

That reasoning applies to this site. **`AUTHORING.md` stays canonical; the site generates its reference from it and says so on the page.** `07__` §2, `08__` Q1.

---

## ⚠️ Keys — this site is the most likely place in the estate to leak one

Rule 13 of the estate's code rules: *"No vault keys in Git… **If one appears in a diff, block the commit.**"*

Every page here is about credentials, so:

- **Every sample uses an obviously-fake placeholder.** Never a realistic-looking key.
- **Add `sk-or-`, `sgit_vk1_` and OpenRouter key shapes to the CI leak check** before the first sample page ships.
- **If the demo vault in `06__` §4 is built: read key only**, and only after spend caps are set. A vault with an LLM key configured **carries a credential** — publishing its read key shares the ability to spend it (`03__` §6).

---

## Publish the security gap

`03__` §5. The corpus states plainly that CSP egress lockdown is not built, and that this is *"the gap that turns the current design from a convenience into a guarantee."*

**Publish it, unsoftened, within one click of the front-page claim.** Publishing a known limitation of your own security design is the estate's own standard — the vault catalogue publishes its own key-exposure incident, and the reality-document rule is *"briefs are aspirations, not facts."*

**Do not** publish an exploitation path, and do not frame it as a vulnerability disclosure. It is a scope statement: *the bridge protects the credential you trusted us with; it does not prevent all egress.*

## Do not publish

`library/alchemist/materials/` (whole tree) · the positioning and competitor briefs · `team/roles/appsec/reviews/02/21/…pki-architecture-security-revised.md` (*"an attack roadmap for live code"*) · `team/roles/grc/reviews/02/19/` (names a private individual with signature blocks).

**Tier-2 rows are marked `HOLD`** — the injection material must not be published until `08__` Q3 has an answer.

## Accuracy

**The API is eight months old and still moving** — `listen` and `imagePart` landed a day after the rest of it. Verify every claim against the shipped code, not only against `AUTHORING.md`, and date the contract on the page.

**The corpus counts here** (442 OpenRouter files, 92 injection, 144 Ollama, 2 cost-per-token) were measured in this session. Generate them or date them.

---

This file is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


==============================================================================
/briefs/code__chat-pane-samples.md
==============================================================================
