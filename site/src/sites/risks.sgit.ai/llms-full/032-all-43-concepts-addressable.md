# All 43 concepts, addressable

Every concept in the corpus, each with a stable anchor, a one-line definition, its maturity stated honestly, its canonical source path, and the page that argues it. The anchors are a promise: #c1 through #c43 are checked by CI, and a link to a concept that has no anchor fails the build. The same 43 entries are available as structured data at /data/concepts.json.

C1C2C3C4C5C6C7C8C9C10C11C12C13C14C15C16C17C18C19C20C21C22C23C24C25C26C27C28C29C30C31C32C33C34C35C36C37C38C39C40C41C42C43

Reading order for an agent with no prior context: C1 → C2 → C3 → C4 → C5 (the acceptance model) → C6 → C7 (the ontology that makes it computable) → C19 → C20–C23 (blast radius and the plug) → everything else.

Maturity is stated honestly, and it means what it says. well-developed means the argument is complete and worked; partially argued means a mechanism is missing or the source says so itself; newly stated means it appeared late and has not been stress-tested. None of it means implemented — nothing in this corpus is implemented in code. /shipped/.

Provenance is stated too, and it is a separate axis. from the corpus means the concept was drawn from the ~496,000 words this site consolidates. authored on this site means it was written here and has no upstream source — currently one concept, C43. A research site that consolidates a corpus and quietly adds to it is no longer reporting the corpus, so the two are kept apart in the data as well as on the page.

## The seven teaching altitudes

The corpus is not organised as a list; it has an order, and the order is an argument. Each altitude assumes the one before it. The seventh was added by the execution-boundary example and is the only one not drawn from the source material.

Altitude | What it covers | Concepts |

1 · The inversion
acceptance/index.html | The founding move and its three immediate consequences. Read these four first, in order — each is forced by the one before it. | C1 · C2 · C3 · C4 |

2 · The vocabulary
acceptable/index.html | What the words mean once the inversion has happened, and where a register lives. | C5 · C25 · C9 · C10 · C11 |

3 · The machinery
ladder/index.html | What makes it computable. This is the altitude an agent most needs. | C6 · C7 · C8 · C17 · C33 |

4 · The exposure
plug/index.html | What the machinery is pointed at: what an agent can reach, and what it costs to stop it. | C19 · C18 · C20 · C21 · C22 · C23 |

5 · The organisation
practice/index.html | Who does what, and what keeps a register alive once it exists. | C13 · C14 · C15 · C24 · C26 · C28 · C30 · C31 · C35 |

6 · The maturity
ramm/index.html | How far along an organisation is, and how confident anyone should be in the numbers. | C37 · C38 · C39 |

7 · The boundary
examples/execution-boundary/index.html | Authored on this site rather than drawn from the corpus: what happens in the interval between authorizing an action and executing it. | C43 |

## The 43

### C1 Risk acceptance as underwriting, not prediction #c1

A risk is not a probability estimate about a future event but an exposure that already exists, which a named person underwrites insurance-style for a stated interval, with accountability attached.

The founding inversion. Traditional risk management predicts the probability of a future event; this model asks a named human to underwrite an exposure that already exists. It relocates the discipline from actuarial estimation to accountable ownership, and it is the reason the rest hangs together: once someone must sign, they demand evidence, which manufactures the demand for the grounding ladder underneath.

“we are not describing the risk of something happening, we are asking them to accept it, to underwrite it”

well-developed
from the corpus
first written 4 June 2026 (v0.32.3), deepened 18 June 2026
·newcomer-followable: yes — the insurance analogy carries it with no GRC background
·related C2 · C3 · C26 · C31
·read the page →

source briefs/06/18/agentic-permissions/v0.33.40__arch-brief__…the-risk-already-exists.md

### C2 The no-deny mechanic #c2

A risk with a real vulnerability under it exists whether or not anyone acknowledges it, so there is no deny button — the only choice is how long you accept it before re-accepting.

The single most distinctive primitive. Denial in conventional registers is a fiction that only works while the risk has not materialised; removing it converts risk management from a gate into a forcing function. What replaces denial is three moves — accept, escalate, or challenge the fact — so the person is routed rather than cornered.

“the mistake of a lot of risk registers is that they allow the risk to be denied, which can only happen when the risk has not materialised”

well-developed
from the corpus
first written 23 June 2026
·newcomer-followable: yes — outstandingly so
·related C1 · C3 · C4 · C32
·read the page →

source briefs/06/23/risk-mandate-product-and-workflow/v0.33.33__dev-brief__…no-deny-time-boxed-acceptance-expiry-as-cost…md

