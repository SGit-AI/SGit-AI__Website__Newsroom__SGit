# Agent-reported capture: the instruction

The cheapest way to start, and the weakest evidence. Give this to an agent as part of its system instructions, together with an append token for its lane. The token lets it write and nothing else.

---

**Journal requirement.** For every tool call you make to a connected system, including reads, append one entry to the journal lane before you continue. The entry contains:

- the tool call exactly as you made it;
- the request the tool sent to the system, if the tool reports it, without any Authorization header, cookie or token;
- the response you received, in full;
- the identifier of the user instruction you were acting on.

Append with one POST to the lane's write endpoint, with the append token in the body. Do not wait for, read or interpret the response beyond checking that it is `{"ok": true}`. If an append fails, stop and report it to the user before making any further write call. Never summarise an entry instead of copying it.

---

## What this does and does not give you

- **Does:** a journal in the same format as the broker's, on day one, with no infrastructure.
- **Does not:** completeness. An agent that skips an entry leaves a gap the chain cannot show, because the chain only links what was written. Every evidence pack built from this mode says *self-reported* on its first line.
- **Worth knowing:** asking the agent to stop when an append fails turns a silent gap into a visible halt, which is the one completeness property this mode can have.
