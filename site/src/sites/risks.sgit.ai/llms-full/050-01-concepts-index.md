# 01 — Concepts Index

**42 risk concepts**, each with its canonical document, first appearance, maturity, newcomer-readiness and best verbatim quote.

This is the file the site's `/concepts/` section is built from, and it is the file an agent should be able to fetch in one request. `briefs/` = `team/humans/dinis_cruz/briefs/` in `SGraph-AI__App__Send` @ v0.33.62. All paths verified.

**Reading order for an agent with no prior context:** C1 → C2 → C3 → C4 → C5 (the acceptance model) → C6 → C7 (the ontology that makes it computable) → C19 → C20–C23 (blast radius and the plug) → everything else.

**Maturity is stated honestly.** Nothing in this corpus is implemented in code — see `00__BRIEF.md` §1.

---

### C1. Risk Acceptance as Underwriting (not prediction)

The founding inversion. Traditional risk management predicts the probability of a future event; this model asks a named human to *underwrite* an exposure that already exists, insurance-style. Because the executive is ultimately accountable for the business, accepting a risk is not an administrative act but the assumption of personal liability for a decision. The move relocates the whole discipline from actuarial estimation to accountable ownership, and it is the reason the rest of the model hangs together: once someone must sign, they demand evidence, which manufactures the demand for the grounding ladder underneath.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/18/agentic-permissions/v0.33.40__arch-brief__sg-send-risk-acceptance-underwriting-flows-upward-cross-domain-the-risk-already-exists.md`; `team/humans/dinis_cruz/briefs/06/04/nhi-2.0/v0.32.3__strategy-brief__sg-send-nhi-2.0-risk-management-acceptance-underwriting-roi.md`
- **First appearance:** 4 June 2026 (v0.32.3), deepened 18 June 2026 (v0.33.40)
- **Maturity:** well-developed
- **Newcomer-followable?** Yes — the insurance analogy carries it with no GRC background
- **Quote:** *"because what we describe is reality, we are not describing the risk of something happening, we are asking them to accept it, to underwrite it. Maybe the analogy is insurance: you are underwriting the damage, the same way an underwriter underwrites the cost. The business executive is ultimately accountable for everything, so whatever they accept, they are underwriting the risk."* — `06/18/agentic-permissions/v0.33.40__arch-brief__sg-send-risk-acceptance-underwriting-flows-upward-cross-domain-the-risk-already-exists.md`

### C2. The No-Deny Mechanic

The single most distinctive primitive. A risk that has a real vulnerability under it exists whether or not anyone acknowledges it, so denial is incoherent — you cannot vote a fact out of existence. The UI therefore has no deny button; the only choice is **how long** you accept it before it must be re-accepted. Denial in conventional registers is a fiction that only works while the risk has not materialised; removing it converts risk management from a gate into a forcing function.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/23/risk-mandate-product-and-workflow/v0.33.33__dev-brief__sg-send-risk-acceptance-service-demo-no-deny-time-boxed-acceptance-expiry-as-cost-graph-evidence.md`; `team/humans/dinis_cruz/briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__sg-send-risk-register-graph-of-graphs-facts-only-no-deny-cascade-cia-blast-radius.md`
- **First appearance:** 23 June 2026 (v0.33.33)
- **Maturity:** well-developed
- **Newcomer-followable?** Yes — outstandingly so
- **Quote:** *"the mistake of a lot of risk registers is that they allow the risk to be denied, which can only happen when the risk has not materialised. Once the vulnerability exists, the risk exists to the business."* — `06/26/risk-register-and-five-whys/v0.33.35__arch-brief__...facts-only-no-deny-cascade-cia-blast-radius.md`

### C3. The Acceptance Interval Ladder

The interval is not metadata about a decision — it *is* the decision. Choosing a duration simultaneously sets severity and commits resources, because each rung implies a specific operational response. Under 24 hours means pull the plug; a day to a week is a lower-grade incident; a week to a month is a project for an existing team; one to three months means assemble and fund; over three months means you are waiting to see, which is legitimate if said out loud. The default is one month — deliberately just above the incident line. Anything under a week is an incident and the rung simply names the grade.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__sg-send-acceptance-interval-ladder-hour-to-six-months-default-one-month-interval-implies-response.md`
- **First appearance:** intervals 23 June 2026; consolidated as a ladder 17 July 2026 (v0.33.49)
- **Maturity:** well-developed (the single cleanest artefact in the corpus)
- **Newcomer-followable?** Yes — it is a six-row table with plain-language consequences
- **Quote:** *"if you have less than a day risk acceptance, then that is fundamentally a P1, because if you say I do not want to accept this risk for more than an hour once I know about it, then that means you need to pull the plug."*

### C4. Unaccepted Equals Critical (escalation without an escalator)

The corpus's sharpest inversion of incentives. In most organisations a risk nobody escalated feels safest to the person holding it. Here it is the worst possible state: an un-underwritten risk has not vanished, it has come to rest on whoever is nearest, and that person is personally carrying an enterprise exposure with no signature above them. So an unaccepted risk is rated critical by default and appears on the holder's own dashboard immediately, and it rolls upward *without anyone deciding to escalate it*.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__sg-send-acceptance-interval-ladder-...md`; demonstrated on live data in `team/humans/dinis_cruz/briefs/08/02/vault-as-substrate/v0.33.55__arch-brief__sg-send-end-to-end-worked-example-article-26-5-creditworthiness-agent-fact-to-board.md`
- **First appearance:** 17 July 2026
- **Maturity:** well-developed, and worked end-to-end on 2 August
- **Newcomer-followable?** Yes
- **Quote:** *"any risk that has not been accepted immediately goes into that one's risk dashboard, because that is a massive risk, that means that that person right now is accountable for the business, which is very bad from a business point of view, but is also very bad for the individual."*

