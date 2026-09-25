# GRC integration, an outline

The service reads from the client's GRC platform and writes back what the platform lacks. The platform stays the system of record for the register.

## Read

- Register rows: id, title, owner, rating, status, review date.
- Owners, and the reporting line if the platform holds it; otherwise from the HR system or a maintained org chart.
- Controls and their mappings to frameworks.

## Write back, per material risk

| Field | Value |
|---|---|
| Accepted by | The named person |
| Accepted until | The interval's end date |
| Rung | The ladder rung |
| Action | What happens before the interval ends |
| Status note | Accepted, expired, escalated, funded, incident or ceased |
| Evidence | A link to the risk's vault, and a read key where the platform can hold secrets |

## Events to push

- Expiry reached, with who it escalated to.
- Funding decided, with the project reference.
- Ceased on facts, with the fact that ended it.

## Integration styles

- **API** where the platform has one.
- **Scheduled export and import** where it does not.
- **A comment and attachment** on the row as the minimum, for platforms that allow nothing else.

The outline is platform-neutral on purpose. The first real integration should be written with a GRC vendor as a partner, not around them.
