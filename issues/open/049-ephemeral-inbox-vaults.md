---
title: Ephemeral inbox vaults: an agent receives messages through a vault it creates for one session
created: 2026-09-25T19:40:00Z
priority: high
type: epic
owner: build.desk
source: admin/inbox/2026-09-25__ephemeral-inbox-vaults.md
parent: 003-chat-and-relay
estimated_effort: medium
---

# Ephemeral inbox vaults

The pattern: an agent that wants to receive messages creates a vault for one session, opens an append lane on it for
each expected sender, publishes the vault id, the endpoint and the public key to encrypt to on the website that is its
identity, hands each sender its append token privately, drains the lane while the session runs (fetch, decrypt, verify,
file, mark processed, purge), and deletes the vault when the session ends. A long-lived recipient (the postmaster of
riskmandate-agent-collab) keeps a permanent vault and drains it at its check-ins. Two vaults, one lane each, each
drained by its owner.

State on 25 September: `newsroom-inbox-2026-09-25` created on dev.send.sgraph.ai with a README; no lane configured.
Configuring, purging and deleting need the vault's write key; the session's permission layer refused materialising
it ("Credential Materialization"), and nothing was tried around that.

Done when: a message from @Cowork arrives in the temporary vault, is drained into briefings/riskmandate.ai/inbox/ as
incoming with a verified signature, and the vault is deleted at the session's end.

## Progress, 26 September

Allowed by the editor of record (the tool may hold the session vault's key; never the chat, never the repository).
`relay.py inbox open|selftest|drain|close` built; the inbox `9c7vcrw4` opened with a lane for @Cowork, self-tested,
published, offered to @Cowork through the lane, and @Cowork's first reply drained, verified and filed. Left: `inbox
close` at the end of the session (the entry marked closed, the vault destroyed); then this is done.
