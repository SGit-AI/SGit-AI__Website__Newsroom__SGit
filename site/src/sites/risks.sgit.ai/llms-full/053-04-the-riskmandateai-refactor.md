# 04 — The riskmandate.ai Refactor

**The commission:** *"I also want to refactor out of riskmandate.ai a lot of those concepts, since that is a commercial site which will be focused on the commercial and customer/user angle of getting risks accepted. i.e. it is the riskmandate.ai that should be referencing the risks.sgit.ai."*

---

## 1. The line

| | riskmandate.ai | risks.sgit.ai |
|---|---|---|
| **Question it answers** | *"How do I get my risks accepted, and what does it cost?"* | *"What is a risk, what is acceptance, and why is it modelled this way?"* |
| **Reader** | Buyer, user, executive | Researcher, practitioner, **agent** |
| **Register** | Product — outcome, price, proof | Research — argument, definition, evidence |
| **Licence** | Commercial site | CC BY 4.0 |
| **Change cadence** | Follows the product | Follows the thinking |

**The dependency direction is one-way: riskmandate.ai cites risks.sgit.ai.** Never the reverse for conceptual claims — the research site must be able to stand without the product.

---

## 2. Page-by-page

Every row is from riskmandate.ai's own `llms.txt`.

### Moves here

| Page | Content | Target | Notes |
|---|---|---|---|
| **`/plug.html`** | Five dimensions (who · blast radius · speed · side effects · **recoverability**); the reversible/irreversible split; *"the mandate states what an agent is authorised to reach; the plug profile states what it costs to take that reach away"* | `/plug/` | ⚠️ The corpus records a **"no plug" correction** the published page does not reflect. Reconcile before republishing — see `07` |
| **`/acceptable.html`** | Two orthogonal axes; four states; the interval table (1–24h P1 → beyond 3 months acknowledged waiting); *"distance to the line sets the clock"*; appetite reframed; Article 9(5) | `/acceptable/` | Strip *"Book a demo"* and the executive-audience targeting |
| **`/ramm.html`** | Five levels as **Node Type Formulas** — *"a path-pattern a query can test"*; the entity model (RiskItem, RiskAcceptanceDecision, DecisionAuthority, RiskAppetiteStatement, ReviewEvent, ExpiryEvent, EvidenceArtifact…); the Agentic `+` variants; crosswalks to OWASP Risk Rating, SAMM, ASVS, WSTG, Threat Dragon, DefectDojo/CycloneDX, RIMS RMM | `/ramm/` | ⚠️ **Base levels 1, 2, 4, 5 are underspecified** — only Level 3 has a stated predicate. Fix before republishing |
| **`/library.html`** — 9 concept pieces: blast radius · the mandate · permission granularity · PBOM · risk acceptance · second/third-order effects · graphs of graphs | The whole `/concepts/` section | ⚠️ **The page currently links nothing.** See §4 |
| The SG/Vault technical section | Zero-knowledge, client-side encryption, key sovereignty | Cite **sgit.ai**, don't own | Not risk's concept |

### Splits

| Page | Concept half → risks.sgit.ai | Product half stays |
|---|---|---|
| **`/how-it-works.html`** | The mechanism: how acceptance nodes carry evidence, ownership, authority, appetite and review | The product walkthrough, the UI, the flow a customer follows |
| **`/scenarios.html`** + **`/statics.html`** | The **ten scenarios as a research artefact** — `briefs/07/02/risk-acceptance-and-scenarios/v0.33.40__strategy-brief__…how-long-would-you-accept…md`. Hook → reveal → punchline, punchline always *"how long?"* | The interactive scenario product |

### Stays commercial

`/v0/…/index.html` ("You own the risk") · `/demos.html` and the three demo pages · `/pricing.html` · `/partners.html`

### Pattern to copy, not move

`/agents.html`, `/llms-full.txt`, `/.well-known/agent-content.json`. **riskmandate.ai's agent surface is the best in the estate** — a dedicated agents page, the full site as one markdown fetch, and a structured JSON manifest. risks.sgit.ai needs its own, and given the commissioned audience it should be *better*.

---

## 3. The leave-behind

Each moved page leaves a stub. Draft, to adapt:

> ### Accepted is not acceptable
>
> Two independent properties. **Accepted** is an act: a named person with the standing to do it says *I carry this*, for a stated interval. **Acceptable** is a threshold the business owns — the point at which it stops funding remediation.
>
> RiskMandate implements both. The full argument, the four states and the Article 9(5) analysis are at **[risks.sgit.ai/acceptable](https://risks.sgit.ai/acceptable/)**.
>
> [See how it works in the product →]

Three sentences of substance, one link out, one link deeper into the product. The buyer gets what they need; the researcher and the agent get sent to the source.

---

## 4. ⚠️ The finding that justifies the split

**`riskmandate.ai/library.html` lists nine concept pieces and links to none of them.**

The page describes *"recorded talks, the full proposition deck, and the long-form pieces"* covering agent authorization scope, authority ownership, residual risk acceptance and comprehensive risk modelling — and ships no URLs for any of it.

That is not an oversight so much as a structural mismatch: a commercial site has no natural place to put nine essays, so they get described rather than published. **A research property does.** This single page is the clearest evidence that the split is the right call.

---

## 5. Sequencing

1. **Stand up risks.sgit.ai with `/acceptance/`, `/acceptable/`, `/ladder/` and `/plug/`.** Four pages, all near-publishable.
2. **Replace those four riskmandate.ai pages with leave-behind stubs** pointing here.
3. **Build `/concepts/` properly** — the nine library pieces plus the other 33 from `01__concepts-index.md`. This is what `library.html` was always trying to be.
4. **Reconcile the two known defects** — the plug correction, the RAMM base levels — before republishing either.
5. **Add `/agents/` and `/llms-full.txt`**, modelled on riskmandate.ai's and extended for the commissioned audience.
6. **Cross-link the four vaults** from both sites: risks.sgit.ai as worked examples of the concepts, riskmandate.ai as product demos. **Same artefacts, two framings — that is the split working.**

---

## 6. What must not happen

- **risks.sgit.ai must not carry pricing, partner positioning, or competitor comparisons.** The `07/12/positioning-and-market/` briefs name two large vendors [REDACTED · Tier-3 · see PUBLIC.md] with dismissive characterisations — commercial, internal-only, and corrosive on a research site.
- **riskmandate.ai must not keep a second, drifting copy of a concept.** Stub and link, or move it wholly. Two versions of the interval ladder that disagree is worse than either.
- **No concept page should depend on the product existing.** Per `00__BRIEF.md` §1, none of this is implemented. The research stands on its own; the product is one implementation of it.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).



==============================================================================
== briefs/05__site-architecture.md — source document, verbatim
==============================================================================

