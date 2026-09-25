# Practice: owners, altitude and the register's health

The organisational altitude of the model. Who confirms, who validates, who accepts, and why they are three different people. What altitude is and why it is a modelling dimension rather than a metaphor. Why the physical act of signing changes executive behaviour. And the four ideas about keeping a register alive — density, meta-risks, self-maintenance, and not internalising what the business decided to carry.

## Technical owner versus business owner

The distinction that prevents the corpus's canonical governance failure. The technical owner validates that the vulnerability exists. The business owner owns and accepts the risk it gives rise to. They are almost never the same person, and collapsing them produces an acceptance made by someone with no standing to make it.

“most of IT should be technical owners of something, but the business owners are the ones that actually own the risk.”

Worked: IT validating that admin accounts lack a second factor is not IT accepting an HR data-breach exposure. In the 2FA example that exact confusion is R2, the governance air gap — a risk accepted by the wrong owner, which then propagates GRC → CIO → CEO → Board as a risk in its own right. The register does not correct the mistake; it makes the mistake visible as an item with a rating.

## Confirmed · Validated · Accepted

Three distinct acts, three distinct roles, tracked per risk per altitude:

Predicate | Who | What kind of claim it is |

Confirmed | The technical stakeholder | Factual. True or false, and checkable against evidence |

Validated | GRC / compliance | Interpretive. Does this obligation genuinely apply, and how? Neither a fact nor an appetite judgement |

Accepted | The business owner with standing | A judgement about appetite. Is this where we are content to sit, and for how long? |

The mismatches are the interesting cases, and they are only visible because the three are tracked separately. A risk accepted but never confirmed is an acceptance of something that may not be true. A risk confirmed but never validated may carry an obligation nobody has read. A risk confirmed and validated but never accepted is critical by default. A single status field cannot express any of these.

## Altitude

The corpus's word for organisational elevation, used as a first-class modelling dimension rather than as a metaphor. Five levels appear in the worked examples: L1 endpoint/IT → L2 security → L3 business → L4 enterprise → L5 board.

Four things vary by altitude, and each is a modelling consequence rather than a presentational one:

- A risk is accepted at the right altitude, and then propagates. Accepting at the wrong one is the governance air gap.

- The same risk is restated in each altitude's own language — and it is the same object, which is what relevance fade makes visible.

- The plug changes at every altitude: who holds which off-switch is a different answer at L1 and at L5. The plug profile →

- A risk may be confirmed at one altitude and accepted at another, which is why the three predicates above are tracked per altitude.

“this is very important, the multiple altitudes of the risk register, because there might be risks that are only accepted at certain altitudes, or might be risks that are only confirmed at certain altitudes.”

## The psychology of the physical act

Why the model insists on a click, a thumbs-up, a signature — rather than a status change made on someone's behalf.

“suddenly the executives ask good questions, they really engage, they get a level of focus that just was not there before, and that is why risk acceptance is so powerful, it drives behaviours that otherwise do not exist.”

The act is the moment a decision stops being ambient and becomes something a named person did, at a known time, on known information. Accountability follows, and eventually liability — as it should. Without the act, declining decays into a non-event: someone says “I'm not comfortable” and nothing happens, and the discomfort is neither recorded nor actioned. Underwriting →

## Three moves, none of which is denial

The reconciliation of the no-deny mechanic with human reactance. Present a single button to a person who feels they have no alternative and you get counter-argument and resentment, not compliance. The resolution was already in the material: there were always three moves — accept for a stated interval, escalate (“this is not mine to accept”), or challenge the fact itself.

The person is routed rather than cornered — and the absence of a reject option should be discovered, not announced.

## Accept first, then adjust the level

For a risk you already have facts for, the first move is universal stakeholder acceptance at its current level, on the record. From there the level is not a fixed number but a dated ledger of adjustments, each re-accepted, triggered by one of three things: new data, a funded project, or an incident.

