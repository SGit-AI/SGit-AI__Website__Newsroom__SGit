#!/usr/bin/env python3
"""The newsroom's agents: render agents/ from the register, and check run records against it.

    python3 tools/agents.py            # write agents/README.md and agents/<id>/ROLE.md, MANDATE.md
    python3 tools/agents.py --check    # exit 1 if agents/ differs from the register (the validator runs this)

The register is data/agents.json. Every file under agents/ is derived from it: edit the register,
never the files. A session that works as a desk reads that desk's ROLE.md and MANDATE.md first,
and records what it did in runs/<when>__<agent>.json; tools/validate.py fails a run record that
names an agent the register does not have, or that changed a folder outside that agent's mandate.
Standard library only.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADER = ('<!-- DERIVED FILE: do not edit. Rendered from data/agents.json by tools/agents.py; '
          'tools/validate.py fails when this file and the register disagree. -->\n\n')


def register():
    return json.load(open(os.path.join(ROOT, 'data', 'agents.json'), encoding='utf-8'))


def bullets(items):
    # a list is rendered item by item; a string is one item (never iterated character by character)
    if isinstance(items, str):
        items = [items]
    return '\n'.join(f'- {x}' for x in items) + '\n'


def role_md(a, reg):
    return (HEADER + f"# {a['name']}: {a['alias']}\n\n"
            f"**Register id** `{a['id']}` · **kind** {a['kind']} · **cadence** {a['cadence']}\n\n"
            f"## Mission\n\n> {a['mission']}\n\n"
            f"## The central claim, written as a failure condition\n\n"
            f"A role that says what it does can only be admired; a role that says when it is failing can be contradicted.\n\n"
            f"> This role is failing when: {a['failing_when']}\n\n"
            f"## Gravity\n\n> {a['gravity']}\n\n"
            f"## Reads\n\n{bullets(a['reads'])}\n"
            f"## Writes (its mandate: the validator holds a run record to these)\n\n{bullets(a['writes'])}\n"
            f"Plus what every run shares: {', '.join('`' + w + '`' for w in reg['shared_writes'])}. {reg['shared_writes_why']}\n\n"
            f"## Produces\n\n{bullets(a['outputs'])}\n"
            f"## How a run goes\n\n" + ''.join(f'{i}. {s}\n' for i, s in enumerate(a['steps'], 1)) + '\n'
            f"## Works with\n\n{bullets(a['works_with'])}\n"
            f"The mandate, what this role refuses and whose work it is not: [MANDATE.md](MANDATE.md).\n")


def mandate_md(a, reg):
    nr = ''.join(f"**{x['what']}**  \nBelongs to: {x['belongs_to']}\n\n" for x in a['not_responsible_for'])
    return (HEADER + f"# {a['name']}: mandate\n\n"
            f"**Register id** `{a['id']}`. A run record for this role names `\"agent\": \"{a['id']}\"`.\n\n"
            f"## Not responsible for\n\nWithout this, every role quietly becomes the same role; each entry says whose the work is.\n\n{nr}"
            f"## Refuses\n\n{bullets(a['refuses'])}\n"
            f"## Wrong when\n\n{bullets(a['failing_when'])}\n"
            f"## May write\n\n{bullets(a['writes'] + reg['shared_writes'])}\n"
            f"Anything else in a run record's `folders_changed` fails `tools/validate.py`.\n")


def readme_md(reg):
    rows = ''.join(f"| [**{a['name']}**]({a['id']}/ROLE.md) | `{a['alias']}` | {a['kind']} | {a['cadence']} | "
                   f"{', '.join('`' + w + '`' for w in a['writes'])} | [ROLE]({a['id']}/ROLE.md) · [MANDATE]({a['id']}/MANDATE.md) |\n"
                   for a in reg['agents'])
    return (HEADER + "# The agents\n\n"
            "The newsroom's work is done by desks, each with a role, a mandate and the folders it may write in. "
            "The register is [`data/agents.json`](../data/agents.json); every file in this folder is rendered from it by "
            "`tools/agents.py`. Edit the register, never these files.\n\n"
            "| Agent | Alias | Kind | Cadence | Writes | Role |\n|---|---|---|---|---|---|\n" + rows +
            "\n## How to work as one\n\n"
            "1. Read the desk's `ROLE.md` and `MANDATE.md`, then `CLAUDE.md` and `brief/06-house-rules.md`.\n"
            "2. Do only that desk's work, in its folders (plus the shared ones: "
            + ', '.join('`' + w + '`' for w in reg['shared_writes']) + ").\n"
            "3. Write `runs/<YYYY-MM-DDTHHMMSSZ>__<agent id>.json` (fields in `runs/README.md`).\n"
            "4. `python3 tools/build.py && python3 tools/validate.py`; commit and push only when both pass.\n\n"
            "The skills do this for you: `/desk <agent> <task>` runs one task as one desk; `/newsroom-run` runs the whole "
            "day, desk by desk, in the order of `brief/05-daily-run.md`.\n\n"
            "**If no desk fits the work, that is a message to the editor, not a licence to invent one.** A new agent is an "
            "editorial decision: a new mandate and a new write scope in the register.\n")


def rendered():
    reg = register()
    out = {'agents/README.md': readme_md(reg)}
    for a in reg['agents']:
        out[f"agents/{a['id']}/ROLE.md"] = role_md(a, reg)
        out[f"agents/{a['id']}/MANDATE.md"] = mandate_md(a, reg)
    return out


def check():
    """Differences between agents/ on disk and the register, as a list of problems."""
    want = rendered()
    problems = []
    for path, text in want.items():
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            problems.append(f'{path}: missing (run python3 tools/agents.py)')
        elif open(full, encoding='utf-8').read() != text:
            problems.append(f'{path}: differs from data/agents.json (edit the register, then run python3 tools/agents.py)')
    base = os.path.join(ROOT, 'agents')
    if os.path.isdir(base):
        for dirpath, _, files in os.walk(base):
            for name in files:
                p = os.path.relpath(os.path.join(dirpath, name), ROOT).replace(os.sep, '/')
                if p not in want:
                    problems.append(f'{p}: not in the register')
    return problems


def check_runs():
    """Every run record names a registered agent and changed only folders in its mandate."""
    reg = register()
    agents = {a['id']: a for a in reg['agents']}
    problems, n = [], 0
    d = os.path.join(ROOT, 'runs')
    if not os.path.isdir(d):
        return problems, n
    for name in sorted(os.listdir(d)):
        if not name.endswith('.json'):
            continue
        n += 1
        where = f'runs/{name}'
        try:
            r = json.load(open(os.path.join(d, name), encoding='utf-8'))
        except ValueError as e:
            problems.append(f'{where}: not JSON ({e})')
            continue
        for field in ('when', 'agent', 'kind', 'task', 'folders_changed', 'did'):
            if field not in r:
                problems.append(f'{where}: no "{field}"')
        a = agents.get(r.get('agent'))
        if not a:
            problems.append(f'{where}: agent {r.get("agent")!r} is not in data/agents.json')
            continue
        allowed = a['writes'] + reg['shared_writes']
        for f in r.get('folders_changed', []):
            if not any(f == w or f.startswith(w) or (w.endswith('/') and f.rstrip('/') + '/' == w) for w in allowed):
                problems.append(f'{where}: {a["id"]} changed {f}, outside its mandate ({", ".join(allowed)})')
    return problems, n


def main():
    if '--check' in sys.argv:
        problems = check()
        for p in problems:
            print('FAIL', p)
        sys.exit(1 if problems else 0)
    for path, text in rendered().items():
        full = os.path.join(ROOT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, 'w', encoding='utf-8') as f:
            f.write(text)
    print(f'agents: {len(register()["agents"])} rendered into agents/')


if __name__ == '__main__':
    main()
