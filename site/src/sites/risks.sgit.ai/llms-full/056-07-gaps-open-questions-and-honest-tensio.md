# 07 — Gaps, Open Questions and Honest Tensions

---

## 1. Must be written fresh

| # | Page | Why |
|---|---|---|
| **G1** | **The front page** | Nothing in the corpus opens this argument for a cold reader. The pieces exist — underwriting, no-deny, unaccepted-is-critical — but nobody has assembled them into 300 words |
| **G2** | **`/agents/` and the definitions endpoint** | The commissioned audience has no surface today. 42 concepts as JSON is the single highest-value artefact this site can ship |
| **G3** | **`/shipped/`** | Nothing is implemented. Without this page the site over-claims and breaks the convention the siblings are built on |
| **G4** | **`/concepts/` as an addressable index** | The concepts exist across ~185 documents with no index, no anchors and no stable URLs. `01__concepts-index.md` is the raw material |
| **G5** | **RAMM base levels** | Levels 1, 2, 4 and 5 are named but only Level 3 has a stated predicate. The Agentic `+` variants are better defined than the base model they extend |
| **G6** | **The plug reconciliation** | The corpus records a *"no plug"* correction that `riskmandate.ai/plug.html` does not reflect. One of the two is wrong |

---

## 2. Open questions worth publishing unresolved

Following the pki.sgit.ai convention of numbering open questions in public. A model this opinionated earns credibility by naming what it has not settled.

| # | Question | Where the corpus gets closest |
|---|---|---|
| **Q1** | What is the **formula language**? Node Type Formulas are the mechanism the whole ontology rests on, and the notation is undefined | C7's canonical brief names this as its own open question |
| **Q2** | Who sets **acceptable**, and what stops it being set to whatever is convenient? | C5 defines it as *"the moment the business is happy to stop funding remediation"* — it does not say who decides or what constrains them |
| **Q3** | What happens when the **named acceptor refuses to sign**? | The no-deny mechanic removes denial of the *risk*; it does not address refusal of the *act* |
| **Q4** | Does **unaccepted = critical** survive contact with a large estate? | On a register of thousands, everything unaccepted being critical may make critical meaningless. C28's register-density argument circles this without resolving it |
| **Q5** | How is the **interval enforced**? Expiry-as-cost is asserted; the mechanism is not specified | C3, C2 |
| **Q6** | Is **recoverability** measurable, or only classifiable? | C23 splits reversible from irreversible; nothing grades the middle |
| **Q7** | What is the **stopping rule** for the grounding ladder in practice? | C6 states the test — *"the last node where going deeper would neither improve observability nor change a decision"* — but no worked example applies it to a hard case |
| **Q8** | How do you stop a register being **gamed** once acceptance carries personal liability? | C31 argues accountability manufactures demand for evidence; the opposite incentive — avoid ever being the named acceptor — is acknowledged but not answered |

---

## 3. Honest tensions

Following pki.sgit.ai's `/roadmap/#tensions`.

1. **The model rates the ability to stop but does not provide it.** The corpus states this refusal itself: *"a customer who scores badly will ask us to supply the stop button, which is exactly the enforcement role the corpus refuses."* That boundary is principled — and commercially uncomfortable.
2. **No-deny is the strongest idea and the hardest sell.** Removing the deny button removes the thing most executives use a register for. The corpus is honest that this is a forcing function, not a convenience.
3. **Personal liability is the mechanism and the risk.** Making acceptance a personal act is what generates demand for evidence. It also gives every rational actor a reason to avoid being named.
4. **Nothing is built.** ~496,000 words of design against zero lines of implementing code. That is fine for a research site *if stated*; it is fatal if implied otherwise.
5. **The corpus names real vendors critically.** The OSMM assessment scores two named real vendors [REDACTED · Tier-3 · see PUBLIC.md] at Level 1 and concludes one presents more exposure on the axis it markets hardest. Rigorous, sourced, and a legal exposure.
6. **Two sites, one voice.** riskmandate.ai and risks.sgit.ai share an author and a thesis. If the research site reads like marketing, the split has failed; if the commercial site reads like research, it will not sell.
7. **The EU AI Act thread is neither risk nor graphs.** ~40,000 words across four brief clusters. Risk's genuine claims within it are narrow and sharp — Article 9(5)'s undefined "acceptable", Article 14 as the plug obligation, Article 26(5)/(6) as the worked example. **The rest may deserve its own property.**

