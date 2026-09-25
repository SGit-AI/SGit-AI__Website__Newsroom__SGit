# Risk Acceptance Office

A business plan for a company that runs the risk acceptance loop for organisations: every material risk established on facts, held by a named person, accepted for a stated interval, and at the end of that interval accepted again, escalated, funded or fixed. It works in the gaps of the client's existing GRC platform rather than replacing it, and it keeps each material risk's evidence and decisions in a vault of its own.

The one-line version: **every risk is already accepted; the service makes sure somebody signed for it, and until when.**

**Start with `index.html`** (it opens automatically). It sets out the principles, replays one invented risk over eight weeks from the facts that establish it to the facts that end it, and then sets out the business. Or read the plan as documents in `plan/`, in order.

## What is in this vault

| Path | What it is |
|---|---|
| `index.html`, `app.json`, `content.json` | The principles, the replay and the plan as a single-page app. All data is inlined, so it renders anywhere the vault opens, offline included. |
| `plan/00-START-HERE.md` | The one-page version and the reading order. |
| `plan/01` to `plan/10` | The idea, the method, the operating model, working in the gaps of the GRC platform, services and pricing, go-to-market, the first ninety days, why invest, the risks, and what is still open. |
| `plan/plan.json` | The principles, the ladder, the services and the assumptions the app displays. |
| `risk/` | One invented risk as its own record: facts, controls, holders, and a hash-chained decision record. The shape of a vault per material risk. |
| `spec/` | The acceptance record and the risk vault layout. |
| `prototypes/` | The acceptance audit, the acceptance meeting, and the GRC integration outline. |
| `diagrams/` | The acceptance loop and one risk from the board to the bytes. |
| `tools/build-content.py` | Chains the record, assembles `content.json` and inlines it into the app. |
| `tools/verify-record.py` | Checks the decision record's hash chain offline. Exit 0 if intact. |
| `PUBLIC.md` | The three rules this vault is published under. |

## Where the method comes from

The method is already published, and this plan builds on it rather than restating it: [risks.sgit.ai](https://risks.sgit.ai/) for the model, [RiskMandate.ai](https://riskmandate.ai/) for acceptance and the licence to operate, [graphs.sgit.ai](https://graphs.sgit.ai/) for fractal risk registers, and the [Risk Graph Explorer](https://sgit.ai/demos/vaults/risk-graph-explorer/index.html) vault for the chain to the board, working. Much of that model is stated as not yet built in code, and this plan says the same where it applies.
