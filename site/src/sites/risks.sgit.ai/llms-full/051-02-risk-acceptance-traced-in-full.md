# 02 — Risk Acceptance, traced in full

**The commissioned centrepiece.** The founder called out "risk acceptance" specifically, and it is the thread everything else in the corpus hangs from.

This file traces it chronologically with exact paths and verbatim quotes, from the February 2026 classical-GRC pre-history through the June inversion to the July–August formalisation.

`briefs/` = `team/humans/dinis_cruz/briefs/`. All paths verified at v0.33.62.

---

### 2.1 Pre-history (Feb–May 2026): classical GRC, later inverted

The corpus's own starting point is orthodox. `team/roles/grc/reviews/02/19/v0.4.12__risk-acceptance__deliberate-token-exposure.md` (19 Feb 2026) is a textbook risk acceptance: R001/R002 rows with Likelihood, Impact, Mitigation, and *"Residual risk: Acceptable"*. `team/roles/grc/reviews/02/17/v0.4.9__vulnerability-classification-framework.md` establishes a P0–P10 scale with a Risk Decision Matrix whose five questions include *"What is the risk of the fix?"* — the earliest instance of the later "every action has risks, including the good ones" principle. `team/roles/grc/ROLE.md` states the classical position: *"Every risk the project faces -- technical, operational, reputational -- must be identified, assessed, and either mitigated or formally accepted with documented rationale."* Note the "either/or" — the June work abolishes it.

**21 April 2026** is the first structural gesture toward the product: `team/humans/dinis_cruz/briefs/04/21/v0.21.9__dev-brief__evidence-packs-risk-acceptance-workflow.md` — *"Risk acceptance in organisations is broken. A decision gets made in a meeting. Someone writes it up (maybe). The reasoning is lost. The approval chain is informal. Six months later, nobody can explain why a particular risk was accepted, who approved it, what evidence was considered."* It proposes a `risk-decision-vault/` with `decision/`, `evidence/`, and `approvals/approval-tree.json`.

### 2.2 The risk already exists (4 June → 18 June 2026)

`06/04/nhi-2.0/v0.32.3__strategy-brief__sg-send-nhi-2.0-risk-management-acceptance-underwriting-roi.md` is where "risk acceptance because the risk already exists" and "time-boxed sign-off as priority and mandate" first appear as new contributions.

`06/18/agentic-permissions/v0.33.40__arch-brief__sg-send-risk-acceptance-underwriting-flows-upward-cross-domain-the-risk-already-exists.md` is the pillar document:

> *"you are not predicting the risk of something happening, you are asking owners to underwrite it, insurance-style… the risk already exists the moment the permission is provisioned, so the only variable is how long you accept it, until it is re-accepted, eliminated, or the permission is narrowed; saying you are not comfortable changes nothing, you either accept it for a realistic fix-window or remove the privilege now."*

And the accountability mechanic, in the founder's own voice:

> *"from a psychological and accountability point of view, it is only when you get somebody to click, or put an emoji, or accept the terms, that they really engage, because that is the moment they become accountable. And if you accept the risk today and something major happens a week or month later, you are accountable, you should have done something. This creates positive pressures."*

> *"risk acceptance is done in multiple levels and flows upward. A department uses a third-party agent: the person using it accepts the risk, then it goes to their boss to underwrite, then to the exec to underwrite, and eventually to the board to underwrite."*

### 2.3 The no-deny mechanic (23 June 2026)

`06/23/risk-mandate-product-and-workflow/v0.33.33__dev-brief__sg-send-risk-acceptance-service-demo-no-deny-time-boxed-acceptance-expiry-as-cost-graph-evidence.md`:

> *"the most important thing is that there is no deny button. The only buttons are accept for one hour, four hours, two days, two weeks, or a month, and the interval is when the risk acceptance expires, when you have to accept the risk again. So if you accept for an hour, you are really saying I need more data, someone needs to get me more data so I can make a better decision."*

> *"four hours means start a P1 straight away, trigger your incident response and come back in four hours with a remediation. Two weeks means a funded project. Six months means you review it then, which means not doing anything, and that costs zero, because you are not doing anything about it."*

The **expiry-as-cost table** (verbatim from that document):

| Accept for | What it means | Action and cost |
|---|---|---|
| 1 hour | I need more data before I can really decide | Someone must go and get more data; near-immediate |
| 4 hours | This is a P1 | Trigger incident response, playbooks, workflow; remediation within four hours; a real cost |
| 2 days | A smaller incident, but still an incident | Something must be done within two days |
| 2 weeks | A funded project | Plan and fund the fix; less immediate, lower cost |
| 6 months | Do nothing | Review in six months; effectively no action; costs zero |

### 2.4 Two dimensions, and who accepts (23 June 2026)

`06/23/risk-mandate-product-and-workflow/v0.33.33__arch-brief__sg-send-risk-acceptance-workflow-multi-stakeholder-graph-underwriting-propagation-override-pre-approval.md` splits an acceptance into **direction** (get more data / reduce / increase / hold) and **revisit interval**, independently:

> *"there are at least two core primitives here, accept and get more data, and accept and deal with it and reduce the risk, and actually there should be another, accept and increase the risk, because it is okay to increase the risk if the business is okay with it."*

