# risks.sgit.ai — Brief Pack

**Pack version:** v1.0 · 22 August 2026
**Target site:** `risks.sgit.ai` — the conceptual and research home for risk
**Sources:** `SGraph-AI__App__Send` @ **v0.33.62** · `docs.diniscruz.ai` @ v0.3.123 · [riskmandate.ai](https://riskmandate.ai) · the four risk vaults published on sgit.ai
**Siblings:** sgit.ai · nhi.sgit.ai · pki.sgit.ai · graphs.sgit.ai (v0.3.9) · sg-sentinel.sgit.ai · newsroom.sgit.ai · issues-fs.sgit.ai

---

## 0. The commission

Two jobs, and the second is what makes this site different from the others in the estate.

**Job 1 — consolidate the concepts.** ~496,000 words across ~185 documents, written between 18 June and 22 August 2026, plus a February pre-history. **42 distinct concepts**, most of them well-developed, almost none of them published anywhere a reader or an agent can reach.

**Job 2 — be the site riskmandate.ai references.** riskmandate.ai is commercial: pricing, demos, partners, the customer/user angle of getting risks accepted. It currently also carries the concepts — nine library pieces, `plug.html`, `acceptable.html`, `ramm.html`. **Those concepts should live here, and riskmandate.ai should link to them.** §4 maps the refactor page by page.

**The primary audience is agents.** The brief says it plainly: *"to handle the cases where I need agents to have a good understanding of some of those key concepts and ideas."* That shapes everything — the concepts must be reachable in one fetch, stated as definitions rather than narrative, and machine-readable where possible.

---

## 1. The honesty constraint — read this before anything else

**Essentially none of this risk corpus is implemented in code.** Greps for `risk_`, `RiskAcceptance`, `risk_register` and `riskmandate` across `sgraph_ai_app_send/**/*.py` return **zero** matches. The Librarian's own reality file says so directly:

> *"All items below are PROPOSED. None have been code-verified. **Do not describe any of these as existing features.**"*
> — `team/roles/librarian/reality/ai-agents/proposed/risk-mandate.md`

What *has* shipped: **riskmandate.ai** as a vault-powered static site, the ten "how long would you accept" scenario documents, and **four published vaults with read keys** (§5).

**The honest sentence for `/shipped/`:** *"This is a research site. The concepts are argued, the worked examples are real graphs, and four vaults are live and browsable. The engine is not built."*

That framing is not a weakness here — it is what separates a research property from a product one, and it is the reason the split from riskmandate.ai works.

---

## 2. The thesis in one paragraph

Traditional risk management predicts the probability of a future event. This model asks a named human to **underwrite an exposure that already exists** — insurance-style, with personal liability attached. From that single inversion everything else follows: if the risk is real, it cannot be denied, so **there is no deny button** — only *how long* you accept it before re-accepting. The interval is not metadata about the decision; **the interval is the decision**, because each rung implies a specific operational response. A risk nobody has accepted has not gone away — it has come to rest on whoever is nearest, so **unaccepted is rated critical** and rolls upward without anyone choosing to escalate it. And because someone must now sign, they demand evidence — which manufactures the demand for the **grounding ladder** underneath: Reality → Twin → Measure → Evidence → Fact → Vulnerability → Risk.

---

## 3. The ten concepts an agent must hold

Full inventory of 42 in `01__concepts-index.md`. These ten carry the rest.

| # | Concept | The one line |
|---|---|---|
| **C1** | **Acceptance is underwriting, not prediction** | *"we are not describing the risk of something happening, we are asking them to accept it, to underwrite it"* |
| **C2** | **The no-deny mechanic** | *"the mistake of a lot of risk registers is that they allow the risk to be denied, which can only happen when the risk has not materialised"* |
| **C3** | **The interval ladder** | The interval *is* the decision. 1h / 4h / 1d / 1w / 1m / 6m. Default one month — deliberately just above the incident line |
| **C4** | **Unaccepted = critical** | An un-underwritten risk rests on whoever is nearest. *"that person right now is accountable for the business"* |
| **C5** | **Accepted is not acceptable** | Two orthogonal axes. Acceptable = *"the moment that the business is happy to stop funding remediation activities"* |
| **C6** | **The grounding ladder** | Reality → Twin → Measure → Evidence → Fact → Vulnerability → Risk. Downward grounds; upward classifies |
| **C7** | **Node type formulas** | *"the ontology definition of a node type is its upward and downward path-pattern, not a sentence about what it contains"* |
| **C19** | **Blast radius / authorization closure** | What the agent *can* reach, computed — not what it did |
| **C20–C23** | **The plug** | Who can stop it, how fast, at what cost, and **recoverability — the dimension money cannot buy back** |
| **C17** | **Not knowing is a fact** | Absence of evidence is a first-class node, countable and assignable |

---

## 4. The refactor: what moves off riskmandate.ai

riskmandate.ai's own `llms.txt` groups its pages. Mapping them:

| riskmandate.ai page | Type | Disposition |
|---|---|---|
| `/plug.html` — Who can pull the plug | **Conceptual** | **→ risks.sgit.ai `/plug/`.** Five dimensions, recoverability maturity, the "no plug" correction. RM keeps a one-paragraph summary + link |
| `/acceptable.html` — Accepted is not acceptable | **Conceptual** | **→ risks.sgit.ai `/acceptable/`.** Two axes, four quadrants, the interval table, Article 9(5). RM links |
| `/ramm.html` — acceptance maturity | **Conceptual** | **→ risks.sgit.ai `/ramm/`.** Five levels as graph predicates, entity model, the Agentic `+` variants, crosswalks |
| `/library.html` — nine concept pieces | **Conceptual** | **→ risks.sgit.ai `/concepts/`.** ⚠️ Currently a landing page with **no items actually linked** — see §7 |
| `/how-it-works.html` | Educational | **Split.** The mechanism → here; the product walkthrough stays |
| `/agents.html`, `/llms-full.txt`, `/.well-known/agent-content.json` | Technical | **Pattern to copy, not move.** RM's agent surface is good; risks.sgit.ai needs its own |
| `/v0/.../index.html` — "You own the risk" | Product | **Stays.** The positioning line |
| `/scenarios.html`, `/statics.html` | Product | **Stays** — but the ten scenarios' *source* (`07/02`) is a research artefact worth publishing here too |
| `/demos.html` + 3 demo pages | Commercial | **Stays** — though the three vaults themselves are shared assets (§5) |
| `/pricing.html`, `/partners.html` | Commercial | **Stays** |

**The line to draw:** riskmandate.ai answers *"how do I get my risks accepted, and what does it cost?"* risks.sgit.ai answers *"what is a risk, what is acceptance, and why is it modelled this way?"*

Every concept page that moves should leave behind a short summary and a link. And each moved page should carry a provenance note — see `06__boundaries-and-house-style.md` §5.

---

## 5. The four risk vaults — live, published, with read keys

From [sgit.ai/demos/vaults/](https://sgit.ai/demos/vaults/index.md). **These are the site's proof and must be first-class, not an afterthought.**

| Vault | What it is | Size | Why it matters here |
|---|---|---|---|
| **Risk Graph Explorer** | Public-by-design application, **7 views** recomputed simultaneously | 33 files · 428 KB · 7 commits | *"Exposed"* preset = **18 facts, 37 risks, 14 provisions**. Amber = exposure, green = assurance, **ghosted = unanswered**. `permissions: {}` — no network, no storage, all client-side |
| **Agentic Browser Isolation** | Living risk graph, **17 entry points** | 104 files · 2.4 MB · 4 commits | 5 altitudes L1 IT → L5 Board. Acceptance-gated escalation with **no deny button** — C2 and C4 running on real data. ~70 JSON files. `fs.write: []` |
| **Risk Mandate** | The software project itself, in a vault | 124 files · 1.9 MB · **98 commits** · 8 app entries | The most-committed vault published. Shows the method applied to its own build |
| **Regulation Graph** | EU AI Act as a citable graph, **11 views** | 207 files · 14.9 MB | **1,523 nodes · 1,944 edges.** Supplies Article 9(5), 14, 26(5)/(6) — the provisions the concepts hang on |

⚠️ Read keys are published for all four. **Never publish write keys, and escrow before publishing** — the standing rule from `08/14/sgit-site-and-hub/…read-keys-yes-write-keys-never…`. The Regulation Graph is already a *redacted republication* after an audit found a plaintext key; adopt its `PUBLIC.md` transparency convention.

---

## 6. The numbers the site can stand on

| | |
|---|---|
| **Browser-isolation graph** | **59 nodes, 75 edges** · Risk 13, Owner 7, Evidence 6, Vulnerability 6, Fact 5 · `gives_rise_to` 22, `backed_by` 14, `owned_by` 11 |
| **2FA graph** | **51 nodes, 53 edges** · ontology **24 node classes, 34 edge types** · MITRE **T1110.004** |
| **Article 26(5) instance** | 8 facts (one unevidenced), 5 risks, 4 stakeholders, **9 questions — 5 unanswered, "the actual output of the exercise"** |
| **The arithmetic finding** | **30 days** retained vs **6 months** required — *"arithmetic, not judgement, which makes it the most defensible finding in the graph"* |
| **Detection floor** | **12–18 hours** hyperscaler cost-reporting delay · the founder's AWS figure: **16 hours** |
| **Interval ladder** | 1h / 4h / 1d / 1w / 1m / 6m — default **one month** |
| **Altitudes** | **5** — L1 endpoint/IT → L2 security → L3 business → L4 enterprise → L5 board |
| **Plug profile** | **5 dimensions** · **4-way** time intersection (detection ∧ decision ∧ blast radius ∧ reversibility) |
| **Corpus** | ~**496,000 words**, ~185 documents, 1,450 files mention "risk" |
| **Prior art** | **59,131 words** across 8 published articles on docs.diniscruz.ai, Feb–Jul 2025 |
| **This pack's manifest** | **37 rows** — 19 Tier-0, 13 Tier-1, 1 Tier-2, 4 Tier-3 (do-not-publish). **69,724 words** of Tier-0+1 source, every path verified to exist at v0.33.62 |

---

## 7. Three things to fix while you are here

1. **`riskmandate.ai/library.html` links nothing.** It describes *"recorded talks, the full proposition deck, and the long-form pieces"* and lists nine concepts — but the page ships no links to them. That is the strongest argument for the split: the concepts have nowhere to live on a commercial site.
2. **RAMM's base levels are underspecified.** Levels 1, 2, 4 and 5 are named; only Level 3 has a stated predicate (*"all acceptance nodes have the five required edges"*). The Agentic `+` variants are better defined than the base model.
3. **The plug material contradicts itself in one place** — the corpus records a *"no plug"* correction that the published page does not reflect. Worth reconciling before republishing.

---

## 8. Build order

| Step | Section | Why here |
|---|---|---|
| **1** | `/acceptance/` — underwriting, no-deny, the ladder, unaccepted=critical | The founding inversion. Four concepts, one page each, all publishable near-as-is |
| **2** | `/acceptable/` — the two axes | Moves off riskmandate.ai. Already written for a public audience |
| **3** | `/ladder/` — the grounding ladder + node type formulas | **What agents most need.** Definitional, machine-readable |
| **4** | `/examples/` — the three worked graphs + the four vaults | Proof, with real numbers and live read keys |
| **5** | `/plug/` — five dimensions, recoverability | Moves off riskmandate.ai |
| **6** | `/register/` — graph of graphs, fractal registers, relevance fade | The register model |
| **7** | `/agents/` — the machine surface | The commissioned audience. Copy RM's pattern |
| **8** | `/shipped/` — what is argued vs what runs | Non-negotiable; §1 |
| **9** | `/ramm/` + `/maturity/` | Moves off riskmandate.ai; fix the base levels first |
| **10** | `/network/` — the seven-site boundary map | The split is the point; state it |

---

## 9. What is in this pack

| File | Contents |
|---|---|
| `00__BRIEF.md` | This document |
| `01__concepts-index.md` | **42 concepts** with canonical paths, maturity, newcomer-readiness and best quote |
| `02__risk-acceptance.md` | The acceptance thread traced in full — the commissioned centrepiece |
| `03__worked-examples-and-vaults.md` | Three worked graphs, four live vaults, every citable number |
| `04__riskmandate-refactor.md` | Page-by-page split, with the leave-behind text |
| `05__site-architecture.md` | Page-by-page IA with sources |
| `06__boundaries-and-house-style.md` | Seven-site boundary map, redaction watch-list, conventions |
| `07__gaps-and-open-questions.md` | Write-fresh list, open questions, honest tensions |
| `08__source-manifest.csv` | Machine-readable, every path verified at v0.33.62 |
| `sources__docs-diniscruz-ai-risk.json` | 8 published articles with dates, authors, PDFs, LinkedIn URLs |

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
