# Accepted is not acceptable

The vocabulary correction that turns risk appetite into something computable. Accepted is an act: a named person with the standing to do it says I carry this, for a stated interval. Acceptable is a threshold the business owns — the point at which it is happy to stop funding remediation. They are two orthogonal axes, not two stages of one process, and conflating them is the failure this whole correction exists to prevent.

“the acceptable risk is the moment that the business is happy to stop funding remediation activities.”

That is a stopping instruction, and it is the one instruction a risk function almost never receives. Teams are told what to worry about, rarely what to stop worrying about — so remediation continues until budget or attention runs out rather than until a stated line is reached. Naming the line makes it arguable, and makes everything above it fundable.

## Two axes, four states

Accepted → has a named person underwritten it, for a stated interval? Acceptable ↓ is it at or below the level the business has said it stops funding remediation at?

accepted · acceptableThe steady stateSomeone owns it, and it sits where the business has said it is content for it to sit. Nothing further is funded. This is the only quadrant where inaction is correct, and most registers never reach it because nobody defined the line.

accepted · not acceptableOwned and over the lineSomebody has signed for an exposure the business has said is too high. Legitimate, temporarily, and it should carry a short interval and funded work. This is what a well-run remediation programme looks like from the register's side.

unaccepted · not acceptableThe dangerous oneOver the line and nobody has signed. By C4 this is rated critical and rolls upward on its own. It is the state the model is built to make impossible to sit in quietly.

unaccepted · acceptableFine, and unrecordedBelow the line but nobody has confirmed that. Harmless in effect and corrosive in aggregate: it is indistinguishable, from the register, from the quadrant above it. This is where a register goes stale.

The diagonal is what makes the two axes worth separating. Accepted but not acceptable and unaccepted but acceptable are opposite situations requiring opposite responses, and a register with one status field cannot tell them apart.

## Acceptable is risk appetite, renamed — and the rename is the point

“Risk appetite” is a phrase most organisations have in a policy document and almost none can act on, because it is written as a sentiment rather than as a threshold. Renaming it acceptable and defining it as the point where funding stops makes it operational, because it now answers a question someone actually has to answer on a Tuesday: do we keep paying for this?

And appetite, so defined, is not declared — it is revealed. Any organisation that has been operating for a while already has one, visible in what it has paid to reduce in the past and in every fresh acceptance going forward. Appetite as a revealed band →

## Article 9(5): the obligation to judge, without the standard

The EU AI Act requires that residual risk be “judged acceptable” — and never defines the word. That is not a drafting slip so much as a structural fact about how the obligation was written: the duty to make the judgement is imposed, and the standard against which to make it is not supplied.

The consequence for a register. An organisation that has never defined its own acceptable level cannot demonstrate compliance with an obligation to judge acceptability — not because its risks are too high, but because it has no line to judge them against. That absence is itself a rateable risk with an owner and an interval: a meta-risk about the organisation's own risk management. In the Article 26(5) worked example it appears explicitly as R5 — no acceptable level defined, one of five risks and the only meta one.

Legal points on this site are factual and are not legal advice. The provisions are cited from the Regulation Graph vault, which carries the Act as 1,523 nodes and 1,944 edges parsed from official Formex XML and hash-verified.

## Distance to the line sets the clock

The connection the corpus flags as new and untested, and the reason the two axes are worth the trouble: if you know where a risk sits and where the line is, the gap between them is a number — and that number could set the interval.

Where the risk sits | Implied interval | Because |

Far above the acceptable line | hours to days | Every day it stands is a day spent above the level the business said it would fund remediation to |

Somewhat above | weeks to a month | A funded project, with a delivery window |

At or below the line | months | Nothing is owed. Review it when something changes |

If it holds, the interval stops being chosen and becomes computed from two numbers the register already carries. It is recorded here as proposed and untested — the corpus states it once and never works it through.

## Who sets the line, and what stops them setting it conveniently

Open question Q2, published unresolved. The definition — the point at which the business stops funding remediation — says what acceptable is and not who decides it or what constrains them. The obvious failure is a business unit that sets its acceptable level wherever its current exposure happens to be, making everything acceptable by construction.

The corpus's partial answer is external anchors: an internal severity is an opinion, and an external requirement is not. A retention period written into a regulation cannot be downgraded by a business unit that finds it inconvenient — which is precisely why the thirty-days-versus-six-months finding is the most defensible thing in that graph. It is arithmetic. When the business downgrades everything →

## Provenance

Concept
C5 — Accepted is not acceptable (two orthogonal axes)

Moved from
https://riskmandate.ai/acceptable.html · moved 22 August 2026 · a stub linking here is published at the source

Source
team/humans/dinis_cruz/briefs/07/28/regulation-graph-and-acceptability/v0.33.53__strategy-brief__…accepted-is-not-acceptable…md

Repository
SGraph-AI__App__Send @ v0.33.53

First written
28 July 2026

Curation
edited — commercial framing and the executive-audience targeting removed

Maturity
well-developed — formalised as node types P-PRED-001 to P-PRED-004

Licence
CC BY 4.0 at source and here

#### For an agent

C5 — accepted is not acceptable. These are two orthogonal properties, not two stages. Accepted = an act by a named person at a dated moment, for a stated interval. Acceptable = a threshold owned by the business: “the moment that the business is happy to stop funding remediation activities.” Crossing them gives four states, each needing a different response: accepted+acceptable is the steady state; accepted+not-acceptable is legitimate but owes a short interval and funded work; unaccepted+not-acceptable is the dangerous one and is rated critical by C4; unaccepted+acceptable is fine in effect and corrosive in aggregate, because the register cannot tell it from the dangerous one. Never collapse the two into a single status field. Acceptable is risk appetite renamed, and it is revealed rather than declared. EU AI Act Article 9(5) requires residual risk to be “judged acceptable” and never defines the term — so an organisation with no defined acceptable level carries a meta-risk about its own risk management. Proposed but untested: distance from the line sets the acceptance interval. Not implemented in code.


==============================================================================
== /acceptable/appetite.html
==============================================================================