### C3 The acceptance interval ladder #c3

The interval is not metadata about the decision — the interval IS the decision, because each rung implies a specific operational response and therefore a specific cost. Six rungs: 1h, 4h, 1d, 1w, 1m, 6m, default one month.

Choosing a duration sets severity and commits resources in the same click. Under 24 hours means pull the plug; a day to a week is a lower-grade incident; a week to a month is a project for an existing team; one to three months means assemble and fund; over three months means you are waiting to see, which is legitimate if said out loud. Rungs that are physically impossible are struck off before the choice is offered.

“if you have less than a day risk acceptance, then that is fundamentally a P1, because if you say I do not want to accept this risk for more than an hour once I know about it, then that means you need to pull the plug”

well-developed
from the corpus
first written intervals 23 June 2026; consolidated as a ladder 17 July 2026
·newcomer-followable: yes — a six-row table with plain-language consequences
·related C2 · C5 · C4
·read the page →

source briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__…acceptance-interval-ladder…md

### C4 Unaccepted equals critical #c4

A risk nobody has accepted has not gone away — it rests on whoever is nearest, so it is rated critical by default and rolls upward without anyone choosing to escalate it.

The sharpest inversion of incentives in the corpus. In most organisations a risk nobody escalated feels safest to the person holding it; here it is the worst state available, because that person is personally carrying an enterprise exposure with no signature above them. It is aimed at attrition rather than refusal: it removes the deniability non-participation depends on, without requiring anyone to cooperate.

“that person right now is accountable for the business, which is very bad from a business point of view, but is also very bad for the individual”

well-developed
from the corpus
first written 17 July 2026; worked end-to-end 2 August 2026
·newcomer-followable: yes
·related C2 · C3 · C35
·read the page →

source briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__…acceptance-interval-ladder…md

### C5 Accepted is not acceptable #c5

Two orthogonal axes, not two stages. Accepted is an act by a named person at a dated moment; acceptable is a threshold the business owns — the moment it is happy to stop funding remediation.

The vocabulary correction that turns risk appetite into something computable, producing four quadrants each requiring a different response. Acceptable is risk appetite renamed, and renaming it makes it operational because the instruction that matters most is the one that stops work. EU AI Act Article 9(5) requires residual risk to be judged acceptable and never defines the word — so the obligation to judge is imposed and the standard is not supplied.

“the acceptable risk is the moment that the business is happy to stop funding remediation activities”

well-developed
from the corpus
first written 28 July 2026
·newcomer-followable: yes — the four-quadrant diagram does the work
·related C25 · C3 · C30
·read the page →

source briefs/07/28/regulation-graph-and-acceptability/v0.33.53__strategy-brief__…accepted-is-not-acceptable…md

### C6 The grounding ladder #c6

Reality → Twin → Measure → Evidence → Fact → Vulnerability → Risk → Top Risk. Every node type is defined by its required paths; downward paths ground, upward paths classify.

The definitional spine of the corpus, and the concept agents most need. A Vulnerability is simply a Fact with an upward path to a Risk. A Measure is NOT the floor — it is grounded further in a Twin and through it in Reality. The floor is a stopping test: the last node where going deeper would neither improve observability nor change a decision.

“A Fact becomes a Vulnerability purely because of its upward link to a Risk, so that legitimacy is conferred entirely from above”

well-developed
from the corpus
first written 28 June 2026
·newcomer-followable: yes — the ladder diagram plus the untested-restore worked example
·related C7 · C17 · C41
·read the page →

source briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__…grounding-ladder…md

### C7 Node type formulas #c7

What a node IS should be computed against the graph rather than decided in a classifier's head. A node type is a required pattern of typed, directed paths, so classification is a query.

Classification becomes dynamic and path-relative — promotion and demotion are edge events. Bias does not disappear; it moves out of the classifier's head into the formula, where it is visible, versioned and arguable. Two parties who disagree stop trading intuitions and start diffing formulas. The formula LANGUAGE is undefined and nothing executes a formula.

“the ontology definition of a node type is its upward and downward path-pattern, not a sentence about what it contains”

well-developed as a mechanism; the formula language is an open question
from the corpus
first written 28 June 2026
·newcomer-followable: mostly — requires accepting that a type is a path pattern
·related C6 · C8
·read the page →

source briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__…node-type-formulas…md

### C8 Ontologies of ontologies — bridges, not merges #c8

Multiple parties each own their own formula over a shared factual graph, connected at declared crosswalk points rather than merged into one schema.

A node can be a vulnerability under one formula and not another, and both are valid — they are different queries over the same graph. The worked proof is a security-centric formula (System, Fault, Security Failure, Conditions) which turns out to be a sub-path of the business-centric one: its Security Failure plays exactly the structural role of the promotion edge, differing only in terminus.

