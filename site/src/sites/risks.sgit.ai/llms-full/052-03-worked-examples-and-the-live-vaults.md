# 03 — Worked Examples and the Live Vaults

The proof layer. Three fully worked risk graphs with node and edge counts, four published vaults with read keys, and every citable number in the corpus.

`briefs/` = `team/humans/dinis_cruz/briefs/`.

---

## A · The four published vaults

**These are live, browsable, and have published read keys.** They are the strongest asset the site has and should be first-class, not a demos page.

| Vault | Read key (published) | Size | Contents |
|---|---|---|---|
| **Risk Graph Explorer** | `sgit_rk1_1c1b95f5903e35850a…` | 33 files · 428 KB · 7 commits | Public-by-design app. **7 views recomputed simultaneously**: estate graph, context, role risk map, risk chains, the register, acceptance (who holds what), incident-to-project. "Exposed" preset = **18 facts, 37 risks, 14 provisions**. Colour semantics: **amber = exposure, green = assurance, ghosted = unanswered**. `app.json` requests `permissions: {}` — no network, no storage, no account |
| **Agentic Browser Isolation** | `sgit_rk1_92cad4cea8f58c55f5…` | 104 files · 2.4 MB · 4 commits | **17 entry points**: narrative spine, per-altitude stakeholder pages, an explorer, two graph visualisations, raw data. ~70 JSON files. Acceptance-gated escalation across **5 altitudes (L1 IT → L5 Board)**, **no deny button**. `fs.write: []` |
| **Risk Mandate** | `sgit_rk1_a702fba803faac436…` | 124 files · 1.9 MB · **98 commits** · 8 app entries | The software project itself, in a vault. The most-committed published vault — the method applied to its own build |
| **Regulation Graph** | `sgit_rk1_c004daae386e8d17fa…` | 207 files · 14.9 MB · 2 commits | **1,523 nodes · 1,944 edges** from official Formex XML, SHA-256 hash-verified. 113 articles, 500 paragraphs, 417 points, 180 recitals, 13 annexes, 68 definitions. **11 views** incl. Cytoscape article graph, SQLite, RDF/Turtle export, an **Art 9 Lab with a Graph REPL** |

**Why each belongs on risks.sgit.ai**

- **Risk Graph Explorer** — the ghosted-edge convention *is* concept C17 (not knowing is a fact) rendered. Nothing else in the estate makes an absence visible.
- **Agentic Browser Isolation** — C2 (no-deny) and C4 (unaccepted = critical) running on real data across five altitudes. Assertion becomes demonstration.
- **Risk Mandate** — 98 commits of the method applied to itself.
- **Regulation Graph** — supplies Article 9(5) (the undefined "acceptable"), Article 14 (the plug obligation) and Article 26(5)/(6) (the worked example anchor). The concepts hang off real provisions.

⚠️ **Publishing rules.** Read keys yes, write keys never; escrow the write key *before* publishing, because a vault whose write key is lost is **frozen** — permanently readable, never updatable. The Regulation Graph is already a redacted republication after an audit found a plaintext key in its history; adopt its `PUBLIC.md` transparency convention. Source: `briefs/08/14/sgit-site-and-hub/v0.33.58__strategy-brief__sgit-topic-sections-catalogue-read-keys-yes-write-keys-never-frozen-vaults.md`

---

## B · The worked graphs

### 4.1 The 2FA worked example (26 June 2026) — the founding scenario

`06/26/risk-register-and-five-whys/v0.33.35__arch-brief__...md` and `06/26/semantic-graph-and-query-paths/v0.33.35__arch-brief__...2fa-use-case...md`.

- Vulnerability **V1**: admin accounts lack 2FA, backed by **E1** (configuration shows no MFA).
- Attack **ATK-1**: credential stuffing, mapped to **MITRE ATT&CK T1110.004**, performed by **TA-1**.
- Risks **R1–R9**: R1 accounts compromised; **R2** governance air gap (accepted by the wrong owner) — accepted by Head of GRC at a **4h** interval (P1), propagating GRC → CIO → CEO → Board, *each accepting at 4h because that is the only option open to them*; R3 unauthorised HR admin access; **R4** risk mis-classified until investigated (spawned by fact **F5**, which *lacks* evidence); **R5** data incident + **R6** GDPR breach (two distinct risks); **R7** salary/record tampering or fabricated hires; **R8** weekly-backup data-loss window; **R9** restore never tested.
- Interval resolution for R3: **4h struck off** (not technically possible), **48h** = P1, **2w** = incident, **1–2m** = funded project, **6m** = do nothing. Evidence **E3** ("no evidence of compromise") backs the absence of clear and present danger; **E4** = backup logs show weekly; **E5** = no record of a tested restore.
- Data classification is the blast-radius multiplier: **DC-1** full HR data (passports, salaries, bonuses, PIPs, reviews, hires, fires, dismissals) vs **DC-2** anonymised timesheets.
- Ontology size: **24 node classes, 34 edge types.**

