#!/usr/bin/env python3
"""The relay: carry this newsroom's messages to another site's agent over a shared sgit vault, Email-FS-lite style.

    python3 tools/relay.py send  --vault ~/vaults/sgit-network-relay      # unsent messages -> .eml in the vault, commit, push
    python3 tools/relay.py check --vault ~/vaults/sgit-network-relay      # pull; mark delivered/handled; bring replies home
    python3 tools/relay.py send  --dry-run /tmp/relay-preview             # write the .eml files to a folder, touch nothing else
    python3 tools/relay.py status                                         # what is unsent, sent, delivered, handled, received

The messages are the files in briefings/<site>/inbox/*.md (status: unsent). The vault is a clone made by the editor
of record with the vault key; this script never sees a key, only a directory that already holds .sg_vault/ (it can
also be named in NEWSROOM_RELAY_VAULT). Identities, peers and folders come from data/relay.json; the protocol is
sgraph.ai's Email-FS-lite (sources/sites/sgraph.ai/en-gb/library/how-it-works/), summarised in brief/08-relay.md:

  SEND     write mail/mailroom/<peer>/NNN-slug.eml and the same file in mail/newsroom.sgit/outbox/<peer>/
  DELIVER  the recipient moves it from their mailroom to their inbox/ (the mailroom copy disappearing is the receipt)
  DONE     the recipient moves it to done/ when the work is complete
  one commit per cycle: "@Newsroom check-in: ..."

Standard library only. `sgit` (pip install sgit-ai) is needed for commit, push and pull; without it the files are
written and the commands to run are printed.
"""
import argparse
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
from email.message import EmailMessage
from email.utils import format_datetime, make_msgid
from email import policy
from email.parser import BytesParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
RELAY = json.load(open('data/relay.json', encoding='utf-8'))
ME = RELAY['self']['name']
MAIL = RELAY['vault'].get('root', 'mail/')
KEY_SHAPES = (re.compile(r'sgit_private_'), re.compile(r'sgit_vk1_'), re.compile(r'\b[a-z0-9]{24}:[a-z0-9]{4,24}\b'))


def now():
    return datetime.datetime.now(datetime.timezone.utc)


def front_matter(text):
    if not text.startswith('---\n'):
        return {}, text
    head, _, body = text[4:].partition('\n---\n')
    meta = {}
    for line in head.split('\n'):
        if ':' in line and not line.startswith(' '):
            k, _, v = line.partition(':')
            meta[k.strip()] = v.strip()
    return meta, body.lstrip('\n')


def set_meta(path, **kv):
    """Rewrite the front matter of a message file with these fields added or replaced; the body is untouched."""
    text = open(path, encoding='utf-8').read()
    meta, body = front_matter(text)
    meta.update({k: v for k, v in kv.items() if v is not None})
    head = '\n'.join(f'{k}: {v}' for k, v in meta.items())
    open(path, 'w', encoding='utf-8').write(f'---\n{head}\n---\n\n{body}')


def messages():
    """Every message file, with its site, peer, path and front matter."""
    out = []
    d = 'briefings'
    for site in sorted(os.listdir(d)) if os.path.isdir(d) else []:
        inbox = os.path.join(d, site, 'inbox')
        if not os.path.isdir(inbox):
            continue
        for name in sorted(os.listdir(inbox)):
            if name.endswith('.md'):
                path = os.path.join(inbox, name)
                meta, body = front_matter(open(path, encoding='utf-8').read())
                out.append({'site': site, 'peer': RELAY['peers'].get(site), 'path': path, 'stem': name[:-3], 'meta': meta, 'body': body})
    return out


def refuse_keys(text, where):
    for pat in KEY_SHAPES:
        if pat.search(text):
            sys.exit(f'refused: {where} holds a credential-shaped string ({pat.pattern}); house rule 4')


def slug(s):
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s.lower())).strip('-')[:60]


def next_seq(outbox):
    n = 0
    if os.path.isdir(outbox):
        for f in os.listdir(outbox):
            m = re.match(r'(\d{3})-', f)
            if m:
                n = max(n, int(m.group(1)))
    return n + 1


