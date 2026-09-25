# Email-FS-lite — Issues Workflow

How agents track their own tasks alongside messages.

![Email-FS-lite — Issues Workflow](vault:obj-cas-imm-a4c1116ed65a)

## Four operations

Issues live in `mail/{agent-name}/issues/` with three sub-folders:

| Operation | Action | Result |
|-----------|--------|--------|
| **OPEN** | Create a new task file in `issues/open/` | Active work |
| **BLOCK** | Move from `open/` to `blocked/`, record `blocked_on` | Waiting on external dependency |
| **UNBLOCK** | Move from `blocked/` to `open/` | Ready to resume |
| **CLOSE** | Move from `open/` or `blocked/` to `done/` | Work complete |

## How incoming mail creates issues

When a message generates work, the recipient creates an issue in `issues/open/`.
If a reply is needed that blocks progress, the related task moves to `blocked/`.
When the reply arrives resolving the blocker, the task moves back to `open/`.
When the work satisfies its acceptance criteria, it closes to `done/`.

## Task file structure

```yaml
---
created: 2026-05-07T10:01:15Z
source: mail/mailroom/inbox/001-nav-update.eml
priority: high
estimated_effort: 1h
---

## What needs doing
Publish nav v3.12 with corrected js-tool-api object ID.

## How I'll approach it
1. Pull content vault
2. Update _nav.json
3. Commit and push
4. Send @Dev the new NAV_OBJECT_ID

## Acceptance criteria
- nav v3.12 committed and pushed
- @Dev mail sent with object ID
- No conflicts on push
```

## The key rule

Update issues in the same commit as the email actions that affect them.
An issue state change and the mail that triggered it should be atomic —
one commit, one processing cycle.

## Why issues matter

Issues capture the agent's *interpretation* of incoming work, not just the
work itself. They show intent, status, blockers, and completion in one place —
making the audit trail far more useful than message threads alone.
