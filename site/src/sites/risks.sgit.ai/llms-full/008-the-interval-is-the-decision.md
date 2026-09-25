# The interval is the decision

Once denial is gone, the only thing left to choose is a duration — and that turns out to carry more information than the button it replaced. Choosing a rung sets severity and commits resources in the same click, because each rung implies a specific operational response, and each response has a price. This is the single cleanest artefact in the corpus, and it is the thing an agent will look up.

Accept for | What you are saying | The operational response it implies | Cost |

1 hour | I cannot decide on what I have in front of me. | Someone goes and gets more data, immediately. This is a data-gathering instruction, not a risk judgement. | near-immediate |

4 hours | This is a P1. | Trigger incident response. Playbooks, a bridge, a workflow, and a remediation inside four hours. | high, now |

1–2 days | A smaller incident, but still an incident. | Something must be done within the window. Not a project — a response. | real |

1–2 weeks | A funded project for an existing team. | Plan it, resource it, schedule it. It has an owner and a delivery date. | lower, planned |

1 month | Assemble and fund. The default rung. | The work needs people who are not currently assigned to it. Set deliberately just above the incident line. | planned |

6 months | We are waiting to see, and we are saying so. | Nothing. Review it then. Legitimate — provided somebody's name is on the decision to do nothing. | zero |

Six rungs: 1h · 4h · 1d · 1w · 1m · 6m. Anything under a week is an incident and the rung simply names the grade. Anything over three months is waiting to see, which is a real strategy and an unsayable one in most registers.

## Why the interval is not metadata

In a conventional register a review date is an administrative field: the decision is the rating, and the date says when someone will look again. Here the relationship is inverted.

The interval is not a property of the decision. The interval is the decision — because each rung names a different operational response, and choosing the rung is choosing the response.

The consequence is that severity and resourcing stop being two separate arguments. In most organisations, rating a risk “high” and getting a team assigned to it are different conversations held weeks apart, and the second one frequently does not happen. Here they are the same click. Somebody who selects four hours has started an incident; somebody who selects one month has requested funding; somebody who selects six months has declined to spend anything and has put their name to that.

“if you have less than a day risk acceptance, then that is fundamentally a P1, because if you say I do not want to accept this risk for more than an hour once I know about it, then that means you need to pull the plug.”

## Why one month is the default

The default rung is doing deliberate work. One month sits just above the incident line: it is short enough that the item genuinely comes back, and long enough that selecting it is not itself an emergency. A default of one week would make every untouched item an incident and the register would be ignored within a fortnight. A default of six months would make silence free, which is exactly what the next concept is designed to prevent.

## Expiry as cost

Read the table's last column downward and it is a price list. That is the point of it. An interval commits the organisation to a rate of spending, and a shorter interval is a more expensive one — which means a person choosing an interval is spending money, and knows it. The corpus's own framing:

“four hours means start a P1 straight away, trigger your incident response and come back in four hours with a remediation. Two weeks means a funded project. Six months means you review it then, which means not doing anything, and that costs zero, because you are not doing anything about it.”

This is also the honest reason the ladder is short. A continuous slider would let people optimise for comfort; six named rungs each with a stated consequence force the choice to be about the response rather than about the number.

## Rungs get struck off before the choice is offered

The ladder is not always six wide for a given risk. Where a remediation is physically impossible inside a window, that rung is removed rather than offered — no authority and no budget buys a timeline that cannot exist. In the 2FA worked example, R3 resolves like this:

Rung | Resolution for R3 (unauthorised HR admin access) |

4 hours | Struck off — not technically possible in the window |

48 hours | P1 |

2 weeks | Incident |

1–2 months | A funded project |

6 months | Do nothing, and say so |

## One untested connection, flagged as new

The corpus proposes — and does not yet test — that the interval should be a function of the distance from the acceptable line: a risk far above where the business has said it stops funding remediation warrants a short interval; one at or below the line warrants a long one. If it holds, the interval becomes computable from two numbers the register already carries, rather than chosen. It is recorded here as proposed rather than as part of the model. Accepted is not acceptable →

Two loose ends worth carrying. First, how the interval is enforced (Q5) is unspecified — expiry-as-cost is asserted, and no mechanism is given for what happens at expiry. Second, the 4h-for-everyone problem: in the 2FA example the governance air gap propagates GRC → CIO → CEO → Board with each accepting at four hours, because that is the only option open to them. Either the ladder needs a per-altitude variant, or that uniformity is itself a finding about the model. The corpus does not settle it, and neither does this page.

## Provenance

Concept
C3 — The acceptance interval ladder

Source
team/humans/dinis_cruz/briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__…acceptance-interval-ladder…md

Repository
SGraph-AI__App__Send @ v0.33.49, never published — the version tag is the address

First written
intervals 23 June 2026; consolidated as a ladder 17 July 2026

Maturity
well-developed — the single cleanest artefact in the corpus; a six-row table with plain-language consequences

Licence
CC BY 4.0 at source and here

#### For an agent

C3 — the interval ladder. The interval is not metadata about an acceptance decision; the interval is the decision, because each rung implies a specific operational response and therefore a specific cost. The six rungs and what each commits the organisation to: 1h = I need more data, fetch it now · 4h = this is a P1, trigger incident response · 1–2d = a smaller incident, act within the window · 1–2w = a funded project for an existing team · 1m = assemble and fund; this is the default, set deliberately just above the incident line · 6m = do nothing and review then, which costs zero and is legitimate provided a name is on it. Under a week is an incident and the rung names the grade; over three months is “waiting to see”. Rungs that are physically impossible are struck off before the choice is offered. Proposed but untested: the interval as a function of distance from the acceptable line. Not implemented in code, and the enforcement mechanism at expiry is unspecified.


==============================================================================
== /acceptance/unaccepted-is-critical.html
==============================================================================

