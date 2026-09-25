# The plug register

The five-dimension profile applied to a real seven-row register. It is the worked proof of the “no plug” correction — every row that an earlier version recorded as having no off-switch turns out to have one, and what was actually missing was recoverability.

## Seven rows, five dimensions

The risk | Who holds the plug | Blast radius | Speed | Recoverability |

Agent misuses the isolated session | IT | Small | Fast | high |

Agent exceeds its granted scope | IT / platform | Small to medium | Fast | high |

Agent consumes budget faster than detection | Platform / finance | Medium | Bounded below by detection — 12–18h | medium |

Agent misuses the platform itself | COO / procurement | Large | Slow — contractual | medium |

Agent action is attributed to the wrong principal | Platform / identity | Medium | Medium | medium |

Data leaves the boundary | Platform, then nobody | Large | Fast to stop, irrelevant after | zero |

Unattributable transaction | Finance, then nobody | Small each, unbounded in aggregate | Fast to stop | zero |

Governance residual | The board | Enterprise | Slowest | lowest |

Side effects, the fourth dimension, are omitted from the table for width and are the reason several of these plugs exist and are not pulled. The register carries them per row.

## What the correction changed

Read the last two dimensions of the two zero-recoverability rows together and the correction becomes obvious. Both are fast to stop. Neither is possible to undo. An earlier register recorded both as “no plug”, which was wrong on the facts and useless in practice:

The blank: “no plug” | The corrected profile |

Not true — you can always disconnect, revoke or shut down |
States who can stop it and how fast, both of which are real and useful |

Unassignable. A blank has no owner |
Has an owner, an altitude and an interval like any other finding |

Unfundable. There is no project that fixes “no” |
Points straight at prevention, because that is what a zero-recoverability row implies |

Ends the conversation |
Escalates it — a recoverability of zero argues for the most senior signature available |

“The blank said stop looking. The corrected profile says here is exactly what to do.”

## Three things this register shows that prose does not

- Speed is not one number. Two rows are “fast” and two are slow for entirely different reasons — one is bounded below by the detection floor, and one by a contract. A plug that requires a supplier's notice period is not a plug you hold.

- The plug moves up the organisation as the blast radius grows. IT holds the small ones; procurement holds the platform; the board holds the residual. That is altitude visible in a single column.

- “Then nobody.” Two rows list a holder and a point past which nobody holds anything. That is the honest way to write a zero-recoverability row, and it is what a single yes/no column cannot express.

## Running the flagship query against it

Show me every accepted risk whose recoverability is zero. — Two rows. Data leaves the boundary. Unattributable transaction.

Two is a good answer. It is short, it is specific, and both entries are things a board can be asked to sign for. The failure mode would be a register that could not produce the list at all — which is what a register without a recoverability dimension is. The flagship query →

## Provenance

Source
briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__…a-real-plug-register-the-worked-proof-five-dimension-profile.md

Repository
SGraph-AI__App__Send @ v0.33.51 — one of 13 documents in the same folder

First written
24 July 2026

Scenario status
Preserved from the source: a product deployment example, shortened and illustrative — not any customer's register. No vendor is named

Licence
CC BY 4.0 at source and here

#### For an agent

The plug register — the worked proof of the five-dimension profile. Seven rows, each carrying who holds the plug · blast radius · speed · side effects · recoverability. Spans from “agent misuses the isolated session” (IT · small · fast · high recoverability) through “agent consumes budget faster than detection” (speed bounded below by the 12–18h detection floor) and “agent misuses the platform itself” (COO/procurement · large · slow, contractual · medium) to two rows at recoverability: zero — data leaves the boundary and unattributable transaction — and finally “governance residual” (the board · enterprise · slowest · lowest). Both zero-recoverability rows are fast to stop and impossible to undo, which is exactly the “no plug” correction: an older register recorded them as having no off-switch, which was false on the facts and unassignable in practice. The corrected profile has an owner, an altitude and an interval, and points at prevention. Note that speed has more than one kind of bound — one row is bounded by detection latency, another by a supplier's contractual notice period; a plug requiring a notice period is not a plug you hold. Running the flagship query against this register returns two rows. Illustrative product example; no customer's register and no vendor named.


==============================================================================
== /concepts/index.html
==============================================================================

