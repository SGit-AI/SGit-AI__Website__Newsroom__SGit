# risks.sgit.ai — you cannot deny a risk, only say how long you accept it

*The conceptual and research home for risk · site v0.2.2 · CC BY 4.0*

Traditional risk management predicts the probability of a future event. This model asks a
named human to **underwrite an exposure that already exists** — insurance-style, with
personal liability attached. Everything else follows from that one inversion: if the risk
is real it cannot be denied, so **there is no deny button**; the only choice is *how long*,
and **the interval is the decision**, because each rung implies a specific operational
response.

> **This is a research site. The concepts are argued, the worked examples are real graphs,
> five vaults are live and browsable, and one worked example is a live instrument you can
> drive. The engine is not built.** Greps for `risk_`, `RiskAcceptance`, `risk_register`
> and `riskmandate` across the implementing repository return zero matches. Do not describe any of this as an existing feature.

## The inversion, in four ideas

| | Concept | The one line |
|---|---|---|
| **C1** | [Acceptance is underwriting, not prediction](acceptance/underwriting.html) | *"we are not describing the risk of something happening, we are asking them to accept it, to underwrite it"* |
| **C2** | [There is no deny button](acceptance/no-deny.html) | *"the mistake of a lot of risk registers is that they allow the risk to be denied, which can only happen when the risk has not materialised"* |
| **C3** | [The interval ladder](acceptance/the-ladder.html) | The interval *is* the decision. 1h / 4h / 1d / 1w / 1m / 6m, default one month — deliberately just above the incident line |
| **C4** | [Unaccepted equals critical](acceptance/unaccepted-is-critical.html) | An un-underwritten risk rests on whoever is nearest. *"that person right now is accountable for the business"* |

Then the vocabulary correction — [accepted is not acceptable](acceptable/index.html), two
orthogonal axes — and underneath all of it [the grounding
ladder](ladder/index.html): Reality → Twin → Measure → Evidence → Fact → Vulnerability →
Risk, where downward paths ground and upward paths classify.

## The numbers this site stands on

- **43** concepts, each with a stable anchor and a JSON definition — 42 drawn from ~496,000
  words, one [authored here](examples/execution-boundary/index.html#new)
- **6** rungs on the interval ladder, default one month
- **0** lines of code implementing any of it
- **5** live vaults, published with read keys — 504 files, 116 commits, one of them built here
- **59 nodes / 75 edges** in the largest worked graph; **51/53** in the 2FA graph; **1,523/1,944** in the regulation graph
- **30 days vs 6 months** — logs retained against logs required, *"arithmetic, not judgement"*
- **12–18 hours** of hyperscaler cost-reporting delay: a hard detection floor
- **3** verdicts at [the execution boundary](examples/execution-boundary/index.html) — and the third,
  *cannot establish*, is the one most systems quietly treat as a pass

## Two sites, one boundary

[riskmandate.ai](https://riskmandate.ai) answers *"how do I get my risks accepted, and what
does it cost?"* — pricing, demos, partners, the product walkthrough. **risks.sgit.ai**
answers *"what is a risk, what is acceptance, and why is it modelled this way?"* The
dependency runs one way: the commercial site cites the research site, never the reverse for
a conceptual claim. [The eight-site boundary map](network/index.html).

## For agents

The commissioned audience for this site is agents, so the machine surface is a deliverable
rather than a courtesy:

- [`/data/concepts.json`](data/concepts.json) — all 43 concepts as structured data: id, name,
  one-line definition, maturity, `origin`, canonical source, page, related concepts
- [`/llms.txt`](llms.txt) — the annotated map, each entry carrying its page's single most
  important fact rather than its topic
- [`/llms-full.txt`](llms-full.txt) — the whole site plus all eleven source documents in one fetch
- [`/briefs/<filename>`](briefs/00__BRIEF.md) — every source document at a stable constructed path
- [`/concepts/`](concepts/index.html) — 43 stable anchors, `#c1` to `#c43`, checked by CI

Reading order for an agent with no prior context: C1 → C2 → C3 → C4 → C5, then C6 → C7, then
C19 → C20–C23, then the rest.

## The site

- [`/acceptance/`](acceptance/index.html) — the founding inversion, five pages
- [`/acceptable/`](acceptable/index.html) — accepted is not acceptable; appetite as a revealed band
- [`/ladder/`](ladder/index.html) — the grounding ladder, node type formulas, bridges, absence
- [`/register/`](register/index.html) — the register as a graph of graphs, fractal registers, cascade
- [`/blast-radius/`](blast-radius/index.html) — authorization closure and CIA expansion
- [`/plug/`](plug/index.html) — who can pull the plug; recoverability as the hard limit
- [`/practice/`](practice/index.html) — owners, altitude, psychology, density, meta-risks
- [`/ramm/`](ramm/index.html) — the maturity models, and where they are underspecified
- [`/examples/`](examples/index.html) — three worked graphs, five live vaults, ten scenarios
- [`/examples/execution-boundary/`](examples/execution-boundary/index.html) — **the one page that
  computes**: can an authorization still be established at the moment of execution? A live vault
  app, read key in the open, with one of its four runs deliberately wrong
- [`/concepts/`](concepts/index.html) — all 43, addressable
- [`/agents/`](agents/index.html) — the machine surface
- [`/shipped/`](shipped/index.html) — what is argued and what runs
- [`/origins/`](origins/index.html) — February 2026 classical GRC to the August formalisation
- [`/network/`](network/index.html) — the boundary map, eight open questions, seven honest tensions

---

Published by the sgit project, which also builds riskmandate.ai — the commercial product
this research underpins. [Participant disclosure](about/participant.html). All content CC BY
4.0 unless a page states otherwise.
