# The lesson note

The contract between the agent that writes a note and the app that shows it. `player/record.json` holds ten invented entries in this shape.

| Field | Meaning |
|---|---|
| `id`, `date`, `type` | `lesson`, `match`, `video` or `briefing`. |
| `by` | The coach's id, `player`, or `agent`. |
| `memo` | For lessons: the coach's transcript, kept beside the note. |
| `note.worked_on` | What the lesson covered. |
| `note.observed` | What the coach saw, specific enough to check next time. |
| `note.focus` | At most three things for the next games, written to the player. |
| `note.drills` | What to practise, with counts. |
| `note.next` | The plan for the next lesson. |
| `themes` | Short statements against the player's tracked themes, such as "working on" or "holding in matches". |
| `disclosure` | Any commercial interest in a recommendation. |
| `credits` | What the processing cost. |

Rules: the transcript is never discarded; the focus list never has more than three items; a recommendation with a commercial interest must carry a disclosure.