**Who accepts** is answered three ways: (a) the underwriting requirement — *"the exec should never make a risk decision that has not been accepted, or explicitly not accepted, which also matters, by at least the technical or direct-line element, the CIO or CTO or CFO depending on the dimension, the respective CSO, and at least GRC"*; (b) altitude and propagation — *"the risk needs to be accepted at the right altitude, and then it propagates out… all the way to the CEO. The CEO acts on behalf of the board, so the buck stops with them, although some risks even the CEO has to take up to the board"*; (c) the technical/business owner split (C13).

**Evidence strikes options off:** *"some risks depend on a set of actions that are not possible within an hour, so even if you start the biggest incident on the planet and throw all the money in, you cannot do it in less than an hour. So that option is removed from the equation."* No override can buy a physically impossible timeline; the only escape is the nuclear option, ceasing the activity.

**Compound pre-approval:** approval attaches to a *risk profile*, not each instance. Further instances become an FYI; a fresh approval is needed only when the profile changes.

### 2.5 Acceptance as a graph node

Four progressive formalisations:

1. **26 June 2026** — `06/26/semantic-graph-and-query-paths/v0.33.35__arch-brief__sg-send-2fa-use-case-semantic-graph-ontology-nodes-edges-instance.md` makes `Acceptance` and `Interval` node classes with edges `accepted_by`, `has_interval`, `propagates_to`, `underwritten_by`, `overrides`.
2. **2 July 2026** — RAMM (`07/02/authorization-and-maturity-model/v0.33.40__arch-brief__...ramm...md`) makes `RiskAcceptanceDecision` the hub node with twelve named directed edges (`ownedBy`, `approvedBy`, `boundedBy`, `withinToleranceOf`, `justifiedBy`, `evidencedBy`, `reviewedAt`, `expiresAt`, `reassessOn`, …).
3. **5 July 2026** — `AcceptanceDecision` becomes a Layer-5 node type in the AWS IAM ontology, with the formula `AcceptableForInterval := a Risk with an accepted_by path to an AcceptanceDecision carrying an owner, a direction, an interval, and a sign-off.`
4. **2 August 2026** — Decision promoted to a fully independent node (C33), enabling many decisions per risk and the calibration record.

### 2.6 Escalation without an escalator

The mechanism's most elegant consequence, stated at `07/17/.../v0.33.49__arch-brief__...interval-ladder...md` and demonstrated on live data at `08/02/vault-as-substrate/v0.33.55__arch-brief__...article-26-5...md`:

> *"R3 appears on the chief financial officer's register as an unowned critical item, and it got there without anybody escalating it deliberately. That is the mechanism working: not doing something is a measurable action."*

And the design consequence for non-participation, at `07/31/keeping-the-register-healthy/v0.33.54__strategy-brief__...design-for-players-who-will-not-play...md`: attrition — not open refusal — is the failure mode that matters, and the roll-up *"removes the deniability attrition depends on, without requiring anyone to cooperate."*

### 2.7 Accepted vs acceptable (28 July 2026)

Covered in full at C5. The one connection flagged as new and untested: **the acceptance interval should be a function of the distance from the acceptable line** — far above the line warrants a short interval, at or below warrants a long one, making the interval computable from two numbers already in the register.

### 2.8 Consequential loose ends in the thread

- The corpus repeatedly cross-references **`v0.33.46__strategy-brief__sg-send-risk-acceptance-redefined-vs-industry-definition-no-deny-only-how-long-accountability.md`** (7 July 2026) — cited by eight documents — but **this file does not exist in the repo**. Nor do the referenced `v0.33.46` "who-holds-the-bag / Vercel allow-all", "risk-to-an-exec", or `v0.33.47` "kitchen-sink" briefs. There are no `briefs/07/06` through `briefs/07/11` directories. **A canonical "risk acceptance redefined" statement is a named gap in the corpus** and is a prime candidate for risks.sgit.ai to author from the surrounding material.
- The metric the founder proposes for the whole model: *"our key metric is not recurring revenue, it is recurring risk acceptance, how many risk acceptances we are having every day, every week, every month, because that is when we know it is working."* (`06/28/use-cases-and-risk-acceptance/v0.33.36__strategy-brief__sg-send-use-case-driven-shipping-risk-acceptance-story-recurring-risk-acceptance-metric.md`)

---

---

## What the site should do with this

1. **`/acceptance/` is the front door**, not a sub-page. It is the most distinctive thing in the corpus and the most immediately graspable — the no-deny mechanic needs no GRC background to land.
2. **Publish the interval ladder as a table**, with the operational consequence stated per rung. It is the single cleanest artefact in the corpus and it is what an agent will look up.
3. **State the two orthogonal axes early.** *Accepted* is an act by a named person at a dated moment; *acceptable* is a threshold owned by the business. Conflating them is the failure the whole vocabulary correction exists to prevent.
4. **Show `unaccepted = critical` on live data.** The Agentic Browser Isolation vault runs acceptance-gated escalation across five altitudes with no deny button — it is C2 and C4 demonstrated, not asserted.
5. **Carry the loose ends honestly** — see `07__gaps-and-open-questions.md`. A model this opinionated earns credibility by naming what it has not resolved.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).



==============================================================================
== briefs/03__worked-examples-and-vaults.md — source document, verbatim
==============================================================================

