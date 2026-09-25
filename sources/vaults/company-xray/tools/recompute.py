#!/usr/bin/env python3
"""Re-run the arithmetic behind every "computed" finding in the sample X-ray.

Run from the vault root:

    python3 tools/recompute.py

It reads only the customer's files in sample/inbox/, recomputes each figure that a computed
finding in sample/xray/findings.json relies on, compares them, and writes the derived tables to
sample/xray/evidence/. A figure that does not match is printed as FAIL and the script exits 1.

This is the discipline the plan sells: a computed finding is one anybody can re-run.
"""
import csv, json, sys
from collections import defaultdict
from datetime import date

INBOX = 'sample/inbox/'
EVID  = 'sample/xray/evidence/'
LINES = ['Cleaning contracts', 'Reactive maintenance', 'Planned maintenance']
SPLIT = '2026-04'          # the April 2026 wage rise; last year is before, this year is from
MOVED = '2026-05'          # the Manchester area supervisor left on 12 May 2026
XRAY_DATE = date(2026, 9, 18)


def rows(name):
    return list(csv.DictReader(open(INBOX + name, newline='')))


def pct(a, b):
    return round(100 * a / b, 1)


class Recompute:

    def __init__(self):
        self.acc = rows('management-accounts.csv')
        self.cus = rows('customers.csv')
        self.com = rows('complaints-log.csv')
        self.pip = rows('sales-pipeline.csv')
        self.sup = rows('supplier-contracts.csv')
        self.too = rows('tools-inventory.csv')
        self.fig = {}

    def period(self, before):
        return [r for r in self.acc if (r['month'] < SPLIT) == before]

    def money(self):
        out = []
        for label, before in [('FY2025_26', True), ('Apr_Aug_2026', False)]:
            rs = self.period(before)
            months = len({r['month'] for r in rs})
            rev = sum(float(r['revenue']) for r in rs)
            cost = sum(float(r['direct_labour']) + float(r['materials']) + float(r['subcontract']) + float(r['overheads']) for r in rs)
            self.fig[f'revenue_per_month_{label}'] = round(rev / months)
            self.fig[f'net_per_month_{label}'] = round((rev - cost) / months)
            self.fig[f'net_margin_{label}'] = pct(rev - cost, rev)
            for line in LINES:
                lr = [r for r in rs if r['line'] == line]
                lrev = sum(float(r['revenue']) for r in lr)
                lcost = sum(float(r['direct_labour']) + float(r['materials']) + float(r['subcontract']) for r in lr)
                self.fig[f'gross_margin_{line.split()[0].lower()}_{label}'] = pct(lrev - lcost, lrev)
                self.fig[f'share_{line.split()[0].lower()}_{label}'] = pct(lrev, rev)
                if line == 'Cleaning contracts':
                    self.fig[f'cleaning_labour_ratio_{label}'] = pct(sum(float(r['direct_labour']) for r in lr), lrev)
                out.append([label, line, round(lrev), round(lcost), pct(lrev - lcost, lrev)])
            self.fig[f'overheads_per_month_{label}'] = round(sum(float(r['overheads']) for r in rs) / months)
        self.fig['revenue_growth_per_month_pct'] = pct(self.fig['revenue_per_month_Apr_Aug_2026'] - self.fig['revenue_per_month_FY2025_26'], self.fig['revenue_per_month_FY2025_26'])
        # what the cleaning margin drop cost, and the price rise that would restore it
        last = [r for r in self.period(True) if r['line'] == 'Cleaning contracts']
        this = [r for r in self.period(False) if r['line'] == 'Cleaning contracts']
        ratio = lambda rs: sum(float(r['direct_labour']) + float(r['materials']) for r in rs) / sum(float(r['revenue']) for r in rs)
        rev_this = sum(float(r['revenue']) for r in this)
        self.fig['cleaning_margin_lost_apr_aug'] = round((ratio(this) - ratio(last)) * rev_this, -2)
        self.fig['cleaning_price_rise_to_restore_pct'] = round(100 * (ratio(this) / ratio(last) - 1), 1)
        with open(EVID + 'margin-by-line.csv', 'w', newline='') as f:
            w = csv.writer(f); w.writerow(['period', 'line', 'revenue', 'direct_costs', 'gross_margin_pct']); w.writerows(out)
        with open(EVID + 'net-by-month.csv', 'w', newline='') as f:
            w = csv.writer(f); w.writerow(['month', 'revenue', 'net', 'net_margin_pct'])
            for m in sorted({r['month'] for r in self.acc}):
                rs = [r for r in self.acc if r['month'] == m]
                rev = sum(float(r['revenue']) for r in rs)
                cost = sum(float(r['direct_labour']) + float(r['materials']) + float(r['subcontract']) + float(r['overheads']) for r in rs)
                w.writerow([m, round(rev), round(rev - cost), pct(rev - cost, rev)])

    def customers(self):
        total = sum(int(c['revenue_fy2025_26']) for c in self.cus)
        ranked = sorted(self.cus, key=lambda c: -int(c['revenue_fy2025_26']))
        self.fig['customers'] = len(self.cus)
        self.fig['revenue_fy2025_26'] = total
        self.fig['share_top1'] = pct(int(ranked[0]['revenue_fy2025_26']), total)
        self.fig['share_top3'] = pct(sum(int(c['revenue_fy2025_26']) for c in ranked[:3]), total)
        calder = next(int(c['revenue_fy2025_26']) for c in self.cus if c['customer'] == 'Calder Retail Group')
        extra = sum(int(p['annual_value']) for p in self.pip if p['customer'] == 'Calder Retail Group')
        self.fig['share_calder_with_new_stores'] = pct(calder + extra, total + extra)
        indexed = [c for c in self.cus if c['indexation'] != 'None']
        self.fig['share_revenue_without_indexation'] = pct(total - sum(int(c['revenue_fy2025_26']) for c in indexed), total)
        # notice dates: contract end minus notice months, for fixed-term contracts
        due = []
        for c in self.cus:
            if c['contract_end'] == 'rolling':
                continue
            y, m, d = map(int, c['contract_end'].split('-'))
            m -= int(c['notice_months'])
            while m <= 0:
                m += 12; y -= 1
            last_day = [31, 29 if y % 4 == 0 else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m - 1]
            notice = date(y, m, min(d, last_day))
            due.append([c['customer'], c['contract_end'], c['notice_months'], notice.isoformat(), int(c['revenue_fy2025_26'])])
        due.sort(key=lambda r: r[3])
        soon = [r for r in due if XRAY_DATE <= date.fromisoformat(r[3]) <= date(2026, 10, 15)]
        self.fig['notice_before_board_customers'] = sorted(r[0] for r in soon)
        self.fig['notice_before_board_revenue'] = sum(r[4] for r in soon)
        self.fig['notice_before_board_share'] = pct(sum(r[4] for r in soon), total)
        self.fig['contracts_already_ended'] = sorted(r[0] for r in due if date.fromisoformat(r[1]) < XRAY_DATE)
        with open(EVID + 'notice-dates.csv', 'w', newline='') as f:
            w = csv.writer(f); w.writerow(['customer', 'contract_end', 'notice_months', 'notice_by', 'revenue_fy2025_26']); w.writerows(due)

    def complaints(self):
        before = [c for c in self.com if c['date'] < MOVED]
        after  = [c for c in self.com if c['date'] >= MOVED]
        self.fig['complaints_total'] = len(self.com)
        self.fig['complaints_per_month_before'] = round(len(before) / 8, 1)   # Sep 2025 to Apr 2026
        self.fig['complaints_per_month_after'] = round(len(after) / 4, 1)     # May to Aug 2026
        self.fig['complaints_manchester_before'] = f"{sum(c['city'] == 'Manchester' for c in before)} of {len(before)}"
        self.fig['complaints_manchester_after'] = f"{sum(c['city'] == 'Manchester' for c in after)} of {len(after)}"
        self.fig['days_to_close_before'] = round(sum(int(c['days_to_close']) for c in before) / len(before), 1)
        self.fig['days_to_close_after'] = round(sum(int(c['days_to_close']) for c in after) / len(after), 1)
        self.fig['complaints_calder'] = sum(c['customer'] == 'Calder Retail Group' for c in self.com)
        self.fig['complaints_calder_since_may'] = sum(c['customer'] == 'Calder Retail Group' for c in after)
        self.fig['complaints_irwell'] = sum(c['customer'] == 'Irwell Business Park Ltd' for c in self.com)
        self.fig['complaints_irwell_since_july'] = sum(c['customer'] == 'Irwell Business Park Ltd' and c['date'] >= '2026-07' for c in self.com)
        with open(EVID + 'complaints-by-month.csv', 'w', newline='') as f:
            w = csv.writer(f); w.writerow(['month', 'complaints', 'manchester', 'calder', 'irwell', 'avg_days_to_close'])
            for m in sorted({c['date'][:7] for c in self.com}):
                cs = [c for c in self.com if c['date'][:7] == m]
                w.writerow([m, len(cs), sum(c['city'] == 'Manchester' for c in cs), sum(c['customer'] == 'Calder Retail Group' for c in cs),
                            sum(c['customer'] == 'Irwell Business Park Ltd' for c in cs), round(sum(int(c['days_to_close']) for c in cs) / len(cs), 1)])

    def pipeline(self):
        total = sum(int(p['annual_value']) for p in self.pip)
        for line in ['Cleaning', 'Planned', 'Reactive']:
            self.fig[f'pipeline_share_{line.lower()}'] = pct(sum(int(p['annual_value']) for p in self.pip if p['service_line'] == line), total)

    def contracts_and_tools(self):
        due = []
        for s in self.sup:
            if s['renewal_date'] == 'rolling' or s['auto_renews'] != 'Yes':
                continue
            renew = date.fromisoformat(s['renewal_date'])
            notice = date.fromordinal(renew.toordinal() - int(s['notice_days']))
            due.append([s['supplier'], s['renewal_date'], s['notice_days'], notice.isoformat(), s['annual_value'], s['owner']])
        due.sort(key=lambda r: r[3])
        self.fig['auto_renewals_notice_by_1_oct_unowned'] = sorted(r[0] for r in due if r[3] == '2026-10-01' and r[5] == 'Nobody named')
        self.fig['auto_renewal_notice_passed'] = sorted(r[0] for r in due if date.fromisoformat(r[3]) < XRAY_DATE)
        with open(EVID + 'supplier-notice-dates.csv', 'w', newline='') as f:
            w = csv.writer(f); w.writerow(['supplier', 'renews', 'notice_days', 'notice_by', 'annual_value', 'owner']); w.writerows(due)
        waste = ['ServiceBook', 'TrackWise', 'Dropbox Business', 'Zoom', 'Google Workspace (old domain)', 'Survey tool', 'Mailchimp']
        self.fig['tools_duplicate_or_unused_per_year'] = 12 * sum(int(t['monthly_cost']) for t in self.too if t['tool'] in waste)
        self.fig['tools_without_owner'] = sum(t['owner'] == 'Nobody named' for t in self.too)

    def run(self):
        self.money(); self.customers(); self.complaints(); self.pipeline(); self.contracts_and_tools()
        return self.fig


if __name__ == '__main__':
    fig = Recompute().run()
    if '--print' in sys.argv:
        print(json.dumps(fig, indent=1)); sys.exit(0)
    findings = json.load(open('sample/xray/findings.json'))['findings']
    bad = 0; n = 0
    for f in findings:
        for k, v in f.get('checks', {}).items():
            n += 1
            ok = fig.get(k) == v
            bad += not ok
            print(('PASS' if ok else 'FAIL'), f['id'], k, v if ok else f'claimed {v}, recomputed {fig.get(k)}')
    print(f'{n - bad} of {n} figures recomputed from sample/inbox/ and matched.')
    sys.exit(1 if bad else 0)
