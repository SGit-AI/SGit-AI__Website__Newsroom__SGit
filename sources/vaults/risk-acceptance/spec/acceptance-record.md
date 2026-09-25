# The acceptance record

One entry per decision about a risk. This is the contract between whoever runs the loop (a person, a tool, or a GRC integration) and whoever reads the record (the holder, the board, an auditor, an insurer). `risk/record.jsonl` is an invented example, 14 entries, chain intact.

## Fields

| Field | Meaning |
|---|---|
| `seq` | Position in the risk's record, from 1. |
| `day` | Days since the risk was established. A real record also carries an ISO 8601 timestamp. |
| `type` | `identified`, `placed`, `accepted`, `expired`, `escalated`, `funded`, `incident`, `evidence`, `reported` or `closed`. |
| `actor` | Who did it: a named person, or "the clock" for expiries and escalations. |
| `role` | The role acting, for acceptances, escalations and funding. |
| `rung` | For acceptances: the ladder rung, such as "1 month". |
| `days` / `hours` | For acceptances: the interval. |
| `action` | For acceptances: what will happen before the interval ends. Required. |
| `holder` | When the holder changes: the new holder. |
| `facts_add` / `facts_remove` | Facts that start or stop holding, by id. Each fact has a source in the risk's facts list. |
| `controls` | Control states that change: `missing`, `proposed`, `funded`, `in_place`. |
| `text` | One or two sentences a board member can read. |
| `prev`, `hash` | The chain. SHA-256 over the entry without `hash`, keys sorted, no whitespace; the first entry's `prev` is 64 zeros. |

## Rules

1. **No acceptance without an interval and an action.**
2. **No acceptance on somebody else's behalf.** `actor` must be the person holding `role`.
3. **An expiry is an entry.** The clock writes it; nobody has to remember to.
4. **Silence escalates.** An expiry with no acceptance, funding or fix within one working day produces an `escalated` entry to the holder's boss.
5. **A risk closes on facts.** A `closed` entry names the fact that ended it, which must be one of the risk's "ceases when" facts.
6. **Nothing is deleted.** Corrections are new entries that point at the one they correct.

`tools/verify-record.py` checks the chain and exits 1 at the first break.
