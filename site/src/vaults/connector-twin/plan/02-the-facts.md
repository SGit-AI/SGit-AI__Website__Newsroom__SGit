# 2. The facts

The case for the service is made from what the platforms document, not from what might go wrong. Every row below links to its source. Checked on 24 September 2026.

## Gmail

| Fact | What it means for an agent | Source |
|---|---|---|
| The API's delete call "Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer messages.trash instead." | An agent holding the full Gmail scope can remove a message with no trash window at all. | [users.messages.delete](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/delete) |
| Messages moved to Trash are kept for 30 days: "After 30 days: The message is permanently deleted. You can't recover the message." | Trash is a real undo, with a deadline. | [Gmail Help: delete or recover](https://support.google.com/mail/answer/7401) |
| Undo Send offers a cancellation period of 5, 10, 20 or 30 seconds, set in Gmail's settings. | It is a feature of the Gmail interface. A message sent through the API is delivered when the call returns. | [Gmail Help: send or unsend](https://support.google.com/mail/answer/2819488) |
| Workspace administrators can restore permanently deleted email for a date range within 25 days, as a bulk operation. | Recovery exists for organisations, but not per message, not per user action, and not after 25 days. | [Workspace Admin Help: restore permanently deleted email](https://knowledge.workspace.google.com/admin/support/troubleshooting/restore-a-users-permanently-deleted-email) |
| messages.insert "Directly inserts a message into only this user's mailbox similar to IMAP APPEND". | Content the twin captured can be put back, as a new message with a new id. | [users.messages.insert](https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/insert) |

## Google Calendar

| Fact | What it means for an agent | Source |
|---|---|---|
| Deleted events stay in the calendar's trash for 30 days. | A delete has a window. We have not tested whether an API deletion appears there, so the twin's re-insert is the path that does not depend on it. | [Calendar Help: delete an event](https://support.google.com/calendar/answer/37113) |
| Calendar's help documents a trash for deleted events, but no version history a user can open for an edited event, unlike Docs, Sheets and Slides. Workspace administrators have a Calendar audit log that records changes to events, including some earlier values such as the old event title, and start and end times. | A moved or retitled event has no undo for the user once the on-screen undo has gone. An administrator can see that it changed and some of what it was, but the log is a record, not a restore, and it does not hold what the agent saw. | [Workspace Admin Help: Calendar log events](https://knowledge.workspace.google.com/admin/reports/calendar-log-events) |
| Google Vault has searched Calendar since November 2023. Without a retention rule, revision information is kept for 30 days; with one, up to 365 revisions, and "the last revision of the day is kept, and previous revisions for that day are discarded." | An organisation with Vault can see some history, but an agent that edits an event three times in a day leaves one revision. | [Vault Help: search Calendar](https://knowledge.workspace.google.com/vault/search/use-vault-to-search-google-calendar), [Workspace Updates, Nov 2023](https://workspaceupdates.googleblog.com/2023/11/Google-Vault-Now-Supports-Google-Calendar.html) |

## Google Vault in general

| Fact | Source |
|---|---|
| "No. Vault isn't designed to be a backup or archive tool." | [Vault FAQ](https://knowledge.workspace.google.com/vault/getting-started/google-vault-faq) |
| "Restoring data from Vault export files is hard. Vault doesn't have any automated recovery tools." | [Vault FAQ](https://knowledge.workspace.google.com/vault/getting-started/google-vault-faq) |
| Vault is included in some Workspace editions, such as Business Plus and Enterprise, and is an add-on for others. | [Vault FAQ](https://knowledge.workspace.google.com/vault/getting-started/google-vault-faq) |

## The substrate

| Fact | Source |
|---|---|
| Connectors built on the Model Context Protocol exchange JSON-RPC 2.0 messages, so every tool call and result is a JSON document that can be copied as it passes. | [MCP specification](https://modelcontextprotocol.io/specification) |
| A vault append lane is a write-only channel gated by a token the writer holds. The write response is exactly `{"ok": true}`, so a sender learns nothing about the lane. Payloads are up to 5 MB; up to 1,000 entries can be pending per token; entries move from pending to processed when read. | [sgit.ai: Append lanes](https://sgit.ai/api/append-lanes.html) |
| An execution broker holds credentials inside its own boundary, performs only permitted operations, and returns a signed receipt, so the evidence chain does not depend on mutable platform logs. It is also the highest-value target in the estate. | [twins.sgit.ai: the execution broker](https://twins.sgit.ai/broker/index.html) |

## What the facts add up to

The platform keeps a way back for some actions (trash, for 30 days), a slow organisational way back for others (administrator bulk restore, for 25 days), a record without a restore for some (the administrator's audit log, and Vault's daily revisions where Vault is licensed), and none for the rest: a sent email, a notification to attendees, and a permanent delete through the API once the restore window has passed. None of those records keeps what the agent saw, or why it acted. A twin is the only place that information can exist.
