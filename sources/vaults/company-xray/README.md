# Company X-Ray

A business plan for a service that reads a company's own documents together. The customer drops them into an encrypted vault; agents run a catalogue of analyses; a person reviews; the customer gets back their questions answered, a board pack, findings tied to their evidence, and a Claude setup to keep asking. No connectors, no integrations. Sold in four levels, the same shape as RiskMandate.ai's.

**Start with `index.html`** (it opens automatically): the idea, one invented company X-rayed end to end with every finding's evidence one click away, how it works, the levels, a calculator and the plan. Or read `plan/` in order.

| Path | What it is |
|---|---|
| `index.html`, `app.json`, `content.json` | The app. All data inlined; opens anywhere, offline included. |
| `plan/00-START-HERE.md` to `plan/10-risks-and-open-questions.md` | The plan as documents. |
| `plan/plan.json` | The problem, steps, catalogue, levels, calculator defaults, phases and risks the app shows. |
| `sample/` | The customer vault as delivered: `inbox/` (12 invented documents and the intake), `xray/` (the X-ray, board pack, questions, ninety days, findings and evidence) and `claude/` (the setup to keep asking). |
| `spec/` | The analysis catalogue, the finding format, the customer vault's layout and life, and the intake checklist. |
| `prototypes/` | The operator's run prompt, the reviewer's checklist, the intake page, the handover call and the Tailored sessions. |
| `diagrams/` | The service and the levels. |
| `tools/recompute.py` | Re-runs every computed figure in the sample from `sample/inbox/`: 46 of 46 match. |
| `tools/render-xray.py`, `tools/build-content.py` | Generate the X-ray documents from `findings.json`, and the app's data. |
| `PUBLIC.md` | The rules this vault is published under. |