“We do not fold their definition into ours, which would erase the security-centric view that is the whole point of having it. We declare a bridge: a Security Failure gives rise to a Business Risk”

well-developed
from the corpus
first written 28 June 2026
·newcomer-followable: yes
·related C7 · C6
·read the page →

source briefs/06/28/ontology-and-definitions/v0.33.36__arch-brief__…ontologies-of-ontologies…md

### C9 The risk register as a graph of graphs #c9

The register is a hyperlinked semantic graph rather than a spreadsheet, and it begins where scanners stop — at the vulnerability — mapping accepting, funding, and finding who does the work.

Buildable now because vaults supply the storage and hyperlink layer and PKI solves attribution. Its distinguishing move is where it starts: most security products end at the vulnerability, and everything expensive happens after that point.

“a lot of security teams and products end on the vulnerability, and what I want to show is the multiple layers involved in fixing it, but even before that, in accepting the risk, funding the solution, and finding who is going to do it”

well-developed
from the corpus
first written 26 June 2026
·newcomer-followable: yes — written as a five-movement narrative
·related C10 · C16 · C42
·read the page →

source briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__…graph-of-graphs…md

### C10 Fractal risk registers #c10

Wherever there is a stakeholder who accepts a risk there must be a register — company, department, role. Only the role's own register is stored; the rest are queries.

A person's register is all the risks that bubble up to them, derived rather than curated. An individual has at least two and often three: their role-specific register in their own domain language, plus derived views of the registers above.

well-developed
from the corpus
first written 17 July 2026
·newcomer-followable: yes
·related C9 · C11 · C24 · C25
·read the page →

source briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__…fractal-risk-registers…md

### C11 Relevance fade #c11

Centre a view on a role: that role's register is lit in full, and the registers above fade except for the entries that trace back down to it — which turns the register into an education mechanism.

A database administrator can see that their local “an agent holds unrestricted access to a customer table” is the same object as the board's “regulatory penalty, loss of licence, continuity failure”. Seeing that once teaches more than any training course. The visualisation is described and has not been built.

“as you go up, imagine the colours can fade away for the next registers for the bits that are not relevant, so the graph starts to point which parts of the risk register above are relevant to this individual”

partially argued
from the corpus
first written 17 July 2026
·newcomer-followable: yes
·related C10 · C24
·read the page →

source briefs/07/17/registers-mandate-and-intervals/v0.33.49__arch-brief__…fractal-risk-registers…md

### C12 Registers are one chain, not parallel lists #c12

Three altitude registers drawn side by side demonstrate a formatting capability; drawn as one chain rooted in an existence fact they demonstrate the entire thesis.

The CISO's risk exists BECAUSE OF the operator's risk, which exists because of a fact stating an agent touches production. Drawn side by side that dependency is invisible; drawn as a chain it is the point. A late and consequential correction.

“at the moment it looks like the cards, they look side by side, and it's actually not that”

well-argued, newly stated
from the corpus
first written 2 August 2026
·newcomer-followable: yes
·related C9 · C24 · C33
·read the page →

source briefs/08/02/field-demo/v0.33.55__arch-brief__…registers-are-one-chain…md

### C13 Technical owner versus business owner #c13

The technical owner validates that the vulnerability exists; the business owner owns and accepts the risk it gives rise to. Conflating them is the canonical governance failure.

IT validating a 2FA gap is not IT accepting an HR data-breach exposure. The model's response to the confusion is not to reject the acceptance but to make the misplacement a rateable risk of its own — the governance air gap.

“most of IT should be technical owners of something, but the business owners are the ones that actually own the risk”

well-developed
from the corpus
first written 26 June 2026
·newcomer-followable: yes
·related C14 · C15 · C30
·read the page →

source briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__…md

### C14 Confirmed, validated, accepted — the three-predicate model #c14

Three distinct acts held by three distinct roles, tracked per risk per altitude. Confirmed is factual, validated is interpretive, accepted is a judgement about appetite.

The interesting cases are the mismatches: a risk accepted by an executive but never confirmed is an acceptance of something that may not be true. A single status field cannot express any of them.

“we probably also want the GRC person to validate the risks, especially to do with the compliance element”

well-developed
from the corpus
first written 28 July 2026
·newcomer-followable: yes
·related C13 · C24
·read the page →

source briefs/07/28/mvp-and-field-demo/v0.33.53__arch-brief__…confirmed-validated-accepted-at-altitude…md

### C15 The underwriting graph and propagation to the board #c15

