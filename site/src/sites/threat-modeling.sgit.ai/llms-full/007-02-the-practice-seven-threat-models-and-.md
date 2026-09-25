# 02 — The Practice: seven threat models, and one that was checked

**Version** v0.33.63 · 7 September 2026
**Source** `SGraph-AI__App__Send/team/roles/appsec/` (58 documents) and `team/humans/dinis_cruz/briefs/`

---

## Why this section is the site

The research in `01__` argues that threat modelling should be objective, repeatable and continuously checked. This section is the evidence that the founder's own estate does it — on a live product, naming its own unmitigated weaknesses. **Publish the method in full; apply the disclosure rule in `04__` to the findings.**

---

## The seven

| # | Document | Date | What it is |
|---|---|---|---|
| 1 | `v0.2.15__threat-model__sgraph-send.md` | 12 Feb 2026 | The flagship: full STRIDE, DFDs, trust boundaries, attack surfaces, ZK verification, 37-entry risk register |
| 2 | `v0.6.30__brief__per-file-security-review-and-threat-modelling.md` | 25 Feb 2026 | The method: bottom-up, file-by-file, parallel security tree |
| 3 | `v0.7.1__appsec__threat-model-sg-send-skill-workflow.md` | 26 Feb 2026 | Two-modes analysis of an agentic workflow; T-001…T-006; risk matrix; prioritised recommendations |
| 4 | `v0.8.4__threat-model__token-consumption-flow.md` | 1 Mar 2026 | Token flow |
| 5 | `v0.10.19__threat-model__office-document-viewers-and-print.md` | 3 Mar 2026 | Document-viewer attack surface |
| 6 | `v0.16.11__appsec-review__simple-token-threat-model.md` | 16 Mar 2026 | The claim |
| 7 | `v0.16.14__appsec-review__simple-token-threat-model-validation.md` | 17 Mar 2026 | **The check** |

---

## Exhibit A — the validation pair (6 → 7)

**This is the site's signature page.** One day apart: a threat model, then a pass that validated every finding *"against the actual backend code"*, grounded in a stated code version and reality document. Its summary table has four verdicts, and the honesty of the "N/A" row is the point — two findings were proposals with no code behind them yet, and the validation says so rather than quietly claiming them:

| Verdict | Meaning | Count |
|---|---|---|
| **CONFIRMED REAL** | The threat model was right; the weakness is in the code, with file and line numbers | 2 |
| **CONFIRMED SAFE** | The threat model said "already mitigated" and the code agrees | 1 |
| **CONFIRMED MISSING** | A control the model said doesn't exist — confirmed absent | 2 |
| **CONFIRMED CORRECT** | A design the model called correct — confirmed correct in implementation | 1 |
| **N/A — proposed, no code yet** | The model proposed something; nothing is built; no credit claimed | 2 |

The confirmed-real findings were located precisely (three route methods, by line number) and the reasoning is a general principle worth publishing on its own: a parameter that bypasses the estate's `Safe_Str__Id` type validation is a finding *even though* downstream lookup validates the value, because **input sanitisation belongs at the route entry point**. That is a rule an agent can apply elsewhere — which is exactly what this site network is for.

**How to publish it**: two columns, claim beside verdict, with the "N/A" rows kept in. A validation table that showed only vindicated predictions would be marketing. The value is in the mixed result.

---

## Exhibit B — the eleven layers (the ThreatModCon vault, already live)

`sgit.ai/demos/vaults/threatmodcon-2025/` — presented at ThreatModCon 2025, Barcelona. **51 nodes, 179 threats, 3 critical findings** across eleven readable layers:

```
Customer → Business → Application → Component → Package → Class
        → Method → Source Code → Environment → Runtime → Compute
```

Its own framing is the best sentence in the corpus on why linked models matter:

> *"One model answers what could go wrong here. Eleven linked models answer what does this line of code put at risk."*

