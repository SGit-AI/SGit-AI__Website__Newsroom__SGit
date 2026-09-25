# The journal entry

One entry per connector call. This is the contract between whatever captures (a broker, a gateway, or the agent itself) and whatever replays. Everything else in the design can change; this should change slowly and with a version.

## Fields

| Field | Type | Meaning |
|---|---|---|
| `seq` | integer | Position in the session, from 1. |
| `ts` | string | UTC time the response was received, ISO 8601 with milliseconds. |
| `session` | string | The agent session this call belongs to. |
| `agent` | string | Which agent made the call. |
| `principal` | string | On whose behalf: the account the connector acts as. |
| `connector` | string | `gmail`, `calendar`, `drive`, `slack` and so on. |
| `capture` | string | `broker`, `gateway` or `agent`. Decides the evidence grade. |
| `prompt_ref` | string or null | The captured instruction that led to this call, if prompt capture is on. |
| `effect` | string | `read` or `write`. Decided by the capture point from the method and the tool, not by the agent. |
| `mcp` | object | The tool call as the agent made it: for MCP, the JSON-RPC request. |
| `request` | object | The upstream request: `method`, `url`, `headers` (see redaction), `body`. |
| `response` | object | The upstream response: `status`, `body`. |
| `prev` | string | SHA-256 of the previous entry, 64 zeros for the first. |
| `hash` | string | SHA-256 of this entry without `hash`, serialised with sorted keys and no whitespace. |

## Redaction

- Never capture `Authorization`, `Cookie`, `Set-Cookie`, or any header carrying a token. Record the header name with the value `[never captured]` so the absence is explicit.
- Never capture OAuth token exchanges at all.
- Attachments over 1 MB are captured as `{ "sha256": ..., "size": ..., "ref": ... }` with the bytes stored separately, because an append is limited to 5 MB.

## Why the upstream response is required

The views are rebuilt from what the platform returned, not from what the agent asked for. A `PATCH` records the intended change; the response records what the platform actually did. Where they differ, the response wins, and the difference is itself worth showing.

## Why the before-state is not stored separately

It does not need to be. The agent read the before-state to act on it, so it is already in an earlier entry. The replay folds entries in order and has the before-state in hand when it reaches the write. The one case where that fails is an agent that writes blind, without reading first. The replay marks those writes as having no captured before-state, and the revert plan says so.

## Example

`journal/session-2026-09-22.jsonl` in this vault: 17 entries, invented, chain intact.