Re-rating up after discovery is honesty rather than failure — the risk did not worsen, the estimate improved. The board sees a living trajectory instead of a static red square, and the ledger is only possible because a decision is its own node.

“you literally cannot mitigate what you cannot count, and the only honest first step is to accept, now, that an unknown and largely over-permissioned population of agents holds access to the enterprise's assets.”

⚠️ This sits awkwardly with the no-deny mechanic, and the corpus does not resolve it: if the level can be adjusted after acceptance, denial has a route back in through the back door. Carried as a loose end rather than smoothed over.

## Everything has risks — register density

The common register failure is holding only big risks and treating the goal as having none. A risk is the unintended side effect of a capability, so anything that does something has risks. Capabilities exceed features, and undocumented capabilities are exactly where unowned risks live. A complex product should have dozens to thousands of interconnected risks, and a register with fifteen entries is a register that has not looked.

Calibration by surprise. A listed risk materialising is expected. An unlisted risk materialising is the real alarm — because it raises two questions at once: why was it missed, and what else was missed?

## Risks that cannot be fully mitigated

Mitigation lowers likelihood or impact and cannot reach zero for structural reasons, so a material residual always remains and must be owned. Demanding zero produces covert acceptance, which is strictly worse than an owned residual: the exposure is identical and nobody's name is on it.

Agentic AI's residual is, today, irreducible — prompt injection, emergence, non-determinism, reach, and the model supply chain. The corpus's honest counterweight, cited deliberately: vendor system cards report browser prompt-injection attack success rates falling from roughly half to about one percent across a single model generation. That is a large, real improvement. It does not reach zero, and “small and non-zero” at machine scale is a different quantity from “small” at human scale.

## Meta-risks — the risk about your risk management

A recurring family, named as a pattern on 31 July 2026 after four instances had accumulated:

Meta-risk | What it is a gap in |

Not knowing how many agents you have | Inventory — and therefore every count downstream of it |

Not having defined an acceptable level | The standard itself. Article 9(5) requires the judgement and never defines the word |

A risk accepted by the wrong person | Authority — the governance air gap |

Systematic downgrading across a business unit | Calibration. Defeated by external anchors: an internal severity is an opinion, an external requirement is not |

Each is stated as a rateable risk with an owner and an interval — which is what triggers and funds the work that closes it.

“we are the meta risk; we allow the creation of the project that is going to discover this and that funds this.”

## The register maintains itself

Why no separate data-quality function is required. Three primitives produce it: the risk already exists, it attaches to a named person, and the decision is reviewed upward. Anticipated review is the engine — it converts care into a demand for evidence before the decision rather than a post-mortem after the incident. The appetite for accurate evidence is a by-product of assigning accountability, so nobody has to fund it separately.

Three named failure conditions, stated in the source rather than discovered later:

- The reviewer's preference is guessable. People conform to it rather than think, and the review adds no information.

- Commitment to a prior position. Having said it once, the reviewer defends it rather than updates.

- Broadened information appetite without improved discrimination. More evidence gets gathered; none of it changes anything.

The commercial reading of the same mechanism is the force of proof: once executives are personally accountable and the graph traces their statement to the evidence beneath it, demand for correct evidence becomes cheap to make and impossible to wave away. That splits the register into two separately liable roles — the risk-acceptor, who owns the decision and its consequence, and the fact-certifier, who owns the truth of the inputs. Risk owns the demand side of that; newsroom.sgit.ai owns the supply side. The boundary →

## Confidence bands, and the two underwritings

Confidence is a first-class property of every node, and a rating needs a band, not a point — widest where the data is thin. A band too wide for comfort triggers the get more data direction; a band spanning trivial to catastrophic cannot be accepted responsibly at any interval. Confidence propagates across the graph the way risk does, and “we don't know” is simply the widest band there is. Absence →

Which produces two underwritings, distinct and both required. The domain expert underwrites that a fact is true and fit for the use being made of it. The business owner underwrites the decision. Every graph traversal adds an abstraction layer that strips detail and drifts weight, so the signature failure is a component used beyond what its owner would underwrite — and decision accountability is only legitimate if the data underneath it is correct.

