# 08 — Gaps, open questions and honest tensions

---

## 1. Must be built fresh

| # | Item | Why |
|---|---|---|
| **G1** | **The website chat pane** | **Half the commission, and the half with almost no existing material.** No component, no documented pattern, no code. `04__` §3 recommends a `sg-llm-chat` web component with a pluggable transport, built to the estate's component conventions, serving all three website options |
| **G2** | **A human-readable API reference** | The full contract exists only inside a 9,487-word agent authoring document. **Extracting it is the single highest-value publishing act on this site** — generated, not hand-written (`07__` §2) |
| **G3** | **The demo vault app** | `06__` §4. One app that exercises every call, published as both the documentation and its test. Also the best possible demonstration of surface 3 |
| **G4** | **An eval suite** | There is none. No benchmark, no regression test for prompt behaviour, nothing that would catch a model swap changing an output. For a site about LLM engineering this is the most conspicuous absence |
| **G5** | **Structured-output guidance** | 41 files. `Type_Safe` validates the *result*; nothing documents how the *request* is shaped to get a valid one |
| **G6** | **Cost analysis** | `cost per token` appears in **2 files**, despite a full two-source reconciled ledger with CSV export. **The data exists and nobody has looked at it** |
| **G7** | **Model routing** | **1 file.** No fallback chain, no cost/quality tiering, no routing logic |
| **G8** | **A prompt-injection position** | 92 files mention it; none addresses the case this site's own product creates. See Q3 |

---

## 2. Open questions

| # | Question | Where it stands |
|---|---|---|
| **Q1** | **How does a public reference avoid becoming a second source of truth?** The corpus refused to create one, with reasons | `07__` §2 proposes: `AUTHORING.md` stays canonical, the site generates from it and says so. **Needs a decision and a build step, not a convention** |
| **Q2** | **Who owns the `/vault` chat-panel page — this site or `sgit.ai`?** | Recommendation: this site owns the *capability*, `sgit.ai` owns the *product tour*. Unresolved |
| **Q3** | **What stops an attached vault file from injecting the prompt?** The panel attaches file contents to the model's context. Those files are untrusted. The 24,000-char budget and the `TRUNCATED` marker are honesty mechanisms, **not injection defences** | **The most important open question on the site**, and it is unaddressed anywhere in the corpus. **Do not publish an injection page until this has an answer** |
| **Q4** | **Can the demo vault publish a read key at all?** A vault with an LLM key configured carries a credential; publishing its read key shares the ability to spend it | `06__` §4: either a `shared`-tier key with hard caps chosen for publication, or BYOK following the Article 9 Lab precedent. **Decide before publishing, not after** |
| **Q5** | **When does the CSP gap get closed, and what does the site claim until then?** | `03__` §5. The scope statement is *"we protect the credential you trusted us with"*, not *"nothing leaves this frame."* That is publishable — but it is a weaker claim than the front page wants to make |
| **Q6** | **Is BYOK-in-the-browser acceptable for a public page?** | The Article 9 Lab does it deliberately. It is honest and it converts badly. Is that the right trade for `*.sgit.ai`? |
| **Q7** | **Should transcription model choice be per-vault?** | It is a constant today. The chat model and the audio model are necessarily different and only one is a setting |
| **Q8** | **What happens to `sg.llm.*` in nested vaults?** | ViV kernels do not relay it. An app inside a nested vault **silently** has no bridge — silently is the problem |

---

## 3. Honest tensions

1. **The thesis and the gap sit in the same sentence.** *"Your app never holds the key"* is true. *"Nothing leaves this frame"* is not, and the corpus says so. The site has to make the strong claim and the qualification together, on the same page, or it is overselling.

2. **The best documentation is the hardest to find.** `AUTHORING.md` is genuinely excellent — the 8190 explanation, the greenlet reasoning, the labelled-cost contract — and it is a 9,487-word agent authoring file that no human reader will ever open. **The quality is not the problem; the discovery layer is.** That is the same finding the agent-access report made about the whole estate.

3. **Half the commission is thin.** The vault story is shipped, complete and documented. The website story is three options and one adjacent precedent. **Say which half is which** rather than levelling them.

4. **A full ledger and no analysis.** Every call is logged with a generation id, tokens, cost and latency, exportable as CSV — and `cost per token` appears in two files. The instrumentation is better than the use made of it.

5. **No evals, in an estate whose thesis is provenance.** The whole position is *"you must be able to say where an output came from."* There is no mechanism for saying whether an output was any good, or for noticing when it stops being.

6. **The honesty mechanisms are the best work and the least visible.** One shared file budget, `TRUNCATED` in the model's own text, estimates never rendered as bills, images clearing after one turn, recording announced in words rather than an icon. **Each is a small refusal to mislead**, and collectively they are more persuasive than any feature list — and none of them is published anywhere.

7. **Publishing a demo vault teaches the thing and creates the risk.** A configured vault carries a credential. The best demonstration of the design is also the clearest instance of its standing warning.

---

## 4. Loose ends worth an hour each

- **Verify the API against the shipped code**, not just against `AUTHORING.md`. The contract is eight months old and moved twice in two days when `listen` and `imagePart` landed.
- **Add key shapes to the CI leak check** — `sk-or-`, `sgit_vk1_`, OpenRouter formats — before the first sample page ships.
- **Confirm the current default-model list.** It was corrected once already after alphabetical matching picked the oldest model on the key.
- **Check whether `hud.show.llm` is still the config key**, and whether `minimal` mode still defaults it off.
- **Establish whether the offline Ollama chat still runs**, and whether its FastAPI proxy is the same shape as the two sg-compute specs.
- **Find out what the audio model constant currently is.** The docs say `google/gemini-3.5-flash` *by default*, which implies configurability that Q7 says does not exist.
- **Ask whether Phase 4 minted credentials are scheduled.** They are described as *"the commercially load-bearing piece"*, and the site's strongest claim depends on them.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
