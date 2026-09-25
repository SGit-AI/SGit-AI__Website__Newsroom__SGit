# RAMM and the maturity models

Three maturity models sit on top of the acceptance machinery, and the interesting thing about the main one is that its levels are meant to be graph predicates rather than descriptions — a level you can test a register against rather than assess it against. That is the right ambition. It is also, at the moment, only half delivered, and this page says which half.

## Levels as predicates, not descriptions

A conventional maturity model describes what an organisation at each level looks like, and an assessor decides which description fits. RAMM's move is to state each level as a node type formula — a path pattern a query can test against the register itself.

A level stated as a predicate can be run. A level stated as a paragraph can only be argued about.

The one level that is fully stated shows what the whole model should look like:

Level 3 := all acceptance nodes have the five required edges.

That is checkable. Point it at a register and it returns true or false, with a list of the acceptance nodes that fail it. No assessor, no workshop, no interpretation — and, importantly, no way to talk your way to a higher level than the graph supports.

## ⚠️ Levels 1, 2, 4 and 5 are underspecified

Stated plainly rather than papered over. Of the five base levels, four are named but carry no stated predicate. Only Level 3 has one. The consequence is that RAMM currently cannot do the thing that makes it worth having: an organisation cannot test itself against four of its five levels, so for those four it falls back to being an ordinary descriptive maturity model with graph vocabulary on top.

Stranger still, the Agentic + variants are better defined than the base model they extend — the extension has more rigour than the thing being extended. Specifying levels 1, 2, 4 and 5 to the standard Level 3 already sets is open ask N2, and it is the single highest-value fix available to this section. Until it lands, this page does not invent the missing predicates: writing four plausible-sounding definitions and presenting them as the model would be exactly the failure this site exists to avoid.

Level | Stated predicate | Status |

Level 1 | — | named only |

Level 2 | — | named only |

Level 3 | all acceptance nodes have the five required edges | stated and testable |

Level 4 | — | named only |

Level 5 | — | named only |

Agentic + variants | Defined | better defined than the base model |

## The entity model

What RAMM's predicates are written against. RiskAcceptanceDecision is the hub node, carrying twelve named directed edges:

RiskAcceptanceDecisionownedByDecisionAuthority
…plus approvedBy · boundedBy · withinToleranceOf · justifiedBy · evidencedBy · reviewedAt · expiresAt · reassessOn and three more. Twelve edges from one node is what makes “the five required edges” a meaningful test rather than a tautology.

The surrounding entity types: RiskItem, RiskAcceptanceDecision, DecisionAuthority, RiskAppetiteStatement, ReviewEvent, ExpiryEvent, EvidenceArtifact. Note that ExpiryEvent and ReviewEvent are nodes rather than dates — which is the same move as decision-as-a-node, and for the same reason: an event you can attach evidence and attribution to.

## Crosswalks

RAMM is positioned against existing frameworks rather than as a replacement for them, and the crosswalks are part of the model rather than an appendix:

Framework | What the crosswalk is for |

OWASP Risk Rating | Severity vocabulary — mapping an existing rating into a register that also carries an interval |

OWASP SAMM | Programme maturity, where RAMM covers only the acceptance slice of it |

OWASP ASVS · WSTG | Verification requirements as sources of facts and evidence |

Threat Dragon | Threat models as an upstream producer of vulnerabilities |

DefectDojo · CycloneDX | Existing tooling as the feed — where the register begins where scanners stop |

RIMS RMM | The enterprise risk-management maturity comparison |

## The plug-pull maturity model

The second model, and the one with the cleanest probe. It asks whether an organisation can compute its plug profile — who holds it, blast radius, speed, side effects, recoverability — for a given system, and it is fractal in the same way registers are: the answer differs at every altitude, because the off-switch at L1 is not the off-switch at L5.

An organisation that can compute the profile has, by construction, measured detection latency, decision availability, blast radius and reversibility. One that cannot has established that somebody believes it can stop the system. The maturity probe →

## AOMM and the observability scale

The third: agent observability maturity, scored on the six objective vectors — capture granularity, log latency, time-to-damage at real throughput, whether monitoring is on and watched, whether a team with playbooks exists, and whether detection has been drilled. Its reframe is the useful part: a loud, detectable, slowly-scaling, well-drilled risk is lower than a quiet, fast, unwatched one of the same capability.

## Prior art: the ancestor, a year early

Maturity Models vs. Traditional Standards in Application Security (2 April 2025, 2,701 words) is RAMM's direct ancestor, published a year before the corpus this site draws on. Its argument — that a maturity model describes a trajectory where a standard describes a bar, and that the two answer different questions — is the reason RAMM is a maturity model at all.

Published on docs.diniscruz.ai under CC0. Cited here rather than republished; the canonical link and the original date stay with the source. All eight prior-art articles →

## Provenance

Concepts
RAMM · AOMM · the plug-pull maturity model · C37 confidence bands · C38 two underwritings · C39 observability

Moved from
https://riskmandate.ai/ramm.html · moved 22 August 2026 · ⚠️ republished with the underspecification stated, which the source page does not do

Source
briefs/07/02/authorization-and-maturity-model/v0.33.40__arch-brief__…risk-acceptance-maturity-model-ramm-graph-native-levels-agentic-crosswalk.md

First written
2 July 2026

Maturity
partially specified — one of five base levels has a stated predicate. Open ask N2

Licence
CC BY 4.0 at source and here

#### For an agent

RAMM and the maturity models. RAMM's design intent is that each of its five levels is a graph predicate — a path pattern a query can test a register against — rather than a description an assessor interprets. Important limit: only Level 3 has a stated predicate (all acceptance nodes have the five required edges). Levels 1, 2, 4 and 5 are named but carry no predicate, and the Agentic + variants are better defined than the base model they extend. Do not quote RAMM levels 1, 2, 4 or 5 as if they were specified, and do not invent predicates for them. The entity model: RiskAcceptanceDecision is the hub node with twelve named directed edges (ownedBy, approvedBy, boundedBy, withinToleranceOf, justifiedBy, evidencedBy, reviewedAt, expiresAt, reassessOn…), surrounded by RiskItem, DecisionAuthority, RiskAppetiteStatement, ReviewEvent, ExpiryEvent, EvidenceArtifact. Crosswalks exist to OWASP Risk Rating, SAMM, ASVS, WSTG, Threat Dragon, DefectDojo/CycloneDX and RIMS RMM. Two companion models: the plug-pull maturity model (can you compute your plug profile? — fractal by altitude) and AOMM, agent observability maturity on six objective vectors. Not implemented in code.


==============================================================================
== /examples/index.html
==============================================================================

