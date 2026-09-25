# X-ray: Northgate Facilities Ltd

*18 September 2026. Standard X-ray (level 3), run on the standard catalogue and reviewed by a person. 13 documents read, listed in `inbox/intake.md`. The company is invented.*

## Your three questions, answered

**Why is profit down when revenue is up?**

Because cleaning costs rose and cleaning prices did not. Revenue is up 3.9% a month, and net profit has halved. Almost all of the fall is cleaning labour: two National Living Wage rises have passed since the last price change in January 2025. A 4.8% rise on cleaning prices would restore last year's cleaning margin.

See F01, F02, F03.

**How exposed are we to Calder Retail Group?**

More than the plan allows, and at a sensitive moment. Calder is 31% of revenue against a target of no customer above 20%, and the six new stores would take it to 34%. Its contract appears to reach its notice date on 30 September, two weeks before the board meets, and its complaints nearly tripled after the Manchester supervisor left.

See F04, F05, F07.

**What should the board be looking at that it is not?**

Six things: the notice dates on 30 September; complaints, which appear in no minutes; the price review, deferred twice; one action carried forward at three meetings; four jobs resting on one person each; and staff using personal ChatGPT accounts with customer information and no rule to cover it.

See F05, F07, F03, F11, F10, F14.

## How to read this

Every finding carries one of three labels:

- **read**: Stated in a document you sent. We quote it and say where.
- **computed**: Arithmetic on your data. Re-run it with tools/recompute.py; every figure is checked.
- **inferred**: Our reading of two or more documents together. Check it before acting on it.

Every finding names the file and the place in it that it rests on. If a finding is wrong, the evidence line shows where to look.

## Findings

### F01. Revenue is up 3.9% a month. Net profit has halved.

**Money** · *computed*: Arithmetic on your data. Re-run it with tools/recompute.py; every figure is checked.

Last year (April 2025 to March 2026) the business averaged £343,350 of revenue and £15,717 of net profit a month, a net margin of 4.6%. From April to August 2026 it averaged £356,600 and £7,780, a net margin of 2.2%. The step is in April 2026, and it has not recovered in any month since.

**Evidence**

- `inbox/management-accounts.csv`, all rows, 2025-04 to 2026-08: Net by month is in xray/evidence/net-by-month.csv: 4.2% to 5.5% every month to March 2026; 1.9% to 2.4% every month from April.

**So what.** At 2.2%, one bad month or one lost contract puts the business at break-even. The plan's target is 8%.

**Do this.** Take the monthly net margin to every board meeting, by service line, as the plan already says to do. *Suggested owner: Finance Manager.*

### F02. The fall is almost all cleaning labour.

**Money** · *computed*: Arithmetic on your data. Re-run it with tools/recompute.py; every figure is checked.

Cleaning's gross margin fell from 19.8% to 16.0%, because direct labour went from 74.4% to 78.2% of cleaning revenue. Reactive maintenance held at 34.0% and planned maintenance at 27.0%. Overheads rose by £2,500 a month. The lower cleaning margin cost about £41,200 in the five months to August, around £99,000 over a year.

**Evidence**

- `inbox/management-accounts.csv`, lines 'Cleaning contracts', 'Reactive maintenance', 'Planned maintenance', 'Overheads': Margin by line and period is in xray/evidence/margin-by-line.csv.

**So what.** The problem is narrow and known: a price that has not kept up with a cost. It is not the maintenance side, and it is not overheads.

**Do this.** Price review on cleaning, starting with the contracts that have no indexation clause (F03). *Suggested owner: Managing Director.*

### F03. Prices have not moved since January 2025. Wages have moved twice.

**Money** · *computed*: Arithmetic on your data. Re-run it with tools/recompute.py; every figure is checked.

The price list is dated 1 January 2025. Since then the National Living Wage rose 6.7% in April 2025 and 4.1% in April 2026. The board noted the second rise in January and deferred the price review in April; it is not on the July agenda. Three quarters of revenue sits in contracts with no indexation clause, so those prices only move if somebody asks. A 4.8% rise on cleaning would restore last year's cleaning margin.

**Evidence**

