# Who can pull the plug

Two symmetric risks, and most organisations have only noticed the first. If nobody holds the mandate to stop an AI system, that is one risk. If the system cannot be stopped even when someone decides to, that is a second and different one — an authority gap versus a capability gap. The second is widely underestimated, and the four capabilities that have to line up to close it must line up inside the same window.

“if you do not have somebody who has the mandate to pull the plug, you have a risk, and if you do not have a system that can be pulled the plug, you have a risk too.”

## The authority gap decomposes into timed sub-risks

“Can we stop it?” is not answerable as a yes or no. It decomposes into a set of dated questions, which is what turns governance into an on-call availability problem:

- Can it be stopped in an hour? In ten hours? In a day? In five days?

- Only during office hours, or at three on a Sunday morning?

- Can the person who holds the switch act without fear of losing their job?

- Is there a clear escalation path when the first person cannot be reached?

That third one is not a soft consideration. A stop button that only a person risking their career will press is, operationally, a stop button that does not exist at three in the morning.

## The four-way time intersection

Four capabilities must line up inside the same window. A gap in any one breaks the whole thing, which is why they are drawn intersecting rather than listed.

1 · detectionHow fast you knowAnd under which scenarios — a curve, not a binary. Some failures announce themselves; others are visible only in a billing line.

2 · decisionWhether the authorised people can be assembledIn time, with the standing to act, and with enough information to act on.

3 · blast radiusHow fast the damage scalesModels execute and scale fast, especially when connected. A steep cost curve, not a linear one.

4 · reversibilityWhether you can put it backStopping is only half the act. Reverting requires journaling and backups that were in place beforehand.

“it is not just pulling the plug, it is pulling the plug and reverting the changes.”

The danger case is specific and worth naming: a steep cost curve where an affordable window of one or two days of damage collides with a decision that cannot be made in one or two days. The organisation can afford the damage and cannot afford the delay, and nobody notices until the two are measured against each other.

## The detection floor is a hard number

Figure | What it means |

12–18 hours | Hyperscaler cost-reporting delay. For any failure that surfaces first as spend, this is a floor on how fast anyone can know — no logging maturity beats it |

16 hours | The founder's own AWS figure: “AWS usually takes 16 hours to give you the data, so how much damage can be done in 16 hours.” |

up to 24 hours | The billing-lag damage window recorded against the cost blast radius |

Numbers like these are what make the intersection concrete. If detection floors at twelve hours and the blast radius is steep, then no amount of decision-making authority helps — the exposure is already realised before the decision is available to be made. That is an argument for prevention, and it is the honest one. Observability as a risk dimension →

## The correction: the plug always exists

This is the pillar correction of the whole series, and it is the reason the page is called who can pull the plug rather than whether there is one.

The plug always exists. You can always disconnect, revoke, or shut down. What earlier registers recorded as “no plug” was never a missing off-switch — it was zero recoverability.

A data breach has a plug: you can cut the connection. A used credential has a plug: you can revoke it. What neither has is a way back — the data is out, the foothold was used. Recording that as “no plug” conflates two very different findings and produces a blank in the register.

“The blank said stop looking. The corrected profile says here is exactly what to do.”

The restatement is not cosmetic. A blank is unassignable and unfundable. A finding that reads “stoppable in minutes by the platform team, blast radius large, side effects severe, recoverability zero” points straight at prevention and at the most senior acceptance — and can be given an owner and an interval like anything else. Recoverability, the hard limit →

⚠️ A live inconsistency, stated rather than tidied. The corpus records this correction. The published page it moved from does not reflect it. One of the two is wrong, and until the source is reconciled this site publishes the corrected version and says so. This is open ask N1.

## The five-dimension plug profile

What replaces a yes/no answer. Every stoppable thing gets a profile with five dimensions, and the profile is the finding:

dimension 1Who holds itWhich role can actually pull it — and at which altitude. The answer changes at every level of the organisation.

dimension 2Blast radiusWhat else stops when this stops. The plug is a sledgehammer, and pulling it has its own risks.

