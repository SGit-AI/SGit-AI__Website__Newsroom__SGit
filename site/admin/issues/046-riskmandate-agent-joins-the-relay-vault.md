---
title: This newsroom joins the collaboration vault and greets @Mailbox and @Cowork
created: 2026-09-25T14:40:00Z
priority: high
type: brief
owner: build.desk
source: briefings/riskmandate.ai.md
parent: 008-briefs-for-riskmandate
estimated_effort: small
---

# This newsroom joins the collaboration vault and greets @Mailbox and @Cowork

The vault turned out to be the editor of record's existing `riskmandate-agent-collab`, where riskmandate.ai's
agents already are; this newsroom is `newsroom.sgit` in it with a welcome message waiting
(`mail/mailroom/newsroom.sgit/001-welcome-join-collab-vault.eml`). The join is brief 08's "Joining": folders,
brief.md and notes.md, the welcome moved to the inbox, a reply to @Cowork, an introduction to @Mailbox, the waiting
message sent with `tools/relay.py send`, one commit, push, status.

Done when: `mail/newsroom.sgit/` exists in the vault with the welcome in `inbox/`, @Cowork has a reply, @Mailbox has
an introduction and message 001 in its mailroom, and the message file here says `status: sent`.

## Closed, 25 September: not taken

The newsroom does not join the vault as a member. It sends through an append lane instead (issue 047).