### C5. Accepted Is Not Acceptable (two orthogonal axes)

The vocabulary correction that turns risk appetite into something computable. **Accepted** is an act by a named person at a dated moment. **Acceptable** is a threshold owned by the business — *"the moment that the business is happy to stop funding remediation activities."* They are orthogonal, not sequential, producing four quadrants, each requiring a different response. Acceptable is risk appetite renamed, and renaming it makes it operational because the instruction that matters most is the one that *stops* work. The EU AI Act Article 9(5) requires residual risk to be "judged acceptable" and never defines the word — so the obligation to judge is imposed and the standard is not supplied. An organisation that has never defined its acceptable level carries a meta-risk about its own risk management.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/28/regulation-graph-and-acceptability/v0.33.53__strategy-brief__sg-send-accepted-is-not-acceptable-orthogonal-axes-appetite-renamed-article-9-mandates-judgement-without-defining-it.md`
- **First appearance:** 28 July 2026 (v0.33.53)
- **Maturity:** well-developed; formalised as node types `P-PRED-001` to `P-PRED-004` in `team/roles/librarian/reality/ai-agents/proposed/risk-mandate.md`
- **Newcomer-followable?** Yes — the four-quadrant ASCII diagram does the work
- **Quote:** *"the acceptable risk is the moment that the business is happy to stop funding remediation activities."*

### C6. The Grounding Ladder (Reality → Twin → Measure → Evidence → Fact → Vulnerability → Risk → Top Risk)

The definitional spine of the whole corpus, and the concept agents most need. Every node type is defined by its **required paths**, not by its content. Downward paths confer *grounding* ("is it real?"); upward paths confer *classification and implication* ("what is it, and why does it matter?"). A Vulnerability is simply a Fact with an upward path to a Risk. A Measure is **not** the floor — it is grounded further in a Twin and through it in Reality. The floor is a stopping *test*: the last node where going deeper would neither improve observability nor change a decision.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__sg-send-grounding-ladder-fact-evidence-measure-vulnerability-risk-definitions.md`
- **First appearance:** 28 June 2026 (v0.33.36)
- **Maturity:** well-developed; the most rigorous document in the corpus
- **Newcomer-followable?** Yes — the rendered ladder diagram plus the untested-restore worked example
- **Quote:** *"A Fact becomes a Vulnerability purely because of its upward link to a Risk, so that legitimacy is conferred entirely from above."*

### C7. Node Type Formulas (classification as a testable path-pattern)

The mechanism beneath C6, and arguably the corpus's most transferable idea. What a node *is* should be computed against the graph, not decided in a classifier's head. A Node Type Formula is a required pattern of typed, directed paths; a node either matches or does not. Classification becomes a **query**, so it is dynamic and path-relative — promotion and demotion are edge events. Bias does not disappear; it moves out of the classifier's head into the formula, where it is visible, versioned and arguable. Two parties who disagree stop trading intuitions and start diffing formulas.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__sg-send-node-type-formulas-classification-as-testable-path-pattern-not-judgment.md`
- **First appearance:** 28 June 2026
- **Maturity:** well-developed as a mechanism; the *formula language* is an open question
- **Newcomer-followable?** Mostly — requires accepting "a type is a path pattern", which the doc argues carefully
- **Quote:** *"the ontology definition of a node type is its upward and downward path-pattern, not a sentence about what it contains."*

### C8. Ontologies of Ontologies — Bridges, Not Merges

