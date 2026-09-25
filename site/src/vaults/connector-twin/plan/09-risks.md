# 9. Risks

| Risk | Why it matters | What to do |
|---|---|---|
| **The twin is sensitive data** | It holds copies of email and calendar content the agent touched. A breach of the twin is a breach of the mailbox. | Encrypt before storage, keep keys with the customer, retain only for the tier's period, and document the data flows for the customer's data protection officer. |
| **The broker is a target** | It holds credentials and sees traffic in flight: the highest-value target in the estate, as twins.sgit.ai puts it. | Offer the customer-cloud deployment, keep the broker minimal, and never make it a requirement for the lower tiers. |
| **Incomplete capture** | Agent-reported mode can omit entries; a gateway can be routed around. | State the capture mode on every evidence pack, and sell the broker where completeness matters. |
| **Personal data and retention** | The journal is personal data under GDPR. Subject access and erasure requests will arrive. | Retention per tier, deletion tooling from day one, and a record of processing the customer can adopt. |
| **Platform change** | APIs and scopes change, and connector vendors may add their own logs. | Capture at the protocol level as well as the upstream call, and treat a native platform log as a source to ingest, not a competitor to fear. |
| **Append lane limits** | 5 MB per write and 1,000 pending entries per token. | Store attachments by reference, shard lanes per agent, and process on a pending-count threshold. |
| **Revert makes things worse** | Reverting re-notifies attendees and cannot unsend email. | The revert plan names every side effect, a person approves each step, and the revert is journalled. |
| **It is sold as fear** | Buyers discount fear quickly and resent it. | Every claim links to the platform's own documentation. |