dimension 3SpeedHow fast, in the worst realistic case, not the demo case. Minutes, hours, or a contractual notice period.

dimension 4Side effectsWhat breaks, who is affected, and what the organisation loses by stopping — the reason a plug that exists sometimes does not get pulled.

dimension 5RecoverabilityThe dimension money cannot buy back. The one that separates catastrophic-but-reversible from smaller-and-permanent. →

The seven-row worked plug register → — from “agent misuses the isolated session” (IT · small · fast · high recoverability) through “agent misuses the platform itself” (COO/procurement · large · slow and contractual · medium) to “data leaves the boundary” and “unattributable transaction”, both at recoverability: zero.

## The plug is a sledgehammer

The symmetric risk on the other side, and easy to forget once you have spent a page arguing that a plug is necessary. Pulling it has a blast radius of its own: stopping the agent stops the work the agent was doing, and everything downstream of that work. A plug that takes out a production dependency may be more expensive than the exposure it was pulled to stop.

That is why side effects is a dimension of the profile rather than an afterthought, and why the decision half of the four-way intersection needs information rather than just authority: the person with the switch has to know what else goes dark.

## Article 14 as the plug obligation

One of this site's three narrow declared bridges into the EU AI Act. Article 14 requires human oversight of high-risk systems, including the ability to intervene and to stop — which makes the plug profile the natural evidence artefact for demonstrating it. Not a compliance product, and not a claim beyond what the provision says: an obligation to be able to stop, met by a register that records who can, how fast, at what cost, and whether it can be undone.

Legal points on this site are factual and are not legal advice. Provisions are cited from the Regulation Graph vault. Why bridges rather than merges →

The boundary this site will not cross. The model rates the ability to stop; it does not provide it. The corpus states the refusal directly and notes what it costs: “a customer who scores badly will ask us to supply the stop button, which is exactly the enforcement role the corpus refuses.” In-line enforcement belongs to sg-sentinel.sgit.ai. We measure and evidence; we never sit in-line. The boundary map →

## Provenance

Concepts
C20 two symmetric risks · C21 the four-way time intersection · C22 the five-dimension profile and the “no plug” correction · C39 the plug is a sledgehammer

Moved from
https://riskmandate.ai/plug.html · moved 22 August 2026 · ⚠️ republished with the “no plug” correction the source page does not carry

Source
briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__…detection-authority-blast-radius-reversibility-intersect-in-time.md — the load-bearing brief, with 12 companion pieces in the same folder

First written
24 July 2026 (the phrase appears from 17 February 2026 in another sense)

Maturity
well-developed — a 13-document series, and newcomer-followable, outstandingly so

Licence
CC BY 4.0 at source and here

#### For an agent

C20–C22 — the plug. Two symmetric risks: nobody holds the mandate to stop the system (an authority gap), and the system cannot be stopped even when someone decides to (a capability gap). The second is widely underestimated. The authority gap decomposes into timed sub-risks — stoppable in an hour, ten hours, a day, five days; office hours only; can the holder act without fear of losing their job; is there an escalation path. Four capabilities must line up inside the same window: detection (a curve, not a binary), decision (assembling authorised people in time), blast radius (models scale fast — a steep cost curve), reversibility (“it is not just pulling the plug, it is pulling the plug and reverting the changes”). Hard detection floor: 12–18 hours of hyperscaler cost-reporting delay for anything that surfaces as spend. The pillar correction: the plug ALWAYS exists — you can always disconnect, revoke or shut down. What older registers recorded as “no plug” was zero recoverability, and restating it that way turns an unassignable blank into an ownable finding. Every stoppable thing gets a five-dimension profile: who holds it · blast radius · speed · side effects · recoverability. Pulling the plug is itself a risk (side effects). Boundary: this model rates the ability to stop and never provides it — in-line enforcement is sg-sentinel's. Not implemented in code.


==============================================================================
== /plug/recoverability.html
==============================================================================