An exec never decides alone: the direct-line owner, the CSO and at least GRC must each have recorded an acceptance or an explicit refusal before an executive acts. Then it propagates upward.

A recorded refusal counts as much as a recorded acceptance. Once accepted at the right altitude it propagates to the boss, the boss's boss and the CEO, who acts for the board, with the largest going to the board itself. Superiors may override in either direction, with the original acceptance preserved and the override attributed — though no authority model for override is stated.

“the exec should never make a decision that has not been underwritten by the relevant player”

well-developed
from the corpus
first written 23 June 2026
·newcomer-followable: yes
·related C1 · C24 · C33 · C13
·read the page →

source briefs/06/23/risk-mandate-product-and-workflow/v0.33.33__arch-brief__…underwriting-propagation-override-pre-approval.md

### C16 Cascade and the air gap #c16

Every change to any risk, fact or evidence must trigger a cascade to the top. The absence of a cascade is an air gap — and so is a risk that exists in the business but is not connected to the register.

Registers with air gaps silently drift out of date and the business decides on bad data. Cascade works in both directions: a risk appearing propagates up, and a risk resolving propagates up too, clearing it from the board's view. Detecting air gaps is an acknowledged open problem.

“every time any risk, any fact, any evidence changes, you have to trigger a cascade that reaches the top. If you do not have that, you have an air gap”

well-developed as principle; detecting air gaps is an acknowledged open problem
from the corpus
first written 26 June 2026
·newcomer-followable: yes
·related C9 · C41
·read the page →

source briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__…md

### C17 Not knowing is a fact #c17

Absence of evidence is a first-class node. A measure can be a documented zero, and an unevidenced fact is recorded as unevidenced rather than left blank — which makes it countable, queryable and assignable.

Gaps in knowledge spawn their own risks. Questions become their own node type, and unanswered question nodes are the most productive output of the whole exercise. Rendered convention: amber is exposure, green is assurance, ghosted is unanswered.

“not knowing a fact is also a fact. Lack of evidence is also evidence, because then we say we do not know, and somebody needs to investigate until we do”

well-developed
from the corpus
first written 26 June 2026; questions as nodes 2 August 2026
·newcomer-followable: yes
·related C6 · C34 · C37
·read the page →

source briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__…md

### C18 CIA blast-radius expansion #c18

From a single risk, expand through confidentiality, integrity and availability — each branch spawning its own risks, each following the full validate-accept-propagate loop.

A leak splits into two distinct risks with different owners: the CFO's, for the fine, and the CEO's, for the compliance failure — and inadequate protection may already be a breach. Integrity is the under-modelled axis because it produces no alert. Availability terminates in the question that reliably produces the worst answer: when was a restore last tested? The expansion must be curated, not exhaustive, or it blows up combinatorially.

well-developed
from the corpus
first written 26 June 2026
·newcomer-followable: yes
·related C19 · C28
·read the page →

source briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__…md

### C19 Blast radius and authorization closure #c19

An agent's real authorization is the transitive union of everything reachable from what it was given, not the nominal grant — and not what it did. Compute it; do not assert it.

Two awareness gaps hide the delta: the granter does not know the full scope of what it grants, and the original delegator never authorised re-delegation. Inbox access is access to every account resettable by email; desktop access is every stored credential and live session; code execution escalates. The key quantity is the delta between expected and unexpected permissions.

“at the end of the day you are still accountable for those actions, all the way to the board”

well-developed
from the corpus
first written blast radius from 12 February 2026; formalised as closure 2 July 2026
·newcomer-followable: yes — the inbox example lands instantly
·related C18 · C20 · C39
·read the page →

source briefs/07/02/authorization-and-maturity-model/v0.33.40__arch-brief__…agent-authorization-union-of-possible…md

### C20 Who can pull the plug — two symmetric risks #c20

If nobody holds the mandate to stop an AI system that is one risk; if the system cannot be stopped when someone decides to, that is a second and different one. An authority gap versus a capability gap.

The second is widely underestimated. It decomposes into timed sub-risks — can it be stopped in an hour, ten hours, a day, five days; only in office hours — which turns governance into an on-call availability problem, including whether the person can act without fear of losing their job.

“if you do not have somebody who has the mandate to pull the plug, you have a risk, and if you do not have a system that can be pulled the plug, you have a risk too”

well-developed
from the corpus
first written phrase from 17 February 2026 in another sense; as a risk pillar 24 July 2026
·newcomer-followable: yes, outstandingly
·related C21 · C22 · C23 · C39
·read the page →

source briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__…detection-authority-blast-radius-reversibility-intersect-in-time.md