---

## 4. Loose ends inside the acceptance thread itself

From the corpus's own record, worth carrying onto the site rather than quietly resolving:

- **The 4h-for-everyone problem.** In the 2FA example the governance air gap propagates GRC → CIO → CEO → Board with *each accepting at 4h because that is the only option open to them*. Either the ladder needs a per-altitude variant, or that uniformity is a finding about the model.
- **Compound pre-approval** is proposed and never worked through.
- **Override** is named in the workflow brief without a stated authority model.
- **The level ledger** (C27 — accept first, then adjust the level) sits awkwardly with the no-deny mechanic: if you can adjust the level after accepting, denial re-enters through the back door.

---

## 5. Fixes worth doing at source

1. **Reconcile the plug correction** across the corpus and `riskmandate.ai/plug.html`.
2. **Specify RAMM levels 1, 2, 4 and 5** to the standard already set by Level 3 and the Agentic variants.
3. **Legal read on the OSMM vendor assessment** before it goes anywhere public, with a right-of-reply process.
4. **Verify what "Odysseus" refers to** — 42 mentions across three documents, reads as a codename for a real product or engagement.
5. **Decide the EU AI Act thread's home** before it accretes further.
6. **Coordinate the mandate split with pki.sgit.ai**, whose own 19 August site review says *"mandate is the gap, registry is the missing half."*

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).



==============================================================================
== briefs/08__source-manifest.csv — source document, verbatim
==============================================================================


