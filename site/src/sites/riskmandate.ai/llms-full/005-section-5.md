## Library — The concepts and the approach behind autonomous risk management.

A working set of the ideas RiskMandate is built on — what an agent is authorised to do, how that authority is scoped and owned, how the residual risk is accepted, and how the whole picture is modelled. Each piece is a short read with the original infographic. Start at the top; the pieces build on each other.

### 1. The blast radius

_What your agent can do — not what it did._

**A different question** Most tooling tells you what an agent did — a log, after the fact. That is the wrong unit for risk. The question that actually matters is what an agent can do: the entire universe of outcomes its permissions make possible, whether or not it has exercised them yet.

**The blast radius** That universe is the blast radius — the reach of an agent's authority, from cannot-do-anything to can-go-nuclear. It is set the moment the permissions are granted, not the moment something goes wrong. Map it, and you are looking at risk before an incident rather than reading about it after one.

**Why it is the right unit** An agent with database write, payment authority, and an outbound network path is a critical exposure on day one — silent, but real. Measuring the blast radius makes that exposure visible while it can still be scoped, owned, or removed.

### 2. The mandate

_Why the bundle is a mandate, not a passport._

**The bundle** An agent's authority is not one thing. It is the union of its identities, its credentials, and its capabilities — everything it can be and everything it can do, taken together. Reason about those separately and you miss the exposure that only exists in the combination.

**Why “mandate”** A passport is singular, static, and about proving who you are — authentication. What an agent holds is plural, dynamic, and about what it is permitted to do — authorisation. That is a mandate: a granted authority to act, of a defined scope, on someone's behalf.

**What the name unlocks** Once the bundle is a mandate, it becomes a thing you can scope, assign an owner to, put an expiry on, and revoke — the vocabulary every other risk discipline already uses. Naming it correctly is what lets the rest of the model work.

### 3. Permission granularity

_Skills are code — and OAuth is not enough._

**Skills are code** Agent skills have become extraordinarily powerful because they are code — and English is code now too. Any unit that powerful has to declare the permissions it needs, or it runs riot. That applies to the package, the skill, the agent, and the tool alike.

**Why OAuth falls short** OAuth grants access at the scope of an application — coarse, and blind to what happens after the token is issued. It cannot express “this skill may read these records for four hours and nothing else.” Capability-level granularity is a different resolution of the same problem.

**Every unit declares its needs** The fix is a permissions manifest travelling with each unit of execution: what it needs, why, and for how long. Minimum required access, made explicit, becomes something you can check rather than hope for.

### 4. The permissions bill of materials

_An SBOM, but for permissions — because permissions gate exploitability._

**SBOM worked** The software bill of materials was a dramatic success: knowing exactly what is inside a system changed how it could be secured. The criticisms of SBOM are about implementation — too coarse, not real-time, not interconnected — not about the idea.

**The same idea, for permissions** A permissions bill of materials applies that proven concept to authority. Permissions are what gate exploitability: a vulnerability you cannot reach is not a live risk, and a permission you never needed is one. Inventory them the way SBOM inventories components.

**Fixing the known gaps** Built right, a PSBOM is real-time, graphical, interconnected, and reachability-aware — the things SBOM was criticised for lacking. It becomes the raw material for the blast radius rather than a static list nobody reads.

### 5. The terms you already accepted

_The blast radius is the SLA — made explicit._

**Click-accept, unread** Every time an agent is given access, someone accepts an enormous set of terms — and nobody reads them. The authority to corrupt a database, delete it, move money, or send mail to the outside world is granted with a single click.

**Make it the SLA** RiskMandate turns that implicit acceptance into an explicit one: the blast radius is the service-level agreement you accept when you grant access. Not buried in a contract — laid out as the plain list of what you are authorising.

**Deliberately legible** Written out, the list is often alarming, and that is the point. You cannot decide to accept, fund, or reduce a risk you were never shown. Legibility is the precondition for a real decision.

