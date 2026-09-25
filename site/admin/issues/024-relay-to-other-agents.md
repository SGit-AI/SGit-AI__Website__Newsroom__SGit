---
title: Relay feedback addressed to another site's agent
created: 2026-09-25T12:05:00Z
priority: high
type: task
owner: editor.desk
source: admin/inbox/2026-09-25__notes-from-the-flight.md
parent: 003-chat-and-relay
blocked_on: the editor of record creates the relay vault (sgit create sgit-network-relay) and puts its id in data/relay.json
estimated_effort: medium
---

# Relay feedback addressed to another site's agent

Feedback that starts "For the RiskMandate agent:" (or names a site) is filed as a message for that agent:
into `briefings/<site>/inbox/` here and shown on that site's briefing page; when a channel exists
(agent@riskmandate.ai's mailbox, an append lane, a vault), sent. The first message is in the notes: ask the
contact who received the voice questionnaire link for feedback, with an introduction, expecting "this is
too much, can this be simpler".

Done when: the chat and the note field recognise the address; the message lands on the briefing page; the
daily run's report lists unsent messages.

## Design and build, 25 September

Channel chosen by the editor of record: a shared sgit vault, Email-FS-lite (sgraph.ai's protocol; the eight pages
are in the snapshot under sources/sites/sgraph.ai/). Built: `data/relay.json` (identities, peers, vault id when it
exists), `tools/relay.py` (send: unsent messages to `.eml` in the mailroom and outbox, commit, push, mark sent;
check: pull, mark delivered/handled from the mailroom and done/ folders, deliver replies into
`briefings/<site>/inbox/` as incoming pages; status; dry-run), `brief/08-relay.md`, the briefing page's message
states. Blocked on the one step only a person does: create the vault and hold the key. Then `relay.py send` sends
the first message.
