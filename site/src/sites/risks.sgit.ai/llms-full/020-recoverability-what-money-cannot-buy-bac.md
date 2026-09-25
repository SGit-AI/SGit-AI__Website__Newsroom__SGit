# Recoverability: what money cannot buy back

The fifth dimension of the plug profile, and the one that stops irreversible harm disappearing into an expected-loss calculation. Most risk arithmetic assumes that a sufficiently large number on one side can be balanced by a sufficiently large number on the other. Some harms are not on that scale at all.

“The money can be refunded; the customer cannot be un-declined.”

That line is from the Article 26(5) worked example, where an agent makes creditworthiness decisions. If it declines someone it should not have, a refund is available for any fee — and nothing is available for the decision itself, which was made, communicated, and acted on. The exposure is not large; it is permanent, which is a different axis.

## Why it is an axis and not a severity

| Reversible | Irreversible |

Large | A production outage. Expensive, visible, survivable — the organisation has done this before and has a playbook | Data leaves the boundary. No amount of money puts it back. This is the quadrant that should carry the most senior signature on the register |

Small | A failed job, a retried transaction. Absorbed without a decision | An unattributable transaction. Individually minor, permanently unfixable, and easy to accept by default precisely because it looks small |

The bottom-right cell is the one the model exists to surface. A small-but-permanent harm attracts no attention on a severity scale, gets accepted at a long interval by someone junior, and accumulates. A large-but-reversible one attracts a great deal of attention and is, in the end, a cost. Ranking them by size alone gets the priority exactly backwards.

## The flagship query

Show me every accepted risk whose recoverability is zero.

This is the single most useful thing the whole model can be asked, and the reason it matters is what the answer looks like in each case:

THE GOOD ANSWERA short, deliberate, senior-owned list. Every irreversible exposure the organisation carries is there, each with a name against it and a recent date. That organisation is in control of its worst exposure — not free of it, in control of it.

THE BAD ANSWERThe query cannot be run. Recoverability is not recorded, so the organisation is accepting its irreversible risks by default and by silence — which is the same state, minus the knowledge.

Note that a long list is not the failure mode. A long list is a finding, and an actionable one. The failure mode is a register that cannot produce a list at all, because nothing in it distinguishes what can be undone from what cannot.

## Can you compute your plug profile?

The corpus turns that into a maturity probe rather than a question, and it is deliberately unkind: an organisation that cannot answer who holds the plug, how fast, at what cost, and whether it can be undone for a given system has not established that it can stop the system at all — it has established that somebody believes it can.

The probe composes with the four-way time intersection: computing a profile requires knowing detection latency, decision availability, blast radius and reversibility as measured quantities. An organisation that can compute the profile has, by construction, measured all four. The plug-pull maturity model →

## What it points at

Recoverability is the dimension that redirects effort from response to prevention, and it does so with an argument rather than an exhortation. If a harm cannot be undone, then every control that reduces the chance of it is worth more than every capability that shortens the response to it — because the response, however fast, arrives after the irreversible part has happened.

That is also the honest reading of the detection floor. Where detection floors at twelve to eighteen hours and the harm is irreversible, response capability is close to worthless for that risk, and saying so plainly is more useful than promising a faster response nobody can deliver.

Open question, published unresolved. Q6 — is recoverability measurable, or only classifiable? The corpus splits reversible from irreversible cleanly and grades nothing in the middle. Most real harms are partially recoverable — a leaked dataset that was already partly public, a transaction reversible for thirty days and not after. Without a way to grade the middle, the dimension collapses into a binary that will be gamed by whoever gets to decide which side something falls on. Named, not solved.

## Provenance

Concept
C23 — recoverability as the hard limit

Source
briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__…what-money-cannot-buy-back-recoverability-the-hard-limit.md · …can-you-compute-your-plug-profile-the-maturity-probe.md

Repository
SGraph-AI__App__Send @ v0.33.51, never published — the version tag is the address

First written
24 July 2026

Maturity
well-developed — but the scoring of recoverability is an open question

Licence
CC BY 4.0 at source and here

#### For an agent

C23 — recoverability, the hard limit. Recoverability is an axis, not a severity: it stops irreversible harm being absorbed into an expected-loss calculation. “The money can be refunded; the customer cannot be un-declined.” Crossing it with size gives four cells, and the important one is small-but-permanent — individually minor, permanently unfixable, and easy to accept by default at a long interval precisely because it looks small. Ranking by size alone inverts the correct priority. The flagship query of the whole model: “show me every accepted risk whose recoverability is zero.” A short, deliberate, senior-owned list means the organisation is in control of its worst exposure; a long list is a finding; an unrunnable query is the failure, because it means irreversible risks are being accepted by default and by silence. Recoverability redirects effort from response to prevention with an argument rather than an exhortation: where harm cannot be undone and detection floors at 12–18 hours, response capability is close to worthless for that risk. Open question Q6: recoverability is currently binary — nothing grades the partially-recoverable middle. Not implemented in code.


==============================================================================
== /practice/index.html
==============================================================================