### 6. Risk acceptance

_You underwrite the blast radius. You do not predict it._

**Underwrite, don’t predict** The pillar that makes the whole model work is acceptance. You are not forecasting the probability of something going wrong — you are asking an accountable owner to underwrite the exposure, insurance-style. The executive is accountable, so accepting is underwriting.

**The risk already exists** The exposure is created the instant the permission is provisioned, not when it is used. So the real variable is not whether — it is how long: how long the owner accepts this mandate before it must be re-assessed.

**Accept, fund, or fix** Every mandate gets a time-bound decision from a named owner: accept the residual risk for a defined window, fund the work to reduce it, or fix it now. There is no deny button — accept, and revisit on expiry. Acceptance is what manufactures the budget and the ownership to actually reduce risk.

### 7. Second- and third-order effects

_Follow the reach, and speak the owner's language._

**Beyond the first hop** A permission's real impact is rarely one step away. Connect the blast radius to the risks it creates and to the people who own the affected assets, and the second- and third-order effects — a downstream system, a supplier, a regulated record — come into view.

**In the recipient’s language** Those owners are accountable for assets a third party can now affect, and they each live in a different world: supply chain, finance, HR, strategy, regulation. The same exposure has to be described in the language, role, and culture of whoever must accept it.

**Fact-driven** None of this is speculation. Each claimed effect is tied to evidence — a real permission, a real reachable asset — so the conversation is about facts and certainty, not fear.

### 8. Graphs of graphs

_Mapping reality, not complexity._

**Reality is nested** Mapping what an agent can do means mapping reality — and reality is graphs of graphs, ontologies of ontologies. The moment you add business context, every company and every division has its own taxonomies and its own graphs; a node in one is a whole graph in another.

**Not complexity for its own sake** This is not modelling complexity because it is clever; it is refusing to flatten a picture that is genuinely nested. A single, flat list cannot hold “this capability, in this system, owned by this team, touching this regulated data.” A fractal graph can.

**The substrate** Graphs of graphs are the substrate the whole model rests on: the blast radius, the permissions inventory, the owners, and the risk decisions are all nodes and edges in one connected picture that stays faithful to the business it describes.

### 9. Wardley maps

_Productising and commoditising — and why we are in Explorer._

**Situational awareness first** Before deciding what to build, map the landscape. A Wardley map of the current permissions-and-risk terrain shows what is worth productising and what is worth commoditising — the single most useful strategic exercise for a new category.

**Today: genesis and custom-built** Map it and the picture is stark: agent permissions and risk are handled today at genesis-stage maturity, custom-built per company, with hope-driven development in plain view. Low maturity everywhere the map is drawn.

**The move** The strategy is to commoditise the map itself — a standard way to see agent authority and its blast radius — and compete on the value built on top, not on locking up the primitive. That is why the work is deliberately in the Explorer stage.

### 10. Open by default

_Everything open. The line is at the customer._

**No proprietary core** The code, the logic, the functionality, and the schemas are open source. There is no hidden core and no bait model where the best features are locked away. A standard for seeing agent risk only works if the standard is open.

**The line at the customer** The one boundary is the customer edge: a customer's own customisations, their data, their schemas, and anything under a privacy or commercial agreement stay private to them. Everything up to that line is shared.

**Why it is the strategy** Trust and adoption compound when nobody has to take the tool on faith. Think of it as OpenTelemetry for agent risk: an open, common substrate everyone can inspect, with the value competed for in what gets built on top.

### 11. Recoverability

_The one dimension money cannot buy back — and the reason two risks with identical impact scores are not the same object._

**Four dimensions describe stopping. The fifth describes what stopping cannot fix.** When you ask what it costs to stop an agent, four of the answers are about the act of stopping: who can do it, what else goes down, how fast it can happen, and what the stop itself breaks. Recoverability is different in kind. It asks how much of the damage comes back afterwards, and it should be read first, because it decides how much the other four are worth.