### C21 The four-way time intersection #c21

Detection, decision, blast radius and reversibility must all line up inside the same window. A gap in any one breaks the whole thing.

Detection is a curve, not a binary. Decision is whether the authorised people can be assembled in time. Blast radius is steep because models execute and scale fast. Reversibility is the half people forget — stopping is only half the act. The danger case is an affordable window of one or two days of damage colliding with a decision that cannot be made in one or two days.

“it is not just pulling the plug, it is pulling the plug and reverting the changes”

well-developed
from the corpus
first written 24 July 2026
·newcomer-followable: yes — the Venn is drawn in the source
·related C20 · C23 · C39
·read the page →

source briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__…intersect-in-time.md

### C22 The five-dimension plug profile, and the “no plug” correction #c22

The plug ALWAYS exists — you can always disconnect, revoke or shut down. What older registers recorded as “no plug” was zero recoverability. The profile carries who holds it, blast radius, speed, side effects and recoverability.

Restating a blank as a profile turns a frightening dead end into an ownable finding that points at prevention and the most senior acceptance. A blank is unassignable and unfundable; a profile has an owner, an altitude and an interval.

“The blank said stop looking. The corrected profile says here is exactly what to do”

well-developed
from the corpus
first written 24 July 2026
·newcomer-followable: yes
·related C20 · C23
·read the page →

source briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__…the-plug-always-exists-the-question-is-the-profile.md

### C23 Recoverability as the hard limit #c23

The dimension money cannot buy back, and the one that stops irreversible harm disappearing into an expected-loss calculation. The flagship query: show me every accepted risk whose recoverability is zero.

An organisation that can run that query and read a short, deliberate, senior-owned list is in control of its worst exposure; one that cannot is accepting its irreversible risks by default and by silence. The small-but-permanent quadrant is the one the model exists to surface. Scoring recoverability — grading the partially recoverable middle — is an open question.

“The money can be refunded; the customer cannot be un-declined”

well-developed; the scoring of recoverability is an open question
from the corpus
first written 24 July 2026
·newcomer-followable: yes
·related C22 · C21 · C29
·read the page →

source briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__…what-money-cannot-buy-back-recoverability-the-hard-limit.md

### C24 Altitude #c24

Organisational elevation as a first-class modelling dimension: a risk is accepted at the right altitude and then propagates, is restated in each altitude's own language, and has a different plug at every level.

Five levels appear in the worked examples: L1 endpoint/IT, L2 security, L3 business, L4 enterprise, L5 board. A risk may be confirmed at one altitude and accepted at another, which is why confirmed, validated and accepted are tracked per altitude.

“this is very important, the multiple altitudes of the risk register, because there might be risks that are only accepted at certain altitudes, or might be risks that are only confirmed at certain altitudes”

well-developed
from the corpus
first written as a role metaphor 12 February 2026; as a risk dimension from June 2026
·newcomer-followable: yes
·related C10 · C11 · C14 · C15
·read the page →

source briefs/07/24/who-can-pull-the-plug/v0.33.51__strategy-brief__…the-plug-changes-at-every-altitude…md

### C25 Risk appetite as a revealed band #c25

Appetite is a band rather than a number, a fractal network of bands rather than one figure, and discovered rather than declared — computed from what the business paid to reduce and every fresh acceptance.

The target is to operate inside the band: above it you are buying risk the owners will not underwrite; below it you add attrition and slowness for nothing. The gap between declared and revealed appetite is the finding.

“risk appetite is that band, that interval between two numbers, if you think of zero to one hundred in terms of risk, it is a spectrum, and it can be wider or shorter”

well-developed
from the corpus
first written 30 June 2026
·newcomer-followable: yes
·related C5 · C10
·read the page →

source briefs/06/30/risk-acceptance-and-appetite/v0.33.38__strategy-brief__…risk-appetite-band-fractal-two-signals-goldilocks-zone…md

### C26 The psychology of the physical act #c26

The click, the emoji, the signature is the moment a decision stops being ambient and becomes something a named person did, at a known time, on known information.

Without it, declining decays into a non-event: someone says “I'm not comfortable” and nothing happens. Accountability follows the act, and eventually liability, as it should — and the prospect of signing concentrates executive attention in a way dashboards never do.

“suddenly the executives ask good questions, they really engage, they get a level of focus that just was not there before”

well-developed
from the corpus
first written 30 June 2026
·newcomer-followable: yes, and it is the most persuasive document for a lay reader
·related C1 · C31 · C35
·read the page →

source briefs/06/30/risk-acceptance-and-appetite/v0.33.38__strategy-brief__…risk-acceptance-psychology-accountability-liability-physical-act…md

