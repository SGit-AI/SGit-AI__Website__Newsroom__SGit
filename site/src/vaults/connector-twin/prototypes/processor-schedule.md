# The processor and its schedule

The processor reads pending entries from the append lane, folds them into views, commits the views, and marks the entries processed. The mechanics are simple: list with `include_content: false`, fetch in batches of up to 100, fold, commit, mark processed. Marking is idempotent, so a retried batch is safe.

The schedule is the open question.

| Trigger | For | Against |
|---|---|---|
| **Timer**, for example every 15 minutes | Predictable cost; views are never more than one interval stale | Wasteful when idle; can fall behind a burst |
| **Pending-count threshold**, for example at 500 pending | Stays clear of the 1,000-per-token limit that refuses writes | Needs something watching the count |
| **On demand**, when somebody opens the replay | No work until it is needed; the freshest view | The first open after a busy day is slow |
| **End of session** | One fold per agent session, a natural unit | Long sessions leave long gaps |

## A starting default

A timer every 15 minutes, a threshold at 500 pending entries per lane, and an on-demand fold of whatever is pending when the replay opens. Then measure: how often each trigger fires, how long a fold takes, how stale the views were when people looked. Change the default when real usage says so.

## One rule regardless of schedule

Capture must not fail silently. In broker and gateway mode, if the lane refuses an append, the entry is held locally and the broker accepts no further write operations until the lane accepts it again. The schedule can be lazy; capture cannot.