## A question is not a risk

A clean quality gate, and one of the few things in the corpus that can be applied mechanically. If a sentence cannot sensibly carry a named acceptor and an interval, it is not a risk.

“Nobody accepts ‘whose call is it at three in the morning' for six months.”

Questions become their own node type, and unanswered question nodes are the most productive output of the whole exercise.

## Five whys as a domain translator

Not a root-cause tool here, but a translator that moves a statement from one domain into another — as many whys as it takes to reach the top of a domain. The graph has natural peaks: on risk it converges to the single risk of staying in business, and because it converges, a legitimate single number can be carried to the top. Aimed downward, the same chain captures the second, third and fourth stories — the root causes.

## Do not internalise the risk

The human-cost argument, and the one page in this section that is about people rather than models. Risk professionals routinely internalise exposures the business decided to carry, at real personal cost — the corpus cites survey data of 63–76% of security leaders experiencing or witnessing burnout in a single year, and names accountability without authority as the defining pressure.

“I would see the risk professionals almost own the risk; they almost take it personally with the risks that the business was taking, and it was a massive source of stress.”

The standard remedy is to give the security leader more authority. That is correct and rarely achievable. This workflow solves the same equation from the other side, by moving accountability to where authority already sits. Nothing is taken from anyone; the register records what was always true. The relief, if it comes, comes from the exposure having a name on it that is not yours.

The source carries an honest scope disclaimer, and it is preserved: this is an argument about where accountability should sit, not a clinical claim about burnout.

## Provenance

Concepts
C13 owners · C14 three predicates · C24 altitude · C26 psychology · C27 the level ledger · C28 density · C29 residuals · C30 meta-risks · C31 self-maintenance · C32 three moves · C34 question-is-not-a-risk · C35 do-not-internalise · C36 evidence economy · C37 confidence bands · C38 two underwritings · C40 five whys

Sources
briefs/06/30/risk-acceptance-and-appetite/…psychology…md · briefs/07/12/acceptance-and-residual/ (3 docs) · briefs/07/31/keeping-the-register-healthy/ (3 docs) · briefs/08/02/field-demo/ (2 docs) · briefs/06/30/ontology-and-data-quality/ (2 docs) · briefs/07/05/evidence-economy/…force-of-proof…md

First written
26 June – 2 August 2026

Maturity
well-developed across the section · partially argued for the evidence economy, which is commercially rich and mechanically thin

Licence
CC BY 4.0 at source and here

#### For an agent

Practice — the organisational layer. Three roles, three acts, tracked per risk per altitude: Confirmed (technical stakeholder; factual, true or false) · Validated (GRC; interpretive — does this obligation apply?) · Accepted (business owner with standing; a judgement about appetite). The mismatches are the findings — accepted-but-never-confirmed is an acceptance of something that may not be true. Never conflate technical owner (validates the vulnerability exists) with business owner (owns and accepts the risk); doing so is the governance air gap. Altitude is a modelling dimension, five levels L1 IT → L5 board: risks are accepted at the right altitude then propagate, are restated in each altitude's language, and the plug is a different answer at each. The physical act of signing is load-bearing — it is when a decision stops being ambient. Register health: a complex product should carry dozens to thousands of risks (a risk is the side effect of a capability); an unlisted risk materialising is the real alarm; demanding zero residual produces covert acceptance, worse than an owned one; meta-risks (no inventory, no defined acceptable level, wrong acceptor, systematic downgrading — defeated by external anchors) are rateable risks with owners and intervals. The register maintains itself because anticipated review converts care into demand for evidence before the decision. Confidence is a band, not a point; there are two underwritings (fact fitness-for-use, and the decision). A question is not a risk: if it cannot carry a named acceptor and an interval, it is a Question node. Not implemented in code.


==============================================================================
== /ramm/index.html
==============================================================================