Multiple parties each own their own formula over a shared factual graph, connected at declared crosswalk points rather than merged into one schema. A node can be a vulnerability under one formula and not another, and both are valid — they are different queries over the same graph. The worked proof is the Manion/Jacobs/Roytman security-centric formula (System, Fault, Security Failure, Conditions), which turns out to be a **sub-path** of the business-centric formula: their Security Failure plays exactly the structural role of the promotion edge, differing only in terminus.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__sg-send-ontologies-of-ontologies-three-layers-formulas-bridges-multiple-definitions.md`; `.../v0.33.36__arch-brief__sg-send-bridge-vulnerability-formula-system-fault-security-failure-conditions-manion-jacobs.md`
- **First appearance:** 28 June 2026
- **Maturity:** well-developed, with one fully worked external bridge
- **Newcomer-followable?** Yes
- **Quote:** *"We do not fold their definition into ours, which would erase the security-centric view that is the whole point of having it. We declare a bridge: a Security Failure gives rise to a Business Risk."*

### C9. The Risk Register as a Graph of Graphs

The register is not a spreadsheet at the top of a company but a hyperlinked semantic graph, buildable now because vaults supply the storage and hyperlink layer and PKI solves attribution. Its distinguishing move is that it *begins where scanners stop* — at the vulnerability — and maps everything after it: accepting, funding, and finding who does the work.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__sg-send-risk-register-graph-of-graphs-facts-only-no-deny-cascade-cia-blast-radius.md`
- **First appearance:** 26 June 2026 (v0.33.35)
- **Maturity:** well-developed, with a full worked example (2FA)
- **Newcomer-followable?** Yes — it is written as a five-movement narrative
- **Quote:** *"a lot of security teams and products end on the vulnerability, and what I want to show is the multiple layers involved in fixing it, but even before that, in accepting the risk, funding the solution, and finding who is going to do it."*

### C10. Fractal Risk Registers (one per accepting entity)

Wherever there is a stakeholder who accepts a risk, there must be a register — for a company, a department, and an individual role. A person's register is simply all the risks that bubble up to them, *derived* rather than curated. An individual has at least two and often three: their role-specific register in their own domain language, plus derived views of the registers above. Only the role's own register is stored; the rest are queries.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__sg-send-fractal-risk-registers-one-per-accepting-role-domain-language-relevance-fade.md`
- **First appearance:** 17 July 2026
- **Maturity:** well-developed
- **Newcomer-followable?** Yes
- **Quote:** *"as you go up, imagine the colours can fade away for the next registers for the bits that are not relevant, so the graph starts to point which parts of the risk register above are relevant to this individual, so that he understands the picture."*

### C11. Relevance Fade (the register as an education mechanism)

The visualisation property that falls out of C10. Centre the view on a role: that role's register is lit in full; the registers above fade except for the entries that trace back down to this role. A database administrator can see that their local "agent holds unrestricted access to a customer table" is *the same object* as the board's "regulatory penalty, loss of licence, continuity failure". Seeing that once teaches more than any training course.

- **Canonical:** same as C10
- **First appearance:** 17 July 2026 · **Maturity:** partially argued (visualisation not built) · **Newcomer-followable?** Yes

### C12. Registers Are One Chain, Not Parallel Lists

A late and consequential correction. Three altitude registers drawn side by side demonstrate a formatting capability; drawn as **one chain rooted in an existence fact** they demonstrate the entire thesis. The CISO's risk exists *because of* the operator's risk, which exists because of a fact stating an agent touches production.

- **Canonical:** `team/humans/dinis_cruz/briefs/08/02/field-demo/v0.33.55__arch-brief__sg-send-demo-review-registers-are-one-chain-question-is-not-a-risk-decision-as-node-paths-are-traversals.md`
- **First appearance:** 2 August 2026 · **Maturity:** well-argued, newly stated · **Newcomer-followable?** Yes
- **Quote:** *"at the moment it looks like the cards, they look side by side, and it's actually not that."*

### C13. Technical Owner vs Business Owner

The technical owner *validates* that the vulnerability exists; the business owner *owns and accepts* the risk. Conflating them is the source of the corpus's canonical governance failure. IT validating a 2FA gap is not IT accepting an HR data-breach exposure.

- **Canonical:** `06/26/risk-register-and-five-whys/v0.33.35__arch-brief__...md`; `team/humans/dinis_cruz/briefs/06/23/risk-mandate-product-and-workflow/v0.33.33__arch-brief__sg-send-risk-acceptance-workflow-multi-stakeholder-graph-underwriting-propagation-override-pre-approval.md`
- **First appearance:** 26 June 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes
- **Quote:** *"most of IT should be technical owners of something, but the business owners are the ones that actually own the risk."*

### C14. Confirmed / Validated / Accepted — the Three-Predicate Model

Three distinct acts held by three distinct roles, tracked per risk per altitude. **Confirmed** is factual (technical stakeholder; true or false). **Validated** is interpretive (GRC/compliance: does this obligation genuinely apply?). **Accepted** is a judgement about appetite (business owner with standing). The interesting cases are the mismatches: a risk accepted by an executive but never confirmed is an acceptance of something that may not be true.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/28/mvp-and-field-demo/v0.33.53__arch-brief__sg-send-scenarios-are-the-mvp-shareable-vault-primitive-sequence-confirmed-validated-accepted-at-altitude-plural-regulations.md`
- **First appearance:** 28 July 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes
- **Quote:** *"we probably also want the GRC person to validate the risks, especially to do with the compliance element."*

