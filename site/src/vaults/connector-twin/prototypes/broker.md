# The broker, as a design

The broker is the execution broker from [twins.sgit.ai](https://twins.sgit.ai/broker/index.html), applied to connectors. The agent never holds a platform credential. It asks the broker to perform an operation; the broker checks the agent's identity and mandate, performs the operation with credentials held inside its own boundary, journals the request and response, and returns the result with a receipt.

## Why it is the strongest mode

Nothing reaches the platform API except through the broker, so the journal is complete by construction. The mandate check also means the broker can refuse: a permanent delete can require a person's approval, a send can be limited to known recipients, and the refusal is journalled too.

## What it costs

- **It concentrates credentials.** The broker is the highest-value target in the estate. Keep it small, run it in the customer's account where possible, and never let it hold more scopes than the agents behind it need.
- **It needs an interpreter per service.** To enforce a mandate, the broker has to understand what each operation does, per provider and per operation class. Gmail and Calendar first; each new connector is real work.
- **It sees traffic in flight.** What it stores is encrypted, but a hosted broker handles plaintext while it works. Say so to the customer.

## Minimum viable broker

An HTTP service with one endpoint per supported operation, a per-agent mandate file listing allowed operations and which need approval, OAuth tokens held in the platform's secret store, and an append to the journal lane after every upstream response. Everything else, including receipts signed with the broker's key, can follow.
