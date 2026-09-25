# Unaccepted is rated critical

The sharpest inversion of incentives in the model. In most organisations, a risk nobody escalated feels like the safest thing on the desk. Here it is the worst state available — because the exposure has not gone away, it has come to rest on whoever is nearest, and that person is now personally carrying an enterprise risk with no signature above them.

“any risk that has not been accepted immediately goes into that one's risk dashboard, because that is a massive risk, that means that that person right now is accountable for the business, which is very bad from a business point of view, but is also very bad for the individual.”

## A risk that nobody accepted has not gone anywhere

This is the observation the rule is built on, and it is a statement about reality rather than about process. Exposures do not wait to be assigned. If an over-permissioned agent can reach the production database, that is true at three in the morning whether or not anyone has looked at the register. The only question is who is carrying it in the meantime — and the answer is always the same: whoever is nearest to it.

An un-underwritten risk has not vanished. It has come to rest, silently, on the person closest to the system — usually the person with the least authority to do anything about it.

So “unaccepted” is not a null state. It is a state in which the risk is being carried by someone who never agreed to carry it, at an altitude far below the one where the consequence would land. Rating it critical is not a scoring convention; it is an accurate description of what is happening.

## Escalation without an escalator

The elegant consequence: nobody has to decide to escalate. If an item is unaccepted, it is critical; critical items roll up; therefore the item appears at the next altitude by default, and the one above that, until somebody signs. No meeting, no judgement call, no career calculation about whether to raise it.

“R3 appears on the chief financial officer's register as an unowned critical item, and it got there without anybody escalating it deliberately. That is the mechanism working: not doing something is a measurable action.”
— demonstrated on live data, the Article 26(5) worked example, 2 August 2026

That last clause is the whole idea in six words. In a conventional register, inaction is invisible — it produces no record, and its absence is indistinguishable from an item that was considered and correctly left alone. Here inaction produces a state, the state has a rating, and the rating has a destination.

## It is aimed at attrition, not refusal

The failure mode a register actually dies of is not open refusal — it is attrition. People stop responding. Items sit. Reviews slip. Nobody says no; nobody says anything. And attrition works precisely because non-participation is deniable: I never saw it, it was never assigned to me, nobody asked.

The roll-up removes the deniability that attrition depends on — without requiring anyone to cooperate.

That is why it composes with the no-deny mechanic rather than merely sitting beside it. No-deny closes the exit marked “no”. Unaccepted-equals-critical closes the exit marked silence. Between them, an item that enters the register leaves as a funded action, a scheduled review, or a dated signature — including a signature on doing nothing.

## The pressure runs both ways, deliberately

It would be easy to read this as a mechanism for pushing work upward. It is at least as much a mechanism for protecting the person at the bottom. The sentence in the source document names both halves: an unaccepted risk is “very bad from a business point of view, but is also very bad for the individual.”

An engineer who can see an exposure and cannot get anyone to own it is, today, in the worst position in the organisation: accountable in practice, powerless in fact, and with no record that they raised it. The roll-up gives them a mechanism rather than a memo. Do not internalise the risk →

## What it looks like on live data

Two of the worked examples show the mechanic running rather than asserted:

Example | What it demonstrates |

Article 26(5) | Three decisions recorded, and one deliberately absent (D3). The risk with no decision against it surfaces on the CFO's register as an unowned critical item, with no human having escalated it. |

Agentic Browser Isolation live vault | Acceptance-gated escalation across five altitudes — L1 IT through to L5 board — with no deny button, running over roughly 70 JSON files. This is C2 and C4 as behaviour rather than as prose. |

The open question this raises, published unresolved. Q4 — does “unaccepted = critical” survive contact with a large estate? On a register of thousands of items, if everything unaccepted is critical then “critical” may stop meaning anything, and the roll-up delivers an unreadable list to an executive who then ignores all of it. The corpus circles this through the register-density argument — that a complex product should have dozens to thousands of interconnected risks — without resolving the tension between the two. It is on the site as an open question rather than smoothed away.

## Provenance

Concept
C4 — Unaccepted equals critical (escalation without an escalator)

Source
team/humans/dinis_cruz/briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__…acceptance-interval-ladder…md

Repository
SGraph-AI__App__Send @ v0.33.49, never published — the version tag is the address

First written
17 July 2026; worked end-to-end on live data 2 August 2026

Maturity
well-developed — and demonstrated, not only argued

Licence
CC BY 4.0 at source and here

#### For an agent

C4 — unaccepted equals critical. Treat the absence of an acceptance as a state, not as a null. A risk nobody has underwritten has not gone away: it rests on whoever is nearest the system, who is carrying an enterprise exposure with no signature above them. So an unaccepted risk is rated critical by default, appears immediately on the holder's own dashboard, and rolls upward without anyone choosing to escalate it — “not doing something is a measurable action”. This is aimed at attrition rather than at refusal: it removes the deniability that non-participation depends on, without requiring anyone to cooperate. It pairs with C2: no-deny closes the exit marked “no”, and this closes the exit marked silence. Open question Q4: whether it survives a register of thousands, where everything-critical may mean nothing-critical. Not implemented in code, though it is demonstrated on live data in the Agentic Browser Isolation vault.


==============================================================================
== /acceptance/workflow.html
==============================================================================