### C15. Underwriting Graph & Propagation to the Board

An exec never decides alone. Before an executive acts, the relevant direct-line owner (CIO/CTO/CFO by dimension), the CSO, and at least GRC must each have recorded an acceptance **or an explicit refusal** — a refusal being as important as an acceptance. Once accepted at the right altitude, the acceptance propagates upward to the boss, the boss's boss and the CEO (who acts for the board), with the largest going to the board itself. Superiors may override in either direction, with the original acceptance preserved and the override attributed.

- **Canonical:** `06/23/risk-mandate-product-and-workflow/v0.33.33__arch-brief__sg-send-risk-acceptance-workflow-multi-stakeholder-graph-underwriting-propagation-override-pre-approval.md`
- **First appearance:** 23 June 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes
- **Quote:** *"the exec should never make a decision that has not been underwritten by the relevant player."*

### C16. Cascade and the Air Gap

Every change to any risk, fact, or piece of evidence must trigger a cascade to the top. The absence of a cascade is an **air gap** — and any risk that exists in the business but is not connected to the register is likewise an air gap. Registers with air gaps silently drift out of date, and the business is deciding on bad data. Cascade works in both directions: a risk appearing propagates up, and a risk resolving propagates up too, clearing it from the board's view.

- **Canonical:** `06/26/risk-register-and-five-whys/v0.33.35__arch-brief__...md`
- **First appearance:** 26 June 2026 (concept of "air gap" appears in the repo from 9 March in another sense)
- **Maturity:** well-developed as principle; *detecting* air gaps is an acknowledged open problem
- **Newcomer-followable?** Yes
- **Quote:** *"every time any risk, any fact, any evidence changes, you have to trigger a cascade that reaches the top. If you do not have that, you have an air gap, which means you do not have good data, and you cannot make good decisions."*

### C17. Not Knowing Is a Fact (absence of evidence as first-class)

Lack of evidence is itself evidence. A measure can be a documented zero — "zero tested-restore records found" is as much a measure as any positive count. An unevidenced fact is recorded as unevidenced rather than left blank, which is what makes it queryable, countable and assignable. Gaps in knowledge spawn their own risks: "the full extent of the impact has not been captured, which means the risk is not yet correctly classified or correctly accepted."

- **Canonical:** `06/26/risk-register-and-five-whys/v0.33.35__arch-brief__...md`; demonstrated as fact **F7** in `08/02/vault-as-substrate/v0.33.55__arch-brief__...article-26-5...md`
- **First appearance:** 26 June 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes
- **Quote:** *"not knowing a fact is also a fact. Lack of evidence is also evidence, because then we say we do not know, and somebody needs to investigate until we do."*

### C18. CIA Blast-Radius Expansion

Where most registers stop is where this one starts working. From a single risk, expand through Confidentiality (leak → GDPR/ICO → CFO for the fine, CEO for compliance — two distinct risks, since inadequate protection may already be a breach), Integrity (salary tampering, fabricated hires, altered performance data) and Availability (backup cadence gaps, and the sharper "when was a restore last tested?"). Each branch spawns its own risks, each following the full validate-accept-propagate loop.

- **Canonical:** `06/26/risk-register-and-five-whys/v0.33.35__arch-brief__...md`
- **First appearance:** 26 June 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes (CIA is standard, but the doc explains it)
- **Honest tension recorded in-doc:** the expansion must be curated, not exhaustive, or it blows up combinatorially

### C19. Blast Radius / Authorization Closure

An agent's *real* authorization is the transitive union of everything reachable from what it was given, not the nominal grant. Two awareness gaps hide the delta: the granter does not know the full scope of what it grants, and the original delegator never authorised re-delegation. Inbox access is access to every account resettable by email; desktop access is every stored credential and every logged-in session; code execution can escalate to admin. The key quantity is the **delta between expected and unexpected** permissions. `AuthorizationClosure` becomes a first-class node type.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/02/authorization-and-maturity-model/v0.33.40__arch-brief__sg-send-agent-authorization-union-of-possible-expected-unexpected-delta-blast-radius-hope-driven.md`
- **First appearance:** "blast radius" from 12 Feb 2026 (`briefs/02/12/`), formalised as closure 2 July 2026
- **Maturity:** well-developed
- **Newcomer-followable?** Yes — the inbox example lands instantly
- **Quote:** *"at the end of the day you are still accountable for those actions, all the way to the board."* (the "hope-driven development" anti-pattern)

### C20. Who Can Pull The Plug — Two Symmetric Risks

