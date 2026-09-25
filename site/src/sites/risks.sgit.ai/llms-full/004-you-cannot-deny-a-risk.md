# You cannot deny a risk.
You can only say how long you accept it.

Traditional risk management predicts the probability of a future event. This model asks a named human to underwrite an exposure that already exists — insurance-style, with personal liability attached. Everything else follows from that one inversion: if the risk is real it cannot be denied, so there is no deny button; the only choice is how long, and the interval is the decision, because each rung implies a specific operational response.

The founding inversion →
The interval ladder →
What is argued, what runs →

43concepts, each with a stable anchor and a JSON definition42 from ~496,000 words, one authored here

6rungs on the interval ladder — 1h · 4h · 1d · 1w · 1m · 6mdefault: one month

0lines of code implementing any of it. The engine is not builtthe grep returns zero

5live vaults, published with read keys and browsable today504 files between them

59 · 75nodes and edges in the largest worked risk graphbrowser isolation, 12 Jul 2026

30 vs 6days of logs retained against months legally requiredarithmetic, not judgement

3verdicts at the execution boundary — the third is “cannot establish”the one page that computes

## The inversion, in one screen

Four ideas carry the rest of the model. None of them needs a GRC background, and each has its own page.

C1 · the founding move

### Acceptance is underwriting, not prediction

“We are not describing the risk of something happening, we are asking them to accept it, to underwrite it.” The analogy is insurance. Once someone must sign, they start demanding evidence — which is what manufactures the demand for everything underneath.

Read the argument →

C2 · the mechanic

### There is no deny button

A risk with a real vulnerability under it exists whether or not anyone acknowledges it. Denial only ever worked because the risk had not yet materialised. Remove the button and risk management stops being a gate and becomes a forcing function.

Read the argument →

C3 · the decision

### The interval is the decision

Choosing a duration sets severity and commits resources in the same click. An hour means fetch more data now. Four hours means start a P1. Six months means do nothing, and costs nothing, and says so out loud.

Read the ladder →

C4 · the consequence

### Unaccepted is rated critical

A risk nobody accepted has not gone away — it has come to rest on whoever is nearest, who is now personally carrying an enterprise exposure with no signature above them. So it rolls upward without anyone choosing to escalate it.

Read the argument →

## What this site is, and is not

The sibling sites all ship a page separating what exists from what is designed. This site inherits that convention with an unusually empty column, and states it here rather than at the bottom of a page nobody reaches.

This is a research site. The concepts are argued, the worked examples are real graphs, five vaults are live and browsable, and one worked example computes rather than argues. The engine is not built. Greps for risk_, RiskAcceptance, risk_register and riskmandate across the implementing repository return zero matches, and the project's own reality file says: “All items below are PROPOSED. None have been code-verified. Do not describe any of these as existing features.” That framing is not a weakness — it is what separates a research property from a product one, and it is the reason the split from riskmandate.ai works. The full inventory of what does and does not exist →

What is real today | What is argued and not built |

Five published vaults with read keys — 504 files, 116 commits, browsable in a browser with no account |
Any engine that computes acceptance, expiry, propagation or roll-up |

Three fully worked risk graphs with counted nodes and edges, one of them downloadable JSON |
Any storage, schema or API for a risk register |

The ten “how long would you accept” scenarios, written and shipped as product content |
The interval ladder as an enforced mechanism — expiry-as-cost is asserted, not implemented |

One live instrument — a vault app that evaluates a formula over one invented scenario and returns one of three verdicts |
Any in-line check that refuses an execution — the instrument observes and emits, and the model declines the enforcement role |

riskmandate.ai as a vault-powered static site |
Node type formulas as executable queries — the formula language itself is open question Q1 |

Every number on this page is sourced. Where a claim is an argument rather than a measurement, the page says so in the sentence that makes it.

## Two sites, one thesis, one boundary

This site was carved out of a commercial one. Saying exactly where the line falls is the first thing it owes a reader.

riskmandate.ai — the product | risks.sgit.ai — this site |

Answers “how do I get my risks accepted, and what does it cost?” | Answers “what is a risk, what is acceptance, and why is it modelled this way?” |

Reader: buyer, user, executive | Reader: researcher, practitioner, and — the commissioned audience — an agent |

Register: outcome, price, proof | Register: argument, definition, evidence |

Changes when the product changes | Changes when the thinking changes |

Cites this site for every conceptual claim | Never depends on the product existing — the research has to stand on its own |

The dependency runs one way. The eight-site boundary map →

