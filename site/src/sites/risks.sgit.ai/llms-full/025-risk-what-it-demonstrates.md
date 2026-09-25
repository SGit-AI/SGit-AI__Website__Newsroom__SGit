# | Risk | What it demonstrates |

R1 | Accounts compromised | The obvious one, and the only one most registers would carry |

R2 | The governance air gap — the risk is accepted by the wrong owner | The canonical failure, modelled as a risk rather than corrected silently. See below |

R3 | Unauthorised HR admin access | The interval resolution worked in full — see below |

R4 | The risk is mis-classified until investigated | Spawned by fact F5, which lacks evidence. Not knowing is a fact, generating a risk of its own |

R5 | A data incident | Distinct from R6, deliberately |

R6 | A GDPR breach | Two distinct risks, not one. Different owners, different consequences, different intervals — the CFO carries the fine, the CEO the compliance failure |

R7 | Salary or record tampering, or fabricated hires | The integrity branch, which produces no alert and no missing data |

R8 | The weekly-backup data-loss window | Availability. Backed by E4: backup logs show weekly |

R9 | The restore has never been tested | Backed by E5: no record of a tested restore — a documented zero, which is a measurement |

## R2: the governance air gap

The most instructive row in the graph, and the reason this example keeps being cited. IT validates that admin accounts lack a second factor — which is correct, and within IT's competence. IT then accepts the risk, which is not.

IT validating a 2FA gap is not IT accepting an HR data-breach exposure. The technical owner confirms; the business owner underwrites. →

The model's response is not to reject the acceptance but to make the misplacement a risk: R2 exists, is rated, and needs an owner. It is accepted by the Head of GRC at a four-hour interval — a P1 — and propagates GRC → CIO → CEO → Board, each accepting at four hours because that is the only option open to them.

The 4h-for-everyone problem, carried as a loose end. Every altitude in that chain selects the same rung, not because four hours is right for each of them but because it is the only rung available once the one below is struck off. Either the ladder needs a per-altitude variant, or that uniformity is itself a finding about the model. The corpus does not settle it. The ladder →

## Interval resolution for R3

What the ladder looks like when applied to a specific risk rather than described in general:

Rung | Resolution | Why |

4 hours | Struck off | Not technically possible in the window — no authority or budget buys it |

48 hours | P1 | The shortest deliverable response |

2 weeks | Incident | A lower grade of the same thing |

1–2 months | A funded project | Assemble and fund |

6 months | Do nothing, and say so | Costs zero. Legitimate with a name on it |

Three pieces of evidence do real work in that resolution. E3 — “no evidence of compromise” — backs the absence of clear and present danger, which is what makes anything longer than four hours defensible at all. E4 establishes the backup cadence. E5 is the documented zero on tested restores.

## Data classification as the blast-radius multiplier

The same vulnerability against two datasets is two different risks, and the graph carries the classification as a node so it can say so:

Class | Contents | Effect |

DC-1 | Full HR data — passports, salaries, bonuses, PIPs, performance reviews, hires, fires, dismissals | Regulatory, financial and reputational simultaneously. The reason R5 and R6 are separate |

DC-2 | Anonymised timesheets | Materially smaller in every dimension. Same vulnerability, different risk |

## The ontology this instance runs on

24 node classes and 34 edge types, including Acceptance and Interval as node classes in their own right, with edges accepted_by, has_interval, propagates_to, underwritten_by and overrides. This is where acceptance stops being a field and becomes a node — 26 June 2026, the first of four progressive formalisations.

The data file is not mirrored here yet. The instance graph exists as a JSON data file in the source repository (briefs/06/26/semantic-graph-and-query-paths/v0.33.35__data__sg-send-2fa-mappings.json), it declares its own principles inline, and it carries a CC BY 4.0 line — it is the only directly downloadable graph in the corpus. Publishing it at a stable path on this site is task T5, open. This page describes it from the brief pack's counts rather than reproducing a file it does not have; a reconstructed graph presented as the original would be worse than a missing one.

## Provenance

Source
briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__…md · briefs/06/26/semantic-graph-and-query-paths/v0.33.35__arch-brief__…2fa-use-case…md · …v0.33.35__data__sg-send-2fa-mappings.json

Repository
SGraph-AI__App__Send @ v0.33.35

First written
26 June 2026

Scenario status
The organisation and its roles are generic and invented. Role titles (IT Director, Head of GRC, CIO, CFO, CEO) carry no reference to any real person

Licence
CC BY 4.0 at source and here; the data file carries its own CC BY 4.0 line inline

#### For an agent

The 2FA instance graph — the founding worked example. 51 nodes, 53 edges; ontology of 24 node classes and 34 edge types including Acceptance and Interval as node classes with edges accepted_by, has_interval, propagates_to, underwritten_by, overrides. Chain: E1 (config shows no MFA) backs the fact that admin accounts lack 2FA → V1 → ATK-1 credential stuffing, MITRE T1110.004, performed by TA-1. Nine risks R1–R9 from one vulnerability. R2 is the canonical governance air gap: the risk is accepted by the wrong owner (IT validating a 2FA gap is not IT accepting an HR data-breach exposure) — modelled as a risk in its own right, accepted by Head of GRC at 4h and propagating GRC → CIO → CEO → Board, each accepting at 4h because it is the only option open to them (an unresolved finding about the ladder). R4 is spawned by fact F5, which lacks evidence. R5 and R6 are two distinct risks (data incident vs GDPR breach), not one. R3's interval resolution strikes 4h off as not technically possible, leaving 48h/2w/1–2m/6m. Data classification multiplies the blast radius: DC-1 full HR data vs DC-2 anonymised timesheets. The organisation and all role titles are invented.


==============================================================================
== /examples/browser-isolation.html
==============================================================================