If nobody holds the mandate to stop an AI system, that is one risk; if the system cannot be stopped even when someone decides to, that is a second, different risk (an authority gap vs a capability gap). The second is widely underestimated. This decomposes into timed sub-risks — can it be stopped in an hour, ten hours, a day, five days; only in office hours? — which turns governance into an on-call availability problem, including whether the person can act *without fear of losing their job* and along a clear escalation path.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__sg-send-who-can-pull-the-plug-ability-to-stop-an-ai-system-fractal-maturity-model-detection-authority-blast-radius-reversibility-intersect-in-time.md` (the load-bearing brief; 12 companion pieces in the same folder)
- **First appearance:** phrase from 17 Feb 2026 in another sense; as a risk pillar, 24 July 2026
- **Maturity:** well-developed — a 13-document series
- **Newcomer-followable?** Yes, outstandingly
- **Quote:** *"if you do not have somebody who has the mandate to pull the plug, you have a risk, and if you do not have a system that can be pulled the plug, you have a risk too."*

### C21. The Four-Way Time Intersection (detection, decision, blast radius, reversibility)

Four capabilities must line up inside the same window, and a gap in any one breaks the whole thing. Detection (how fast you know, and under what scenarios — a curve, not a binary). Decision (can the authorised people be assembled in time). Blast radius (models execute and scale fast, especially when connected — a steep cost range). Reversibility (stopping is only half the act; reverting requires journaling and backups). The danger case is a steep cost curve where an affordable window of one or two days of damage collides with a decision that cannot be made in one or two days.

- **Canonical:** same as C20
- **First appearance:** 24 July 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes (the Venn is drawn in ASCII)
- **Quote:** *"it is not just pulling the plug, it is pulling the plug and reverting the changes."*

### C22. The Five-Dimension Plug Profile (and the "no plug" correction)

The pillar correction of the series: **the plug always exists** — you can always disconnect, revoke, or shut down. What earlier registers recorded as "no plug" for a data breach or a used foothold was never a missing off-switch; it was **zero recoverability**. Restating it that way turns a frightening blank into an ownable finding that points straight at prevention and the most senior acceptance. The profile carries five dimensions: **who holds it, blast radius, speed, side effects, recoverability**.

- **Canonical:** `07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__sg-send-a-real-plug-register-the-worked-proof-five-dimension-profile.md`; `.../v0.33.51__strategy-brief__sg-send-who-can-pull-the-plug-pillar-the-plug-always-exists-the-question-is-the-profile.md`
- **First appearance:** 24 July 2026 · **Maturity:** well-developed with a worked register · **Newcomer-followable?** Yes
- **Quote:** *"The blank said stop looking. The corrected profile says here is exactly what to do."*

### C23. Recoverability as the Hard Limit

The dimension that stops irreversible harm disappearing into an expected-loss calculation. Money can be refunded; the customer cannot be un-declined. The flagship query in the entire model is: **show me every accepted risk whose recoverability is zero.** An organisation that can run it and read a short, deliberate, senior-owned list is in control of its worst exposure; one that cannot is accepting its irreversible risks by default and by silence.

- **Canonical:** `07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__sg-send-what-money-cannot-buy-back-recoverability-the-hard-limit.md`; `.../v0.33.51__strategy-brief__sg-send-can-you-compute-your-plug-profile-the-maturity-probe.md`
- **First appearance:** 24 July 2026 · **Maturity:** well-developed; the *scoring* of recoverability is an open question · **Newcomer-followable?** Yes
- **Quote:** *"The money can be refunded; the customer cannot be un-declined."* — `08/02/vault-as-substrate/v0.33.55__arch-brief__...article-26-5...md`

### C24. Altitude

The corpus's word for organisational elevation, used as a first-class modelling dimension: a risk is accepted "at the right altitude" and then propagates; the same risk is restated in each altitude's own language; the plug changes at every altitude (who holds which off-switch); a risk may be confirmed at one altitude and accepted at another.

- **Canonical:** `07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__sg-send-the-plug-changes-at-every-altitude-who-holds-which-off-switch.md`; five-level table in `team/humans/dinis_cruz/briefs/07/12/worked-business-case/v0.33.48__briefing__...five-levels-graph.md`
- **First appearance:** as a role metaphor 12 Feb 2026; as a risk dimension from June 2026
- **Maturity:** well-developed · **Newcomer-followable?** Yes
- **Quote:** *"this is very important, the multiple altitudes of the risk register, because there might be risks that are only accepted at certain altitudes, or might be risks that are only confirmed at certain altitudes."*

### C25. Risk Appetite as a Revealed Band (and the Goldilocks Zone)

Appetite is a **band**, not a number; a **fractal network** of bands (one per division and team, consolidated upward); and it already exists in any company that has operated for a while, so it is *discovered*, not declared. It is computed from two signals: what the business has paid to reduce in the past, and every fresh acceptance decision going forward. The target is to operate inside the band — above it you are buying risk the owners will not underwrite; below it you add attrition and slowness for nothing. Declared vs revealed appetite: **the gap between the two is the finding.**

- **Canonical:** `team/humans/dinis_cruz/briefs/06/30/risk-acceptance-and-appetite/v0.33.38__strategy-brief__sg-send-risk-appetite-band-fractal-two-signals-goldilocks-zone-revealed-dataset.md`
- **First appearance:** 30 June 2026 (v0.33.38) · **Maturity:** well-developed · **Newcomer-followable?** Yes
- **Quote:** *"risk appetite is that band, that interval between two numbers, if you think of zero to one hundred in terms of risk, it is a spectrum, and it can be wider or shorter."*

### C26. The Psychology of the Physical Act

Why the model insists on a click, a thumbs-up, a signature. The act is the moment a decision stops being ambient and becomes something a named person did, at a known time, on known information — a moment of accountability, which eventually carries liability, *as it should*. Without it, declining decays into a non-event: someone says "I'm not comfortable" and nothing happens. The forcing function closes that escape: declining is a trigger, not a terminal state. And it changes executive behaviour — the prospect of signing concentrates attention in a way dashboards never do.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/30/risk-acceptance-and-appetite/v0.33.38__strategy-brief__sg-send-risk-acceptance-psychology-accountability-liability-physical-act-revealed-appetite.md`
- **First appearance:** 30 June 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes, and it is the most persuasive doc for a lay reader
- **Quote:** *"suddenly the executives ask good questions, they really engage, they get a level of focus that just was not there before, and that is why risk acceptance is so powerful, it drives behaviours that otherwise do not exist."*

