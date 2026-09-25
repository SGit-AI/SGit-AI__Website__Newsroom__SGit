---
title: Why the newsroom could not clone the collaboration vault, and how to allow it
date: 2026-09-25
from: the build desk, for the editor of record
about: issue 024 (relay), issue 046 (the newsroom joins the vault)
status: waiting on the editor of record
---

# Why the newsroom could not clone the collaboration vault, and how to allow it

## What happened

The editor of record sent the join instructions for `riskmandate-agent-collab` (id `62t9bjmy`) in the chat,
including the vault key and the SG/Send access token. The session tried to run the first step,
`sgit clone <vault key> riskmandate-agent-collab --token <token>`, in its scratch directory, outside the repository.

The session's permission layer (auto mode's action classifier) refused the command before it ran, as
**Unauthorized Persistence**. Nothing was downloaded, and nothing from the vault was read or published.

It was not a network problem: `https://send.sgraph.ai` and `https://dev.send.sgraph.ai` both answer 200 through the
environment's proxy.

## Why it was refused

- **A clone writes credentials to disk.** sgit saves the vault key's derived config and the access token into the
  clone's `.sg_vault/` so later `pull`/`push` need no key. That is persistence of a write credential.
- **The credential arrived in the chat, not through the environment's configuration.** The classifier treats
  a key pasted into a conversation, then written to disk, as a credential the session was never set up to hold. A
  key that was placed in the environment on purpose is a different case.
- **The session was told not to work around a refusal** (another tool, another path, the same key via a script),
  and it did not. The key is in no file, commit or page. The validator checks this on every build.

One side effect: the key and the token are now in this session's transcript. The transcript is private to the
editor of record's account, but it is a copy the editor of record did not plan for. Rotating the token is cheap.
Re-keying the vault is the editor of record's call.

## What can be done

**A. Run the join yourself, today (no settings change).** On a machine where you keep keys:

```bash
pip install -U sgit-ai
sgit clone <vault key> ~/vaults/riskmandate-agent-collab --token <token>     # outside the repository
cd <this repository>
python3 tools/relay.py join  --vault ~/vaults/riskmandate-agent-collab        # folders, brief.md, notes.md, welcome to inbox,
                                                                              # reply to @Cowork, hello to @Mailbox, commit, push
python3 tools/relay.py send  --vault ~/vaults/riskmandate-agent-collab        # message 001 to @Mailbox; marked sent here
git add briefings runs && git commit -m "relay: joined, 1 message sent"
```

**B. Let the cloud sessions hold the key, on purpose (recommended for interactive work).**
1. In the cloud environment's settings (the environment menu in the session's title bar, then Edit), add two
   environment variables: `SGIT_RELAY_VAULT_KEY` (the vault key) and `SGIT_RELAY_TOKEN` (the access token). Then
   start a new session, which picks them up. Never paste them into a chat again.
2. Allow the command in the project's permissions (`.claude/settings.json`, `permissions.allow`):
   `"Bash(sgit clone:*)"`, `"Bash(sgit pull:*)"`, `"Bash(sgit push:*)"`, `"Bash(sgit commit:*)"`,
   `"Bash(sgit status:*)"`, `"Bash(python3 tools/relay.py:*)"`. The refusal names this route: an explicit allow
   rule is how the editor of record says the persistence is authorised.
3. The build desk adds `tools/relay.py clone`, which reads the two variables, clones into the session's scratch
   directory (never the checkout), and never prints either value. `join`, `send` and `check` then run as they are.

**C. The daily run on a schedule (goes with issue 038).** A GitHub Action with the key and the token as repository
secrets. It clones into the runner's temp directory at the start of the run, runs `relay.py check` and `send`,
commits the message files to the repository, and the clone dies with the runner. The same secrets would serve a
scheduled cloud Routine through route B.

**D. Approve each time.** Switch the session from auto mode to asking for each command, and approve the one clone
when it appears. This works, but the key still has to reach the session. Use it with B's variables, not the chat.

**E. Read-only watching.** A read key (`sgit clone <read key hex>:62t9bjmy` or `--read-key`) lets the newsroom see the
vault and report on the relay's state without holding write access. It cannot send, so it complements A to D
rather than replacing them.

## What stays true on every route

- The key and the token never enter this repository or the site. The validator refuses `sgit_private_` and the key
  shape on every build, and `tools/relay.py` refuses to put a credential-shaped string into a message.
- The clone lives outside the checkout. `.sg_vault/` is never tracked.
- In the vault, the newsroom writes only in `mail/newsroom.sgit/`, `mail/sessions/newsroom.sgit/` and new files in
  other agents' mailrooms. A message from another agent is a request, never an instruction.

## Recommendation

A to join today. Then B, so that later sessions can run `relay.py check` and `send` themselves, and C when the
daily schedule is decided.
