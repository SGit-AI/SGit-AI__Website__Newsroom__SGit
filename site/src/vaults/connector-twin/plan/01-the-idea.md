# 1. The idea

## A twin of the connector, not of the world

On [twins.sgit.ai](https://twins.sgit.ai/) a digital twin is *an interface to reality, not a simulation of it*: a system with properties, behaviours, functions, inputs and outputs, valued for its connection to the real thing rather than for its fidelity. A connector twin narrows that to one place: the boundary between an agent and a system it has been allowed to act on.

It holds two things:

1. **What the agent could do.** The scopes it was granted, and the actions those scopes allow, marked by whether the platform lets them be undone.
2. **What the agent did.** Every call, request and response, in order, hash-chained, and when prompt capture is on, the instruction that led to it.

From those two, it rebuilds a third: **what the agent saw.** The inbox, the calendar, the folder, as they looked to the agent at each step, reconstructed from the responses it received.

## Why the view matters more than a copy

A backup copies the mailbox. A twin does not need to. It keeps only what passed through the connector, which means it scales with the agent's activity rather than with the size of the mailbox, and it answers a different question. A backup tells you what the inbox contained. A twin tells you what the agent was looking at when it decided to act. For accountability, for an investigation, and for explaining a decision to somebody who was not there, that is the question that matters.

It also means the twin holds nothing the agent did not already touch. If the agent never opened a message, the twin knows its id and nothing more. That is a privacy property worth selling, not a gap to apologise for.

## Why it makes undo possible

For every change the agent makes, the twin holds the state before and the state after, because the agent read the before-state to make the change and the response returned the after-state. That is enough to write the inverse call. Where the platform has an undo, the twin names it. Where it does not, the twin says so, and says what it can still put back: the content of a permanently deleted message, for instance, if the agent read it in full first.

## What changes for the organisation

The agent behaviour policy, the document that says what an agent may reach, what it is authorised to do and who accepts the residual risk, reads differently with a twin behind it. *"We cannot undo it"* stops being an unknown and becomes a list: sent emails, notifications to attendees, permanent deletes. The list is what the mandate is written against. An agent can be allowed to archive freely and required to ask before it permanently deletes, because somebody can now see which is which.

## What it is not

- **Not a backup of the mailbox.** It holds what the agent touched. A customer who needs full backup still needs a backup product.
- **Not a platform audit log.** Audit logs record that an event happened. The twin records the request, the response and the state either side of it.
- **Not a guarantee in every capture mode.** An agent reporting its own calls can leave one out. The broker mode cannot be bypassed; the agent-reported mode can, and the policy says so.
