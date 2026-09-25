# The browser-isolation business case

The largest single graph in the corpus: 59 nodes and 75 edges across five altitudes, from an IT desktop team to the board. It is also the most self-critical thing here — it carries three risks of the mitigation itself, and cites a number that cuts against the argument it appears in.

## The graph, counted

Node type | Count | Edge type | Count |

Risk | 13 | gives_rise_to | 22 |

Owner | 7 | backed_by | 14 |

Evidence | 6 | owned_by | 11 |

Vulnerability | 6 | measured_by | 5 |

Fact | 5 | protected_by | 5 |

Asset | 4 | exposes | 3 |

Measure | 4 | reaches | 3 |

PreventiveControl | 3 | observed_on | 2 |

Grant | 2 | grants | 2 |

AuthorizationClosure | 2 | accepted_by | 2 |

BlastRadius | 2 | underwritten_by | 2 |

AcceptanceDecision | 2 | connected_to | 1 |

Reality | 1 | impairs | 1 |

Twin | 1 | emits | 1 |

DetectiveControl | 1 | conditional_on | 1 |

Total | 59 | Total | 75 |

Two things are worth reading off that table directly. First, gives_rise_to at 22 is nearly a third of all edges — the graph is mostly promotion, which is what the grounding ladder predicts it should be. Second, Reality appears exactly once and Twin exactly once: the whole structure is grounded in a single real system through a single representation of it, and every measure in the graph traces back through that one twin.

## The structure

Organised as F1–F8 facts, E1–E8 evidence, V1–V6 vulnerabilities, R1–R5 risks and L1–L5 altitudes:

L1

### IT and the desktop estate
Where the facts are observable and where the first vulnerabilities sit. Also where the plug is fastest and smallest.

L2

### The CISO
Security's reading of the same facts, and the first altitude at which the risk is stated in business rather than configuration terms.

L3

### CFO · COO · DPO
Three owners, three dimensions of the same exposure — cost, operations and data protection. The altitude where one risk visibly becomes several.

L4

### The CEO
Where the buck stops for everything except what has to go higher.

L5

### The board
The terminus, and the altitude at which the register converges to the single risk of staying in business.

The same risk restated at each altitude is the same object — which is exactly the point registers are one chain, not parallel lists is making, and what relevance fade would render.

## Three risks of the mitigation itself

The graph's most unusual feature, and the one that makes it worth reading even if the subject matter is not yours. Browser isolation is the proposed control. The graph carries three risks that the control creates:

1 · CONCENTRATED PLATFORM DEPENDENCYRouting all browsing through one platform makes that platform a single point of failure for every user who was previously independent of it.

2 · THE PLATFORM NOW SEES THE CONTENTIsolation works by interposing. Whatever interposes, reads. A control that reduces one confidentiality exposure creates another with a different counterparty.

3 · FRICTION ROUTES USERS AROUND ITThe oldest failure in security engineering, and the one most reliably omitted from a business case. A control users can avoid is a control that measures well and protects nothing.

Every action has risks, including the good ones. A mitigation whose own risks are not on the register has not been assessed — it has been advocated for.

That principle traces back to the pre-history: a Risk Decision Matrix from February 2026 whose five questions include “what is the risk of the fix?” Origins →

## The counterweight number

The graph cites vendor system cards reporting browser prompt-injection attack success rates falling from roughly half to about one percent across a single model generation — and it cites them deliberately, as the honest counterweight, because the number argues against the urgency of the business case it appears in.

How to read it, in both directions. A drop from ~50% to ~1% in one generation is a large, real improvement, and a risk assessment that hides it is not honest. It also does not reach zero — and at machine scale, “about one percent” of a very large number of attempts is not a small number of successes. The corpus states both halves and lets them sit against each other rather than resolving the tension in the direction that suits the argument. That is the posture this site inherits: the residual is real, and demanding zero produces covert acceptance.

## What this example is for

If you are looking for… | This graph shows it |

What a complete risk graph looks like at realistic size | 59 nodes is small enough to hold in your head and large enough to be real |

Authorization closure as a node type | Two AuthorizationClosure and two BlastRadius nodes, alongside the grants they were computed from |

Altitude as a modelling dimension | Five levels with named owners, and the same exposure restated at each |

Preventive and detective controls in the same graph | 3 PreventiveControl and 1 DetectiveControl, distinguished rather than lumped together as “controls” |

## Provenance

Source
briefs/07/12/worked-business-case/v0.33.48__briefing__…browser-isolation-agentic-automation-business-case-facts-vulnerabilities-risks-five-levels-graph.md

Repository
SGraph-AI__App__Send @ v0.33.48. Counts parsed from the JSON embedded in the document

First written
12 July 2026

Scope note
Preserved from the source: generic to the secure-browser and browser-isolation category. No vendor is named. The system-card figures are cited as a category observation, not as a claim about any product

Licence
CC BY 4.0 at source and here

#### For an agent

The browser-isolation business case — the largest worked graph. 59 nodes, 75 edges. Node types: Risk 13, Owner 7, Evidence 6, Vulnerability 6, Fact 5, Asset 4, Measure 4, PreventiveControl 3, Grant 2, AuthorizationClosure 2, BlastRadius 2, AcceptanceDecision 2, Reality 1, Twin 1, DetectiveControl 1. Edge types: gives_rise_to 22, backed_by 14, owned_by 11, measured_by 5, protected_by 5, exposes 3, reaches 3, observed_on 2, grants 2, accepted_by 2, underwritten_by 2, connected_to 1, impairs 1, emits 1, conditional_on 1. Structured F1–F8 facts, E1–E8 evidence, V1–V6 vulnerabilities, R1–R5 risks, L1–L5 altitudes (IT/desktop → CISO → CFO/COO/DPO → CEO → board). Reality and Twin each appear exactly once — the whole graph is grounded through one representation of one real system. Distinctive: the graph carries three risks of the mitigation itself — concentrated platform dependency, the platform now seeing the content, and friction routing users around it. Honest counterweight cited deliberately: vendor system cards report browser prompt-injection success falling from roughly half to about one percent across a single model generation — a large real improvement that does not reach zero. Generic to the category; no vendor is named.


==============================================================================
== /examples/article-26-5.html
==============================================================================

