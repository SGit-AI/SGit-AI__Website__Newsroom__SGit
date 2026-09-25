# Article 26(5): one provision, one agent, one graph

The complete instance. A single regulatory provision, a single deployed agent, and the whole ladder run end to end — from a fact about log retention up to a board-level exposure, and back down to the five questions nobody could answer. It carries its own node and edge inventory, and its most defensible finding is a subtraction.

## The inventory

Type | Count | Notes |

Reality | 1 | The running system |

Twin | 1 | The deployed agent |

Fact | 8 | One deliberately unevidenced — F7: the suspension procedure has never been exercised |

Evidence | 7 | One absent, which is why there are eight facts and seven evidence nodes |

Provision | 5 | Annex III 5(b), Articles 26(5), 26(6), 14, 27 |

Vulnerability | 3 | Each derived from a fact and a provision — the bridge point between the two graphs |

Risk | 5 | Four in a chain, one meta — R5: no acceptable level has been defined |

Stakeholder | 4 | ML platform lead, head of lending operations, DPO, CFO |

Decision | 3 | Plus one deliberately absent — D3 |

Question | 9 | Five unanswered — “those five are the actual output of the exercise” |

Project | 2 | Plus one unfunded |

## The finding that carries the whole example

Thirty days of log retention observed. At least six months required by Article 26(6). — “arithmetic, not judgement, which makes it the most defensible finding in the graph.”

Everything else in a risk assessment can be argued with. A severity is an opinion, a likelihood is an estimate, an impact is a model. This one is a subtraction, and it survives every conversation an executive can have about it: there is no rating to negotiate down and no methodology to dispute. It is also, deliberately, an external anchor — the six months is not the organisation's number, so no business unit can decide it is inconvenient. External anchors defeat systematic downgrading →

## Three deliberate absences

The most instructive thing about this graph is what is missing from it on purpose. Each absence is a modelling decision rather than an oversight, and each demonstrates a different concept:

What is absent | What it demonstrates |

F7's evidence — the suspension procedure has never been exercised, and there is no record either way | Not knowing is a fact. F7 is recorded as unevidenced, which makes it countable and assignable rather than a blank |

D3 — a decision that should exist and does not | Unaccepted equals critical. The risk it should have covered surfaces on the CFO's register as an unowned critical item, with nobody having escalated it |

R5's threshold — no acceptable level has been defined anywhere in the organisation | Article 9(5) mandates the judgement and never defines the word. The absence is itself a rateable meta-risk |

“R3 appears on the chief financial officer's register as an unowned critical item, and it got there without anybody escalating it deliberately. That is the mechanism working: not doing something is a measurable action.”

## The decisions, and their intervals

Decision | Interval | Reading |

D1 | 1 month | The default rung — assemble and fund |

D2 | 1 month | Same |

D3 | none | Deliberately absent — this is the one that rolls up |

D4 | 3 months | The upper end of “funded project”, approaching “waiting to see” |

## Five unanswered questions as the output

The claim that inverts what a risk assessment is normally judged by. The graph carries nine Question nodes; four have an answers edge and five do not — and the source says of those five that they are the actual output of the exercise.

An assessment that produced no unanswered questions almost certainly did not look hard enough.

It follows the quality gate on the same page: a question is not a risk. A sentence that cannot carry a named acceptor and an interval belongs in a different node type — and once it does, the unanswered ones become the work list rather than the residue.

## Four new edge types proposed here

The example proposes edges the earlier ontologies did not have, which is a good sign about the method — a worked instance pushing back on the schema rather than fitting into it:

Edge | What it connects |

governed_by | A fact or system to the provision that governs it — the bridge between the risk graph and the regulation graph |

in_scope_when | A provision to the condition that brings it into scope, so applicability is a path rather than an assertion |

answers | Evidence or a decision to the Question it resolves — and its absence is what makes a question unanswered |

re_rates | A later decision to the rating it supersedes, which is what makes the level ledger queryable |

## Provenance

Source
briefs/08/02/vault-as-substrate/v0.33.55__arch-brief__…end-to-end-worked-example-article-26-5-creditworthiness-agent-fact-to-board.md

Repository
SGraph-AI__App__Send @ v0.33.55

First written
2 August 2026

Scenario status
Preserved from the source: the organisation is invented, and every invented element is marked. Stakeholder titles (ML platform lead, head of lending operations, DPO, CFO) are generic roles, not people

Provisions
Cited from the Regulation Graph vault — the EU AI Act parsed from official Formex XML and SHA-256 hash-verified. Legal points are factual and are not legal advice

Licence
CC BY 4.0 at source and here

#### For an agent

Article 26(5) — the complete worked instance. Inventory: Reality 1 · Twin 1 · Fact 8 (one deliberately unevidenced — F7, the suspension procedure has never been exercised) · Evidence 7 · Provision 5 (Annex III 5(b), Articles 26(5), 26(6), 14, 27) · Vulnerability 3 (each derived from a fact and a provision) · Risk 5 (four in a chain, one meta — R5, no acceptable level defined) · Stakeholder 4 · Decision 3, plus one deliberately absent (D3) · Question 9, five unanswered · Project 2 plus one unfunded. Intervals: D1 = 1 month, D2 = 1 month, D3 = none, D4 = 3 months. The load-bearing finding: 30 days of log retention observed against at least 6 months required by Article 26(6) — “arithmetic, not judgement, which makes it the most defensible finding in the graph.” It is an external anchor, so no business unit can downgrade it. Three deliberate absences each demonstrate a concept: F7's missing evidence (not knowing is a fact), D3's missing decision (the risk surfaces on the CFO's register as an unowned critical item with nobody escalating it), R5's missing threshold (Article 9(5) mandates the judgement without defining the word). The five unanswered questions are “the actual output of the exercise.” Four new edge types proposed: governed_by, in_scope_when, answers, re_rates. The organisation is invented and every invented element is marked.


==============================================================================
== /examples/vaults.html
==============================================================================