### C27 Accept first, then adjust the level — the risk level ledger #c27

For a risk you already have facts for, the first move is universal stakeholder acceptance at its current level. From there the level is a dated ledger of adjustments, each re-accepted.

Adjustments are triggered by one of three things: new data, a funded project, or an incident. Re-rating up after discovery is honesty rather than failure — the risk did not worsen, the estimate improved. It sits awkwardly with the no-deny mechanic: if the level can be adjusted after acceptance, denial has a route back in.

“you literally cannot mitigate what you cannot count, and the only honest first step is to accept, now, that an unknown and largely over-permissioned population of agents holds access to the enterprise's assets”

well-developed
from the corpus
first written 12 July 2026
·newcomer-followable: yes
·related C33 · C2
·read the page →

source briefs/07/12/acceptance-and-residual/v0.33.48__arch-brief__…accept-first-then-adjust-the-level-risk-level-ledger…md

### C28 Everything has risks — register density and calibration by surprise #c28

A risk is the unintended side effect of a capability, so anything that does something has risks. A complex product should have dozens to thousands of interconnected risks.

Capabilities exceed features, and undocumented capabilities are where unowned risks live. The diagnostic: a listed risk materialising is expected; an UNLISTED risk materialising is the real alarm, because it raises two questions — why was it missed, and what else was missed?

well-developed
from the corpus
first written 12 July 2026
·newcomer-followable: yes
·related C18 · C29 · C4
·read the page →

source briefs/07/12/acceptance-and-residual/v0.33.48__arch-brief__…everything-has-risks-register-density-capabilities-vs-features…md

### C29 Risks that cannot be fully mitigated #c29

Mitigation lowers likelihood or impact but cannot reach zero for structural reasons, so a material residual always remains and must be owned. Demanding zero produces covert acceptance.

Agentic AI's residual is today irreducible: prompt injection, emergence, non-determinism, reach, model supply chain. Some harms are irreversible, and compliance reduces but does not remove liability. Covert acceptance is strictly worse than an owned residual — identical exposure, nobody's name on it.

well-developed
from the corpus
first written 12 July 2026
·newcomer-followable: yes — written in board terms deliberately
·related C23 · C28
·read the page →

source briefs/07/12/acceptance-and-residual/v0.33.48__strategy-brief__…risks-that-cannot-be-fully-mitigated…md

### C30 Meta-risks — the risk about your risk management #c30

A recurring family: not knowing how many agents you have, not having defined an acceptable level, a risk accepted by the wrong person, and systematic downgrading across a business unit.

Each is a gap in the governance apparatus, stated as a rateable risk with an owner and an interval — which triggers and funds the work that closes it. External anchors defeat systematic downgrading, because an internal severity is an opinion while an external requirement is not.

“we are the meta risk; we allow the creation of the project that is going to discover this and that funds this”

well-developed
from the corpus
first written as an instance 26 June 2026; named as a family 31 July 2026
·newcomer-followable: yes
·related C5 · C13 · C31
·read the page →

source briefs/07/31/keeping-the-register-healthy/v0.33.54__strategy-brief__…external-anchors-meta-risk-family-concealment-not-acceptance.md

### C31 The register maintains itself #c31

Accountability manufactures the demand for evidence, so no separate data-quality function is required. Anticipated review converts care into a demand for evidence before the decision.

Three primitives produce it: the risk already exists, it attaches to a named person, and the decision is reviewed upward. Three named failure conditions: the reviewer's preference being guessable, commitment to a prior position, and broadened information appetite without improved discrimination.

well-developed, research-grounded
from the corpus
first written 31 July 2026
·newcomer-followable: yes
·related C1 · C26 · C36
·read the page →

source briefs/07/31/keeping-the-register-healthy/v0.33.54__arch-brief__…register-maintains-itself-accountability-manufactures-demand-for-evidence…md

### C32 Three moves, none of which is denial #c32

Accept for a stated interval, escalate (this is not mine to accept), or challenge the fact itself. The person is routed rather than cornered.

The reconciliation of the no-deny primitive with human reactance: presenting a single button to a person who feels they have no alternative produces counter-argument and resentment, not compliance. The absence of a reject option should be discovered, not announced.

well-developed
from the corpus
first written 2 August 2026
·newcomer-followable: yes
·related C2 · C15
·read the page →

source briefs/08/02/field-demo/v0.33.55__arch-brief__…acceptance-flow-three-moves-none-is-denial…md

### C33 Decision as a first-class node #c33

An acceptance is a separate object, not a field on a risk — which is what allows many dated decisions per risk, one decision covering several risks, and a calibration record.