### 4.2 The browser-isolation business case (12 July 2026) — the largest single graph

`07/12/worked-business-case/v0.33.48__briefing__...five-levels-graph.md`. Parsed from the embedded JSON:

- **59 nodes, 75 edges.**
- Node type distribution: Risk 13, Owner 7, Evidence 6, Vulnerability 6, Fact 5, Asset 4, Measure 4, PreventiveControl 3, Grant 2, AuthorizationClosure 2, BlastRadius 2, AcceptanceDecision 2, Reality 1, Twin 1, DetectiveControl 1.
- Edge type distribution: `gives_rise_to` 22, `backed_by` 14, `owned_by` 11, `measured_by` 5, `protected_by` 5, `exposes` 3, `reaches` 3, `observed_on` 2, `grants` 2, `accepted_by` 2, `underwritten_by` 2, `connected_to` 1, `impairs` 1, `emits` 1, `conditional_on` 1.
- Structured as **F1–F8** facts, **E1–E8** evidence, **V1–V6** vulnerabilities, **R1–R5** risks, **L1–L5** altitudes (IT/desktop → CISO → CFO/COO/DPO → CEO → Board).
- Concrete figure: vendor system cards reporting browser prompt-injection **attack success rates falling from roughly half to about one percent across a single model generation** — cited deliberately as the honest counterweight, since it is a large real improvement that still does not reach zero.
- Three risks *of the mitigation itself* are on the register: concentrated platform dependency, the platform now seeing the content, and friction routing users around it.

### 4.3 The Article 26(5) creditworthiness example (2 August 2026) — the complete instance

`08/02/vault-as-substrate/v0.33.55__arch-brief__...article-26-5...md`. Its own **Node and Edge Inventory** table:

| Type | Count | Notes |
|---|---|---|
| Reality | 1 | The running system |
| Twin | 1 | The deployed agent |
| Fact | 8 | One deliberately unevidenced (**F7**: suspension procedure never exercised) |
| Evidence | 7 | One absent |
| Provision | 5 | Annex III 5(b), Articles 26(5), 26(6), 14, 27 |
| Vulnerability | 3 | Derived from fact + provision |
| Risk | 5 | Four in a chain, one meta (**R5**: no acceptable level defined) |
| Stakeholder | 4 | ML platform lead, head of lending ops, DPO, CFO |
| Decision | 3 | Plus one deliberately absent (**D3**) |
| Question | 9 | **Five unanswered — "those five are the actual output of the exercise"** |
| Project | 2 | Plus one unfunded |

Hard numbers inside it: **thirty days** log retention observed vs **at least six months** required by Article 26(6) — *"arithmetic, not judgement, which makes it the most defensible finding in the graph."* Acceptance intervals: D1 = 1 month, D2 = 1 month, D3 = none, D4 = 3 months. Proposed new edge types: `governed_by`, `in_scope_when`, `answers`, `re_rates`.

### 4.4 The plug register (24 July 2026)

`07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__...five-dimension-profile.md` — a seven-row register re-expressed in the five-dimension profile, spanning from *"Agent misuses the isolated session"* (IT / small / fast / high recoverability) through *"Agent misuses the platform itself"* (COO/procurement / large / slow-contractual / medium) to *"Data leaves the boundary"* and *"Unattributable transaction"* (**recoverability: zero**) and *"Governance residual"* (the board / slowest / lowest).

### 4.5 The ten scenarios (2 July 2026) — the shipped MVP content

`07/02/risk-acceptance-and-scenarios/v0.33.40__strategy-brief__...how-long-would-you-accept...md`: every email you own; your calendar; your private messages; the company card; the OAuth token; all your repositories; the production database; your unlocked laptop; a database of customers' passwords; one customer reaching another. Each written as hook → reveal → punchline, the punchline always *"how long?"* Slide four shows the interval choices: **an hour, four hours, a day, a week, a month, six months.**

### 4.6 Concrete figures scattered across the corpus, with sources

