# 4. Working in the gaps of the GRC platform

The service does not replace the customer's governance, risk and compliance platform. It works in the gaps that platform leaves, and it should be sold that way from the first meeting.

## What GRC platforms already do well

- **The register.** A list of risks with owners, ratings and review dates.
- **Workflow.** Assignments, reminders, approvals and sign-off.
- **Frameworks and controls libraries.** Mapping controls to ISO/IEC 27001, SOC 2, NIST and the rest.
- **Reporting.** Dashboards and board packs.

Those are solved problems. A customer who has one of these platforms has paid for it, trained people on it, and built reporting on it. The service keeps all of that.

## The gaps

| Gap | What it looks like | What the service adds |
|---|---|---|
| **The air gap to reality** | A register row is typed by a person and reviewed quarterly. Nothing connects it to the configuration, log or fact that made it true. | Every risk is established by named facts, each with its source, and ceases when other named facts hold. |
| **Acceptance without a clock** | "Accepted" is a status that never expires, or a review date nobody enforces. | Every acceptance has an interval. When it ends, the risk is accepted again, escalated, funded or fixed. |
| **Acceptance without a name** | Risks are accepted by a committee, a function, or nobody. | Every acceptance is by a named person, and nobody accepts on anybody else's behalf. |
| **Orphaned risks** | A risk held by a team that has no manager in the register, or by nobody at all. | Every risk has a holder, every holder has a boss, and every path ends at the board. Arrival is computed, not reported. |
| **Coarse granularity** | One row for "third-party risk" covers forty suppliers and six technologies. | Risks are fractal: a corporate line opens into business, operational and technical risks, each with its own holder and evidence. |
| **Evidence that evaporates** | Screenshots in an email, a spreadsheet on a laptop, a decision in a meeting nobody minuted. | Each significant risk gets a vault: evidence, decisions, history and the acceptance record, hash-chained and openable with a read key. |

## How the integration works

- **Read from the platform.** Pull the register, owners and controls from the GRC platform's API or export.
- **Write back what it lacks.** Push acceptance intervals, expiry dates, escalations and links to each risk's vault back as fields, comments or attachments.
- **Keep the platform as the system of record.** The service is the evidence and decision layer, not a second register.

## Why the GRC vendors should sponsor this

Every GRC vendor sells the register and the workflow. None of them can close the air gap alone, because closing it means connecting to the customer's reality: configurations, logs, agents and people. A service that does that work makes their platform more valuable and harder to leave. The plan proposes offering each major vendor an integration partnership early, and asking for co-selling rather than competing for the same budget line.