### C27. Accept First, Then Adjust the Level — the Risk Level Ledger

For a risk you already have facts for, the first move is universal stakeholder acceptance **at its current level**, on the record. From there the level is not a fixed number but a **dated ledger of adjustments**, each re-accepted, triggered by one of three things: new data, a funded project, or an incident. Re-rating *up* after discovery is honesty, not failure — the risk did not worsen, the estimate improved. The board sees a living trajectory rather than a static red square.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/12/acceptance-and-residual/v0.33.48__arch-brief__sg-send-accept-first-then-adjust-the-level-risk-level-ledger-agentic-ai-shadow-agents.md`
- **First appearance:** 12 July 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes
- **Key line:** *"you literally cannot mitigate what you cannot count, and the only honest first step is to accept, now, that an unknown and largely over-permissioned population of agents holds access to the enterprise's assets."*

### C28. Everything Has Risks — Register Density and Calibration by Surprise

The common register failure is holding only big risks and treating the goal as having none. A risk is the unintended side effect of a capability, so anything that *does* something has risks; capabilities exceed features, and undocumented capabilities are where unowned risks live. A complex product should have dozens to thousands of interconnected risks. The diagnostic: a listed risk materialising is expected; an **unlisted** risk materialising is the real alarm, because it raises two questions — why was it missed, and what else was missed?

- **Canonical:** `team/humans/dinis_cruz/briefs/07/12/acceptance-and-residual/v0.33.48__arch-brief__sg-send-everything-has-risks-register-density-capabilities-vs-features-calibration-by-surprise.md`
- **First appearance:** 12 July 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes

### C29. Risks That Cannot Be Fully Mitigated (the residual)

Mitigation lowers likelihood or impact but cannot reach zero for structural reasons, so a material residual always remains and must be owned. Demanding zero produces **covert acceptance**, which is worse than an owned residual. Agentic AI's residual is today irreducible: prompt injection, emergence, non-determinism, reach, model supply chain. Some harms are irreversible; compliance reduces but does not remove liability.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/12/acceptance-and-residual/v0.33.48__strategy-brief__sg-send-risks-that-cannot-be-fully-mitigated-board-terms-examples-agentic-ai-cyber-business.md`
- **First appearance:** 12 July 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes (written in board terms deliberately)

### C30. Meta-Risks (the risk about your risk management)

A recurring family, named as a pattern on 31 July after four instances: not knowing how many agents you have; not having defined an acceptable level; a risk accepted by the wrong person (the governance air gap); and systematic downgrading across a business unit. Each is a gap in the governance apparatus, stated as a rateable risk with an owner and an interval, which triggers and funds the work that closes it. External anchors defeat systematic downgrading, because an internal severity is an opinion while an external requirement is not.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/31/keeping-the-register-healthy/v0.33.54__strategy-brief__sg-send-when-the-business-downgrades-everything-external-anchors-meta-risk-family-concealment-not-acceptance.md`; first instance in `06/26/.../v0.33.35__arch-brief__...md`
- **First appearance:** as instance 26 June 2026; named as a family 31 July 2026
- **Maturity:** well-developed · **Newcomer-followable?** Yes
- **Quote:** *"we are the meta risk; we allow the creation of the project that is going to discover this and that funds this."*

### C31. The Register Maintains Itself (accountability manufactures demand for evidence)

Why no separate data-quality function is required. Three primitives produce it: the risk already exists, it attaches to a named person, and the decision is reviewed upward. Anticipated review is the engine — it converts care into a demand for evidence *before* the decision. The appetite for accurate evidence is a by-product of assigning accountability, so nobody has to fund it separately. Three named failure conditions: the reviewer's preference being guessable (people conform rather than think), commitment to a prior position, and broadened information appetite without improved discrimination.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/31/keeping-the-register-healthy/v0.33.54__arch-brief__sg-send-register-maintains-itself-accountability-manufactures-demand-for-evidence-three-failure-conditions.md`
- **First appearance:** 31 July 2026 · **Maturity:** well-developed, research-grounded · **Newcomer-followable?** Yes