| Figure | Meaning | Source |
|---|---|---|
| **12 to 18 hours** | Hyperscaler cost-reporting delay = a hard detection floor; that much damage before anyone sees it | `07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__...ability-to-stop...md` |
| **16 hours** | The founder's separate AWS figure: *"AWS usually takes 16 hours to give you the data, so how much damage can be done in 16 hours."* | `07/05/aws-configuration-risk-engine/` |
| **up to 24h** | Billing-lag damage window on the cost blast radius | librarian P-424, `.../reality/ai-agents/proposed/risk-mandate.md` |
| **1,088 prompts → 5,317 agent-executed commands**, 34 sessions, **305 internal servers**, **400+ custom attack scripts**, 20 known vulnerabilities, **~400 million records**, **9 Mexican government bodies** (incl. federal tax authority, civil registry, electoral institute), Dec 2025–Feb 2026 | Check Point AI Security Report 2026 | `07/28/agentic-risk-research/v0.33.53__research-brief__...has-it-happened-before...md:40` |
| **~30 targets**, **80–90%** of tactical operations agent-handled; detected Sept 2025, disclosed 13 Nov 2025; US Senate letter 2 Dec 2025 | GTG-1002 state-sponsored campaign | same file, line 38 |
| **1 outbound entry** in the escaped-agent population | July 2026 evaluation-sandbox escape (published 16 & 21 July 2026) | `07/27/outbound-agentic-risk/v0.33.52__research-brief__...md` |
| **63–76%** of security leaders experiencing or witnessing burnout in a single year | The internalisation argument | `07/31/keeping-the-register-healthy/v0.33.54__strategy-brief__...do-not-internalise...md` |
| **72% / 43% / 76%** | Change-resistance failure rates from three sources | `07/31/.../v0.33.54__strategy-brief__...design-for-players-who-will-not-play...md` |
| **7,500+ participants** | Preregistered escalation-of-commitment experiments: precommitment made later de-escalation seem more trustworthy | `07/31/projects-budgets-and-evidence/v0.33.54__arch-brief__...pre-approve-the-ladder...md` |
| **19.7M transfers** | Collision threshold cited as a P6 example | `team/roles/grc/reviews/02/17/v0.4.9__vulnerability-classification-framework.md` |
| **August 2026** | EU AI Act high-risk compliance deadline | `07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__...ability-to-stop...md` |
| **2026-08-04** | Black Hat USA Business Hall opening — the field-demo deadline the Aug briefs are written against | `07/28/mvp-and-field-demo/v0.33.53__arch-brief__...hand-them-the-ipad...md` |
| **~3,000 entries** | Recommended per-directory limit that shapes vault packaging | `08/14/sgit-site-and-hub/v0.33.58__strategy-brief__...component-registry...md` |
| **~496,000 words** | Size of the core June-18-to-August risk corpus | measured across the risk brief folders |

---

---

## C · Prior art — published risk articles on docs.diniscruz.ai

**59,131 words across 8 articles, February – July 2025** — a year before the `__Send` corpus, in the founder's public voice, already circulated. Full metadata with canonical URLs, first-published dates, authors, PDFs and LinkedIn posts in `sources__docs-diniscruz-ai-risk.json`.

| First published | Title | Words |
|---|---|---|
| 2025-02-15 | [Project SupplyShield: GenAI-Driven Supply Chain Risk Management and Compliance](https://docs.diniscruz.ai/2025/02/15/project-supplyshield__genai-driven-supply-chain-risk-management-and-compliance.html) | 8,802 |
| 2025-04-02 | [Maturity Models vs. Traditional Standards in Application Security](https://docs.diniscruz.ai/2025/04/02/maturity-modes-vs-traditional-standards-in-application-security.html) | 2,701 |
| 2025-04-10 | [Project Cybersage: AI-Powered Risk Contextualization & Security Reporting](https://docs.diniscruz.ai/2025/04/10/project-cybersage__ai-powered-risk-contextual.html) | 6,270 |
| 2025-05-29 | [Threat Models as Mandatory Disclosures](https://docs.diniscruz.ai/2025/05/29/threat-models-as-mandatory-disclosures__a-vision-for-security-transparency.html) | 7,160 |
| 2025-05-29 | [Advancing Threat Modeling with Semantic Knowledge Graphs](https://docs.diniscruz.ai/2025/05/29/advancing-threat-modeling-with-semantic-knowledge-graphs.html) | 9,217 |
| 2025-06-02 | [Linking Threat Models with Semantic Business Graphs](https://docs.diniscruz.ai/2025/06/02/linking-threat-models-with-semantic-business-graphs.html) | 9,816 |
| 2025-07-06 | [Finding the "Good Enough" Threshold: Optimizing Risk, Creativity, and Product Decisions](https://docs.diniscruz.ai/2025/07/06/finding-the-good-enough-threshold-optimizing-risk-creativity-and-product-decisions.html) | 4,924 |
| 2025-07-27 | [Project VulnAI: AI-Powered Vulnerability Risk Management Platform](https://docs.diniscruz.ai/2025/07/27/project-vulnai-ai-powered-vulnerability-risk-.html) | 10,241 |

**Two are directly load-bearing.** *Maturity Models vs. Traditional Standards* (Apr 2025) is the ancestor of RAMM, a year early. *Finding the "Good Enough" Threshold* (Jul 2025) is the ancestor of C5 and C25 — it is the appetite argument before it had the vocabulary, and it carries **15 mentions of risk acceptance / appetite**, the highest density on the site.

⚠️ **Provenance contract applies.** Anything republished keeps its original date, original link, original co-authors and an honest curation label — the same rules as the newsroom pack. `docs.diniscruz.ai` is **CC0** at source; the sgit.ai estate is CC BY 4.0. State the source licence per page.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).



==============================================================================
== briefs/04__riskmandate-refactor.md — source document, verbatim
==============================================================================

