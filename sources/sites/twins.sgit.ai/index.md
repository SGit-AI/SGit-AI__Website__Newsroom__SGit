# twins.sgit.ai — an interface to reality, not a simulation of it

> The industry's digital twin is a simulation of a physical asset, valued for how
> faithfully it copies. This one is different, and the difference is the point: a twin
> here is an **interface to a real thing, valued for whether it is connected**. It is
> where a graph stops modelling and starts touching the world.

*Source: <https://twins.sgit.ai/index.html> · site v0.1.0 · markdown twin of the front page.*

---

## The definition

> "a digital twin is, in essence, **a system that has properties, behaviours, functions,
> and inputs and outputs**, and we can define all of those."

And its generality, which is the sentence worth memorising: one can be made *"of anything:
an organisation, an element, a mail system, an inbox, a person, a behaviour, an event, an
action, external factors like weather, **even luck**."* Non-determinism is included rather
than excluded: *"the fact that in the real world they are not deterministic, or maybe
random, we can capture that."*

[The full primitive](what-is-a-twin/index.html).

## Why the graph needs one at every edge

These graphs refuse properties: *"properties do not have meaning, they are just words; we
capture meaning through connectivity."* Which creates a problem at the edge. If meaning is
connectivity, where does connectivity stop?

> "the power of the twin is that **we always arrive at the twin**, so the edges and the
> peaks and the endpoints of the graph continue into the twin, and then ideally into
> reality."

Every terminal node is a twin, and the twin is *"the doorway from the model to the real
system."* This is why the grounding ladder reads `Measure := an observation of the node it
measures, grounded on a Twin`, and why the established edge grammar ends with *"the
connection from any node to a twin and onward to reality is `connected_to`."*

## Four ideas that are original here

1. [**Connectedness is a measurable fact**](discipline/index.html#connectedness) —
   *"whether we can continue to reality is a measurable fact, it is connected or it is
   not."* Where it is not, the state is recorded as a **tracked air gap**. Applied to a
   legal instrument, that becomes a computable coverage measure.
2. [**The discipline of reality**](discipline/index.html#reality) — *"everything has to be
   relevant, everything has to be a fact, everything has to exist ... either we have
   evidence and it exists, or we do not."* No speculative risks polluting the graph.
3. [**Twins as actors**](actors/index.html) — *"every action that updates the graph,
   including accepting a risk, is performed by a twin"*, with reasoning documented and a
   persona carried.
4. [**Twins make risk testable**](what-is-a-twin/index.html#testable) — *"the same
   techniques we use with software"*, turned on an organisation's risk, because the twin
   gives them something to run against.

## The build state, unsoftened

| Artefact | State | What it proves |
|---|---|---|
| The S3-compatible vault container | **Working** | A twin is a drop-in interface: *"code using boto3 believes it is talking to real S3"*, and the consuming code does not change |
| The AWS twins in the IAM config risk engine | Partial | Facts from twins, judgement elsewhere. Python, unit-tested, JSON out |
| `Twin` in the grounding ladder, `connected_to` in the edge grammar | **Established** | Cited across the estate |
| The 2FA demo, the world model, the org twin, the agent twin | **Designed, unbuilt** | Nothing yet, and labelled as design everywhere |

One working twin, one set of half-built twins, two established primitives, and a large
designed layer. [The full table](shipped/index.html).

## The one that works

> "the container is **a digital twin of S3**, presenting the same S3-compatible API, so
> that code using boto3, the AWS CLI, or any S3 SDK **believes it is talking to real S3**,
> while the files are served from a vault, from local disk, or from memory, chosen as a
> swappable backend; **the service's own code does not change**."

Its value is not that it simulates S3 well. It is that boto3 cannot tell the difference.
[The worked proof](built/index.html).

## The naming collision, ruled on

A brief arrived in August calling a credential-holding execution broker a "Service Twin",
and the corpus's own review said: *"the name collides, because twin already means something
specific in this corpus."* It does, and in the dimension that matters most: a corpus twin
holds no credentials, and the broker's whole function is to hold them.

The ruling: **twin keeps its corpus meaning, and the broker is presented by its function.**
The collision itself is published, and enforced by a name-watch in the release gate.
[The ruling](naming/index.html) · [the broker](broker/index.html).

## Published unresolved

Five open questions travel with this material. The two that matter most: how connected a
twin really is once staleness is admitted (binary connectedness is what makes coverage
computable, and a twin updated *"manually once a week"* is connected and six days stale),
and whether the broker's concentration risk is acceptable, since it *"inverts the
catastrophic failure property the rest of the architecture depends on."*
[Gaps and open questions](open-questions/index.html).

## Who is writing this

Published by the sgit project, which builds the graph model and the vault layer the twin
primitive sits inside. A participant publishing a definition, stated upfront.
[Where this approach loses](about/participant.html) ·
[what this site owns and what it does not](network/index.html).

---

All content CC BY 4.0. The brief pack this site is built from is published verbatim at
[/briefs/](documents/index.html). Machine-readable summaries: [/llms.txt](llms.txt) and
[/llms-full.txt](llms-full.txt).