### C32. Three Moves, None of Which Is Denial

The reconciliation of the no-deny primitive with human reactance. Presenting a single button to a person who feels they have no alternative produces counter-argument and resentment, not compliance. The resolution was already in the corpus: three moves exist — **accept for a stated interval with a stated action, escalate (this is not mine to accept), or challenge the fact itself**. The person is routed rather than cornered. The absence of a reject option should be *discovered*, not announced.

- **Canonical:** `team/humans/dinis_cruz/briefs/08/02/field-demo/v0.33.55__arch-brief__sg-send-acceptance-flow-three-moves-none-is-denial-loop-closes-event-as-elicitation.md`
- **First appearance:** 2 August 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes

### C33. Decision as a First-Class Node

An acceptance is a separate object, not a field on a risk. That is what allows one risk to accumulate many dated decisions without overwriting, one decision to cover several risks, and — crucially — a **calibration record** to be built over time asking whether the person who accepted for a month was right.

- **Canonical:** `08/02/field-demo/v0.33.55__arch-brief__sg-send-demo-review-registers-are-one-chain-question-is-not-a-risk-decision-as-node-paths-are-traversals.md`
- **First appearance:** 2 August 2026 · **Maturity:** newly stated, well-argued · **Newcomer-followable?** Yes
- **Quote:** *"a decision is actually captured independently from the risk."*

### C34. A Question Is Not a Risk (the acceptability test)

A clean quality gate. If a sentence cannot sensibly carry a named acceptor and an interval, it is not a risk and does not belong in the register. *"Nobody accepts 'whose call is it at three in the morning' for six months."* Questions become their own node type, and **unanswered question nodes are the most productive output of the whole exercise**.

- **Canonical:** `08/02/field-demo/v0.33.55__arch-brief__...registers-are-one-chain...md`; questions-as-nodes worked in `08/02/vault-as-substrate/v0.33.55__arch-brief__...article-26-5...md`
- **First appearance:** 2 August 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes

### C35. Do Not Internalise the Risk

The human-cost argument. Risk professionals frequently internalise exposures the business decided to carry, at real personal cost — the corpus cites survey data of 63–76% of security leaders experiencing or witnessing burnout in a single year, and names accountability-without-authority as the defining pressure. The standard remedy is to give the security leader more authority, which is correct and rarely achievable. The workflow solves the same equation from the other side, by moving accountability to where authority already sits. Nothing is taken from anyone; it records what was always true.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/31/keeping-the-register-healthy/v0.33.54__strategy-brief__sg-send-do-not-internalise-the-risk-accountability-without-authority-relocated-not-augmented-mental-load.md`
- **First appearance:** 31 July 2026 · **Maturity:** well-developed, research-grounded, with an honest scope disclaimer · **Newcomer-followable?** Yes
- **Quote:** *"I would see the risk professionals almost own the risk; they almost take it personally with the risks that the business was taking, and it was a massive source of stress."*

### C36. Evidence Economy — Force of Proof and the Fact Certifier

Once executives are personally accountable and the graph traces their statement to the evidence beneath it, a **force of proof** appears: demand for correct evidence becomes cheap to make and impossible to wave away. This splits the register into two separately liable roles — the **risk-acceptor** (owns the decision and its consequence) and the **fact-certifier** (owns the truth of the inputs and sells a correctness guarantee). A wide confidence band is the trigger that converts unease into a purchase order for better evidence, and two prices become legible: the cost of getting good evidence, and the cost of underwriting while the band stays wide.

- **Canonical:** `team/humans/dinis_cruz/briefs/07/05/evidence-economy/v0.33.44__strategy-brief__sg-send-evidence-economy-force-of-proof-fact-certification-two-prices-evidence-based-revenue-models.md`; catalogued as P-429 in `team/roles/librarian/reality/ai-agents/proposed/risk-mandate.md`
- **First appearance:** 5 July 2026 · **Maturity:** partially argued (commercially rich, mechanically thin) · **Newcomer-followable?** Mostly

### C37. Confidence Bands and Margin of Error

Confidence is a first-class property of every node. A rating needs a band, not a point, and the band is widest where data is thin. A band too wide for comfort triggers the get-more-data direction; a band spanning trivial to catastrophic cannot be accepted responsibly. Confidence propagates across the graph like risk, and "we don't know" is the widest band.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/30/ontology-and-data-quality/v0.33.38__arch-brief__sg-send-confidence-margin-of-error-node-uncertainty-band-comfort-zone-more-data.md`
- **First appearance:** 30 June 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes

