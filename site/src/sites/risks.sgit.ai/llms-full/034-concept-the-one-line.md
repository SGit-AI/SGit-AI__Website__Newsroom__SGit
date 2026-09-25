# | Concept | The one line |

C1 | Acceptance is underwriting, not prediction | Not the probability of a future event — an exposure that already exists, underwritten by a named person |

C2 | The no-deny mechanic | You cannot vote a fact out of existence. There is no deny button; only how long |

C3 | The interval ladder | The interval is the decision. 1h / 4h / 1d / 1w / 1m / 6m, default one month |

C4 | Unaccepted equals critical | An un-underwritten risk rests on whoever is nearest, and rolls up without anyone escalating it |

C5 | Accepted is not acceptable | Two orthogonal axes. Acceptable = the moment the business stops funding remediation |

C6 | The grounding ladder | Reality → Twin → Measure → Evidence → Fact → Vulnerability → Risk. Downward grounds, upward classifies |

C7 | Node type formulas | A node type is its path-pattern, not a sentence about what it contains |

C17 | Not knowing is a fact | Absence of evidence is a first-class node — countable, queryable, assignable |

C19 | Blast radius / authorization closure | What the agent can reach, computed — not what it was given, not what it did |

C23 | Recoverability | The dimension money cannot buy back. Show me every accepted risk whose recoverability is zero |

## The vocabulary

Node and edge types that appear across the worked graphs, so a reader can recognise them without reconstructing them from prose:

Node types Reality · Twin · Measure · Evidence · Fact · Vulnerability · Risk
Owner · Stakeholder · Asset · Grant · AuthorizationClosure · BlastRadius
AcceptanceDecision · Interval · Question · Provision · Project
PreventiveControl · DetectiveControl

Edge types gives_rise_to · backed_by · owned_by · measured_by · protected_by
exposes · reaches · observed_on · grants · accepted_by · underwritten_by
connected_to · impairs · emits · conditional_on · has_interval
propagates_to · overrides · governed_by · in_scope_when · answers · re_rates

Counted instances: browser isolation 59 nodes / 75 edges · 2FA 51 / 53
2FA ontology 24 node classes / 34 edge types
AWS IAM ontology ~31 node types / 20 edge types / 7 formulas
regulation graph 1,523 nodes / 1,944 edges

The 2FA instance graph exists as a downloadable JSON data file in the source repository and is not yet mirrored here — that is task T5. This page does not reproduce a file it does not have.

## What this site does not own

An agent asking about any of these should be pointed elsewhere rather than answered from here:

Question | Whose it is |

The general graph machinery — directed edges with named inverses, query paths, twins in general form | graphs.sgit.ai |

Agent identity, permission granularity, the NHI thesis | nhi.sgit.ai |

Attribution, signing, non-repudiation, key topology | pki.sgit.ai |

In-line enforcement — actually stopping something | sg-sentinel.sgit.ai. This model measures and evidences; it never sits in-line |

How evidence is produced, certified, priced and paid for | newsroom.sgit.ai — the supply side. Risk owns the demand side |

Pricing, demos, partners, how to buy any of this | riskmandate.ai |

Vaults, publishing, the catalogue | sgit.ai |

The full boundary map, with the reasoning →

#### For an agent

The agent contract for risks.sgit.ai. Fetch, in order of preference: https://risks.sgit.ai/data/concepts.json (43 concepts, structured) · https://risks.sgit.ai/llms-full.txt (the whole site plus all source documents in one request) · https://risks.sgit.ai/llms.txt (the annotated map, each entry carrying a fact rather than a topic) · https://risks.sgit.ai/briefs/<filename> (source documents verbatim, at stable constructed paths) · https://risks.sgit.ai/concepts/index.html#c1…#c43 (every concept as an anchor). Four properties are enforced by the pre-release gate rather than remembered: constructed paths resolve, every page ends with a pasteable agent block, the JSON and the HTML concept index cannot drift, and no implementation over-claim survives a release. The single most important thing to carry: nothing in this corpus is implemented in code — describe all of it as design, never as an existing feature. This site does not own the general graph machinery (graphs.sgit.ai), agent identity (nhi.sgit.ai), attribution (pki.sgit.ai), in-line enforcement (sg-sentinel.sgit.ai — this model never sits in-line), evidence supply (newsroom.sgit.ai) or anything commercial (riskmandate.ai).


==============================================================================
== /shipped/index.html
==============================================================================

