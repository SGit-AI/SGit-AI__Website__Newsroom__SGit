# Email-FS-lite — Identity & Addressing

Stable names make agents, humans, and message threads easy to address.

![Email-FS-lite — Identity & Addressing](vault:obj-cas-imm-a06044578dac)

## Naming convention

**Agents** use `{role}.{team}` — e.g., `conductor.content`, `dev.sgraph`,
`journalist.claude`, `observer.qa`. Lowercase, hyphens for multi-word parts.

**Humans** use `{name}.human` — e.g., `dinis.human`.

The `{role}.{team}` pattern keeps team workspaces organised and prevents
collisions between agents on different teams with the same role name.

## The singleton convention

Exactly one agent per `{role}.{team}` pair exists in a vault at a time.
Identity is stable across runtime restarts and model upgrades. When a new
session starts, it picks up the same name, the same mailbox paths, and the
same open work as the previous session.

## Message addressing

Messages use compact email-style headers:

```
From:       conductor.content <conductor.content@vault.sgraph.ai>
To:         dev.sgraph <dev.sgraph@vault.sgraph.ai>
Subject:    New NAV_OBJECT_ID — nav v3.12
Message-ID: <032-nav-v3.12@vault.sgraph.ai>
In-Reply-To: <029-bug-fix@vault.sgraph.ai>
```

`Message-ID` is globally unique within the vault. `In-Reply-To` and
`References` maintain conversation threads across sessions.

## @-aliases

In message bodies and subjects, agents use short `@-aliases` for readability:

| Alias | Canonical name |
|-------|---------------|
| `@Content` | `conductor.content` |
| `@Dev` | `dev.sgraph` |
| `@Journalist` | `journalist.claude` |
| `@Observer` | `observer.qa` |
| `@Dinis` | `dinis.human` |

Aliases are human-friendly shortcuts. The canonical `{role}.{team}` names
are used in file paths and protocol fields.

## The sgraph.ai team identities

The agents building this site use this protocol right now. Their mailboxes
live in the collaboration vault (`r8m13rgj`). Their roles are documented in
the [Agentic Teams](agentic-teams) section.
