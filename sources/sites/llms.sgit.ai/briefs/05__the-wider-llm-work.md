# 05 — The wider LLM work

Beyond the chat pane, the estate's LLM material is broad and unevenly developed. This is what is there, measured, with the threads worth building pages on.

---

## 1. The oldest thread, and the most distinctive: provenance and determinism

**The earliest dated artefact in the entire estate** is a talk: *Deterministic GenAI Outputs with Provenance*, **OWASP AppSec Lisbon, 28 June 2024** — 9,879 words of slides and notes, published on `docs.diniscruz.ai` under CC0.

Two years later the same instinct runs through everything: **431 files mention provenance, 421 mention determinism.** The chat panel logs an OpenRouter generation id per call. The Regulation Graph vault carries a SHA-256 of the retrieved bytes on every node. The grounding ladder terminates a claim at a measure.

**This is the site's spine, and it predates the products.** The position is not *"models are unreliable, use a better one"* — it is *"a model output is only usable when you can say where it came from."* Everything else on this site is a mechanism serving that.

---

## 2. Grounding, not prompting

`hallucin*` appears in only 45 files — and where it does, it is framed as a **grounding** problem rather than a model problem. The estate's answer is the grounding ladder:

```
Risk          := a downward path to a Vulnerability AND an upward path toward a top risk
Vulnerability := a Fact (grounded below) AND an upward path to a Risk
Fact          := a downward path to Evidence
Evidence      := a downward path to a Measure
Measure       := an observation of the node it measures, grounded on a Twin
```

And the anti-fabrication argument that follows: **a model asked to assess something will produce a plausible answer; a model asked to attach a finding to a provision hash, and to a measure, and to a twin, either finds the path or reports that it cannot.**

⚠️ **The ladder belongs to `risks.sgit.ai` and `standards.sgit.ai`.** This site should state it in three lines and link out — it is the *reason* the LLM work looks the way it does, not this site's subject. `07__` §5.

---

## 3. OpenRouter as the provider layer

**442 files mention it.** It is the estate's actual model-access path, and several design consequences follow that are worth a page:

- **BYOK per vault** — the key is the vault owner's, not a platform key.
- **Model allow-lists as globs** — `anthropic/*` in `models.allow`.
- **Generation ids as the reconciliation handle** — the ledger stores them, and cost is reconciled two-source (stream, then the authoritative `/generation` lookup).
- **Capability read from the live catalogue**, not a hard-coded list, *"so a new vision model works the day it ships."*
- **The default-picker bug** (`01__` §6) — alphabetical vendor-prefix matching silently selected the oldest model on the key.

**Nobody has written up "why route through a provider aggregator"**, and it is a real position with real trade-offs: one key for many models, capability metadata for free, and a single point of dependency between you and every model you use.

---

## 4. Local and offline

**144 files mention Ollama**, and there are three concrete artefacts:

- **The offline Docker chat** (18 March 2026) — a chat UI plus a FastAPI proxy to a host-native Ollama, with sessions surviving container rebuilds. The stated use case is disarmingly specific: *"Offline LLM chat during travel (flight on 19 March 2026). Must work completely disconnected from the internet once the Docker image is built and Ollama models are pulled."*
- **Two sg-compute specs** — `ollama` (939 LOC, `llm-inference`, 120s boot, EXPERIMENTAL) and `local_claude` (1,498 LOC, `llm-inference`, 180s boot, EXPERIMENTAL), each with manifest, CLI, service, schemas and tests.
- **A `docker/local-claude/` image** — a local LLM plus Claude Code harness.

**The through-line to publish:** the same `/api/chat` proxy shape works against local Ollama and against a remote tunnel, which is why the offline work was never a detour. And it connects to `open-source.sgit.ai`'s sovereignty argument — *"you are one SLA away from losing access"* applies to model providers more sharply than to almost anything else.

---

## 5. Prompt injection and agent security

**92 files.** Concentrated in the agent-to-agent communication and SG/Sentinel clusters, and adjacent to a lot of security work that is this estate's home ground.

The relevant mechanism already ships in the LLM bridge: **`JS__Expression__Allowlist` is deny-by-default**, and the corresponding rule is documented — *"Evaluate action is allowlist-gated"* — with a CI guard behind it. *"No arbitrary code execution — the shell-server pattern from OSBot-Playwright is not carried forward."*

**The unwritten page:** the chat panel attaches vault files to prompts. Those files are untrusted content. **What stops a file that says "ignore previous instructions" from doing so?** The 24,000-character budget and the `TRUNCATED` marker are honesty mechanisms, not injection defences. `08__` Q3 — and it is the most important open question on the site.

---

## 6. What is thin

| Topic | Files | Note |
|---|---:|---|
| **Structured output** | 41 | Underdeveloped relative to how much the estate depends on models emitting valid schemas. `Type_Safe` validates the result — but nothing documents how the *request* is shaped |
| **Evals** | 576 mentions of `eval`, mostly the ordinary word | **No eval suite, no benchmark, no regression test for prompt behaviour anywhere** |
| **Cost per token** | **2** | Despite a full ledger being built. The data exists; nobody has analysed it |
| **Model routing** | **1** | One mention. No routing logic, no fallback chain, no cost/quality tiering |
| **Embeddings** | 100 | Mentioned; no vector store, no retrieval implementation |

**Publish this table.** A site about LLM work that lists what it has *not* built is more credible than one that does not, and three of these five are genuinely load-bearing gaps: **evals, structured output and model routing** are the difference between a working integration and an engineered one.

---

## 7. The agent-facing documentation convention

Worth its own short page, because it is unusual and it is evidence rather than assertion.

The estate writes documentation **explicitly for model readers**, and says so in the filename:

```
library/dependencies/osbot-utils/type_safe/v3.1.1__for_llms__type_safe__testing_guidance.md
                                            ^^^^^^^^^
```

Together with the markdown twin at every URL, `/llms.txt` on every site, and the `llms-full.txt` single-file concatenation, that is a consistent practice: **when a model is a primary reader, write it a document rather than expecting it to parse yours.**

Cross-links to `coding.sgit.ai` `05__` §5 (the conventions chosen for agent readers) and `open-source.sgit.ai` `05__` (the argument about who reads code now).

---

## 8. How to sequence these pages

1. **`/provenance/`** — the 2024 talk forward. The spine, and the oldest thing here.
2. **`/openrouter/`** — the provider-layer position, including the default-picker bug.
3. **`/local/`** — Ollama, the offline chat, the two specs, and the sovereignty link.
4. **`/injection/`** — after answering `08__` Q3, not before. Do not publish a page about prompt-injection defences until the file-attachment question has an answer.
5. **`/not-built/`** — §6's table, on `/shipped/`.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