def build_eml(msg, seq):
    """One RFC 2822 message from a briefings/<site>/inbox file."""
    peer, meta = msg['peer'], msg['meta']
    m = EmailMessage(policy=policy.SMTP)
    m['From'] = f'{ME} <{RELAY["self"]["address"]}>'
    m['To'] = f'{peer["name"]} <{peer["address"]}>'
    m['Subject'] = meta.get('title', msg['stem'])
    m['Date'] = format_datetime(now())
    mid = f'<{seq:03d}-{slug(meta.get("title", msg["stem"]))}@{RELAY["message_id_domain"]}>'
    m['Message-ID'] = mid
    if meta.get('in_reply_to'):
        m['In-Reply-To'] = meta['in_reply_to']
    m['X-Newsroom-File'] = msg['path']
    m['X-Newsroom-Page'] = f'https://{RELAY["self"]["site"]}/briefings/{msg["site"]}.html'
    if meta.get('about'):
        m['X-About'] = meta['about']
    body = msg['body'].rstrip() + '\n\n-- \n' + (f'{RELAY["self"]["alias"]} ({ME}), on behalf of {meta.get("from", "the editor of record")}. '
                                                 f'Reply in this vault: {MAIL}mailroom/{ME}/. The same message as a page: {m["X-Newsroom-Page"]}\n')
    m.set_content(body)
    return m, mid


def sgit(vault, *args, check=True):
    exe = shutil.which('sgit')
    if not exe:
        print(f'  (no sgit on PATH; run in {vault}: sgit {" ".join(args)})')
        return None
    r = subprocess.run([exe, *args], cwd=vault, capture_output=True, text=True)
    if r.stdout.strip():
        print('  ' + r.stdout.strip().replace('\n', '\n  '))
    if r.returncode and check:
        sys.exit(f'sgit {args[0]} failed: {r.stderr.strip()[:400]}')
    return r


def vault_dir(args):
    v = args.vault or os.environ.get('NEWSROOM_RELAY_VAULT')
    if args.dry_run:
        os.makedirs(args.dry_run, exist_ok=True)
        return args.dry_run
    if not v:
        sys.exit('no vault: pass --vault <clone of the relay vault> (or NEWSROOM_RELAY_VAULT), or --dry-run <folder>. '
                 'brief/08-relay.md says how the clone is made.')
    if not os.path.isdir(os.path.join(v, '.sg_vault')):
        sys.exit(f'{v} is not an sgit clone (no .sg_vault/). Clone the relay vault there first; the key stays in the clone.')
    return v


def cmd_send(args):
    v = vault_dir(args)
    todo = [m for m in messages() if m['meta'].get('status', 'unsent') == 'unsent' and m['meta'].get('direction', 'outgoing') == 'outgoing']
    if not todo:
        print('nothing unsent'); return
    sent = []
    for msg in todo:
        if not msg['peer']:
            print(f'  skip {msg["path"]}: no peer for {msg["site"]} in data/relay.json'); continue
        peer = msg['peer']['name']
        outbox = os.path.join(v, MAIL, ME, 'outbox', peer)
        mailroom = os.path.join(v, MAIL, 'mailroom', peer)
        seq = next_seq(outbox)
        eml, mid = build_eml(msg, seq)
        raw = eml.as_bytes()
        refuse_keys(raw.decode('utf-8', 'replace'), msg['path'])
        name = f'{seq:03d}-{slug(msg["meta"].get("title", msg["stem"]))}.eml'
        for d in (outbox, mailroom):
            os.makedirs(d, exist_ok=True)
            open(os.path.join(d, name), 'wb').write(raw)
        rel_ = f'{MAIL}{ME}/outbox/{peer}/{name}'
        print(f'  {msg["path"]} -> {rel_} and {MAIL}mailroom/{peer}/{name}')
        sent.append((msg, mid, rel_))
    if args.dry_run:
        print(f'dry run: {len(sent)} message(s) written under {v}; nothing committed, nothing marked'); return
    notes = os.path.join(v, MAIL, 'sessions', ME)
    os.makedirs(notes, exist_ok=True)
    with open(os.path.join(notes, 'notes.md'), 'a', encoding='utf-8') as f:
        f.write(f'\n{now().strftime("%Y-%m-%dT%H:%M:%SZ")} sent {len(sent)} message(s): ' + ', '.join(mid for _, mid, _ in sent) + '\n')
    sgit(v, 'commit', f'{RELAY["self"]["alias"]} check-in: sent {len(sent)} message(s) to ' + ', '.join(sorted({m["peer"]["alias"] for m, _, _ in sent})))
    sgit(v, 'push')
    sgit(v, 'status', check=False)
    stamp = now().strftime('%Y-%m-%dT%H:%MZ')
    for msg, mid, rel_ in sent:
        set_meta(msg['path'], status='sent', sent=stamp, message_id=mid, eml=rel_)
    print(f'sent {len(sent)}; the message files now say so (commit them with the run)')


