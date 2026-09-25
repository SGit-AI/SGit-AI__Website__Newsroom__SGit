#!/usr/bin/env python3
"""Helpers for the Cartographer: turn data into Mermaid text, so a map is a few lines of data, not syntax.

    from diagrams import wardley, timeline, graph, mindmap, fence

    print(fence(wardley('The value chain',
                        anchors={'Founder': (0.95, 0.60)},
                        components={'sgit.ai site': (0.70, 0.55), 'Encrypted vaults': (0.45, 0.50)},
                        links=[('Founder', 'sgit.ai site'), ('sgit.ai site', 'Encrypted vaults')],
                        evolve={'Encrypted vaults': 0.70})))

Every name is quoted, so dots and spaces are safe; every helper returns the diagram's text, and fence() wraps it in
the ```mermaid block a desk file needs. Run the file to see each helper's output.
"""
import json
import re


def q(name):
    return '"' + str(name).replace('"', "'") + '"'


def fence(text):
    return '```mermaid\n' + text.strip() + '\n```'


def wardley(title, anchors, components, links, evolve=None, notes=None):
    """anchors and components: {name: (visibility, evolution)}, both 0..1; links: [(from, to)]; evolve: {name: evolution}."""
    out = ['wardley-beta', f'title {title}']
    for name, (vis, evo) in anchors.items():
        out.append(f'anchor {q(name)} [{vis:.2f}, {evo:.2f}]')
    for name, (vis, evo) in components.items():
        out.append(f'component {q(name)} [{vis:.2f}, {evo:.2f}]')
    for a, b in links:
        out.append(f'{q(a)} -> {q(b)}')
    for name, evo in (evolve or {}).items():
        out.append(f'evolve {q(name)} {evo:.2f}')
    for text, (vis, evo) in (notes or {}).items():
        out.append(f'note {q(text)} [{vis:.2f}, {evo:.2f}]')
    return '\n'.join(out)


def timeline(title, events, per_section=8):
    """events: [(date, text)] sorted or not; long lists are split into sections so they stay readable."""
    events = sorted(events)
    out = ['timeline', f'title {title}']
    for i in range(0, len(events), per_section):
        chunk = events[i:i + per_section]
        if len(events) > per_section:
            out.append(f'section {chunk[0][0]} to {chunk[-1][0]}')
        for date, text in chunk:
            out.append(f'  {date} : {re.sub(r"[:#]", " ", str(text))[:80]}')
    return '\n'.join(out)


def graph(nodes, edges, direction='LR', classes=None, links=None):
    """nodes: {id: label} or [id]; edges: [(from, to)] or [(from, to, label)]; classes: {class: (ids, style)};
    links: {id: href} (needs Mermaid's antiscript level, which the site's diagrams.js sets)."""
    nid = lambda i: 'n_' + re.sub(r'[^A-Za-z0-9]', '_', str(i))
    labels = nodes if isinstance(nodes, dict) else {n: n for n in nodes}
    out = [f'flowchart {direction}']
    for i, label in labels.items():
        out.append(f'  {nid(i)}[{q(label)}]')
    for e in edges:
        if len(e) == 3 and e[2] not in (None, ''):
            out.append(f'  {nid(e[0])} -->|{e[2]}| {nid(e[1])}')
        else:
            out.append(f'  {nid(e[0])} --> {nid(e[1])}')
    for cls, (ids, style) in (classes or {}).items():
        out.append(f'  classDef {cls} {style}')
        out.append(f'  class {",".join(nid(i) for i in ids)} {cls}')
    for i, href in (links or {}).items():
        out.append(f'  click {nid(i)} {q(href)}')
    return '\n'.join(out)


def mindmap(root, tree):
    """tree: {branch: [leaves] or {sub: [...]}}"""
    out = ['mindmap', f'  root(({root}))']

    def walk(node, depth):
        pad = '  ' * (depth + 2)
        if isinstance(node, dict):
            for k, v in node.items():
                out.append(f'{pad}{k}')
                walk(v, depth + 1)
        else:
            for leaf in node:
                out.append(f'{pad}{leaf}')
    walk(tree, 0)
    return '\n'.join(out)


def network_from_json(path, top=30, site_pages=True):
    """The site-to-site network in data/network.json as a flowchart of its strongest links."""
    net = json.load(open(path, encoding='utf-8'))
    links = net['links'][:top]
    nodes = sorted({l['from'] for l in links} | {l['to'] for l in links})
    return graph(nodes, [(l['from'], l['to'], l['files']) for l in links],
                 links={n: f'../reading-room/{n}.html' for n in nodes} if site_pages else None)


if __name__ == '__main__':
    print(fence(wardley('Example', {'Reader': (0.95, 0.6)}, {'sgit.ai site': (0.7, 0.55), 'Object storage': (0.15, 0.9)},
                        [('Reader', 'sgit.ai site'), ('sgit.ai site', 'Object storage')], evolve={'sgit.ai site': 0.7})))
    print(fence(timeline('Two dates', [('2026-09-20', 'A read key refused'), ('2026-09-24', 'Four plans as vaults')])))
    print(fence(graph({'a': 'sgit.ai', 'b': 'riskmandate.ai'}, [('a', 'b', 16)])))
    print(fence(mindmap('newsroom', {'Desks': ['Librarian', 'Journalist'], 'Data': ['index', 'concepts']})))
