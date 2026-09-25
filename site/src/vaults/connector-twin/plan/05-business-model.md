# 5. Business model

Recurring revenue per agent, a set-up fee per customer, and paid incidents. Every number below is a hypothesis to test, with the arithmetic shown so it can be redone with better inputs.

## Unit costs

| Item | Assumption | Per agent per month |
|---|---|---|
| Journal volume | About 500 connector calls a day at about 20 KB per call and response: 10 MB a day, 0.3 GB a month | |
| Storage | About 0.02 USD per GB per month. A year of retention is about 3.6 GB | under £0.10 |
| Broker, gateway and processor compute | Estimated at small scale | about £3.00 |
| **Infrastructure** | | **about £3.10** |

Storage is not the cost. Compute and, above all, support are. Budget support as people, not as a percentage.

## Margin per tier

| Tier | Price | Infrastructure | Infrastructure margin |
|---|---|---|---|
| Journal | £15 | £3.10 | 79% |
| Twin | £40 | £3.10 | 92% |
| Assured | £90 | £3.10 | 97%, before the evidence packs and replays, which are people-time |

## Break-even

Two founders at £6,000 a month each fully loaded, plus £2,000 a month of tooling, is £14,000 a month. At the Twin price less infrastructure, £36.90 per agent, that is about **380 agents**: roughly 38 customers with ten agents each. Set-up fees and incident replays shorten the path; they are not counted here because they are lumpy.

The calculator in the app lets every one of these inputs move.

## Shape of the first two years, as a scenario

| | Customers | Agents | Monthly recurring |
|---|---|---|---|
| Month 3 | 5 design partners | 30 | £0: free while they are design partners, worth about £1,200 at list price |
| Month 12 | 40 | 400 | about £16,000 |
| Month 24 | 150 | 2,000 | about £80,000 |

A scenario, not a forecast. The month-12 line is the one to test hardest: it assumes an average of ten agents per customer on the Twin tier.

## What moves the numbers

- **Agents per customer.** The price is per agent, so the business grows with adoption inside each customer, not only with new logos.
- **Tier mix.** Assured customers are few and worth a lot; they are also the ones who will ask the hardest security questions.
- **Channel.** Managed service providers selling the service to their own clients change customer acquisition cost more than any price change does. See `06-go-to-market.md`.
