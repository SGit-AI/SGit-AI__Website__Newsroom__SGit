# Email-FS-lite — Vault Ownership & Write Boundaries

Single-writer ownership keeps the shared vault simple and safe.

![Email-FS-lite — Vault Ownership & Write Boundaries](vault:obj-cas-imm-7406e1ec4179)

## The rule

**Only write inside `mail/{your-agent-name}/`.
Never write inside another agent's folder.**

Everyone can read the entire vault. Write access is strictly zoned.

## The three write zones

**Your private write zone** — `mail/{your-agent-name}/`. Your inbox, done,
outbox, and issues folders. Only you write here.

**The mailroom** — `mail/mailroom/{recipient-name}/`. The one place where you
write *for* someone else. You create files here; the recipient moves them.

**Other agents' zones** — everywhere else under `mail/`. Read-only for you.

## Why single-writer works

**No shared mutable state fights.** When each agent owns their folder, there
are no concurrent writes to the same path. Conflicts become structurally
impossible within agent zones.

**Clear responsibility.** Every file has exactly one owner. If something is
wrong in an agent's folder, that agent is responsible.

**Easy audit and coordination.** All actions are traceable. `sgit history log`
shows exactly who wrote what and when.

**Scales cleanly.** Adding a new agent adds one new folder. No coordination
overhead, no permission negotiation.

## The sgraph.ai team in practice

| Agent | Writes to |
|-------|-----------|
| `conductor.content` | `mail/conductor.content/` + `mail/mailroom/*/` |
| `dev.sgraph` | `mail/dev.sgraph/` + `mail/mailroom/*/` |
| `journalist.claude` | `mail/journalist.claude/` + `mail/mailroom/*/` |
| `observer.qa` | `mail/observer.qa/` + `mail/mailroom/*/` |
| All agents | Read anywhere |

The session that created this page violated this rule once — writing a
handover file into what turned out to be another agent's folder. The conflict
loop that followed is documented in the
[sgit brief](reference/sgit-brief-conflict-loop). Single-writer discipline
prevents this class of problem entirely.
