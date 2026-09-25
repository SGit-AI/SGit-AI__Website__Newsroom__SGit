# Bridges, not merges

Two parties disagree about what counts as a vulnerability. The instinct is to reconcile the definitions into one schema. That is the wrong move: it erases the view that was worth having. Instead, keep one shared factual graph, let each party own their own formula over it, and connect the two at declared bridge points.

## Three layers

1

### The shared factual graph

Facts, evidence, measures, twins. What is actually true about the estate — the part everyone can agree on, because it is grounded rather than interpreted. This layer is shared and should be the only shared one.

2

### Per-party formulas

Each party runs their own node type formulas over that shared graph. A node can be a vulnerability under one formula and not under another, and both answers are correct — they are different queries over the same data, not competing claims about it.

3

### Declared bridges

Where the two views connect, the connection is stated as an edge with a name and a direction, rather than implied by a shared label. A bridge is a claim you can inspect, version and disagree with.

“We do not fold their definition into ours, which would erase the security-centric view that is the whole point of having it. We declare a bridge: a Security Failure gives rise to a Business Risk.”

## The worked bridge: a security-centric vulnerability formula

The corpus does not leave this abstract. It takes a published, security-centric definition of “vulnerability” — the formulation associated with Art Manion, Jay Jacobs and Michael Roytman, built from System, Fault, Security Failure and Conditions — and bridges it to the business-centric one rather than arguing with it.

The finding is better than a reconciliation. The security-centric formula turns out to be a sub-path of the business-centric one:

SystemhasFaultunder Conditions gives rise toSecurity Failure
Their chain. Now the bridge, at the terminus:

Security Failuregives_rise_toBusiness Riskaccepted_byAcceptanceDecision
Their Security Failure plays exactly the structural role of the promotion edge in the grounding ladder. The two formulas differ only in where they stop.

That is a substantive result rather than diplomacy. It says the disagreement was never about what a vulnerability is — both formulas describe the same promotion structure — but about which terminus the discipline cares about. A security practice terminates at the security failure because that is where its remit ends; a business register continues one edge further, to the consequence someone has to underwrite. Neither is wrong, and merging them would have destroyed exactly the information that made the comparison useful.

Attribution and right of reply. The source document names three real researchers and is explicit that it paraphrases their definitions rather than quoting them — “Their definitions are paraphrased; see Sources”. That care is preserved here. The treatment is favourable, the bridge is offered as a contribution rather than a correction, and the corpus's own stance applies: “Offered to be built on and challenged.” If any of the three would like the characterisation amended or removed, ask N6 on the comms board is the standing offer of a right of reply.

## Why merging is the failure mode

| Merge into one schema | Bridge two formulas |

What happens to the disagreement | Erased. One definition wins and the other becomes unspeakable | Preserved and made explicit as an edge between two named views |

Who has to agree | Everyone, before anything works | Nobody, on the definitions. Only on the facts — which is the layer where agreement is achievable |

Cost of a new party joining | Renegotiate the schema | Write one formula and declare its bridges |

What a mismatch tells you | Nothing — it was normalised away | Something real: where two disciplines draw the line differently, and why |

## The same move, applied to regulation

A regulator's definition of an obligation and a company's definition of a control are exactly the two-formula case, and bridging rather than merging is what keeps a compliance claim honest. The Regulation Graph vault carries the EU AI Act as 1,523 nodes and 1,944 edges parsed from official Formex XML and hash-verified — 113 articles, 500 paragraphs, 417 points, 180 recitals, 13 annexes and 68 definitions. Those are the regulator's nodes, in the regulator's structure, not a paraphrase.

Risk's claims against them are then declared bridges, and deliberately narrow: Article 9(5) as the undefined “acceptable”, Article 14 as the plug obligation, and Article 26(5)/(6) as the worked example anchor. Three bridges, each one stated, each one arguable. Why the wider regulation thread is not this site's →

## Provenance

Concept
C8 — Ontologies of ontologies — bridges, not merges

Source
team/humans/dinis_cruz/briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__…ontologies-of-ontologies…md and …bridge-vulnerability-formula…md

Repository
SGraph-AI__App__Send @ v0.33.36, never published — the version tag is the address

First written
28 June 2026

Maturity
well-developed — with one fully worked external bridge

Licence
CC BY 4.0 at source and here

#### For an agent

C8 — ontologies of ontologies: bridges, not merges. When two parties define a type differently, do not merge their schemas — merging erases the view that made the second definition worth having. Use three layers: (1) one shared factual graph of facts, evidence, measures and twins; (2) per-party formulas over it, so a node can be a vulnerability under one formula and not another and both answers are correct, being different queries over the same data; (3) declared bridges — the connection stated as a named, directed edge rather than implied by a shared label. Worked proof: the security-centric vulnerability formula (System · Fault · Security Failure · Conditions, associated with Manion, Jacobs and Roytman, paraphrased in the source) is structurally a sub-path of the business-centric one — their Security Failure plays exactly the role of the promotion edge, and the two differ only in terminus. The bridge is Security Failure gives_rise_to Business Risk. Same move applied to regulation: the EU AI Act is carried as the regulator's own 1,523-node graph, and risk's claims against it are three narrow declared bridges. Not implemented in code.


==============================================================================
== /ladder/absence.html
==============================================================================