Two demonstrations ride on top of it. **Multi-persona reframing**: one SQL injection in a payment gateway, told four ways for Board, CISO, CTO and Developer — the practical form of the *Linking Threat Models with Semantic Business Graphs* paper. **Five Wardley walkthroughs**: the progression from *"everything is critical"* to risk-based prioritisation.

The vault also carries an engineering story worth telling on `/eleven-layers/`: it was adapted for **offline vault operation** — d3, three.js and tween.js inlined at pinned versions, data read through `sg.vfs.readText()` on vault-relative paths, with network fallback that reports failure rather than hiding it. And a data-integrity note that models the discipline the whole network runs on: two upstream JSON files had formatting errors, and both were repaired *"using only bracket adjustments and repositioning — no field edits or invented content."*

---

## Exhibit C — the method (2), publishable in full

The per-file framework, from a brief that opens with unusual candour about why it was commissioned: the team had shipped fast, *"some access tokens have already been leaked in posts (not yet abused, but only because usage is low and assets aren't high-value yet). This won't stay true as the platform grows."* The goal stated is not remediation but coverage — *"to make informed, risk-based decisions about what to address and when."*

**The approach is bottom-up, and the reasoning is fractal**: `File → Method → Class → Module → Path/Journey → Endpoint → Full Attack Surface`. Against every source file sits a `.security.json` in a parallel tree, with a schema the site can publish as a reusable artefact: `attack_surface` (endpoints, auth, input validation, rate limiting), `vulnerabilities` (id, severity, attack vector, impact, status, mitigation, and — the interesting field — **`risk_decision`**, which records an explicit accept-for-now with its reasoning), `secrets_exposure`, `dependencies` (including `trust_boundary_crossings`), and `redundant_code`.

That `risk_decision` field is the schema-level expression of the estate's whole posture: a finding is not binary, and the decision to defer is itself data with an owner and a rationale.

---

## Exhibit D — STRIDE, applied honestly (1)

The flagship threat model runs all six STRIDE categories as tables of *threat × likelihood × impact × mitigation status* — and the status column is populated with `NOT MITIGATED` as often as `MITIGATED`, each cross-referenced to a numbered vulnerability. It reaches a conclusion most vendor threat models never print: for the server-breach case the impact is recorded as **None**, mitigated *by design* through the zero-knowledge architecture, and Section 6 is a dedicated zero-knowledge verification rather than an assertion.

It also has a **Section 9: Assumptions and Open Questions** — the house rule (publish tensions unresolved) appearing in security work eight months before this pack.

---

## Exhibit E — the two-modes pattern (3)

The agentic-workflow threat model contains a transferable idea the site should extract as its own page. The document's most important section is a refusal to average two things together:

> *"The two modes look similar from the outside (both produce a download link) but have radically different security properties."*

Mode A (symmetric, key in the URL fragment): *"The key IS in the URL. Anyone who has the full URL can decrypt. Security = secrecy of the URL."* Mode B (PKI): *"The key is NOT in the URL… Security = possession of the recipient's private key."*

Its risk matrix scores eight threats across both modes with likelihood, impact and **residual risk after mitigations** — and the recommendations are prioritised P0–P3 **with an owner named for each** (DevOps, Dev, Designer, DPO, Sherpa). Two of them are notable for a threat model to produce: *"Publish the honest entity list in user documentation"* (a transparency action, owned by the DPO) and *"Document Anthropic log retention policy in DPO register"* (a supply-chain-of-AI action). The threat scenarios include **prompt injection via file content**, scored Medium likelihood / High impact for agentic use — this pack's clearest evidence that the estate threat-models AI systems, not just web ones.

---

## What the practice teaches that the papers cannot

The research says threat models should be living, checkable artefacts. The practice shows what that costs and what it produces: a model written in a day, a validation that partly contradicts it the next, findings that stay open with a recorded risk decision, and named owners for each recommendation. **The site should publish the mixed results, not the wins.** That is both the more useful memory for an agent and the only honest way to hold the mandatory-disclosure position in `01__`.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).


---