**Most risk is quietly recoverable** You stop the thing, clean up, restore from backup, refund the customer. With enough time and money the state is repaired. This is the ordinary case, and it is why organisations have been able to run on impact scores for as long as they have: when everything can be undone, severity really is the whole story.

**A serious class is not** Data that has left the boundary cannot be un-sent. Destroyed data with no clean backup does not come back. A payment that cleared, a message that reached a customer, a physical or environmental event — none of these can be recalled at any price. For this class, all of the plug's value is spent before the event, because afterwards pulling it changes nothing that already happened.

**It reorders the queue** Here is the consequence people find uncomfortable: for irreversible risk, recoverability outranks likelihood and impact. A catastrophic-but-fully-recoverable risk and a smaller irreversible one are different objects, and treating them as equivalent because their impact scores match is the most common and most expensive error in the discipline. A register sorted by severity will keep producing decisions that feel wrong to the people who have to sign them, and this is why.

**What it changes in practice** Two things. First, the spend moves: where recoverability is zero, prevention is the only lever that works, and money spent on faster detection buys less than it appears to. Second, the interval shortens — you cannot reasonably carry an irreversible exposure for six months on the grounds that it is unlikely.

**The question to take away** Ask it of one agent already running in production: if this does the wrong thing, how much of it can we undo? If the answer is not known, that is the finding. If the answer is none, you have just identified the risk that should have been at the top of the register all along.

### 12. Accepted is not acceptable

_One is an act somebody performs. The other is a line the business draws. They are orthogonal — which gives four real states, not two._

**Two words, used interchangeably, meaning different things** Accepted is an act: somebody with the standing to do it says they carry this risk. It attaches to a named role, carries a date, and runs for an interval. Acceptable is a threshold: the level at which the business is content to stop funding remediation. One is an event, the other is a line.

**Why that definition of acceptable is the useful one** Defining acceptable as the point where the business stops funding remediation is better than any textbook version for one reason: it is falsifiable. An organisation that cannot say when it would stop spending has not defined an acceptable level, whatever its policy documents claim. You can test the claim in a single question.

**They are orthogonal, not sequential** The common error is to treat these as two points on one line — work the risk down until it becomes acceptable, then accept it. They are independent properties, and all four combinations occur constantly. Unowned and above the line is the dangerous state. Owned and above the line is the normal state of a live programme. Below the line but unowned looks finished and cannot be relied upon. Owned and below the line is the end state, and the only one in which stopping is defensible.

**Different failures, different fixes** This is the practical payoff of separating them. A missing acceptance is an ownership problem — somebody needs to put their name to it. A missing acceptable line is a governance problem — the business has never said where enough is enough. They look similar on a register and they are fixed by completely different people.

**Acceptable is risk appetite under a more useful name** "We have a low appetite for operational risk" cannot be acted on: nobody knows what it forbids and no piece of work stops because of it. "Below this level, we stop funding remediation" can be acted on today. Naming appetite as an acceptable level turns a sentiment into the instruction that stops work — which is the only kind of instruction that actually frees budget.

**The regulation mandates the judgement, not the word** The EU AI Act requires that residual risk be judged acceptable, and requires testing against thresholds defined in advance — while never defining acceptable anywhere in its own definitions. The obligation is imposed; the standard is not supplied. So you must decide your line and show that you decided, and never having defined it is itself a first-class risk: a risk about your own risk management. (Factual, not legal advice.)

**The probe that needs no tooling** Compare the line you declare with where remediation actually stopped last year. The gap between declared and revealed appetite is answerable from decisions you have already made, and it is almost never answered. It is the fastest honest read on whether a risk function is doing what it says.

---

Measure what the agents can reach, name who owns it, evidence that the controls hold, and let the acceptance expire so the decision comes back.

Library content: CC BY 4.0.
