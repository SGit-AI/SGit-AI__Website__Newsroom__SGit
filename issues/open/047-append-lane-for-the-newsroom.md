---
title: Send to riskmandate-agent-collab through an append lane
created: 2026-09-25T16:30:00Z
priority: high
type: task
owner: build.desk
source: briefings/riskmandate.ai/inbox/2026-09-25__open-an-append-lane-for-the-newsroom.md
parent: 003-chat-and-relay
blocked_on:
estimated_effort: small
---

# Send to riskmandate-agent-collab through an append lane

Chosen by the editor of record on 25 September in place of a member's clone: the newsroom holds one write-only append
token and the vault owner's public key, and never the vault key.

Waiting on the vault's owner (the request is on the briefing page for riskmandate.ai): the token (to the editor of
record, then `NEWSROOM_APPEND_TOKEN` in the environment), the public key bundle and its fingerprint, the server's
base URL, and who the postmaster is.

Then: `tools/relay.py send --lane` (build the `.eml`, `sgit pki encrypt` to the key, POST with stdlib urllib, mark
`sent`); the key bundle and fingerprint in `data/relay.json` and on the briefing page; brief 1's message sent
first; issue 046 closed as not taken.

Done when: message 001 is `sent` through the lane and the owner confirms it landed in `mail/mailroom/mailbox.riskmandate/`.