tier,concept,repo_path_or_url,title,words,proposed_page,publishability,why_it_matters
0,C9 register,team/humans/dinis_cruz/briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__sg-send-risk-register-graph-of-graphs-facts-only-no-deny-cascade-cia-blast-radius.md,The Risk Register as a Graph of Graphs,3187,/register/,clean,"The founding register document. Facts-only, no-deny, cascade, air gaps, CIA blast radius, told as a five-movement narrative."
0,C6 grounding ladder,team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__sg-send-grounding-ladder-fact-evidence-measure-vulnerability-risk-definitions.md,The Grounding Ladder,2325,/ladder/,clean,THE most rigorous document in the corpus and what agents most need. Reality-Twin-Measure-Evidence-Fact-Vulnerability-Risk as one formula.
0,C7 node type formulas,team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__sg-send-node-type-formulas-classification-as-testable-path-pattern-not-judgment.md,Node Type Formulas,1511,/ladder/formulas/,clean,"Classification as a computed path query. Bias relocated from the classifier into the formula, where it is visible and arguable."
0,C8 ontologies of ontologies,team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__sg-send-ontologies-of-ontologies-three-layers-formulas-bridges-multiple-definitions.md,Ontologies of Ontologies,1275,/ladder/bridges/,clean,"Three layers: shared factual graph, per-party formulas, declared bridges. Merging erases the disagreement."
0,C8 worked bridge,team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__sg-send-bridge-vulnerability-formula-system-fault-security-failure-conditions-manion-jacobs.md,Bridging a Security-Centric Vulnerability Formula,1713,/ladder/bridges/,clean - names 3 real researchers favourably,"The first worked external bridge. Their Security Failure is structurally the promotion edge, differing only in terminus."
0,C2 no-deny,team/humans/dinis_cruz/briefs/06/23/risk-mandate-product-and-workflow/v0.33.33__dev-brief__sg-send-risk-acceptance-service-demo-no-deny-time-boxed-acceptance-expiry-as-cost-graph-evidence.md,The Risk Acceptance Service,1831,/acceptance/no-deny/,clean,The no-deny button and the expiry-as-cost table. The most immediately graspable idea in the corpus.
0,C15 underwriting graph,team/humans/dinis_cruz/briefs/06/23/risk-mandate-product-and-workflow/v0.33.33__arch-brief__sg-send-risk-acceptance-workflow-multi-stakeholder-graph-underwriting-propagation-override-pre-approval.md,The Risk Acceptance Workflow,2003,/acceptance/workflow/,clean,"Two dimensions, underwriting graph, altitude, override, compound pre-approval. Override and pre-approval are loose ends."
0,C3 interval ladder,team/humans/dinis_cruz/briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__sg-send-acceptance-interval-ladder-hour-to-six-months-default-one-month-interval-implies-response.md,The Acceptance Interval Ladder,2449,/acceptance/the-ladder/,clean,THE SINGLE CLEANEST ARTEFACT IN THE CORPUS. The interval IS the decision. Publish as a table.
0,C10 fractal registers,team/humans/dinis_cruz/briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__sg-send-fractal-risk-registers-one-per-accepting-role-domain-language-relevance-fade.md,Fractal Risk Registers,2674,/register/,clean,One register per accepting entity; relevance fade as an education mechanism.
0,C5 accepted != acceptable,team/humans/dinis_cruz/briefs/07/28/regulation-graph-and-acceptability/v0.33.53__strategy-brief__sg-send-accepted-is-not-acceptable-orthogonal-axes-appetite-renamed-article-9-mandates-judgement-without-defining-it.md,Accepted Is Not Acceptable,3291,/acceptable/,clean,"Two orthogonal axes, four quadrants, the Article 9(5) definitional gap. Moves off riskmandate.ai."
0,C25 appetite,team/humans/dinis_cruz/briefs/06/30/risk-acceptance-and-appetite/v0.33.38__strategy-brief__sg-send-risk-appetite-band-fractal-two-signals-goldilocks-zone-revealed-dataset.md,Risk Appetite: The Band a Company Reveals,1970,/acceptable/,clean,"Appetite as a fractal, revealed band. Two signals. The Goldilocks zone."
0,C26 psychology,team/humans/dinis_cruz/briefs/06/30/risk-acceptance-and-appetite/v0.33.38__strategy-brief__sg-send-risk-acceptance-psychology-accountability-liability-physical-act-revealed-appetite.md,The Psychology of Risk Acceptance,1666,/practice/,clean,Why the physical act matters. Accountability becomes liability; liability becomes the forcing function.
0,C20-C23 the plug,team/humans/dinis_cruz/briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__sg-send-who-can-pull-the-plug-ability-to-stop-an-ai-system-fractal-maturity-model-detection-authority-blast-radius-reversibility-intersect-in-time.md,Who Can Pull The Plug,3940,/plug/,clean,"Two symmetric risks, fractal maturity model, four-way time intersection, EU AI Act Art 14. Detection floor 12-18h."
0,RAMM,team/humans/dinis_cruz/briefs/07/02/authorization-and-maturity-model/v0.33.40__arch-brief__sg-send-risk-acceptance-maturity-model-ramm-graph-native-levels-agentic-crosswalk.md,RAMM,2265,/ramm/,clean - FIX BASE LEVELS,Five levels as graph predicates plus Agentic RAMM. Only Level 3 has a stated predicate.
0,worked example,team/humans/dinis_cruz/briefs/08/02/vault-as-substrate/v0.33.55__arch-brief__sg-send-end-to-end-worked-example-article-26-5-creditworthiness-agent-fact-to-board.md,"End To End: One Provision, One Agent, One Graph",4272,/examples/article-26-5/,clean - org invented and marked,"8 facts, 5 risks, 4 stakeholders, 9 questions (5 unanswered). The 30-days-vs-6-months arithmetic finding."
0,C1 underwriting,team/humans/dinis_cruz/briefs/06/18/agentic-permissions/v0.33.40__arch-brief__sg-send-risk-acceptance-underwriting-flows-upward-cross-domain-the-risk-already-exists.md,Risk Acceptance as Underwriting,2265,/acceptance/underwriting/,clean,THE FOUNDING INVERSION. The insurance analogy carries it with no GRC background.
0,worked example,team/humans/dinis_cruz/briefs/07/12/worked-business-case/v0.33.48__briefing__sg-send-browser-isolation-agentic-automation-business-case-facts-vulnerabilities-risks-five-levels-graph.md,Browser Isolation Business Case,4601,/examples/browser-isolation/,clean,"59 nodes 75 edges, drop-in renderable. Includes 3 risks OF THE MITIGATION. 5 altitudes."
0,worked example,team/humans/dinis_cruz/briefs/06/26/semantic-graph-and-query-paths/v0.33.35__data__sg-send-2fa-mappings.json,2FA instance graph (DATA),1253,/examples/2fa/,clean - CC BY 4.0 inline,51 nodes 53 edges. THE ONLY DOWNLOADABLE GRAPH. Declares its own principles inside the file.
0,scenarios,team/humans/dinis_cruz/briefs/07/02/risk-acceptance-and-scenarios/v0.33.40__strategy-brief__sg-send-how-long-would-you-accept-risk-scenario-slides-gamified-survey-vault-capture.md,The Ten Scenarios,1621,/examples/scenarios/,clean,"Hook-reveal-punchline, punchline always 'how long?'. The shipped MVP content."
1,C19 blast radius,team/humans/dinis_cruz/briefs/07/05/aws-configuration-risk-engine/v0.33.44__arch-brief__sg-send-aws-iam-config-risk-ontology-taxonomy-nodes-edges-formulas-bridges.md,AWS IAM Config Risk Ontology,2968,/blast-radius/,clean,"6 layers, ~31 node types, 20 edge types (40 readings), 7 Node Type Formulas. AuthorizationClosure as the agentic union."
1,C39 observability,team/humans/dinis_cruz/briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__sg-send-the-plug-is-a-sledgehammer-blast-radius-and-side-effects-of-pulling-it.md,The Plug Is A Sledgehammer,1384,/plug/,clean,The blast radius and side effects of pulling it - the symmetric risk.
1,C23 recoverability,team/humans/dinis_cruz/briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__sg-send-what-money-cannot-buy-back-recoverability-the-hard-limit.md,What Money Cannot Buy Back,1714,/plug/,clean,Recoverability as the hard limit. The dimension that separates catastrophic-but-reversible from smaller-and-permanent.
1,C35 do not internalise,team/humans/dinis_cruz/briefs/07/31/keeping-the-register-healthy/v0.33.54__strategy-brief__sg-send-do-not-internalise-the-risk-accountability-without-authority-relocated-not-augmented-mental-load.md,Do Not Internalise The Risk,3338,/practice/,clean,63-76% of security leaders experiencing or witnessing burnout in a single year. The register is the boundary.
1,C36 evidence economy,team/humans/dinis_cruz/briefs/07/05/evidence-economy/v0.33.44__strategy-brief__sg-send-evidence-economy-force-of-proof-fact-certification-two-prices-evidence-based-revenue-models.md,The Force of Proof,1980,/practice/,clean - DEMAND side only,The risk-acceptor / fact-certifier split. Supply side belongs to newsroom.sgit.ai.
1,C41 twins,team/humans/dinis_cruz/briefs/06/26/digital-twins-and-world-models/v0.33.35__arch-brief__sg-send-digital-twins-twin-of-anything-dimensions-discipline-of-reality-simulation-testing.md,Digital Twins of Anything,1593,/ladder/,CITE graphs.sgit.ai,Twins are where the graph stops modelling and continues into a real system. General form belongs to graphs.
1,origin doc,team/humans/dinis_cruz/briefs/06/04/nhi-2.0/v0.32.3__strategy-brief__sg-send-nhi-2.0-risk-management-acceptance-underwriting-roi.md,"NHI 2.0: Risk Management, Acceptance, Underwriting, ROI",3010,/origins/,CITE nhi.sgit.ai,RISK'S ORIGIN DOCUMENT - first appearance of 'the risk already exists'. Lives on nhi.sgit.ai; cite from here.
1,live vault,https://sgit.ai/demos/vaults/risk-graph-explorer/,Risk Graph Explorer (LIVE),0,/examples/vaults/,published,"7 views, 18 facts / 37 risks / 14 provisions in the Exposed preset. Ghosted edges = unanswered. permissions: {}"
1,live vault,https://sgit.ai/demos/vaults/agentic-browser-isolation/,Agentic Browser Isolation (LIVE),0,/examples/vaults/,published,"17 entry points, 5 altitudes, acceptance-gated escalation with NO DENY BUTTON. C2 and C4 on real data."
1,live vault,https://sgit.ai/demos/vaults/risk-mandate/,Risk Mandate vault (LIVE),0,/examples/vaults/,published,"124 files, 98 commits, 8 app entries. The most-committed published vault - the method applied to its own build."
1,live vault,https://sgit.ai/demos/vaults/regulation-graph/,Regulation Graph (LIVE),0,/examples/vaults/,published,"1,523 nodes / 1,944 edges. Supplies Art 9(5), 14, 26(5)/(6) - the provisions the concepts hang on."
1,prior art,https://docs.diniscruz.ai/2025/07/06/finding-the-good-enough-threshold-optimizing-risk-creativity-and-product-decisions.html,Finding the Good Enough Threshold,4924,/acceptable/,PUBLISHED - CC0 at source,The appetite argument before it had the vocabulary. 15 risk-acceptance mentions - highest density on the site.
1,prior art,https://docs.diniscruz.ai/2025/04/02/maturity-modes-vs-traditional-standards-in-application-security.html,Maturity Models vs Traditional Standards,2701,/ramm/,PUBLISHED - CC0 at source,"The ancestor of RAMM, a year early."
2,EU AI Act thread,team/humans/dinis_cruz/briefs/07/28/regulation-graph-and-acceptability/,Regulation graph cluster (4 docs),13895,/acceptable/ (narrow claims only),needs a home decision,"~40,000 words across 4 clusters. Neither risk nor graphs. Risk's claims are narrow: Art 9(5), 14, 26(5)/(6)."
3,vendor assessment,[REDACTED - Tier-3 - see PUBLIC.md],OSMM Assessment 001,2811,HOLD - LEGAL READ,legal read + right of reply,"Names two real vendors and scores both Level 1. Rigorous and sourced - and a legal exposure. Names and path redacted for publication."
3,competitor map,[REDACTED - Tier-3 - see PUBLIC.md],Competitor comparison,2090,DO-NOT-PUBLISH,INTERNAL ONLY,"Competitor map naming two large vendors. Commercial positioning, not research. Names and path redacted for publication."
3,investor,team/humans/dinis_cruz/briefs/06/02/v0.31.9__strategy-brief__sg-send-investment-strategy-why-now-alchemist-guidance.md,Investment strategy,2821,DO-NOT-PUBLISH,INTERNAL ONLY,"Illustrative revenue, valuation and exit figures. Explicitly scenarios, not projections. Figures redacted for publication - see PUBLIC.md."
3,contract,[REDACTED - Tier-3 - see PUBLIC.md],Partnership contract draft,2452,DO-NOT-PUBLISH,INTERNAL ONLY,An actual contract draft with commercial terms.



==============================================================================
== briefs/PUBLIC.md — source document, verbatim
==============================================================================

