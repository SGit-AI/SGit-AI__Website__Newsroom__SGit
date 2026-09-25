#!/usr/bin/env python3
"""Render sample/xray/findings.json into the documents the customer reads.

Run from the vault root:

    python3 tools/render-xray.py

findings.json is the source of truth. The markdown is generated from it, so the report, the
board pack and the app can never disagree.
"""
import json

X = json.load(open('sample/xray/findings.json'))
F = {f['id']: f for f in X['findings']}
DATE = '18 September 2026'


def finding_md(f):
    out = [f"### {f['id']}. {f['title']}", '',
           f"**{f['area']}** · *{f['label']}*: {X['labels'][f['label']]}", '',
           f['detail'], '', '**Evidence**', '']
    for e in f['evidence']:
        out.append(f"- `{e['file']}`, {e['where']}: {e['text']}")
    out += ['', f"**So what.** {f['so_what']}", '',
            f"**Do this.** {f['action']} *Suggested owner: {f['owner']}.*", '']
    return out


def report():
    out = [f"# X-ray: {X['company']}", '',
           f"*{DATE}. {X['level']}. {X['documents_read']} documents read, listed in `inbox/intake.md`. The company is invented.*", '',
           '## Your three questions, answered', '']
    for a in X['answers']:
        out += [f"**{a['question']}**", '', a['answer'], '', 'See ' + ', '.join(a['findings']) + '.', '']
    out += ['## How to read this', '',
            'Every finding carries one of three labels:', '']
    for k, v in X['labels'].items():
        out.append(f"- **{k}**: {v}")
    out += ['', 'Every finding names the file and the place in it that it rests on. If a finding is wrong, the evidence line shows where to look.', '',
            '## Findings', '']
    for f in X['findings']:
        out += finding_md(f)
    out += ['## What this X-ray does not cover', '']
    out += [f'- {n}' for n in X['not_covered']]
    out += ['', 'Next: `board-pack.md` for the one-page version, `questions-for-you.md`, `next-90-days.md`, and `../claude/` to keep asking.', '']
    open('sample/xray/X-RAY.md', 'w').write('\n'.join(out))


def board_pack():
    out = [f"# Board pack: {X['company']}", '', f"*From the X-ray of {DATE}. One page. The company is invented.*", '',
           '## Five things', '']
    for fid in ['F01', 'F03', 'F05', 'F06', 'F11']:
        f = F[fid]
        out.append(f"{len([l for l in out if l[:1].isdigit()]) + 1}. **{f['title']}** {f['so_what']} *({fid}, {f['label']})*")
    out += ['', '## Proposed agenda', '']
    out += [f'- {a}' for a in X['board_agenda']]
    out += ['', '## Decisions asked for', '',
            '- Who calls Calder and Irwell before 30 September, and with what.',
            '- Whether to restart the Manchester supervisor recruitment now.',
            '- A date for the price review paper.', '']
    open('sample/xray/board-pack.md', 'w').write('\n'.join(out))


def questions():
    out = ['# Questions for you', '', 'What your documents did not answer. Each one would change or firm up a finding.', '']
    out += [f'{i}. {q}' for i, q in enumerate(X['questions_for_you'], 1)]
    out += ['']
    open('sample/xray/questions-for-you.md', 'w').write('\n'.join(out))


def ninety():
    out = ['# The next ninety days', '', '| When | What | Owner | Done means |', '|---|---|---|---|']
    out += [f"| {s['when']} | {s['what']} | {s['owner']} | {s['done']} |" for s in X['next_90_days']]
    out += ['']
    open('sample/xray/next-90-days.md', 'w').write('\n'.join(out))


report(); board_pack(); questions(); ninety()
print(f"{len(X['findings'])} findings rendered into four documents")