- `inbox/price-list.md`, line 3: Effective 1 January 2025.
- `inbox/board-minutes-2026.md`, 22 January, item 2: Price review to be considered after the increase is confirmed.
- `inbox/board-minutes-2026.md`, 23 April, item 2: Carried forward; Helen wants to avoid unsettling Calder before its six new stores are confirmed.
- `inbox/customers.csv`, column 'indexation': Only Pennine Housing Trust, Wharfe Valley Schools Trust and Kirkgate Medical Partnership have indexation: 25.0% of revenue.
- `public source`, https://www.gov.uk/national-minimum-wage-rates: National Living Wage: £11.44 to £12.21 in April 2025, £12.21 to £12.71 in April 2026.

**So what.** Every month without a review costs about £8,000 of margin on cleaning.

**Do this.** Write the price review in October: a proposed rise per contract, the notice each contract needs, and which conversations to have first. *Suggested owner: Managing Director.*

### F04. Calder is 31% of revenue. The top three are 52%.

**Customers** · *computed*: Arithmetic on your data. Re-run it with tools/recompute.py; every figure is checked.

Calder Retail Group was £1,277,000 of last year's £4,120,200. With Pennine Housing Trust and Wharfe Valley Schools Trust, the top three customers were 51.9% of revenue. The plan's target is no customer above 20%. The six new Calder stores in the pipeline, if won, would take Calder to 34%.

**Evidence**

- `inbox/customers.csv`, column 'revenue_fy2025_26': Calder Retail Group 1,277,000; 22 customers in total.
- `inbox/strategy-2026-2028.md`, line 12: No customer above 20% of revenue.
- `inbox/sales-pipeline.csv`, 'Calder Retail Group: 6 new stores': annual value 190,000, stage Verbal

**So what.** Winning the new stores moves the company further from its own target, and at last January's prices.

**Do this.** Decide the price for the new stores before accepting them, and report concentration quarterly as the plan says. *Suggested owner: Managing Director.*

### F05. £1.5m of contracts reach their notice date on 30 September, before the board meets.

**Customers** · *inferred*: Our reading of two or more documents together. Check it before acting on it.

Calder's contract ends on 31 March 2027 with six months' notice, and Irwell Business Park's ends on 31 December 2026 with three. Both give 30 September 2026 as the date by which notice must be given. Together they were £1,503,000, 36.5% of revenue. The next board meeting is on 15 October. We have not seen the contracts, so we do not know who may give notice, or whether they renew automatically. Separately, Holme Logistics' contract ended on 31 May 2026 and its renewal is still in negotiation.

**Evidence**

- `inbox/customers.csv`, rows 'Calder Retail Group' and 'Irwell Business Park Ltd': 2027-03-31, 6 months; 2026-12-31, 3 months
- `inbox/board-minutes-2026.md`, 16 July, items 2 and 6: Relationship strong; renewal expected in the new year. Next meeting: 15 October 2026.
- `inbox/sales-pipeline.csv`, 'Holme Logistics: PPM renewal': stage Negotiation
- `xray/evidence/notice-dates.csv`, all rows: Notice-by dates, computed from end date and notice period.

**So what.** If either customer can give notice by 30 September, the board will learn about it after the fact. The July minutes expect Calder's renewal 'in the new year', which is after its notice date.

**Do this.** This week: read both contracts, confirm what 30 September means, and call both customers. *Suggested owner: Managing Director.*

### F06. Complaints nearly doubled after the Manchester supervisor left.

**Operations** · *computed*: Arithmetic on your data. Re-run it with tools/recompute.py; every figure is checked.

From September 2025 to April 2026 the business logged 3.0 complaints a month, 8 of 24 of them in Manchester, closed in 2.7 days on average. From May to August 2026 it logged 5.5 a month, 18 of 22 in Manchester, closed in 7.0 days. The Manchester area supervisor left on 12 May; recruitment was paused in June to save cost, and the Operations Director has scheduled both cities from Leeds since.

**Evidence**

- `inbox/complaints-log.csv`, all 46 rows: By month in xray/evidence/complaints-by-month.csv.
- `inbox/org-chart.csv`, 'Manchester Area Supervisor': Vacant since 12 May 2026; Recruitment paused in June to save cost
- `inbox/board-minutes-2026.md`, 16 July, item 3: Paused in June to save cost. Tom continues to cover.

**So what.** The saving on one salary is set against the two contracts with notice dates on 30 September, both mostly serviced from Manchester.

**Do this.** Restart the Manchester recruitment, or name an interim supervisor, before speaking to Calder and Irwell. *Suggested owner: Operations Director.*

### F07. The two customers with notice dates are the two complaining most.

**Customers** · *computed*: Arithmetic on your data. Re-run it with tools/recompute.py; every figure is checked.