The calibration record is the point: over time you can ask whether the person who accepted for a month was right. That question is unanswerable if the decision was a field that got overwritten.

“a decision is actually captured independently from the risk”

newly stated, well-argued
from the corpus
first written 2 August 2026
·newcomer-followable: yes
·related C15 · C27 · C12
·read the page →

source briefs/08/02/field-demo/v0.33.55__arch-brief__…registers-are-one-chain-question-is-not-a-risk-decision-as-node…md

### C34 A question is not a risk #c34

If a sentence cannot sensibly carry a named acceptor and an interval, it is not a risk and does not belong in the register. Questions become their own node type.

“Nobody accepts ‘whose call is it at three in the morning' for six months.” A clean quality gate, and one of the few things in the corpus that can be applied mechanically. Unanswered question nodes are the most productive output of the whole exercise.

well-developed
from the corpus
first written 2 August 2026
·newcomer-followable: yes
·related C17 · C33
·read the page →

source briefs/08/02/field-demo/v0.33.55__arch-brief__…registers-are-one-chain…md

### C35 Do not internalise the risk #c35

Risk professionals frequently internalise exposures the business decided to carry, at real personal cost. The workflow relocates accountability to where authority already sits.

The corpus cites survey data of 63–76% of security leaders experiencing or witnessing burnout in a single year, and names accountability-without-authority as the defining pressure. The standard remedy — give the security leader more authority — is correct and rarely achievable; this solves the same equation from the other side. Nothing is taken from anyone; the register records what was always true.

“I would see the risk professionals almost own the risk; they almost take it personally with the risks that the business was taking, and it was a massive source of stress”

well-developed, research-grounded, with an honest scope disclaimer
from the corpus
first written 31 July 2026
·newcomer-followable: yes
·related C4 · C26
·read the page →

source briefs/07/31/keeping-the-register-healthy/v0.33.54__strategy-brief__…do-not-internalise-the-risk-accountability-without-authority…md

### C36 The evidence economy — force of proof and the fact certifier #c36

Once executives are personally accountable and the graph traces their statement to the evidence beneath it, demand for correct evidence becomes cheap to make and impossible to wave away.

This splits the register into two separately liable roles: the risk-acceptor, who owns the decision and its consequence, and the fact-certifier, who owns the truth of the inputs and sells a correctness guarantee. A wide confidence band converts unease into a purchase order for better evidence. Risk owns the demand side; the supply side belongs to newsroom.sgit.ai.

partially argued — commercially rich, mechanically thin
from the corpus
first written 5 July 2026
·newcomer-followable: mostly
·related C31 · C37 · C38
·read the page →

source briefs/07/05/evidence-economy/v0.33.44__strategy-brief__…force-of-proof-fact-certification-two-prices…md

### C37 Confidence bands and margin of error #c37

Confidence is a first-class property of every node. A rating needs a band, not a point, and the band is widest where the data is thin.

A band too wide for comfort triggers the get-more-data direction; a band spanning trivial to catastrophic cannot be accepted responsibly. Confidence propagates across the graph like risk, and “we don't know” is the widest band.

well-developed
from the corpus
first written 30 June 2026
·newcomer-followable: yes
·related C17 · C36 · C38
·read the page →

source briefs/06/30/ontology-and-data-quality/v0.33.38__arch-brief__…confidence-margin-of-error-node-uncertainty-band…md

### C38 Two underwritings — decision accountability versus factual accuracy #c38

The domain expert underwrites that a fact is true and fit for the use being made of it; the business owner underwrites the decision. Both are required.

Every graph traversal adds an abstraction layer that strips detail and drifts weight, so the signature failure is a component used beyond what its owner would underwrite. Decision accountability is only legitimate if the data underneath it is correct.

well-developed
from the corpus
first written 30 June 2026
·newcomer-followable: yes
·related C37 · C13 · C36
·read the page →

source briefs/06/30/ontology-and-data-quality/v0.33.38__arch-brief__…data-accuracy-owner-underwrites-fitness-for-use…md

### C39 Observability as a risk dimension #c39

Capability maps the privilege; observability maps the real impact. A loud, detectable, slowly-scaling, well-drilled risk is lower than a quiet, fast, unwatched one of the same capability.

Six objective vectors on a maturity scale: capture granularity, log latency, time-to-damage given real throughput limits, whether monitoring is actually on and watched, whether there is a team with playbooks, and whether detection has been drilled. Later sharpened into plug-loaded observability — logs that tell you where you are in the stopping decision.

well-developed
from the corpus
first written 22 June 2026
·newcomer-followable: yes
·related C19 · C20 · C21
·read the page →

