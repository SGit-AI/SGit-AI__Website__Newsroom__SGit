# Email-FS-lite — Audit, Verification & Recovery

Why sgit is the substrate that makes the protocol auditable and recoverable.

![Email-FS-lite — Audit, Verification & Recovery](vault:obj-cas-imm-72080c980377)

## 1. Audit

Every `sgit pull` output acts as an inbox notification. The pull diff shows
exactly what was added, modified, or deleted since your last sync. New files
in your mailroom are new messages.

`sgit history log` shows the activity story over time — one entry per
processing cycle, with the agent name, timestamp, and a summary of what
was done. The complete history of the collaboration is always recoverable.

## 2. Verify

After every `sgit push`, run `sgit status`. A clean status confirms your
local state matches the remote ref. If the push pulled remote changes first,
read those changes carefully before continuing — they may affect files you
were working on.

## 3. Recovery

When a bad commit is made, the recovery path is:

**Step 1 — Find the last good commit:**
```
sgit history log --max 10
```
Identify the commit hash before the bad one.

**Step 2 — Rewind to the good commit:**
```
sgit history reset <good-commit-hash>
```
Your local view rewinds. The bad commit becomes orphaned locally.

**Step 3 — Overwrite the remote ref:**
```
sgit push --force
```
The bad commit is removed from the remote. Content-addressed objects are
not immediately deleted — the bad commit becomes orphaned and is garbage
collected only after normal retention windows.

## A note on the conflict loop

The recovery diagram shows `sgit history reset` as a reliable escape route.
In practice, this requires the commit objects to be cached locally. After a
standard clone, older commit objects may not be cached, making reset unavailable.

This was encountered during this project — both `sgit history reset` and
`sgit merge-abort` (referenced in pull output but not implemented) were
unavailable during a conflict loop. A full brief has been filed with the
sgit team. The workaround is a fresh clone with backup-and-reapply.

See the [sgit conflict resolution brief](../../reference/sgit-brief-conflict-loop)
for the full account and proposed fixes.
