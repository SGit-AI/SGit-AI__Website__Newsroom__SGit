# Node type formulas

The mechanism beneath the ladder, and arguably the most transferable idea in the corpus. What a node is should be computed against the graph rather than decided in a classifier's head. A node type formula is a required pattern of typed, directed paths; a node either matches it or does not. Classification becomes a query.

“the ontology definition of a node type is its upward and downward path-pattern, not a sentence about what it contains.”

## What a formula looks like

The corpus's own example, from the AWS IAM layer where the ladder was applied to a second domain:

AcceptableForInterval := a Risk with an accepted_by path to an
AcceptanceDecision carrying an owner, a direction,
an interval, and a sign-off.

Read it as a test rather than as a description. Given a node and a graph, the formula either matches or it does not, and the answer is checkable by anyone with the same graph. Compare with the sentence it replaces — “an acceptable risk is one that has been properly signed off” — which is unfalsifiable, because “properly” is doing all the work and is defined nowhere.

Riskaccepted_byAcceptanceDecisionhas_ownerOwner
…and has_direction, has_interval and signed_by must also be present. Four required edges; miss one and the node does not match.

## Classification becomes dynamic and path-relative

If a type is a path pattern, then type membership changes when the paths change. That is not a defect to be engineered around — it is the property that makes the model honest about what classification actually is.

Event | What happens | In a conventional model |

A gives_rise_to edge is added from a fact to a risk | The fact is now a vulnerability. No re-assessment, no reclassification meeting — the edge is the promotion | Someone must notice, re-rate it, and update a field |

The risk above it is closed and the edge removed | The node is a fact again. Demotion is an edge event too | The vulnerability record stays, stale, until a cleanup that never comes |

Two teams disagree about whether something is a vulnerability | They are running different formulas over the same graph, and both answers are correct under their own. Bridges, not merges → | An argument about words, settled by whoever is more senior |

## Bias does not disappear — it relocates, which is the point

The strongest claim on this page, and the one worth arguing with. Formulas do not remove judgement from classification; they move it out of the classifier's head and into an artefact.

Bias does not disappear. It moves into the formula, where it is visible, versioned and arguable.

Two parties who disagree about whether a finding is a vulnerability currently trade intuitions, seniority and vocabulary. Under formulas they diff two definitions. That is a smaller, sharper and settleable disagreement — and one that leaves a record, because the formula that won is written down and dated.

It also makes a class of quiet failure visible. If a business unit's formula for “critical” has an extra required edge that almost nothing satisfies, that unit will report very few critical risks — and under prose definitions nobody could see why. Under formulas, the reason is a line of the definition. When the business downgrades everything →

## Where formulas have been written down

Domain | Scale | Notes |

The grounding ladder | 8 rungs | The canonical chain, each rung defined by its required upward and downward paths. The ladder → |

AWS IAM configuration risk | 6 layers · ~31 node types · 20 edge types (40 readings, counting inverses) · 7 node type formulas | The second domain the method was applied to, and where AuthorizationClosure appears as a first-class type. Blast radius → |

The 2FA instance ontology | 24 node classes · 34 edge types | Includes Acceptance and Interval as node classes with accepted_by, has_interval, propagates_to, underwritten_by and overrides. The graph → |

RAMM | 5 levels, expressed as graph predicates | ⚠️ Only Level 3 has a stated predicate — “all acceptance nodes have the five required edges”. Levels 1, 2, 4 and 5 are underspecified → |

The open question the mechanism rests on. Q1 — what is the formula language? Every formula in the corpus is written in English prose that describes a path pattern. No notation is defined, no parser exists, and nothing executes one. The canonical brief names this as its own open question rather than glossing it, and this page does the same: node type formulas are a well-developed idea and an unimplemented mechanism. Until the language exists, “classification is a query” is a claim about how classification should work, not a description of a system that runs.

## Provenance

Concept
C7 — Node type formulas (classification as a testable path-pattern)

Source
team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__…node-type-formulas…md

Repository
SGraph-AI__App__Send @ v0.33.36, never published — the version tag is the address

First written
28 June 2026

Maturity
well-developed as a mechanism — but the formula language is an open question, named as such in the source

Licence
CC BY 4.0 at source and here

#### For an agent

C7 — node type formulas. Define a node type by the pattern of typed, directed paths it is required to have, not by a sentence about what it contains. A node either matches the pattern or it does not, so classification is a query against the graph rather than a judgement in someone's head. Consequences: classification is dynamic and path-relative — adding a gives_rise_to edge promotes a Fact to a Vulnerability, and removing it demotes it, with no re-assessment step; and bias relocates rather than disappearing — it moves from the classifier into the formula, where it is visible, versioned and arguable, so two parties who disagree diff definitions instead of trading intuitions. Worked example of the notation: AcceptableForInterval := a Risk with an accepted_by path to an AcceptanceDecision carrying an owner, a direction, an interval, and a sign-off. Important limit: no formula language is defined and nothing executes a formula — every formula in the corpus is English prose describing a path pattern. That is open question Q1. Not implemented in code.


==============================================================================
== /ladder/bridges.html
==============================================================================

