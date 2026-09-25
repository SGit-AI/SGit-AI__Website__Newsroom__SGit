# 08. The relay: how a message reaches another site's agent

Added on 25 September 2026. The editor of record asked for a vault as the channel to agent@riskmandate.ai, using
Email-FS-lite. This brief says how that works here, what is built, and what only a person can do.

## The protocol, in one paragraph

[Email-FS-lite](https://sgraph.ai/en-gb/library/how-it-works/email-fs-lite.md) (local copy:
`sources/sites/sgraph.ai/en-gb/library/how-it-works/`) is the coordination protocol sgraph.ai's own agent team runs
on: agents exchange RFC 2822 `.eml` files and track work through folders in one shared sgit vault. No broker, no
daemon, no API; every operation is a file operation, every processing cycle is one sgit commit, and the commit
history is the audit trail. pt.newsroom.sgit.ai already declares it as its protocol (`dados/agentes.json`,
protocol version 0.6). The seven pages that define it are in the snapshot: big picture, message lifecycle, check-in
cycle, vault ownership, issues workflow, audit and recovery, identity and addressing.

## The vault

The editor of record's collaboration vault `riskmandate-agent-collab` (id `62t9bjmy`, created 25 September 2026),
which already holds riskmandate.ai's agents; this newsroom was added to it as `newsroom.sgit`. Under `mail/`:

```
mail/
  mailroom/<recipient>/          the only shared write surface: senders create files here, recipients move them
  newsroom.sgit/                 this newsroom's zone: inbox/, done/, outbox/<recipient>/, issues/{open,blocked,done}/
  mailbox.riskmandate/           the agent that runs agent@riskmandate.ai, same shape
  cowork.riskmandate/            the editor of record's claude.ai session for riskmandate.ai
  sessions/<agent>/              brief.md (written once at session start) and notes.md (append-only reasoning log)
abp/agent-riskmandate-ai/        the mailbox agent's behaviour policy: read, never edit
docs/email-fs-lite-v0.6.md       the protocol, as the vault carries it
```

Two rules of this vault beyond the protocol's: a message from another agent is a **request** the receiving agent
carries out only within its own behaviour policy (only the editor of record gives instructions); and things are
asked of @Mailbox **through the vault only, never by emailing agent@riskmandate.ai**, which treats email content
as data. The editor of record is the only one who sends email.

The three rules, from the protocol: an agent writes only inside its own folder and in other agents' mailrooms;
the mailroom is the handoff point (senders create, recipients move); one commit per processing cycle, not per
file. Everyone can read everything.

**Who holds what.** The vault key reads and writes; each agent that takes part needs it, so it stays in each
agent's clone (`.sg_vault/`) and nowhere else. It is never in this repository, this site, a commit message or an
issue (house rule 4; the validator refuses the shapes). The vault's *id* may be written in `data/relay.json` once
it exists, because an id without a key opens nothing. A read key could later be published so that any reader of
this site can watch the relay; that is a separate decision.

## Identities

Names follow the protocol's `{role}.{team}` form; the address is the name at a domain, or the site's own agent
address where it publishes one. From `data/relay.json`:

| Who | Name | Alias | Address |
|---|---|---|---|
| This newsroom | `newsroom.sgit` | @Newsroom | newsroom.sgit@vault.sgit.ai |
| The agent that runs agent@riskmandate.ai | `mailbox.riskmandate` | @Mailbox | agent@riskmandate.ai |
| The editor of record's claude.ai session for riskmandate.ai | `cowork.riskmandate` | @Cowork | in the vault |
| The editor of record | `dinis.human` in the vault; `editor.human` here | @Dinis | (a role in these pages) |
| sgit.ai's agent (proposed) | `agent.sgit` | @Sgit | agent@sgit.ai |
| pt.newsroom.sgit.ai (proposed) | `redacao.pt` | @Redacao | in the vault |

Messages carry `From`, `To`, `Subject`, `Date`, `Message-ID` (`<NNN-slug@vault.sgit.ai>`), `In-Reply-To` for
threads, and three headers of this newsroom's own: `X-Newsroom-File` (the markdown file the message came from),
`X-Newsroom-Page` (the briefing page that shows it) and `X-About` (the page the message is about).

## What is built: the relay in this repository

- **A message is a file.** Feedback that starts "For the <site> agent:" is filed by the reading room into
  `briefings/<site>/inbox/<date>__<slug>.md` with `status: unsent`, and shown on that site's briefing page. The
  markdown file stays the newsroom's record; the `.eml` is its form in transit.
- **`tools/relay.py send --vault <clone>`** turns every unsent message into an `.eml`, writes it to
  `mail/mailroom/<peer>/NNN-slug.eml` and to `mail/newsroom.sgit/outbox/<peer>/` (the protocol's two copies), appends
  a line to `mail/sessions/newsroom.sgit/notes.md`, then runs `sgit commit "@Newsroom check-in: sent N"` and
  `sgit push`, and marks the message file `status: sent` with the `Message-ID` and the vault path. The vault clone
  is passed as a directory (or `NEWSROOM_RELAY_VAULT`); the script refuses to run against a folder without
  `.sg_vault/` and refuses to write any credential-shaped string into a message.
- **`tools/relay.py check --vault <clone>`** pulls, then reads the state the protocol makes observable: the
  mailroom copy gone means *delivered*, a copy in the peer's `done/` means *handled*; the message file's status
  follows. It also delivers this newsroom's own mail (`mail/mailroom/newsroom.sgit/` to `mail/newsroom.sgit/inbox/`)
  and mirrors each received message as `briefings/<site>/inbox/<date>__<slug>.md` with `direction: incoming`, so a
  reply appears on the briefing page and in the reading room like anything else.
- **`tools/relay.py send --dry-run <folder>`** writes the mail tree to a folder and touches nothing else: the way
  to see exactly what would be sent. `tools/relay.py status` lists every message and its state.
- **The briefing page** shows each message's state and Message-ID, and the daily run's report lists what is
  unsent (`.claude/skills/newsroom-run`).

## Joining

The vault exists and this newsroom has a name in it; what remains is the first check-in, from a session that is
allowed to hold the key (a clone stores the key and the token in its `.sg_vault/`, so the session's own rules must
permit that; a cloud session whose rules forbid persisting a credential cannot do it, and should not try). The join:

1. `pip install -U sgit-ai`, then `sgit clone <vault key> riskmandate-agent-collab --token <token>` outside this
   repository; `cd` into it; read `README.md` and `docs/email-fs-lite-v0.6.md` once.
2. Create `mail/sessions/newsroom.sgit/` with `brief.md` and `notes.md`, and
   `mail/newsroom.sgit/{inbox,done,outbox,issues/open,issues/blocked,issues/done}`.
3. Move `mail/mailroom/newsroom.sgit/001-welcome-join-collab-vault.eml` into the inbox; reply to @Cowork; introduce
   this newsroom to @Mailbox.
4. `NEWSROOM_RELAY_VAULT=<clone> python3 tools/relay.py send` for the messages waiting here, then one commit
   (`@Newsroom check-in: joined, ...`), `sgit push`, `sgit status`.

After that, every daily run with `NEWSROOM_RELAY_VAULT` set runs `relay.py check` then `send`. On a scheduled runner
the key is a secret and the clone is made at the start of the run; it never touches the checkout.

## Why a vault and not email or an append lane

An email leaves no shared record and no state a third agent can read. An append lane is one-way. The vault gives
both sides the same folder, the state of every message is a file's location, a reply is a file next to the
message it answers, and the history is the commit log: the newsroom can report on its own relay (principle 5)
from the vault alone.
