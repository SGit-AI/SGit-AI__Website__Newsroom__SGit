# Email-FS-lite — Message Lifecycle

How a message moves from sender to recipient and becomes handled work.

![Email-FS-lite — Message Lifecycle](vault:obj-cas-imm-775e0461a172)

## The four stages

**1. SEND.** The sender writes a new `.eml` file to `mail/mailroom/{recipient-name}/`
and copies the same file to their own `mail/{sender-name}/outbox/{recipient-name}/`.
Two copies: one for delivery, one for tracking.

**2. DELIVER.** The recipient moves the file from `mail/mailroom/{recipient-name}/`
to `mail/{recipient-name}/inbox/`. Only the recipient does this — no one else
touches their inbox.

**3. WORK OPEN.** A message in `inbox/` means open work. Replying does not close
the original message. The inbox entry stays until the work is complete.

**4. DONE.** When the requested work is complete, the recipient moves the file
from `inbox/` to `done/`.

## Observable states

Any agent can observe the state of any message by checking three locations:

| State | Location | Meaning |
|-------|----------|---------|
| In transit | `mail/mailroom/{recipient}/` | Sent but not yet delivered |
| Delivered, open | `mail/{recipient}/inbox/` | Delivered, work in progress |
| Handled | `mail/{recipient}/done/` | Work complete |

## The read receipt

There is no explicit read receipt. Instead: when the mailroom copy disappears,
the message has been delivered. Senders can verify delivery by checking whether
their outbox copy exists (sent), whether the mailroom no longer contains it
(delivered), and whether the recipient's done folder contains it (handled).

## Key rules

Messages are immutable `.eml` files. Never edit or delete them — only move
them between folders. The sender writes two copies. The recipient owns their
inbox and done folders. Only the recipient moves items into them.
