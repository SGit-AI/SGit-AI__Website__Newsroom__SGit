# Blast radius and authorization closure

An agent's real authorization is the transitive union of everything reachable from what it was given — not the nominal grant. The gap between those two is where the exposure lives, and computing it turns “what could this thing do?” from a question people answer with intuition into one a query answers with a number.

## Authorization closure

The mandate states what an agent is authorised to reach. The authorization closure states what it can reach — computed, not asserted, and not a record of what it did.

Three things are being kept apart, and conflating any two of them is the usual mistake:

Quantity | What it is | How you get it |

The grant | What was explicitly given — the role, the token, the scope | Read it off the configuration |

The closure | Everything transitively reachable from the grant | Compute it. Walk the graph until it stops expanding |

The activity log | What it actually did | Read the logs — and note that this is the smallest of the three, and the one people usually look at |

AuthorizationClosure is a first-class node type in the AWS IAM ontology — 6 layers, ~31 node types, 20 edge types (40 readings counting inverses) and 7 node type formulas — where it is defined as the agentic union of the possible. How formulas scale →

## Two awareness gaps hide the delta

GAP 1 · THE GRANTER DOES NOT KNOW THE SCOPE OF WHAT THEY GRANTGranting inbox access feels like granting access to email. It is access to every account whose password can be reset by email — which is most of them. The granter is not careless; the scope is genuinely not visible at the moment of granting.

GAP 2 · THE DELEGATOR NEVER AUTHORISED RE-DELEGATIONThe person who gave the agent a credential did not agree that the agent could hand its reach to a sub-agent, a tool or a scheduled job. Nothing in the grant said it could not, either.

The key quantity is the delta between expected and unexpected permissions — not the size of the closure, but the size of the part nobody meant to give.

## Three examples that land immediately

What was granted | What the closure contains |

Access to an inbox | Every account resettable by email — which is a large fraction of everything the person can log into |

Access to a desktop | Every stored credential, every logged-in session, every saved token, every VPN profile |

The ability to execute code | Whatever that code can escalate to — frequently admin, and always more than the grant named |

These are not exotic attack paths. They are the ordinary consequences of a grant, visible to anyone who works the transitive closure by hand — which is precisely why the corpus's insistence that it be computed matters. Hand-working it does not scale past one example, and the anti-pattern it replaces has a name in the source: hope-driven development.

“at the end of the day you are still accountable for those actions, all the way to the board.”

## CIA expansion: where most registers stop is where this one starts

From a single risk, expand along three axes. Each branch spawns its own risks, and each of those follows the full confirm-accept-propagate loop with its own owner and its own interval.

C

### Confidentiality

A leak becomes a regulatory exposure, and the regulatory exposure splits into two distinct risks with different owners: the CFO's, for the fine, and the CEO's, for the compliance failure. And note the sharper reading — inadequate protection may already be a breach, before any data has moved.

I

### Integrity

Salary tampering, fabricated hires, altered performance data. The under-modelled axis, because it produces no alert — nothing is missing, the numbers are just wrong, and they stay wrong until something downstream fails to reconcile.

A

### Availability

Backup cadence gaps, and the question that reliably produces the worst answer in the room: when was a restore last tested? That question is where the grounding-ladder worked example starts, and the honest answer is usually a documented zero.

The tension the source records about its own method. The expansion must be curated, not exhaustive, or it blows up combinatorially: every risk branches into three, each of those into three, and within four levels the register is unreadable and useless. The corpus names this as an unresolved tension rather than claiming the expansion is safe to automate — and it sits directly against the register-density argument, which says a complex product should carry thousands of risks. Both are in the corpus; neither resolves the other.

## Data classification is the multiplier

The same vulnerability against two datasets is two very different risks, and the register needs the classification node to say so. From the 2FA worked example:

Class | Contents | Effect on the blast radius |

DC-1 | Full HR data — passports, salaries, bonuses, PIPs, reviews, hires, fires, dismissals | Regulatory, financial and reputational, in every direction at once |

DC-2 | Anonymised timesheets | Materially smaller in every dimension |

## Observability is the other half of the picture

Capability maps the privilege; observability maps the real impact. Six objective vectors on a maturity scale: capture granularity, log latency, time-to-damage given real throughput limits, whether monitoring is actually on and watched, whether there is a team with playbooks, and whether detection has ever been drilled.

A loud, detectable, slowly-scaling, well-drilled risk is lower than a quiet, fast, unwatched one of the same capability.

Later sharpened into plug-loaded observability — logs that tell you where you are in the stopping decision, rather than generic logging that tells you what happened after you no longer need to know. That connects this page directly to the detection floor: a hyperscaler cost-reporting delay of 12–18 hours is a hard limit on how fast anyone can know, whatever the logging maturity.

## Provenance

Concepts
C19 blast radius / authorization closure · C18 CIA expansion · C39 observability as a risk dimension

Sources
briefs/07/02/authorization-and-maturity-model/v0.33.40__arch-brief__…agent-authorization-union-of-possible…md · briefs/07/05/aws-configuration-risk-engine/v0.33.44__arch-brief__…aws-iam-config-risk-ontology…md · briefs/06/22/how-and-why-and-authorization/v0.33.32__arch-brief__observability-as-a-risk-dimension…md

First written
“blast radius” from 12 February 2026; formalised as closure 2 July 2026; observability 22 June 2026

Maturity
well-developed — and newcomer-followable: the inbox example lands instantly

Licence
CC BY 4.0 at source and here

#### For an agent

C19, C18, C39 — blast radius. Keep three quantities apart: the grant (what was explicitly given, read from config), the authorization closure (everything transitively reachable from the grant — computed, and a first-class node type), and the activity log (what it actually did — the smallest of the three, and the one people look at). Two awareness gaps hide the delta: the granter does not know the full scope of what they grant (inbox access is access to every email-resettable account; desktop access is every stored credential and live session; code execution escalates), and the original delegator never authorised re-delegation to sub-agents or tools. The key quantity is the delta between expected and unexpected permissions, not the raw size of the closure. CIA expansion: each risk branches into confidentiality (a leak splits into two distinct risks — the CFO's fine and the CEO's compliance failure — and inadequate protection may already be a breach), integrity (tampering, which produces no alert) and availability (“when was a restore last tested?”). The expansion must be curated, not exhaustive, or it explodes combinatorially — the corpus records this as unresolved. Observability maps real impact where capability maps privilege: a loud, detectable, slow, well-drilled risk is lower than a quiet, fast, unwatched one of the same capability. Not implemented in code.


==============================================================================
== /plug/index.html
==============================================================================

