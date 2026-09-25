# 7. The first ninety days

## Weeks 1 to 2: the contract

- Fix the journal entry format (`spec/journal-entry.md`) and the chain rule.
- Stand up the agent-reported capture instruction (`prototypes/agent-reported-capture.md`) for Gmail and Calendar.
- Create one vault per customer with an append lane, and a read-key-only replay.

**Done when:** a real agent session against a test Google account lands in a lane and replays in the app.

## Weeks 3 to 6: the gateway and the processor

- Build the gateway for MCP traffic: copy each `tools/call` and result, plus the upstream request and response where the connector exposes them.
- Build the processor on a timer and on a pending-count threshold (`prototypes/processor-schedule.md`).
- Write the Gmail and Calendar view folders: the inbox, the calendar, the timeline.

**Done when:** a day of real use by one design partner is captured completely and replays.

## Weeks 7 to 10: revert

- Implement `spec/revert-rules.md` for the Gmail and Calendar actions in scope.
- Add the supervised revert: plan, approve, execute through the gateway, journal the result.
- Run a replay drill with each design partner: pick a real session, answer "what did it do, what did it see, what can we put back" in under thirty minutes.

**Done when:** a revert has been executed on a real, non-critical change and journalled.

## Weeks 11 to 13: price and sell

- Convert design partners to paid tiers at the hypothesis prices, and record who refuses and why.
- Offer the irreversibility map to twenty prospects; count how many turn into a review.
- Sign one managed service provider.

**Done when:** five paying customers, one reseller, and a written account of which prices held.

## Team

Two founders: one who can build the gateway and the processor, one who can sell to CISOs and MSPs. A part-time security reviewer from week 6, because the first serious customer will ask for the threat model.
