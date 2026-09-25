# 2. The method, and where it comes from

The method is already published across four places. This plan adopts it and points at the sources rather than restating them in full.

- **risks.sgit.ai**: the model. No deny button, the interval ladder, accepted versus acceptable, unaccepted as critical, fractal registers, and an honest inventory that states, in capitals, that essentially none of it is implemented in code. https://risks.sgit.ai/
- **RiskMandate.ai**: acceptance applied to AI agents, the licence to operate, the plug profile, and "Accepted is not acceptable". https://riskmandate.ai/
- **graphs.sgit.ai**: fractal risk registers, "one register per accepting entity", and the chain from a database administrator's risk to the board's. https://graphs.sgit.ai/v1/docs/fractal-risk-registers.html
- **The Risk Graph Explorer vault**: the chain to the board, computed, with "assigned" versus "through", risk chains, acceptance per role, and what happens next. https://sgit.ai/demos/vaults/risk-graph-explorer/index.html

## The principles

The ten principles the app displays are in `plan.json`. The ones that carry the business:

1. Every risk is already accepted; the question is by whom, and for how long.
2. There is no deny button.
3. Accept, fund or fix. Silence escalates.
4. The interval is the decision.
5. A named person, and no delegation.
6. Every path ends at the board.
7. Accepted is not acceptable.
8. Established by facts, ended by facts.
9. GRC validates, the business accepts.

## The ladder

As published on risks.sgit.ai:

| Rung | What it means |
|---|---|
| 1 hour | "I need more data." Fetch it now. |
| 4 hours | A priority-one incident. Trigger incident response. |
| 1 to 2 days | A smaller incident. |
| 1 to 2 weeks | A funded project for a team that already exists. |
| 1 month | Assemble and fund. The default rung, set just above the incident line. |
| 6 months | Do nothing, and review it then. Legitimate, with a name on it. |

RiskMandate.ai's "Accepted is not acceptable" page publishes different bands (1 to 24 hours, 1 day to 1 week, 1 week to 1 month as the default, 1 to 3 months, over 3 months). The plan uses the risks.sgit.ai ladder and lists the reconciliation as an open question.

## Accepted is not acceptable

Accepted is an act by a named person at a dated moment. Acceptable is a threshold: in RiskMandate's words, "the moment that the business is happy to stop funding remediation activities". They are two separate questions with four combinations, and the dangerous one is a risk over the line that nobody has accepted.

The EU AI Act makes this concrete for one class of organisation. Article 9(5) of Regulation (EU) 2024/1689 requires providers of high-risk AI systems to adopt risk management measures "such that the relevant residual risk associated with each hazard, as well as the overall residual risk of the high-risk AI systems is judged to be acceptable". The Act never defines "acceptable". The duty to judge is imposed, and the standard is not supplied, so an organisation has to draw its own line and be able to show it did. Sources: https://eur-lex.europa.eu/eli/reg/2024/1689/oj and https://artificialintelligenceact.eu/article/9/.

## What the method does not yet say, and this plan proposes

- **What happens at expiry.** risks.sgit.ai lists this as open: who is told, what changes, whether anything blocks. The plan's operating model proposes an answer: the same decision returns to the same desk, and if nobody renews, it escalates one level.
- **Whether unaccepted risk rolls up automatically.** The Agentic Browser Isolation vault describes a risk that "sits pending until that owner accepts it personally". risks.sgit.ai says unaccepted rolls upward. The plan takes the second, because silence has to cost something.
