# The grounding ladder

The definitional spine of the whole model, and the part an agent most needs to hold. Every node type is defined by the paths it is required to have, not by what it contains. Downward paths confer grounding — is this real? Upward paths confer classification and implication — what is it, and why does it matter? A Vulnerability is not a special kind of Fact. It is a Fact with an upward path to a Risk.

## Reality → Twin → Measure → Evidence → Fact → Vulnerability → Risk → Top Risk

Realityhas_twinTwinmeasured_byMeasureproducesEvidencebacksFactgives_rise_toVulnerabilitygives_rise_toRiskrolls_up_toTop Risk
Read downward it is an answer to “how do you know?”. Read upward it is an answer to “so what?”. Both directions are typed, and neither is optional.

1

### Reality

The running system, the actual estate, the world. Not a record of it — the thing itself. Everything in the graph is ultimately an assertion about this, and the only rung that is not a node in your model.

2

### Twin

A representation of a piece of reality, connected to it. The twin is where the graph stops modelling and continues into a real system — an inventory that is actually synced, a config that is actually read. How connected a twin is to reality is itself a measurable property, which produces a useful recursion: trust in a measure depends on the twin's connectedness, and that connectedness is itself a measure. A twin not connected to reality is a tracked air gap.

3

### Measure

An observation taken through the twin. A Measure is not the floor. That is the most common misreading of the ladder: a measurement feels like bedrock, but it is grounded further, in the twin and through it in reality. A measure with no twin beneath it is a number nobody can defend.

4

### Evidence

What a measure produces, and what a fact is backed by. Evidence is a first-class node, so it can be counted, dated, attributed and — crucially — found to be absent. Not knowing is a fact →

5

### Fact

A statement about reality that evidence backs. Admin accounts do not require a second factor. Logs are retained for thirty days. Facts are the layer where a register and reality touch, and a register built on unevidenced facts is a register of opinions.

6

### Vulnerability

A Fact with an upward path to a Risk. Nothing about the fact changes when it becomes a vulnerability; what changes is that something above it now depends on it. This is the rung that makes the whole formula idea click, and it is why classification is dynamic: add the upward edge and the fact is promoted; remove it and it is demoted.

7

### Risk

A business consequence that a vulnerability gives rise to, and the level at which acceptance happens. One vulnerability commonly gives rise to several risks in different dimensions — confidentiality, integrity and availability each spawn their own, and each follows the full confirm-accept-propagate loop.

8

### Top Risk

What risks roll up to at the highest altitude. The chain converges: pushed far enough, business risk converges on the single risk of staying in business, which is why a legitimate single number can be carried to the top at all. Five whys as a domain translator →

## Downward grounds, upward classifies

The two directions are not symmetrical, and keeping them straight is most of the value:

| Downward | Upward |

Question | How do you know this is real? | What is it, and why does it matter? |

Confers | Grounding | Classification and implication |

Failure | An assertion nobody can defend | A true statement nobody has a reason to act on |

Example | A risk with no fact beneath it is somebody's worry | A fact with no risk above it is trivia — accurate, evidenced, and irrelevant |

“A Fact becomes a Vulnerability purely because of its upward link to a Risk, so that legitimacy is conferred entirely from above.”

## Where the ladder stops — a test, not a rung

Every grounding chain has to stop somewhere, and the obvious answers are all wrong: not at the measure, not at the tool, not at wherever the data happened to come from. The corpus gives a test instead of a level:

The floor is the last node where going deeper would neither improve observability nor change a decision.

This is a good rule and an under-worked one. It is decision-relative, which means the same graph can have different floors for different questions, and it means the floor moves when the decision changes. Open question Q7: no worked example in the corpus applies the test to a genuinely hard case, so how it behaves at the margin is unknown.

## The worked example the source uses: the untested restore

Backup systemhas_twinBackup config + logsmeasured_by“restore tests in last 12 months”producesE5: zero records foundbacksF: no restore has been testedgives_rise_toV: recovery capability unprovengives_rise_toR9: data loss is unrecoverable in practice
Note that the measure returned zero, and the zero is the evidence. A documented absence is a measurement, not a missing one.

## The boundary with graphs.sgit.ai

Node type formulas as a mechanism belong to graphs.sgit.ai; the grounding ladder as a risk formula belongs here. This site cites the mechanism rather than restating it — the general case for directed edges with named inverses, query paths that prevent node explosion, and digital twins in their general form is argued at length there and is not re-argued here. What is risk's own is this specific chain, its stopping test, and what each rung licenses you to say. The full boundary map →

## Provenance

Concept
C6 — The grounding ladder

Source
team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__…grounding-ladder…md

Repository
SGraph-AI__App__Send @ v0.33.36, never published — the version tag is the address

First written
28 June 2026

Maturity
well-developed — the most rigorous document in the corpus, and the one agents most need

Licence
CC BY 4.0 at source and here

#### For an agent

C6 — the grounding ladder. Reality → Twin → Measure → Evidence → Fact → Vulnerability → Risk → Top Risk. Every node type is defined by its required paths, not by its content. Downward paths confer grounding (“is it real?”); upward paths confer classification and implication (“what is it, why does it matter?”). Key definitions to carry: a Vulnerability is a Fact with an upward path to a Risk — legitimacy is conferred entirely from above, so promotion and demotion are edge events, not re-assessments. A Measure is not the floor: it is grounded further in a Twin and through it in Reality. The floor is a test, not a level — the last node where going deeper would neither improve observability nor change a decision. A risk with no fact beneath it is a worry; a fact with no risk above it is trivia. The general graph machinery (directed edges with named inverses, query paths, twins in general form) belongs to graphs.sgit.ai and is cited rather than restated here. Not implemented in code.


==============================================================================
== /ladder/formulas.html
==============================================================================

