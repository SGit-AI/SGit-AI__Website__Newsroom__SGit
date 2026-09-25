# 05 — Site Architecture

**Status:** ✅ near-as-is · ✏️ needs framing · ✍️ write fresh · 🔗 links out · 📎 provenance block · ⚠️ correction first

`briefs/` = `team/humans/dinis_cruz/briefs/`. Concept refs (C1…C42) are defined in `01__concepts-index.md`.

---

## Shape

Two audiences, and the second is the commissioned one: **a human deciding whether this model makes sense**, and **an agent that needs the definitions**. The IA serves the human by depth and the agent by addressability — every concept gets a stable URL and an anchor.

```
risks.sgit.ai
├── /                    the inversion, in one screen
├── /acceptance/         ★ underwriting · no-deny · the ladder · unaccepted=critical
├── /acceptable/         accepted ≠ acceptable · appetite as a revealed band
├── /ladder/             ★ the grounding ladder · node type formulas · ontologies of ontologies
├── /register/           graph of graphs · fractal registers · relevance fade
├── /blast-radius/       authorization closure · CIA expansion
├── /plug/               who can stop it · five dimensions · recoverability
├── /practice/           owners · altitude · psychology · density · meta-risks · health
├── /ramm/               RAMM · AOMM · the plug-pull maturity model
├── /examples/           ★ three worked graphs + four live vaults
├── /concepts/           all 42, addressable, one anchor each
├── /agents/             ★ the machine surface
├── /shipped/            what is argued vs what runs
├── /origins/            Feb 2026 GRC → the June inversion → Aug formalisation
├── /network/            the seven-site boundary map
├── /documents/          raw markdown, source of truth
├── /admin/{comms,versions,index} · /about/participant.html
└── /llms.txt + /llms-full.txt
```

---

## `/` — the front page

| Element | Content | Status |
|---|---|---|
| The inversion | *"We are not describing the risk of something happening. We are asking someone to underwrite it."* | ✅ C1 |
| The mechanic | **There is no deny button.** Only how long you accept it before re-accepting | ✅ C2 |
| The consequence | A risk nobody accepted has not gone away — it rests on whoever is nearest, and it is rated **critical** | ✅ C4 |
| Proof strip | 59/75 · 51/53 · 1,523/1,944 · 4 live vaults · 5 altitudes · 6 intervals | ✅ §6 of `00` |
| Honesty line | *"This is a research site. The concepts are argued, the graphs are real, four vaults are live. The engine is not built."* | ✍️ |
| The split | One line on what riskmandate.ai is for, and a link | ✍️ |

---

## `/acceptance/` — build first

| Page | Concept | Source | Status |
|---|---|---|---|
| `/acceptance/underwriting/` | **C1** — *"the analogy is insurance: you are underwriting the damage… The business executive is ultimately accountable for everything"* | `briefs/06/18/agentic-permissions/v0.33.40__arch-brief__…the-risk-already-exists.md` | ✅ |
| `/acceptance/no-deny/` | **C2** — *"the mistake of a lot of risk registers is that they allow the risk to be denied, which can only happen when the risk has not materialised"* | `briefs/06/23/risk-mandate-product-and-workflow/v0.33.33__dev-brief__…no-deny-time-boxed-acceptance-expiry-as-cost…md` | ✅ **the most graspable page on the site** |
| `/acceptance/the-ladder/` | **C3** — the interval *is* the decision. 1h / 4h / 1d / 1w / 1m / 6m, one month default, each rung with its operational consequence | `briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__…acceptance-interval-ladder…md` | ✅ **publish as a table** |
| `/acceptance/unaccepted-is-critical/` | **C4** — *"that person right now is accountable for the business, which is very bad from a business point of view, but is also very bad for the individual"* | same, + the Article 26(5) worked example | ✅ |
| `/acceptance/workflow/` | **C15** underwriting graph · **C33** decision as a node · override and pre-approval | `briefs/06/23/…v0.33.33__arch-brief__…risk-acceptance-workflow-multi-stakeholder-graph-underwriting-propagation-override-pre-approval.md` | ✏️ |

---

## `/ladder/` — what agents most need

Definitional, not narrative. Every node type stated as a required path pattern, machine-readable where possible.

| Page | Concept | Source | Status |
|---|---|---|---|
| `/ladder/index.html` | **C6** Reality → Twin → Measure → Evidence → Fact → Vulnerability → Risk. Downward grounds; upward classifies. *"A Fact becomes a Vulnerability purely because of its upward link to a Risk, so that legitimacy is conferred entirely from above."* | `briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__…grounding-ladder…md` | ✅ **the most rigorous document in the corpus** |
| `/ladder/formulas/` | **C7** — *"the ontology definition of a node type is its upward and downward path-pattern, not a sentence about what it contains"* | `briefs/06/28/…v0.33.36__arch-brief__…node-type-formulas…md` | ✅ |
| `/ladder/bridges/` | **C8** three layers — shared facts, per-party formulas, declared bridges. Plus the worked Manion/Jacobs/Roytman bridge | `briefs/06/28/…ontologies-of-ontologies…md` + `…bridge-vulnerability-formula-system-fault-security-failure-conditions-manion-jacobs.md` | ✅ names three real researchers favourably |
| `/ladder/absence/` | **C17** not knowing is a fact — countable, queryable, assignable | `briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__…facts-only-no-deny-cascade-cia-blast-radius.md` | ✏️ |

🔗 **Cite graphs.sgit.ai, don't restate it.** Node type formulas *as a mechanism* belong there; the grounding ladder *as a risk formula* belongs here.

---

## `/examples/` — the proof