Calder accounts for 19 of the 46 complaints, 11 of them since May. Irwell Business Park accounts for 14, 7 of them since July. Complaints do not appear in any of the three sets of minutes, and in July the board recorded the Calder relationship as 'strong'.

**Evidence**

- `inbox/complaints-log.csv`, column 'customer': Calder Retail Group 19; Irwell Business Park Ltd 14
- `inbox/board-minutes-2026.md`, 16 July, item 2: Relationship strong; renewal expected in the new year.

**So what.** What the board hears about customers and what the complaints log records have drifted apart.

**Do this.** Add complaints by customer to the board pack, and open the Calder and Irwell conversations with what is being done about Manchester. *Suggested owner: Operations Director.*

### F08. The plan says 40% planned maintenance. The business is moving the other way.

**Plan and reality** · *computed*: Arithmetic on your data. Re-run it with tools/recompute.py; every figure is checked.

Planned maintenance was 17.8% of revenue last year and 17.0% since April. Of the sales pipeline's value, 72.8% is cleaning and 20.9% is planned maintenance. The plan's first step, a planned maintenance sales lead, is not on the org chart; the estimator post has been vacant since January; and one coordinator builds every planned maintenance schedule.

**Evidence**

- `inbox/strategy-2026-2028.md`, lines 11 and 18: Planned maintenance at 40% of revenue... Hire a planned maintenance sales lead in 2026.
- `inbox/sales-pipeline.csv`, column 'service_line': Cleaning is 5 of the 10 opportunities and 72.8% of their value
- `inbox/org-chart.csv`, 'Estimator', 'Planned maintenance coordinator': Vacant since January 2026; Only person who builds planned maintenance schedules

**So what.** Either the plan needs its first hire, or the target needs to change. At the current mix, 40% by March 2028 is out of reach.

**Do this.** Put the planned maintenance hire, or a revised target, on the October agenda. *Suggested owner: Managing Director.*

### F09. New cleaning work is likely being priced below the plan's own floor.

**Plan and reality** · *inferred*: Our reading of two or more documents together. Check it before acting on it.

The plan says to take new cleaning contracts only at a margin of 22% or more. Cleaning is running at 16.0% on the January 2025 prices. The pipeline does not record margins, but if the £952,000 of cleaning opportunities is priced from the same list, it is below the floor.

**Evidence**

- `inbox/strategy-2026-2028.md`, line 20: Only take new cleaning contracts at a margin of 22% or more.
- `inbox/price-list.md`, line 3: Effective 1 January 2025.

**So what.** Growth in cleaning at these prices adds revenue and labour faster than it adds profit.

**Do this.** Add an expected margin column to the pipeline, and apply the 22% rule to the six Calder stores. *Suggested owner: Business Development Manager.*

### F10. Four jobs rest on one person each.

**People** · *read*: Stated in a document you sent. We quote it and say where.

The Finance Manager is the only finance employee and the sole administrator on the bank portal. The Operations Director has scheduled every cleaning rota for both cities since May. One coordinator builds every planned maintenance schedule. The Maintenance Manager has covered estimating since January.

**Evidence**

- `inbox/org-chart.csv`, 'Finance Manager', 'Operations Director', 'Planned maintenance coordinator', 'Estimator': Only finance employee; sole administrator on the bank portal. Schedules all cleaning rotas for Leeds and Manchester since May 2026. Only person who builds planned maintenance schedules. Vacant since January 2026.
- `inbox/board-minutes-2026.md`, 23 April, item 5: Ian covering quotes.

**So what.** A two-week absence in any of these roles stops payments, rotas, planned maintenance or quotes. Separately, one person able to approve payments alone is the control most insurers and auditors ask about first.

**Do this.** Set up the second bank administrator now (F11), and write down who covers each of the other three. *Suggested owner: Managing Director.*

### F11. The same action has been carried forward at three meetings.

**Governance** · *read*: Stated in a document you sent. We quote it and say where.

In January the Chair asked for a second administrator on the bank portal. It was carried forward in April and again in July. The price review was deferred in January and April and is not on the July agenda. In July, margin commentary was deferred because the management accounts were late.

**Evidence**

- `inbox/board-minutes-2026.md`, 22 January item 4; 23 April item 4; 16 July item 4: Action: Priya to arrange. Carried forward: Priya. Carried forward: Priya.
- `inbox/board-minutes-2026.md`, 16 July, item 1: Margin commentary deferred to the next meeting, as the management accounts were late.

