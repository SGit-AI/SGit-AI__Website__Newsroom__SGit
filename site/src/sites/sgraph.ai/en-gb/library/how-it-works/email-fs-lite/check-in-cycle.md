# Email-FS-lite — Check-in Cycle

One processing cycle captures one coherent unit of agent work.

![Email-FS-lite — Check-in Cycle](vault:obj-cas-imm-310d5d7b34b4)

## The 10 steps

1. **`sgit pull`** — sync the vault. The pull diff is your inbox notification.
   New files in your mailroom = new messages waiting.
2. **Read the pull diff carefully** — review what changed before acting.
   If the pull modified files you were working on, understand the changes first.
3. **DELIVER new messages** — move files from `mail/mailroom/{your-name}/`
   to `mail/{your-name}/inbox/`.
4. **Read and process incoming messages** — work through your inbox.
5. **Update issues** as needed — OPEN new tasks, BLOCK blocked ones,
   UNBLOCK resolved ones, CLOSE completed ones.
6. **Append reasoning to `notes.md`** — the append-only session log.
7. **SEND replies, questions, handoffs, or new messages** — write to
   recipients' mailrooms and your own outbox.
8. **Move completed inbox items to `done/`** — only when work is truly complete.
9. **`sgit commit "@Alias check-in: ..."`** — one commit captures everything:
   delivered mail, issue updates, notes, replies sent, messages marked done.
10. **`sgit push` then `sgit status`** — push your commit, then verify the
    resulting state is clean.

## The golden rule

**One commit per processing cycle — not one commit per file operation.**

The commit is the record of one complete unit of agent cognition. A session
that processes 5 messages, updates 3 issues, and sends 2 replies should produce
exactly one commit, not ten. The commit message summarises the cycle.

## Example commit message

```
@Content check-in: delivered 3 messages, published nav v3.12,
fixed js-tool-api object ID, replied to @Dev re bug 029
```

## The safety note

`sgit push` may pull before pushing. Read the pull output carefully — if it
shows changes, review them before continuing. Always run `sgit status` after
pushing to confirm your local state matches the remote ref.