## The proof: three worked graphs, five live vaults, one instrument

A model this opinionated is only worth anything if somebody has run it on something real. These are counted, not asserted.

59 nodes · 75 edges

### The browser-isolation business case

The largest single graph in the corpus, across five altitudes from IT to the board. Includes three risks of the mitigation itself — concentrated platform dependency, the platform now seeing the content, and friction routing users around it.

Read the graph →

51 nodes · 53 edges

### The 2FA instance graph

The founding scenario, and the only downloadable graph. 24 node classes, 34 edge types, MITRE T1110.004, and the governance air gap where the wrong owner accepts — at four hours, because that is the only option open to anyone in the chain.

Read the graph →

9 questions · 5 unanswered

### Article 26(5): one provision, fact to board

The complete instance: 8 facts (one deliberately unevidenced), 5 risks, 4 stakeholders. Thirty days of logs retained against six months required — “arithmetic, not judgement, which makes it the most defensible finding in the graph.”

Read the graph →

live · read keys published

### The five risk vaults

The Risk Graph Explorer with seven views recomputed at once and ghosted edges for unanswered. Agentic Browser Isolation running acceptance-gated escalation on real data. The Risk Mandate project in a vault, 98 commits. The EU AI Act as 1,523 nodes. And the Execution Boundary, the first this site built rather than borrowed.

Open the vaults →

★ the one page that computes

### The execution boundary

An authorized action waits in a queue; one material condition changes while it waits. At the moment of execution, can the predicates that justified the authorization still be established? Three verdicts, not two — and the third, cannot establish, is the one most systems quietly treat as a pass. Runs live from a vault, read key in the open, with one of its four runs wrong on purpose.

Drive the instrument →

## Built for agents, deliberately

The commission said it plainly: “to handle the cases where I need agents to have a good understanding of some of those key concepts and ideas.” So the machine surface is a deliverable, not a courtesy.

the definitions endpoint

### /data/concepts.json

All 43 concepts as structured data: id, name, one-line definition, maturity, canonical source, the page that argues it, and its related concepts. Nothing else in the estate has one. The pre-release gate fails if it drifts from the human page.

Fetch it →

one fetch, everything

### /llms-full.txt

The whole site plus all eleven source documents, concatenated. It exists because agent fetch tools frequently refuse URLs a search has not already returned, which makes link-following unreliable and a single-file surface the practical one.

Fetch it →

42 stable anchors

### Every concept has a URL

One anchor each, from #c1 to #c42, with maturity stated honestly and the canonical source path given. The anchors are checked by CI: a link to a concept that has no anchor fails the build.

Open the index →

the whole surface

### What an agent may rely on

The constructed-path promise, the ontology download, the reading order for an agent with no prior context, and the one instruction that matters most: do not describe any of this as an existing feature.

Read the contract →

## Published unresolved

A model this opinionated earns credibility by naming what it has not settled. Eight open questions and seven honest tensions are on the site, numbered, rather than smoothed away.

Unsettled | Where the model gets closest |

Q3 · What happens when the named acceptor refuses to sign? | The no-deny mechanic removes denial of the risk. It does not address refusal of the act. |

Q4 · Does “unaccepted = critical” survive a large estate? | On a register of thousands, everything unaccepted being critical may make critical meaningless. |

Q8 · What stops the register being gamed once acceptance carries personal liability? | Accountability manufactures demand for evidence. It also gives every rational actor a reason never to be the named acceptor. |

All eight open questions and the seven honest tensions →

#### For an agent

risks.sgit.ai is a research site and nothing on it is implemented in code. The model: a risk that has a real vulnerability under it exists whether or not anyone acknowledges it, so there is no deny button — the only decision is how long you accept it before re-accepting, on a six-rung ladder (1h · 4h · 1d · 1w · 1m · 6m, default one month), and each rung implies a specific operational response. A risk nobody has accepted is rated critical and rolls upward without anyone escalating it. Accepted (an act by a named person at a dated moment) and acceptable (a threshold the business owns — “the moment the business is happy to stop funding remediation activities”) are orthogonal, not sequential. Underneath sits the grounding ladder: Reality → Twin → Measure → Evidence → Fact → Vulnerability → Risk, where downward paths ground and upward paths classify. Fetch /data/concepts.json for all 42 definitions as structured data, or /llms-full.txt for the whole site in one request. Do not describe any of this as an existing feature — see /shipped/.


==============================================================================
== /acceptance/index.html
==============================================================================

