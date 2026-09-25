# 00 — The Brief: `threat-modeling.sgit.ai`

**Version** v0.33.63 · 7 September 2026
**From** Dinis Cruz, via the SG/Send Librarian
**To** the agent commissioned to build `threat-modeling.sgit.ai`
**Licence** CC BY 4.0

---

## 1. The commission

A site for the threat-modeling work: the published research (six white papers on docs.diniscruz.ai), the **practice** (seven real threat models written against a live codebase, one of them validated line-by-line against the code afterwards), and the platform argument (threat models as vault-native graph data rather than documents). The corpus is substantial — 269 files mention threat models; 58 AppSec review documents exist; a ThreatModCon 2025 vault is already published at `sgit.ai/demos/vaults/threatmodcon-2025/`.

**The name**: `threat-modeling.sgit.ai`. American spelling, because the discipline's own literature, its conference (ThreatModCon), and the founder's published article titles all use it — even though his prose sometimes writes *modelling*. Pick one, redirect the other; `threat-modelling.sgit.ai` should 301 here.

---

## 2. The thesis

> **A threat model is a claim about a system, and the site's job is to show claims being checked.**

This is what the estate has that the discipline mostly does not. The industry's own diagnosis, in the founder's words, is that threat modeling is *"a fairly subjective process"* producing *"static documents"* that are *"siloed"*, *"fragmented"*, and *"context-poor"* — the five failure modes named in the 2025 research. The answer this site publishes is not another methodology. It is two moves:

1. **Make the model machine-readable** — a semantic knowledge graph, not a Word document, so that overlaying STRIDE, MITRE ATT&CK and OWASP Top 10 on one system becomes a query rather than a workshop.
2. **Make the model falsifiable** — and then actually falsify it. On 16 March 2026 the AppSec role wrote a threat model of the Simple Token flow; on 17 March a validation pass checked every finding against the backend code and marked each one **CONFIRMED REAL / CONFIRMED SAFE / CONFIRMED MISSING / N/A (proposed, no code yet)**. Two claims were confirmed real, one was confirmed already mitigated, two were confirmed missing, and two were marked as proposals with no code behind them yet.

That second move is the site's differentiator. Everyone publishes threat models. Almost nobody publishes the audit that says which parts of their threat model turned out to be wrong.

---

## 3. What already exists (all verified on disk or live)

**Published research — six white papers, all 2025, all on docs.diniscruz.ai:**

| Date | Paper | The claim it makes |
|---|---|---|
| 29 May | Advancing Threat Modeling with Semantic Knowledge Graphs | The foundational one: threats/assets/mitigations/incidents as nodes; multi-ontology overlay; MGraph-DB as the memory-first store |
| 29 May | Threat Models as Mandatory Disclosures | The boldest: security's *"market for lemons"*; threat model publication as regulation, like financial statements and ingredient labels |
| 30 May | Graphs of Graphs of Graphs (G³) in Threat Modeling | Multi-view/multi-graph architecture; organic file-based evolution; ontologies as semantic layers |
| 30 May | Using Threat Modeling and Semantic Graphs to Secure the Digital Supply Chain | Supply chain as the hardest case |
| 30 May | Scaling Supply Chain Security using Threat Modeling, Semantic Knowledge Graphs and Maps | Adds the Wardley-map layer |
| 9 June | Supercharging AppSec Threat Modeling Services with GenAI and Semantic Graphs | The services/consulting argument; multi-stakeholder deliverables |
| 2 June | Linking Threat Models with Semantic Business Graphs | Technical findings ↔ business impact |

**The ThreatModCon 2025 vault (Barcelona) — already live**, and the single best artefact the site has: **eleven linked threat models** running Customer → Business → Application → Component → Package → Class → Method → Source Code → Environment → Runtime → Compute; **51 nodes, 179 threats, 3 critical findings**. Its own framing is the line the site should lead with: *"One model answers what could go wrong here. Eleven linked models answer what does this line of code put at risk."* It also carries the multi-persona demo (one SQL injection in a payment gateway, reframed for Board / CISO / CTO / Developer) and five Wardley walkthroughs moving from *"everything is critical"* to risk-based prioritisation.

**Seven real threat models in `team/roles/appsec/`**, written against SG/Send itself — see `02__`. They include a full STRIDE analysis with per-threat mitigation status, data flow diagrams, trust boundaries, attack surfaces, zero-knowledge verification, and a 37-entry risk register.

---

## 4. The honest constraints

- **Most of the practice material is a security review of the founder's own live product.** It names unmitigated vulnerabilities by number. `04__` sets the disclosure rule: publish the *method* and the *resolved* findings; hold anything still open. This is the site's hardest editorial problem and it must be solved before launch, not after.
- **The research is co-authored with AI** (several papers credit *"ChatGPT Deep Research"*). Keep that attribution visible — it is part of how the work was done.
- **The graph tooling is real but young**: MGraph-DB exists, the ThreatModCon vault is live, but the "continuous threat modeling" pipeline described in the papers is a vision with partial implementation. Mark the boundary on every page.

---

## 5. Build order

1. **`/eleven-layers/`** — the ThreatModCon vault, embedded and explained. The strongest thing here; lead with it.
2. **`/validated/`** — the 16→17 March threat-model-then-check-it pair, side by side. The site's signature.
3. **`/papers/`** — the six white papers, each with a one-screen summary and the PDF/LinkedIn links.
4. **`/practice/`** — the redacted method: STRIDE tables, the `.security.json` per-file schema, the two-modes pattern.
5. **`/graph/`** — threat models as vault-native data; the schema; the AppSec-tooling argument.
6. **`/disclosure/`** — the mandatory-disclosure thesis, published as the policy position it is.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


---
