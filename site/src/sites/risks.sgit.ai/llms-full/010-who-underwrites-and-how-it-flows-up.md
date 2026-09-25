# Who underwrites, and how it flows up

An executive never decides alone, and an acceptance is not a field on a risk. This page is the machinery around the act: the underwriting graph that must be complete before a decision is legitimate, the propagation upward to the board, the two independent dimensions of a decision, override, and compound pre-approval — including the parts the corpus proposes and never finishes.

## A decision has two independent dimensions

An acceptance is usually described as a single choice. It is two, chosen independently: the direction — what is going to happen to the risk — and the revisit interval — when it comes back. Neither implies the other.

“there are at least two core primitives here, accept and get more data, and accept and deal with it and reduce the risk, and actually there should be another, accept and increase the risk, because it is okay to increase the risk if the business is okay with it.”

DIRECTION · GET MORE DATAAccept it, and commission the evidence. Usually paired with a short interval, because the point is to come back better informed. The rung and the direction are still separate choices.

DIRECTION · REDUCEAccept it, and fund work that lowers it. The interval is the delivery window for that work.

DIRECTION · INCREASEAccept it, and deliberately take on more — because the business wants the capability that comes with it. Rarely offered in a conventional register, and its absence is why registers read as one-directional.

DIRECTION · HOLDAccept it as it stands, and do nothing until the interval expires. Paired with a long rung, this is the honest form of “we are waiting to see”.

## Who has to have signed before an executive can act

The corpus is specific, and the specificity is the point — an underwriting is not legitimate because a senior person clicked, but because the graph beneath their click is complete.

“the exec should never make a risk decision that has not been accepted, or explicitly not accepted, which also matters, by at least the technical or direct-line element, the CIO or CTO or CFO depending on the dimension, the respective CSO, and at least GRC”

Who | What they underwrite | Why the decision is not legitimate without them |

The direct-line owner
CIO / CTO / CFO by dimension | That the exposure is real in their domain and the response is deliverable | An executive accepting a technical exposure nobody technical has confirmed is accepting something that may not be true |

The CSO | The security reading of it | Security's view is a distinct dimension, not a subset of IT's |

GRC | That the obligation genuinely applies, and how | Compliance is interpretive work; it is neither a fact nor an appetite judgement |

The business owner | The decision itself, and its consequence | This is the underwriting proper — the others are inputs to it |

A recorded refusal counts as much as a recorded acceptance. The phrase in the source is “accepted, or explicitly not accepted, which also matters”. This is not a contradiction of the no-deny mechanic: no-deny removes denial of the risk. What is being recorded here is a named person's refusal to be the one who underwrites it — which is a legitimate, informative and attributable act, and is the “escalate” move rather than a rejection. Q3 asks what happens when a refusal has nowhere left to go.

## Propagation, and where the buck stops

Once accepted at the right altitude, an acceptance does not stay there. It propagates to the boss, the boss's boss, and eventually to the CEO — with the largest going to the board itself.

Riskaccepted_byDecisionunderwritten_byOwner (L1)propagates_toL2 … L4propagates_toCEOpropagates_toBoard
Read as a sentence: this risk was accepted by a decision, underwritten by an owner at the altitude where it belongs, and propagates to every altitude above it, ending at the board for the largest.

“the risk needs to be accepted at the right altitude, and then it propagates out… all the way to the CEO. The CEO acts on behalf of the board, so the buck stops with them, although some risks even the CEO has to take up to the board.”

Altitude does real work here and is treated as a first-class modelling dimension throughout: the same risk is restated in each altitude's own language, may be confirmed at one altitude and accepted at another, and — on the plug question — has a different off-switch at every level. Altitude →

## A decision is its own node, not a field

Late in the corpus (2 August 2026) the acceptance is promoted to a fully independent node. It is a small modelling change with three consequences that are not small:

- Many decisions per risk, without overwriting. A risk accumulates a dated history of decisions rather than carrying one mutable status field. The trajectory becomes visible.

- One decision covering several risks. Which is what actually happens in a meeting, and what a status field cannot express.

- A calibration record. Over time you can ask the only question that matters about a decision: was the person who accepted this for a month right? That question is unanswerable if the decision was a field that got overwritten.

“a decision is actually captured independently from the risk.”

## Two mechanisms the corpus proposes and does not finish

Both are on the site as stated rather than as settled, because a research site that quietly completes its sources is not a research site.

Mechanism | What is stated | What is missing |

Override |
A superior may override an acceptance in either direction. The original acceptance is preserved and the override is attributed — so the record shows both what was decided and what it was changed to, by whom. |
No authority model. Who may override whom, on what grounds, and whether the original acceptor's liability survives the override, are all unstated. |

Compound pre-approval |
Approval attaches to a risk profile rather than to each instance. Further instances matching the profile become an FYI; a fresh approval is needed only when the profile changes. |
Never worked through. What constitutes a profile, what counts as a change to one, and who notices, are not specified. |

One thing is settled, and it constrains both: no override can buy a physically impossible timeline. Where a remediation cannot be delivered inside a window, that rung is struck off the ladder before the choice is offered, and the only escape is ceasing the activity. The plug →

## Provenance

Concepts
C15, C33 — the underwriting graph and propagation; decision as a first-class node

Source
team/humans/dinis_cruz/briefs/06/23/risk-mandate-product-and-workflow/v0.33.33__arch-brief__…underwriting-propagation-override-pre-approval.md

Repository
SGraph-AI__App__Send @ v0.33.33, never published — the version tag is the address

First written
23 June 2026; decision-as-node 2 August 2026

Maturity
well-developed — with override and compound pre-approval explicitly incomplete

Licence
CC BY 4.0 at source and here

#### For an agent

C15 and C33 — the underwriting workflow. An acceptance decision has two independent dimensions: a direction (get more data · reduce · increase · hold) and a revisit interval. Neither implies the other, and “increase” is a legitimate direction. A decision is not legitimate until the underwriting graph beneath it is complete: the direct-line owner (CIO/CTO/CFO by dimension), the CSO and at least GRC must each have recorded an acceptance or an explicit refusal — a recorded refusal carries the same weight as an acceptance. Once accepted at the right altitude it propagates upward — line manager, executive, CEO (who acts for the board), and for the largest, the board itself. Model a decision as its own node, never as a field on the risk: that is what allows many dated decisions per risk, one decision covering several risks, and a calibration record asking whether the person who accepted for a month was right. Two mechanisms are named and unfinished: override (no authority model) and compound pre-approval (never worked through). No override can buy a physically impossible timeline. Not implemented in code.


==============================================================================
== /acceptable/index.html
==============================================================================

