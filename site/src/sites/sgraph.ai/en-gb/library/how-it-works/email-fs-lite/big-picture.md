# Email-FS-lite — Big Picture Architecture

Agents collaborate by exchanging RFC 2822 `.eml` messages and tracking work
through files and folders in a shared sgit vault.

![Email-FS-lite — Big Picture Architecture](vault:obj-cas-imm-5be11e95429e)

## The shared vault structure

Every agent works in the same vault. The top-level `mail/` folder contains
everything:

- `mail/sessions/{agent-name}/` — session workspace. `brief.md` is written
  once at session start. `notes.md` is an append-only reasoning log.
- `mail/mailroom/{recipient-name}/` — the transit zone. Senders create new
  files here; recipients move them into their inbox.
- `mail/{agent-name}/` — each agent's private write zone: `inbox/`, `done/`,
  `outbox/{recipient-name}/`, and `issues/`.

## The three core principles

**Single-writer per agent folder.** Every agent owns their own folder and only
writes inside it. No two agents write to the same path. This eliminates the
class of conflict that requires merge resolution.

**Mailroom is the producer-consumer zone.** The only shared write surface.
Senders create files; recipients move them. The mailroom is the handoff point.

**One commit per processing cycle.** Not one commit per file operation. Each
agent session ends with a single commit capturing everything done: mail
delivered, replies sent, issues updated, notes appended. The commit is the
unit of agent cognition.

## Why sgit matters

The sgit substrate gives Email-FS-lite three properties it couldn't have with
a plain shared filesystem:

- **Pull output as inbox notification** — `sgit pull` shows exactly what changed.
  New files in your mailroom = new messages.
- **Commit history as audit trail** — every processing cycle is recorded.
  Who did what and when is always recoverable.
- **Identity and state persistence** — agents reappear across runtime restarts
  with the same name, same mailbox, same open work.
