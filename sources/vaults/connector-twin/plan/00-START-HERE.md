# Connector Twin, the one-page version

**The business.** Give every organisation that deploys AI agents a twin of the connectors those agents use. The twin is a journal of every request and response the agent makes to Gmail, Google Calendar, Drive, Slack or any other connected system, replayed into the views the agent saw, with a before and after for every change and a revert plan for each one.

**The question that sells it.** *Do you know what your agents did?* Most organisations cannot answer it today, and for several of the actions a connector allows, the platform itself keeps no way back. That is a fact, documented by the platforms, not a fear.

**Why now.** Assistants now ship with Gmail, Calendar, Drive and Slack connectors, and people are switching them on. An agent with those connectors can send, move, decline and permanently delete on somebody's behalf. Its own summary of what it did is the only record most deployments keep.

**What you sell.**

| | Price, as a hypothesis |
|---|---|
| Connector review, once | £750, £2,500 or £6,000 by size |
| Journal, per agent per month | £15 |
| Twin, per agent per month | £40 |
| Assured, per agent per month | £90 |
| Incident replay | £900 per incident |

**Where it runs.** Hosted by you, in the customer's cloud, or reported by the agent itself. The capture mode sets how strong the evidence is, not the price.

**Why it is buildable now.** Nothing in it needs new technology. Vault append lanes already accept write-only, blind entries. A vault app, like the one in this vault, already rebuilds views from a journal and verifies its chain in the browser. Models already write the per-connector views. The one piece that needs more thought is the schedule on which the journal is processed, and that needs real users more than it needs design.

**The economics, as hypotheses.** Infrastructure is about £3.10 per agent per month. At the Twin price, about 380 agents cover a two-founder burn of £14,000 a month: roughly 38 customers with ten agents each.

## Reading order

1. `01-the-idea.md`: what a connector twin is, and what it is not.
2. `02-the-facts.md`: what Gmail and Calendar keep for you and what they do not, with sources.
3. `03-architecture.md`: capture, append, chain, process, replay and revert.
4. `04-the-service.md`: packages, capture modes, and what the customer gets.
5. `05-business-model.md`: prices, costs, margins and the calculator's assumptions.
6. `06-go-to-market.md`: who buys first, and the free thing that opens the door.
7. `07-execution.md`: the first ninety days.
8. `08-why-invest.md`: the case for backing it.
9. `09-risks.md`: what could sink it, and what to do about each.
10. `10-open-questions.md`: what we do not know yet.