**So what.** The board is recording decisions it is not closing. A half-hour task has been open for eight months.

**Do this.** Start each board meeting with the open actions, their age and their owner. Close the bank portal action before 15 October. *Suggested owner: Chair.*

### F12. Two auto-renewals with nobody named as owner need notice by 1 October.

**Contracts and tools** · *computed*: Arithmetic on your data. Re-run it with tools/recompute.py; every figure is checked.

ServiceBook, the legacy job system, renews on 31 October with 30 days' notice, and TrackWise renews on 30 November with 60 days' notice: both need notice by 1 October, and neither has an owner. ServiceBook duplicates FieldDesk but still runs four Manchester contracts; TrackWise duplicates the tracking included in the Fleetline van leases. The Fleetline lease notice date, 2 September, has already passed. ChemPro's is 1 November.

**Evidence**

- `inbox/supplier-contracts.csv`, rows 'ServiceBook', 'TrackWise Telematics', 'Fleetline Leasing', 'ChemPro Supplies': renewal dates, notice days and owners
- `inbox/tools-inventory.csv`, rows 'ServiceBook', 'TrackWise', 'Fleetline Connect': Still paid; Manchester still uses it for 4 contracts. Fleetline vans also include tracking. Included in lease; not used.
- `xray/evidence/supplier-notice-dates.csv`, all rows: Notice-by dates, computed from renewal date and notice days.

**So what.** Missing 1 October commits the business to another year of both.

**Do this.** Give notice on TrackWise and switch to the lease's tracking. Give notice on ServiceBook and move the four Manchester contracts to FieldDesk before 31 October, or negotiate a monthly term. *Suggested owner: Operations Director.*

### F13. About £18,300 a year goes on tools that duplicate others or are unused.

**Contracts and tools** · *computed*: Arithmetic on your data. Re-run it with tools/recompute.py; every figure is checked.

ServiceBook duplicates FieldDesk, TrackWise the lease tracking, Dropbox the OneDrive in Microsoft 365, Zoom the Teams in Microsoft 365. The old Google Workspace domain is still paid three years after the acquisition, the survey tool has sent nothing since 2024, and Mailchimp's last campaign was March 2025. Five tools have nobody named as owner.

**Evidence**

- `inbox/tools-inventory.csv`, columns 'owner', 'monthly_cost', 'status': 22 tools, 5 with 'Nobody named'

**So what.** Small next to the pricing question, but it is money, and nobody is watching it.

**Do this.** Give every tool an owner, and cancel or keep each one at its next renewal. *Suggested owner: Office Manager.*

### F14. Staff use personal ChatGPT accounts for customer work, and no rule covers it.

**Governance** · *inferred*: Our reading of two or more documents together. Check it before acting on it.

Nine staff use ChatGPT on their own accounts to write quotes, emails and method statements. The company does not pay for or manage those accounts. The handbook says customer information must only be stored in company systems, and that the company holds personal data about customers' staff and residents, but it was last reviewed in March 2021 and says nothing about AI tools. In July the board noted the use as 'helpful' and took no action.

**Evidence**

- `inbox/tools-inventory.csv`, row 'ChatGPT (personal accounts)': 9 users; Staff own accounts; not paid for or managed by the company
- `inbox/staff-handbook-excerpt.md`, line 3; 7.3; 8.1: Handbook last reviewed March 2021. Customer information must only be stored in company systems. We hold personal data about staff and about customers' staff and residents.
- `inbox/board-minutes-2026.md`, 16 July, item 5: Noted as 'helpful'. No action.

**So what.** Quotes and method statements carry customer names, sites and access arrangements. In personal accounts the company cannot see them, keep them or remove them when somebody leaves, and on consumer plans the account holder, not the company, chooses whether chats may be used for training.

**Do this.** Keep the benefit and close the gap: a one-page rule for AI use, company accounts on business terms, and a list of what never goes into a prompt. RiskMandate.ai publishes a free twenty-minute exercise for writing down what an AI tool can reach and what you meant to allow. *Suggested owner: Office Manager, with the HR Manager.*

## What this X-ray does not cover

- Cash and banking: no statements were sent.
- Payroll and individual pay: removed before upload, as asked.
- Full contract terms: only the summary columns in customers.csv were sent.
- Profit by customer or by site: the accounts are by service line.
- Health and safety records, insurance and legal matters.

Next: `board-pack.md` for the one-page version, `questions-for-you.md`, `next-90-days.md`, and `../claude/` to keep asking.