### C38. Two Underwritings — Decision Accountability vs Factual Accuracy

Distinct and both required. The domain expert underwrites that a fact is true *and fit for the use being made of it*; the business owner underwrites the decision. Every graph traversal adds an abstraction layer that strips detail and drifts weight, so the signature failure is a component used beyond what its owner would underwrite. Decision accountability is only legitimate if the data underneath it is correct.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/30/ontology-and-data-quality/v0.33.38__arch-brief__sg-send-data-accuracy-owner-underwrites-fitness-for-use-vs-decision-accountability-tolerance.md`
- **First appearance:** 30 June 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes

### C39. Observability as a Risk Dimension

Capability maps the privilege; observability maps the *real impact*. Six objective vectors on a maturity scale: capture granularity, log latency, time-to-damage given real throughput limits, whether monitoring is actually on and watched, whether there is a team with playbooks, and whether detection has been drilled. The reframe: **a loud, detectable, slowly-scaling, well-drilled risk is lower than a quiet, fast, unwatched one of the same capability.** Later sharpened into "plug-loaded observability" — logs that tell you where you are in the stopping decision, not generic logging.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/22/how-and-why-and-authorization/v0.33.32__arch-brief__observability-as-a-risk-dimension-detectability-time-to-damage-response-maturity-scale.md`
- **First appearance:** 22 June 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes

### C40. Five Whys as a Domain Translator

Not a root-cause tool here but a **translator** that moves a statement from one domain into another. It is as many whys as it takes to reach the top of a domain. The graph has natural peaks — on risk it converges to the single risk of staying in business — and because it converges, a legitimate single number can be carried to the top. Aimed downward, the same chain captures the second, third and fourth stories: the root causes.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/26/risk-register-and-five-whys/v0.33.35__strategy-brief__five-whys-as-a-domain-translator-natural-peaks-root-cause-stories.md`
- **First appearance:** 26 June 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes

### C41. Digital Twins and the Discipline of Reality

The twin is where the graph stops modelling and continues into a real system — the grounding point beneath every measure. How connected a twin is to reality is itself a measurable property, which introduces a useful recursion: trust in a measure depends on the twin's connectedness, and that connectedness is itself a measure. A twin not connected to reality is a tracked air gap.

- **Canonical:** `team/humans/dinis_cruz/briefs/06/26/digital-twins-and-world-models/v0.33.35__arch-brief__sg-send-digital-twins-twin-of-anything-dimensions-discipline-of-reality-simulation-testing.md`; `.../v0.33.35__arch-brief__sg-send-digital-twins-integration-layer-real-world-tracked-air-gaps-agent-twin.md`
- **First appearance:** 15 Feb 2026 (general); as risk grounding, 26 June 2026 · **Maturity:** well-developed · **Newcomer-followable?** Yes

### C42. The Narrative Engine (register as story)

The register is meant to be experienced as a story, not read as a spreadsheet: replay the change history through timestamps, commits or a series of queries, so the analyst watches the vulnerability appear, risks propagate, a governance risk fire and resolve, the blast radius bloom, and everything settle into the board's consolidated view. The commit log is the script; the query advances the scene.

- **Canonical:** `06/26/risk-register-and-five-whys/v0.33.35__arch-brief__...md`
- **First appearance:** 26 June 2026 · **Maturity:** partially argued (mechanism undecided in-doc) · **Newcomer-followable?** Yes
- **Quote:** *"I want to show this story played as a narrative, almost like a football commentator, this happens and then that happens, almost like a whodunit, like investigative journalism."*

---

---

## Teaching order for the site

| Altitude | Pages | Concepts |
|---|---|---|
| **1 · The inversion** | `/acceptance/` | C1 underwriting · C2 no-deny · C3 the ladder · C4 unaccepted=critical |
| **2 · The vocabulary** | `/acceptable/` · `/register/` | C5 accepted≠acceptable · C25 appetite as revealed band · C9 register as graph of graphs · C10 fractal registers · C11 relevance fade |
| **3 · The machinery** | `/ladder/` | C6 grounding ladder · C7 node type formulas · C8 ontologies of ontologies · C17 not-knowing-is-a-fact · C33 decision as a node |
| **4 · The exposure** | `/plug/` · `/blast-radius/` | C19 authorization closure · C18 CIA expansion · C20–C23 the plug, four-way intersection, five dimensions, recoverability |
| **5 · The organisation** | `/practice/` | C13 technical vs business owner · C14 confirmed/validated/accepted · C15 underwriting graph · C24 altitude · C26 the physical act · C28 register density · C30 meta-risks · C31 self-maintaining register · C35 do-not-internalise |
| **6 · The maturity** | `/ramm/` | RAMM · AOMM · the plug-pull maturity model · C37 confidence bands · C38 two underwritings · C39 observability |

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).



==============================================================================
== briefs/02__risk-acceptance.md — source document, verbatim
==============================================================================