def cmd_check(args):
    v = vault_dir(args)
    if not args.dry_run:
        sgit(v, 'pull', check=False)
    changed = 0
    # outgoing: the mailroom copy gone means delivered; a copy in the peer's done/ means handled
    for msg in messages():
        meta = msg['meta']
        if meta.get('direction', 'outgoing') != 'outgoing' or meta.get('status') not in ('sent', 'delivered') or not msg['peer']:
            continue
        name = os.path.basename(meta.get('eml', ''))
        peer = msg['peer']['name']
        if not name:
            continue
        if os.path.exists(os.path.join(v, MAIL, peer, 'done', name)):
            new = 'handled'
        elif not os.path.exists(os.path.join(v, MAIL, 'mailroom', peer, name)):
            new = 'delivered'
        else:
            new = 'sent'
        if new != meta.get('status'):
            set_meta(msg['path'], status=new, **{new: now().strftime('%Y-%m-%dT%H:%MZ')})
            print(f'  {msg["path"]}: {meta.get("status")} -> {new}'); changed += 1
    # incoming: deliver my mailroom to my inbox, and mirror each message as a page
    my_room = os.path.join(v, MAIL, 'mailroom', ME)
    my_inbox = os.path.join(v, MAIL, ME, 'inbox')
    delivered = []
    for name in sorted(os.listdir(my_room)) if os.path.isdir(my_room) else []:
        if not name.endswith('.eml'):
            continue
        src = os.path.join(my_room, name)
        eml = BytesParser(policy=policy.default).parse(open(src, 'rb'))
        sender = re.sub(r'\s*<.*', '', str(eml.get('From', ''))).strip() or 'unknown'
        site = next((s for s, p in RELAY['peers'].items() if p['name'] == sender), None) or slug(sender)
        body = eml.get_body(preferencelist=('plain',))
        text = body.get_content() if body else ''
        refuse_keys(text, name)
        out_dir = os.path.join('briefings', site, 'inbox')
        os.makedirs(out_dir, exist_ok=True)
        stem = f'{now().strftime("%Y-%m-%d")}__{slug(str(eml.get("Subject", name)))}'
        page = os.path.join(out_dir, stem + '.md')
        head = {'title': str(eml.get('Subject', name)), 'date': now().strftime('%Y-%m-%d'), 'direction': 'incoming', 'from': sender,
                'to': ME, 'status': 'received', 'message_id': str(eml.get('Message-ID', '')), 'in_reply_to': str(eml.get('In-Reply-To', '')) or None,
                'eml': f'{MAIL}{ME}/inbox/{name}', 'received': now().strftime('%Y-%m-%dT%H:%MZ')}
        open(page, 'w', encoding='utf-8').write('---\n' + '\n'.join(f'{k}: {v}' for k, v in head.items() if v) + '\n---\n\n' + text.strip() + '\n')
        if not args.dry_run:
            os.makedirs(my_inbox, exist_ok=True)
            shutil.move(src, os.path.join(my_inbox, name))
        delivered.append(name)
        print(f'  received {name} from {sender} -> {page}')
    if delivered and not args.dry_run:
        sgit(v, 'commit', f'{RELAY["self"]["alias"]} check-in: delivered {len(delivered)} message(s)')
        sgit(v, 'push')
        sgit(v, 'status', check=False)
    print(f'check: {changed} status change(s), {len(delivered)} received')


def cmd_status(args):
    counts = {}
    for msg in messages():
        st = msg['meta'].get('status', 'unsent')
        counts[st] = counts.get(st, 0) + 1
        print(f'  {st:10} {msg["path"]}  ->  {(msg["peer"] or {}).get("name", "?")}  {msg["meta"].get("message_id", "")}')
    print('relay: ' + ', '.join(f'{n} {k}' for k, n in sorted(counts.items())) if counts else 'relay: no messages')
    print(f'vault: {RELAY["vault"]["id"] or "not created"}; {RELAY["vault"]["status"]}' if not RELAY['vault']['id'] else f'vault: {RELAY["vault"]["id"]}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('command', choices=['send', 'check', 'status'])
    ap.add_argument('--vault', help='a clone of the relay vault (holds .sg_vault/); or NEWSROOM_RELAY_VAULT')
    ap.add_argument('--dry-run', metavar='DIR', help='write the mail tree here instead; no sgit, no status change')
    a = ap.parse_args()
    {'send': cmd_send, 'check': cmd_check, 'status': cmd_status}[a.command](a)
