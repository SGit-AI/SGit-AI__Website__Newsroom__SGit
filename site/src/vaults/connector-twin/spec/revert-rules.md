# Revert rules, Gmail and Google Calendar

For each action in scope: what the platform keeps, what the twin can offer, and the side effects the revert plan must name. Sources are in `plan/02-the-facts.md`.

| Action | API call | What the platform keeps | Twin's inverse | Grade | Side effects to name |
|---|---|---|---|---|---|
| Archive | `messages.batchModify` removing `INBOX` | The message, unchanged but for the label | `batchModify` adding `INBOX` | exact | None |
| Label change | `messages.modify` | The message | `modify` with the opposite labels | exact | None |
| Move to trash | `messages.trash` | The message, for 30 days | `messages.untrash` | exact, within 30 days | None |
| Permanent delete | `messages.delete` | Nothing the user can reach. An administrator can bulk-restore a date range within 25 days | `messages.insert` with the captured content, if the agent read it in full | content only | A new message id; threading may differ |
| Send | `messages.send` | The sent message | None | none | The recipient has it |
| Create draft | `drafts.create` | The draft | `drafts.delete` | exact | None |
| Move or edit an event | `events.patch` or `events.update` | The new state only, for the user; an administrator's audit log records some earlier values | `events.patch` with the captured before-state | exact | Attendees are notified again if `sendUpdates` is set |
| Respond to an invitation | `events.patch` on the attendee's `responseStatus` | The new response | `patch` back to the captured response | exact | The organiser is notified |
| Delete an event | `events.delete` | Google's help says deleted events stay in trash for 30 days; not yet tested for API deletions | `events.insert` with the captured event | partial | A new event id; the cancellation already sent cannot be recalled |
| Create an event | `events.insert` | The event | `events.delete` | exact | Attendees receive a cancellation |

## Rules for the revert plan

1. Newest first. Undo in the reverse order of doing.
2. Name every side effect. A revert that re-notifies six people is not free.
3. Never execute without a person's approval.
4. Execute through the same capture path, so the revert is journalled like everything else.
5. Where the grade is `none`, say what a person can do instead, such as a follow-up email.
