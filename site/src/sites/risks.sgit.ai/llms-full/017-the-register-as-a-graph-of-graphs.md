# The register as a graph of graphs

A risk register is not a spreadsheet at the top of a company. It is a hyperlinked semantic graph — one per accepting entity, all of them views of one connected structure rather than parallel lists. Its distinguishing move is where it starts: at the vulnerability, which is exactly where scanners and security products stop.

“a lot of security teams and products end on the vulnerability, and what I want to show is the multiple layers involved in fixing it, but even before that, in accepting the risk, funding the solution, and finding who is going to do it.”

## It begins where scanners stop

A scanner's output is a list of vulnerabilities, and its implicit theory is that the hard part is finding them. In practice the finding is the cheap part. What follows is where the work is, and none of it is in the scanner's output:

1 · WHO CONFIRMS ITThe technical owner validates that the vulnerability is real in their domain. Factual, and either true or false. Confirmed →

2 · WHO OWNS THE CONSEQUENCENot the same person. The business owner owns the risk the vulnerability gives rise to, which is usually in a different department and a different vocabulary. Technical vs business owner →

3 · WHO ACCEPTS IT, AND FOR HOW LONGThe underwriting act, at the right altitude, on the interval ladder.

4 · WHO FUNDS THE FIX, AND WHO DOES ITThe interval already committed the organisation to a response. This is where that commitment turns into a project with a name against it.

## Fractal: one register per accepting entity

Wherever there is a stakeholder who accepts risk, there is a register. For the company, for a department, for an individual role. That is not an organisational nicety — it follows directly from acceptance being a personal act: if a named person underwrites, they need a place where the things they have underwritten are listed.

Most of those registers are derived rather than curated. An individual has at least two and often three: their own role-specific register in their own domain language, plus views of the registers above them. Only the role's own register is stored; the rest are queries.

Register | Stored or derived | Whose language it is in |

The role's own | Stored | The role's — a DBA's register says “unrestricted access to the customer table” |

The department's, seen from the role | Derived | The department's, with the parts that trace back to this role lit up |

The board's, seen from the role | Derived | The board's — “regulatory penalty, loss of licence, continuity failure” |

## Relevance fade, and why it teaches

The visualisation property that falls out of the fractal structure, and the most quietly powerful idea in this section. Centre a view on a role: that role's register is lit in full, and the registers above it fade — except for the entries that trace back down to this role, which stay lit.

“as you go up, imagine the colours can fade away for the next registers for the bits that are not relevant, so the graph starts to point which parts of the risk register above are relevant to this individual, so that he understands the picture.”

A database administrator can see that their local “an agent holds unrestricted access to a customer table” is the same object as the board's “regulatory penalty, loss of licence, continuity failure”. Seeing that once teaches more than any training course.

partially argued The visualisation is described and has not been built.

## One chain, not parallel lists

A late correction (2 August 2026) and a consequential one. Three altitude registers drawn side by side demonstrate a formatting capability. Drawn as one chain rooted in an existence fact, they demonstrate the entire thesis.

F1: an agent has write access to productiongives_rise_toL1: the operator's riskgives_rise_toL3: the CISO's riskgives_rise_toL5: the board's risk
The CISO's risk exists because of the operator's risk, which exists because of a fact. Side by side, that dependency is invisible; as a chain, it is the point.

“at the moment it looks like the cards, they look side by side, and it's actually not that.”

## Cascade, and the air gap

Every change to any risk, fact or piece of evidence must trigger a cascade that reaches the top. The absence of a cascade has a name:

“every time any risk, any fact, any evidence changes, you have to trigger a cascade that reaches the top. If you do not have that, you have an air gap, which means you do not have good data, and you cannot make good decisions.”

Air gap is used in two senses, and both are useful. A missing cascade is one. A risk that exists in the business but is not connected to the register at all is the other — and it is the more dangerous, because nothing about the register indicates it is there. A twin that is not connected to reality is a third instance of the same shape.

Cascade runs in both directions, which is easy to miss: a risk resolving propagates upward too, clearing it from the board's view. A register that only ever accumulates is as misleading as one that never updates.

Detecting air gaps is an acknowledged open problem. The principle is well developed and the detection mechanism is not specified — by construction it is hard, since an air gap is defined by the absence of a connection nobody recorded. The corpus states this rather than glossing it.

## The register as a story

The last idea in this section, and the one furthest from being built. The register is meant to be experienced rather than read: replay its change history through timestamps, commits or a series of queries, and watch the vulnerability appear, the risks propagate, a governance risk fire and resolve, the blast radius bloom, and everything settle into the board's consolidated view.

“I want to show this story played as a narrative, almost like a football commentator, this happens and then that happens, almost like a whodunit, like investigative journalism.”

The commit log is the script and the query advances the scene. partially argued — the mechanism is undecided in the source document. The nearest thing that exists is the Risk Mandate vault's 98 commits, which is the method applied to its own build and is a change history somebody could replay.

## Provenance

Concepts
C9 register as a graph of graphs · C10 fractal registers · C11 relevance fade · C12 one chain not parallel lists · C16 cascade and air gaps · C42 the narrative engine

Sources
briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__…graph-of-graphs…md · briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__…fractal-risk-registers…md · briefs/08/02/field-demo/v0.33.55__arch-brief__…registers-are-one-chain…md

First written
26 June 2026 · 17 July 2026 · 2 August 2026

Maturity
well-developed for the register, fractal structure and cascade · partially argued for relevance fade and the narrative engine

Licence
CC BY 4.0 at source and here

#### For an agent

The register (C9, C10, C11, C12, C16, C42). A risk register is a hyperlinked semantic graph, not a spreadsheet, and it begins at the vulnerability — where scanners stop — and maps confirming, owning, accepting, funding and staffing the fix. It is fractal: one register per accepting entity (company, department, role), of which only the role's own register is stored — the rest are queries. Relevance fade: centring a view on a role lights that role's register in full and fades the registers above it except for entries tracing back down, so a DBA can see their local exposure and the board's “regulatory penalty” are the same object. Registers are one chain, not parallel lists — the CISO's risk exists because of the operator's risk, which exists because of an existence fact; drawn side by side that dependency is invisible. Cascade: any change to any risk, fact or evidence must propagate to the top, in both directions (resolution clears the board's view too); a missing cascade, or a risk not connected to the register at all, is an air gap, and detecting air gaps is an acknowledged open problem. Not implemented in code; relevance fade and the narrative engine are not even specified.


==============================================================================
== /blast-radius/index.html
==============================================================================

