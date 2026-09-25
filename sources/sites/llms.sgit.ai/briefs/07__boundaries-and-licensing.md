# 07 — Boundaries and licensing

## 1. Licensing

**This site's content is CC BY 4.0**, consistent with the network. Stamp every raw markdown document; gate with `licence-audit.py --check`.

**The code quoted throughout is Apache-2.0** — `SGraph-AI__App__Send` and the vault-html guides carry it. Retain the notice where snippets run long, and do not imply the code carries the site's CC BY licence.

**The samples in `code__chat-pane-samples.md`** are written for this pack and are CC BY 4.0. The `sg.llm.*` calls inside them are the shipped API; the surrounding UI is ours. Say so, so a reader knows which half is a contract and which half is an example.

---

## 2. ⚠️ Do not create a second source of truth

The corpus already refused to do this, deliberately, and gave its reasons:

> *"**No — and deliberately.** It belongs in the two homes that already exist: `AUTHORING.md` — the canonical `window.sg.*` contract. **Adding a competing document would create a second source of truth that drifts.**"*

That was about a proposed skill, and **the same logic applies to this site.** A hand-written API reference on `llms.sgit.ai` will drift from `AUTHORING.md` within a release.

**The resolution:** `AUTHORING.md` stays canonical; the site **generates** its reference from it and says so on the page. That gives a human-readable public surface without a competing contract — which is the gap the corpus's own reasoning leaves open, since `AUTHORING.md` is an agent authoring contract that no human reader will find. `08__` Q1.

---

## 3. Do not publish

- **Any OpenRouter key, or any vault key.** Rule 13 of the estate's code rules: *"No vault keys in Git… If one appears in a diff, block the commit."* This site's subject matter makes it the most likely place in the estate for a key to end up in a sample.
- **The demo vault's write key**, if the demo in `06__` §4 is built. Read key only, and only after the spend caps are set.
- **`library/alchemist/materials/`** — the whole tree.
- **`team/roles/grc/reviews/02/19/`** — names a private individual with signature blocks.
- **`team/roles/appsec/reviews/02/21/…pki-architecture-security-revised.md`** — classified as *"an attack roadmap for live code."*
- **The competitor and positioning briefs.**

**And a rule specific to this site:** every sample must use a placeholder that is obviously a placeholder. Not a realistic-looking key. **Add `sk-or-`, `sgit_vk1_` and OpenRouter key shapes to the CI key-leak check** before the first sample page ships.

---

## 4. Publish the security gap — do not soften it

`03__` §5. The corpus states plainly that the CSP egress lockdown is not built and that this is *"the gap that turns the current design from a convenience into a guarantee."*

**Publishing a known limitation of your own security design is the estate's own standard** — the vault catalogue publishes its own key-exposure incident; the reality-document rule is *"briefs are aspirations, not facts."* A site that omitted this would be below the standard the rest of the network keeps.

**Do not** publish an exploitation path, and do not frame it as a vulnerability disclosure. It is a scope statement: *the bridge protects the credential you trusted us with; it does not prevent all egress.*

---

## 5. Network boundaries

| Site | Owns | Boundary |
|---|---|---|
| **`llms.sgit.ai`** | The chat pane, `sg.llm.*`, the LLM security model, provenance, providers, local models | — |
| `sgit.ai` | The vault product, the catalogue, the demos | **The closest neighbour.** `AUTHORING.md` and the vault UI belong there; the LLM capability *inside* them belongs here. Agree who owns the `/vault` chat-panel page — recommendation: **this site owns the capability, `sgit.ai` owns the product tour** |
| `coding.sgit.ai` | How code is written | **The samples follow its component conventions.** If `sg-llm-chat` gets built (`04__` §3), that site owns the component pattern and this one owns the LLM contract |
| `risks.sgit.ai` · `standards.sgit.ai` | Risk and instruments | **They own the grounding ladder.** State it in three lines and link out — `05__` §2 |
| `open-source.sgit.ai` | The open-source position | Sovereignty applies sharply to model providers (*"one SLA away from losing access"*); the agent-era theses are shared. Two links |
| `graphs.sgit.ai` | Graph theory | RAG-over-graphs sits on the boundary. Light link |
| `sg-compute.sgit.ai` | The compute platform | **Owns the `ollama` and `local_claude` specs.** This site links to them for the local-model story; that site owns the specs themselves |
| `newsroom.sgit.ai` | The future of news | Shares training-data licensing and the fact-graph-as-training-material thread |

---

## 6. House style

- **Every sample is runnable, and tested by being a real vault app** (`06__` §4).
- **Every API claim is traceable to `AUTHORING.md`**, with the date the contract shipped.
- **Estimates are rendered with `~`.** The site's own cost figures follow the rule it teaches.
- **State the grant before the call.** Default-deny is the model; the grant is the first thing a reader needs.
- **Publish the traps.** The 8190 bug shipped three times — that is documentation, not embarrassment.
- **-ise, not -ize**, and no em-dashes in the markdown deliverables.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