| Page | Content | Status |
|---|---|---|
| `/examples/browser-isolation/` | **59 nodes, 75 edges**, inline JSON. 5 altitudes, 3 risks *of the mitigation itself*. Vendor system cards: prompt-injection success falling **~50% → ~1%** across one model generation, cited as the honest counterweight | ✅ |
| `/examples/2fa/` | **51 nodes, 53 edges**, downloadable JSON. Ontology **24 node classes, 34 edge types**. MITRE **T1110.004**. The R2 governance air gap accepted at 4h by the wrong owner, propagating GRC → CIO → CEO → Board | ✅ **the only downloadable graph** |
| `/examples/article-26-5/` | 8 facts (one unevidenced), 5 risks, 4 stakeholders, **9 questions — 5 unanswered**. The **30 days vs 6 months** arithmetic finding | ✅ |
| `/examples/vaults/` | 🔗 The four live vaults with read keys — see `03__worked-examples-and-vaults.md` §A | 🔗 ✅ |
| `/examples/scenarios/` | The ten scenarios, hook → reveal → punchline, punchline always *"how long?"* | ✅ |
| `/examples/plug-register/` | The seven-row plug register, from *"agent misuses the isolated session"* to *"unattributable transaction"* (**recoverability: zero**) | ✅ |

---

## The rest

| Section | Concepts | Notes |
|---|---|---|
| `/acceptable/` | **C5** two axes, four quadrants, Article 9(5) · **C25** appetite as a revealed band, the Goldilocks zone | 📎 Moves off riskmandate.ai |
| `/register/` | **C9** graph of graphs · **C10** fractal registers · **C11** relevance fade · **C12** one chain not parallel lists · **C16** cascade and air gaps · **C42** the narrative engine | ✅ |
| `/blast-radius/` | **C19** authorization closure — *what the agent can reach, computed* · **C18** CIA expansion | ✅ |
| `/plug/` | **C20** two symmetric risks · **C21** four-way time intersection · **C22** five dimensions · **C23** recoverability. Detection floor **12–18h** | 📎 ⚠️ reconcile the "no plug" correction |
| `/practice/` | **C13** technical vs business owner · **C14** confirmed/validated/accepted · **C24** altitude · **C26** the physical act · **C27** the level ledger · **C28** density and calibration by surprise · **C29** residuals · **C30** meta-risks · **C31** the self-maintaining register · **C32** three moves · **C34** a question is not a risk · **C35** do not internalise (**63–76%** burnout) | ✏️ |
| `/ramm/` | RAMM five levels · AOMM · the plug-pull maturity model · **C37** confidence bands · **C38** two underwritings · **C39** observability | 📎 ⚠️ base levels underspecified |
| `/concepts/` | All 42, one anchor each, addressable | ✍️ |
| `/origins/` | Feb 2026 classical GRC (`team/roles/grc/`) → 4 June *"the risk already exists"* → 23 June no-deny → 28 June the ladder → 17 July intervals → 28 July accepted≠acceptable → 2 Aug end-to-end | ✏️ |

---

## `/agents/` — the commissioned surface

The brief says the point of this site is that **agents need a good understanding of these concepts**. So this is not a courtesy page.

| Element | Content |
|---|---|
| `/llms.txt` | Each entry carries the concept's **single most important fact**, not its topic. *"C2 no-deny — a risk with a real vulnerability under it exists whether or not anyone acknowledges it, so there is no deny button; the only choice is how long"* |
| `/llms-full.txt` | The whole site in one fetch. **Non-negotiable here** — measured on sgit.ai, agent fetch tools refuse URLs a search has not returned, so link-following fails |
| `/.well-known/agent-content.json` | Structured manifest — copy riskmandate.ai's pattern |
| **The definitions endpoint** | The 42 concepts as JSON: name, one-line definition, canonical source, maturity, related concepts. **Nothing else in the estate has this and it is the single highest-value thing this site can ship** |
| **The ontology download** | Node types and edge types with their path formulas, plus the 2FA instance graph |
| Per-page agent block | Every concept page ends with a pasteable summary an agent can carry into another session |

---

## `/shipped/` — non-negotiable

Nothing in the risk corpus is implemented. Greps for `risk_`, `RiskAcceptance`, `risk_register`, `riskmandate` across `sgraph_ai_app_send/**/*.py` return **zero**. The reality file says *"Do not describe any of these as existing features."*

What *does* exist: riskmandate.ai as a vault-powered static site · the ten scenario documents · **four live vaults with read keys** · three fully worked graphs as parseable JSON.

---

## `/network/` — the seven-site map

The split is the point of this site, so state it on a page rather than leaving it implicit. Full boundaries in `06__boundaries-and-house-style.md` §1.

| Site | Boundary in one line |
|---|---|
| **riskmandate.ai** | Commercial. *How do I get my risks accepted, and what does it cost?* Cites this site |
| **graphs.sgit.ai** | Owns the graph machinery. Node type formulas as a *mechanism* are theirs; the grounding ladder as a *risk formula* is ours |
| **nhi.sgit.ai** | Owns agent identity. The `06/04/nhi-2.0/` series is theirs — but its risk-management brief is **risk's origin document** and should be cited here |
| **pki.sgit.ai** | Owns attribution and signing. ⚠️ Currently carries **mandate** material that arguably belongs here — coordinate a split |
| **sg-sentinel.sgit.ai** | Enforces. **We measure and evidence; we never sit in-line.** The corpus states this refusal explicitly |
| **newsroom.sgit.ai** | Owns the evidence *supply* side. We own the *demand* side — accountability is what generates it |
| **sgit.ai** | Owns vaults, publishing and the catalogue. Consume the topic-section pattern, don't re-argue it |

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).



==============================================================================
== briefs/06__boundaries-and-house-style.md — source document, verbatim
==============================================================================