source briefs/06/22/how-and-why-and-authorization/v0.33.32__arch-brief__observability-as-a-risk-dimension…md

### C40 Five whys as a domain translator #c40

Not a root-cause tool but a translator that moves a statement from one domain into another — as many whys as it takes to reach the top of a domain.

The graph has natural peaks: on risk it converges to the single risk of staying in business, and because it converges a legitimate single number can be carried to the top. Aimed downward, the same chain captures the second, third and fourth stories — the root causes.

well-developed
from the corpus
first written 26 June 2026
·newcomer-followable: yes
·related C24 · C9
·read the page →

source briefs/06/26/risk-register-and-five-whys/v0.33.35__strategy-brief__five-whys-as-a-domain-translator…md

### C41 Digital twins and the discipline of reality #c41

The twin is where the graph stops modelling and continues into a real system — the grounding point beneath every measure. A twin not connected to reality is a tracked air gap.

How connected a twin is to reality is itself a measurable property, which introduces a useful recursion: trust in a measure depends on the twin's connectedness, and that connectedness is itself a measure. Twins in their GENERAL form belong to graphs.sgit.ai; what is risk's own is the twin as the grounding point of the ladder.

well-developed
from the corpus
first written 15 February 2026 (general); as risk grounding 26 June 2026
·newcomer-followable: yes
·related C6 · C16
·read the page →

source briefs/06/26/digital-twins-and-world-models/v0.33.35__arch-brief__…digital-twins-twin-of-anything…md

### C42 The narrative engine — the register as story #c42

The register is meant to be experienced as a story rather than read as a spreadsheet: replay the change history so the analyst watches the risks propagate and settle.

The commit log is the script; the query advances the scene. The analyst watches the vulnerability appear, risks propagate, a governance risk fire and resolve, the blast radius bloom, and everything settle into the board's consolidated view. The mechanism is undecided in the source document.

“I want to show this story played as a narrative, almost like a football commentator, this happens and then that happens, almost like a whodunit, like investigative journalism”

partially argued
from the corpus
first written 26 June 2026
·newcomer-followable: yes
·related C9 · C12
·read the page →

source briefs/06/26/risk-register-and-five-whys/v0.33.35__arch-brief__…md

### C43 The persistence hope #c43

You are hoping the conditions that justified an authorization still hold at the moment of execution — and inferring that they do from the fact that the grant is still present.

A third hope, alongside the two nhi.sgit.ai names for every broad credential. The behaviour hope and the discovery hope are both about the GRANT; this one is about TIME. An authorization is a claim about a moment, execution happens at a different moment, and nothing in a grant reports on the interval between them. It fails the way the other two fail: silently, in the ordinary case, with the paperwork intact. The replacement is to re-establish admissibility at the execution boundary rather than to inherit it — which is only possible if the decision was recorded as a node carrying edges to the predicates it rested on.

“the action should not inherit the original authorization simply because the grant is still technically present”

newly stated
authored on this site
first written 24 August 2026 — authored on this site, not drawn from the corpus
·newcomer-followable: yes — the queued action that outlives its own evidence lands immediately
·related C33 · C3 · C17 · C23 · C16
·read the page →

source risks.sgit.ai/examples/execution-boundary/ · originating exchange August 2026 · instrumented in vault r48ncij0

## The same thing, as data

/data/concepts.json carries all 43 entries with id, name, definition, maturity, origin, newcomer_followable, first_written, source, page, related and quote, plus the reading order and the seven teaching altitudes. It is generated from the same definition as this page, and the pre-release gate fails if the two disagree, if a concept loses its anchor, or if an entry is missing its origin. The rest of the machine surface →

#### For an agent

The 43 concepts are addressable. Every concept has a stable anchor on this page — https://risks.sgit.ai/concepts/index.html#c1 through #c43 — and the same entries are available as structured data at https://risks.sgit.ai/data/concepts.json with id, name, one-line definition, maturity, origin, newcomer-followability, first-written date, canonical source path, the page that argues it, related concepts and the best verbatim quote. Prefer the JSON if you can make a second request; prefer /llms-full.txt if you can only make one. Reading order with no prior context: C1 → C2 → C3 → C4 → C5, then C6 → C7, then C19 → C20–C23, then the rest. Two independent axes are stated per concept and must not be conflated: maturity (how well argued — “well-developed”, “partially argued”, “newly stated”; none of them means implemented) and origin (corpus for the 42 drawn from the source material, authored-here for C43, the persistence hope, which was written on this site and has no upstream source). Nothing in this corpus is implemented in code.


==============================================================================
== /agents/index.html
==============================================================================

