# The analysis catalogue

The standard analyses every X-ray runs. This is the part of the business that improves with every customer: each X-ray either confirms an analysis, sharpens it, or adds a new one. Each analysis says what it needs, so a customer who sends less gets fewer findings rather than weaker ones.

| # | Analysis | The question | Needs | Typical label |
|---|---|---|---|---|
| A1 | Money trend | Is the business making more or less per month, and since when? | Monthly management accounts, 12 months or more | computed |
| A2 | Margin by line | Which line of business makes the money, and which moved? | Accounts split by service or product line | computed |
| A3 | Price against cost | When did prices last move, and what moved since? | Price list with a date; the cost the price depends on | computed, with a public source |
| A4 | Concentration | How much rests on the largest customers, and against what target? | Customer list with revenue | computed |
| A5 | Dates that bind | Which contracts reach a notice, renewal or end date soon? | Customer and supplier lists with dates and notice periods | computed; inferred without the contract text |
| A6 | Complaints and service | Is service getting better or worse, where, and for whom? | A complaints or ticket log with dates | computed |
| A7 | Say and do | Where do the plan, the minutes and the numbers disagree? | The plan, the minutes, the accounts | inferred |
| A8 | Open actions | Which decisions are recorded and not closed? | Minutes with actions | read |
| A9 | One person | Which jobs rest on one person? | An org chart with notes and vacancies | read |
| A10 | Tools and spend | What is paid for, duplicated, unowned or unused? | A software or supplier list with owners | computed |
| A11 | AI and data | Where is AI used, on what information, under what rule? | Tool list, handbook or policies, minutes | inferred |
| A12 | What is missing | What would a board expect to see that was not sent? | The intake form | read |

## Rules for every analysis

- **Run it only on what was sent.** No web search about the customer, no guessing at what a missing document says.
- **Every finding names its evidence**: the file, and the row, line or section. See `finding.md`.
- **Arithmetic is code, not prose.** A computed finding is backed by a script that re-runs it from the inbox, like `tools/recompute.py` in this vault. The agent writes the script; the reviewer runs it.
- **Cross-document findings are the valuable ones.** A7 is where most of the "we did not know that" comes from: the minutes say one thing, the log says another.
- **Public facts are allowed as context** when they are cited with their source, such as a wage rate or a regulation. They are never the finding by themselves.
- **Stop at the evidence.** Where the documents cannot settle a point, it becomes a question in `questions-for-you.md`, not a finding.

## Sector packs

A sector pack adds analyses to the catalogue for one kind of business: for example rota coverage and wage floors for cleaning and care, fee-earner utilisation for professional services, stock turn for retail, or grant restrictions for charities. A pack is written after the third X-ray in a sector, from what the first three had in common.
