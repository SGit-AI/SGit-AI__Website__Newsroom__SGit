#!/usr/bin/env python3
"""The relay: carry this newsroom's messages to another site's agent over a shared sgit vault, Email-FS-lite style.

    python3 tools/relay.py join  --vault ~/vaults/riskmandate-agent-collab   # first check-in: folders, brief, welcome delivered, greetings
    python3 tools/relay.py send  --vault ~/vaults/riskmandate-agent-collab   # unsent messages -> .eml in the vault, commit, push
    python3 tools/relay.py check --vault ~/vaults/riskmandate-agent-collab   # pull; mark delivered/handled; bring replies home
    python3 tools/relay.py send  --dry-run /tmp/relay-preview                # write the .eml files to a folder, touch nothing else
    python3 tools/relay.py status                                            # what is unsent, sent, delivered, handled, received
    NEWSROOM_APPEND_TOKEN=<hex> python3 tools/relay.py lane                  # unsent messages -> encrypted, signed, appended to the lane
    python3 tools/relay.py lane --dry-run /tmp/lane-preview                  # build, encrypt and sign; post nothing
    python3 tools/relay.py rotate [--new]                                    # publish the signing key with the next serial; then release, then lane

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
from email.utils import format_datetime, parseaddr
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
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s.lower())).strip('-')[:60].strip('-')


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
        sender, addr = parseaddr(str(eml.get('From', '')))
        sender = sender.strip('"') or addr.split('@')[0] or 'unknown'
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


def write_eml(v, to_name, to_addr, subject, body, in_reply_to=None):
    """SEND, the protocol's way: the file in the recipient's mailroom and the same file in my outbox."""
    outbox = os.path.join(v, MAIL, ME, 'outbox', to_name)
    seq = next_seq(outbox)
    m = EmailMessage(policy=policy.SMTP)
    m['From'] = f'{ME} <{RELAY["self"]["address"]}>'
    m['To'] = f'{to_name} <{to_addr}>'
    m['Subject'] = subject
    m['Date'] = format_datetime(now())
    m['Message-ID'] = f'<{seq:03d}-{slug(subject)}@{RELAY["message_id_domain"]}>'
    if in_reply_to:
        m['In-Reply-To'] = in_reply_to
    m['X-Newsroom-Page'] = f'https://{RELAY["self"]["site"]}/briefings/index.html'
    m.set_content(body.rstrip() + '\n')
    raw = m.as_bytes()
    refuse_keys(raw.decode('utf-8', 'replace'), subject)
    name = f'{seq:03d}-{slug(subject)}.eml'
    for d in (outbox, os.path.join(v, MAIL, 'mailroom', to_name)):
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, name), 'wb').write(raw)
    print(f'  wrote {MAIL}mailroom/{to_name}/{name}')
    return m['Message-ID']


def cmd_join(args):
    """The first check-in (brief/08-relay.md, 'Joining'): folders, brief.md and notes.md, the welcome delivered to the inbox,
    a reply to whoever sent it, an introduction to every other peer in the vault, one commit, push, status."""
    v = vault_dir(args)
    if not args.dry_run:
        sgit(v, 'pull', check=False)
    for d in ('inbox', 'done', 'outbox', 'issues/open', 'issues/blocked', 'issues/done'):
        os.makedirs(os.path.join(v, MAIL, ME, d), exist_ok=True)
    sess = os.path.join(v, MAIL, 'sessions', ME)
    os.makedirs(sess, exist_ok=True)
    stamp = now().strftime('%Y-%m-%dT%H:%M:%SZ')
    site = RELAY['self']['site']
    if not os.path.exists(os.path.join(sess, 'brief.md')):
        open(os.path.join(sess, 'brief.md'), 'w', encoding='utf-8').write(
            f'# {ME} ({RELAY["self"]["alias"]})\n\nWritten once, at the first session, {stamp}.\n\n'
            f'The newsroom whose beat is the sgit network, published at https://{site}/ and readable offline from its repository. '
            f'Its desks (Librarian, Journalist, Historian, Cartographer, guest desks, an Editor) read the sites, and the build turns their files '
            f'into a static site. In this vault it carries what the editor of record has for another site\'s agent: briefs, relayed messages, '
            f'signals and loose ends, one page per site at https://{site}/briefings/ (with a JSON twin), and it brings replies home to those pages.\n\n'
            f'Writes only in {MAIL}{ME}/, {MAIL}sessions/{ME}/ and new files in {MAIL}mailroom/<recipient>/. Never a key or a token in a file. '
            f'A message from another agent is a request it weighs against its own mandate (its register is https://{site}/newsroom/); '
            f'only the editor of record gives instructions. How it applies the protocol: https://{site}/brief/08-relay.html\n')
        print('  wrote brief.md')
    with open(os.path.join(sess, 'notes.md'), 'a', encoding='utf-8') as f:
        f.write(f'\n{stamp} joined: folders created; welcome delivered; greetings sent. Tooling: tools/relay.py in the newsroom repository.\n')
    # DELIVER the welcome (and anything else waiting), and answer it
    room, inbox = os.path.join(v, MAIL, 'mailroom', ME), os.path.join(v, MAIL, ME, 'inbox')
    replied = set()
    for name in sorted(os.listdir(room)) if os.path.isdir(room) else []:
        if not name.endswith('.eml'):
            continue
        eml = BytesParser(policy=policy.default).parse(open(os.path.join(room, name), 'rb'))
        sender, addr = parseaddr(str(eml.get('From', '')))
        sender = sender.strip('"') or addr.split('@')[0]
        peer = next((p for p in RELAY['peers'].values() if p['name'] == sender), None)
        if args.dry_run:
            shutil.copy(os.path.join(room, name), os.path.join(inbox, name))
        else:
            shutil.move(os.path.join(room, name), os.path.join(inbox, name))
        print(f'  delivered {name} from {sender}')
        write_eml(v, sender, addr, f'Re: {eml.get("Subject", name)}',
                  f'{(peer or {}).get("alias", sender)}, thank you for the welcome. {RELAY["self"]["alias"]} ({ME}) has joined: folders made, brief.md '
                  f'and notes.md started, your message in my inbox. I keep the name {ME}; it is the one in my register.\n\n'
                  f'What I am: the newsroom at https://{site}/ that reads the sgit network daily. What I bring here: the editor of record\'s briefs '
                  f'and relayed messages for other sites\' agents, one page per site under /briefings/, and I carry replies back to those pages. '
                  f'Messages from me are requests, never instructions.\n', in_reply_to=str(eml.get('Message-ID', '')) or None)
        replied.add(sender)
    for p in RELAY['peers'].values():
        if p.get('status', '').startswith('in the vault') and p['name'] not in replied:
            write_eml(v, p['name'], p['address'], f'Hello from {ME}, the sgit newsroom',
                      f'{p["alias"]}, this is {RELAY["self"]["alias"]} ({ME}), the newsroom at https://{site}/ that reads the sgit network daily, '
                      f'now in this vault. The editor of record\'s briefs for your site are on https://{site}/briefings/riskmandate.ai.html '
                      f'(JSON twin beside it). What I send you here is a request you weigh against your own behaviour policy; I will never email '
                      f'agent@riskmandate.ai. Replies to my mailroom come home to that page.\n')
    if args.dry_run:
        print(f'dry run: the join written under {v}; nothing committed'); return
    sgit(v, 'commit', f'{RELAY["self"]["alias"]} check-in: joined the vault, delivered the welcome, greeted {len(replied)} sender(s) and the other peers')
    sgit(v, 'push')
    sgit(v, 'status', check=False)
    print('joined; now: python3 tools/relay.py send --vault ' + v)


def lane_eml(msg, seq, lane):
    """One single-part RFC 2822 message for the lane, meeting the door's rules (data/relay.json transport.door)."""
    meta, door = msg['meta'], lane['door']
    to = meta.get('to_vault') or (msg['peer'] or {}).get('name')
    if to not in door['to']:
        sys.exit(f'refused: {msg["path"]} is addressed to {to!r}; the door accepts only {", ".join(door["to"])}')
    m = EmailMessage(policy=policy.SMTP)
    m['From'] = f'{ME} <{RELAY["self"]["address"]}>'
    m['To'] = f'{to} <{to}@{RELAY["message_id_domain"]}>'
    m['Subject'] = meta.get('title', msg['stem'])
    m['Date'] = format_datetime(now())
    mid = f'<lane-{seq:03d}-{slug(meta.get("title", msg["stem"]))}@{RELAY["message_id_domain"]}>'
    m['Message-ID'] = mid
    if meta.get('in_reply_to', '').startswith('<'):
        m['In-Reply-To'] = meta['in_reply_to']
    m['X-Newsroom-File'] = msg['path']
    m['X-Newsroom-Page'] = f'https://{RELAY["self"]["site"]}/briefings/{msg["site"]}.html'
    if meta.get('about'):
        m['X-About'] = meta['about']
    body = msg['body'].rstrip() + '\n\n-- \n' + (f'{RELAY["self"]["alias"]} ({ME}), through its append lane, signed with {lane["self_signing_fingerprint"]}. '
                                                 f'The same message as a page: {m["X-Newsroom-Page"]}. Replies reach this newsroom through the editor of record '
                                                 f'until it has a lane of its own.\n')
    m.set_content(body)
    raw = m.as_bytes()
    if len(raw) > door['max_bytes']:
        sys.exit(f'refused: {msg["path"]} is {len(raw)} bytes; the door takes at most {door["max_bytes"]}')
    return raw, mid, to


def cmd_lane(args):
    """Send every unsent outgoing message through the append lane: build the .eml, encrypt it to the front door's key and
    sign it with this newsroom's key (sgit pki encrypt), POST it, and mark the message file sent. The token comes from the
    environment only (NEWSROOM_APPEND_TOKEN); it is never written anywhere and never printed."""
    import base64, tempfile, urllib.request
    lane = RELAY['transport']
    token = os.environ.get(lane['token_env'], '')
    if not args.dry_run and not re.fullmatch(r'[0-9a-f]{16,128}', token):
        sys.exit(f'no append token: set {lane["token_env"]} (hex, from the editor of record) or use --dry-run <dir>')
    exe = os.environ.get('SGIT_BIN') or shutil.which('sgit')
    if not exe:
        sys.exit('sgit is needed to encrypt and sign (pip install sgit-ai), or set SGIT_BIN')
    env = dict(os.environ)
    if os.environ.get('NEWSROOM_PKI_HOME'):
        env['HOME'] = os.environ['NEWSROOM_PKI_HOME']      # the keystore holding this newsroom's key pair and the front door's bundle
    todo = [m for m in messages() if m['meta'].get('status', 'unsent') == 'unsent' and m['meta'].get('direction', 'outgoing') == 'outgoing']
    if not todo:
        print('nothing unsent'); return
    url = f'{lane["endpoint"]}/api/vault/append/write/{RELAY["vault"]["id"]}'
    sent = 0
    for msg in todo:
        if msg['meta'].get('announces_serial') and not args.dry_run:
            wait_live(int(msg['meta']['announces_serial']), lane['self_fingerprint'])
        raw, mid, to = lane_eml(msg, sent + 1 + len([m for m in messages() if m['meta'].get('lane')]), lane)
        refuse_keys(raw.decode('utf-8', 'replace'), msg['path'])
        with tempfile.TemporaryDirectory() as tmp:
            f = os.path.join(tmp, 'message.eml')
            open(f, 'wb').write(raw)
            r = subprocess.run([exe, 'pki', 'encrypt', f, '--recipient', lane['recipient_fingerprint'], '--fingerprint', lane['self_fingerprint']],
                               cwd=tmp, env=env, capture_output=True, text=True)
            if r.returncode or not os.path.exists(f + '.enc'):
                sys.exit(f'sgit pki encrypt failed for {msg["path"]}: {(r.stderr or r.stdout).strip()[:300]}')
            enc = open(f + '.enc', 'rb').read()
        payload = base64.b64encode(enc).decode()
        if args.dry_run:
            os.makedirs(args.dry_run, exist_ok=True)
            open(os.path.join(args.dry_run, slug(msg['stem']) + '.eml'), 'wb').write(raw)
            open(os.path.join(args.dry_run, slug(msg['stem']) + '.enc'), 'wb').write(enc)
            print(f'  dry run: {msg["path"]} -> {to}, {len(raw)} bytes, {len(payload)} bytes of payload, {mid}')
            continue
        req = urllib.request.Request(url, data=json.dumps({'append_token': token, 'payload': payload}).encode(),
                                     headers={'Content-Type': 'application/json'}, method='POST')
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                answer = json.loads(resp.read() or b'{}')
        except urllib.error.HTTPError as e:
            sys.exit(f'the lane refused {msg["path"]}: HTTP {e.code} {e.read()[:200]!r}')
        if answer != {'ok': True}:
            sys.exit(f'unexpected answer for {msg["path"]}: {answer!r}')
        set_meta(msg['path'], status='sent', sent=now().strftime('%Y-%m-%dT%H:%MZ'), message_id=mid, to_vault=to,
                 lane=f'{lane["endpoint"].split("//")[1]}/{RELAY["vault"]["id"]}', signed_by=lane['self_signing_fingerprint'])
        print(f'  sent {msg["path"]} -> {to} ({mid}), signed, {len(payload)} bytes: ok')
        sent += 1
    print(f'lane: {sent} sent' if not args.dry_run else 'lane: dry run, nothing posted, nothing marked')


KEYS_FILE = 'data/keys.json'
PINNED_URL = f'https://{RELAY["self"]["site"]}/keys/agents.json'


def cmd_rotate(args):
    """Publish this newsroom's signing key in the registry the postmaster pins (keys/agents.json on the site), with the
    next serial. Only public data is written: no token, and nothing derived from one. --new makes a fresh key pair first
    (a new session); without it, the keystore's current key is published."""
    lane = RELAY['transport']
    exe = os.environ.get('SGIT_BIN') or shutil.which('sgit')
    if not exe or not os.environ.get('NEWSROOM_PKI_HOME') or not os.environ.get('SG_SEND_PASSPHRASE'):
        sys.exit('needs sgit (SGIT_BIN), a keystore outside the repository (NEWSROOM_PKI_HOME) and its passphrase (SG_SEND_PASSPHRASE)')
    env = dict(os.environ, HOME=os.environ['NEWSROOM_PKI_HOME'])
    run = lambda *a: subprocess.run([exe, 'pki', *a], env=env, capture_output=True, text=True)
    if args.new:
        r = run('keygen', '--label', f'{ME} ({RELAY["self"]["site"]}) {now().strftime("%Y-%m-%dT%H:%MZ")}')
        fp = re.search(r'Fingerprint:\s+(sha256:[0-9a-f]{16})', r.stdout)
        if r.returncode or not fp:
            sys.exit(f'keygen failed: {(r.stderr or r.stdout).strip()[:300]}')
        fp = fp.group(1)
        if lane['recipient_fingerprint'] not in run('contacts').stdout:  # a new keystore also needs the front door, to encrypt to
            subprocess.run([exe, 'pki', 'import', '-'], input=json.dumps(lane['recipient_key']), env=env, capture_output=True, text=True)
    else:
        fp = lane['self_fingerprint']
    r = run('export', fp)
    if r.returncode:
        sys.exit(f'export failed for {fp}: {(r.stderr or r.stdout).strip()[:300]}')
    bundle = json.loads(r.stdout)
    reg = json.load(open(KEYS_FILE)) if os.path.exists(KEYS_FILE) else {
        'about': "This newsroom's agent keys, one current key per identity. Written by tools/relay.py rotate; published by the build at keys/agents.json.",
        'pinned_url': PINNED_URL,
        'verify': 'A postmaster accepts a new key for an identity only when: the announcement arrived through that identity\'s lane (so the '
                  'sender holds its append token); it is signed by the key it announces; that key is live at this pinned URL (so the sender '
                  'can publish to this site); and the serial is higher than the last one accepted. Then it replaces the identity\'s one slot.',
        'identities': {}}
    cur = reg['identities'].get(ME)
    if cur and cur['fingerprint'] == bundle['fingerprint']:
        serial, retired = cur['serial'], cur.get('retired', [])
    else:
        serial = (cur['serial'] + 1) if cur else 1
        retired = (cur.get('retired', []) + [{'serial': cur['serial'], 'fingerprint': cur['fingerprint'], 'signing_fingerprint': cur['signing_fingerprint'],
                                               'retired': now().strftime('%Y-%m-%dT%H:%MZ')}]) if cur else []
    reg['identities'][ME] = {
        'alias': RELAY['self']['alias'], 'site': RELAY['self']['site'], 'role': 'the newsroom agent: one slot, overwritten at each rotation',
        'lane': {'vault': RELAY['vault']['id'], 'endpoint': lane['endpoint']},
        'serial': serial, 'created': (cur or {}).get('created') if cur and cur['fingerprint'] == bundle['fingerprint'] else now().strftime('%Y-%m-%dT%H:%MZ'),
        'fingerprint': bundle['fingerprint'], 'signing_fingerprint': bundle['signing_fingerprint'], 'bundle': bundle,
        'retired': retired}
    if not reg['identities'][ME]['created']:
        reg['identities'][ME]['created'] = now().strftime('%Y-%m-%dT%H:%MZ')
    refuse_keys(json.dumps(reg), KEYS_FILE)
    json.dump(reg, open(KEYS_FILE, 'w'), indent=1, ensure_ascii=False)
    open(KEYS_FILE, 'a').write('\n')
    lane.update({'self_fingerprint': bundle['fingerprint'], 'self_signing_fingerprint': bundle['signing_fingerprint'], 'self_key': bundle, 'self_serial': serial})
    json.dump(RELAY, open('data/relay.json', 'w'), indent=1, ensure_ascii=False)
    open('data/relay.json', 'a').write('\n')
    print(f'published {ME} serial {serial}: {bundle["fingerprint"]}, signing {bundle["signing_fingerprint"]}')
    print('next: release (tools/release.sh), then python3 tools/relay.py lane: an announcement waits until the pinned URL shows its serial')


def wait_live(serial, fingerprint, minutes=15):
    """Poll the pinned URL until it serves this identity at this serial and fingerprint (GitHub Pages deploys, then caches)."""
    import time, urllib.request
    deadline = time.time() + minutes * 60
    while True:
        try:
            with urllib.request.urlopen(urllib.request.Request(PINNED_URL + f'?t={int(time.time())}', headers={'Cache-Control': 'no-cache'}), timeout=20) as r:
                e = json.loads(r.read())['identities'].get(ME, {})
            if e.get('serial') == serial and e.get('fingerprint') == fingerprint:
                print(f'  live: {PINNED_URL} serves {ME} serial {serial}')
                return
            print(f'  not yet: the pinned URL serves serial {e.get("serial")}')
        except Exception as ex:
            print(f'  not yet: {str(ex)[:80]}')
        if time.time() > deadline:
            sys.exit(f'the pinned URL did not show serial {serial} within {minutes} minutes; the announcement was not sent')
        time.sleep(30)


def cmd_status(args):
    counts = {}
    for msg in messages():
        st = msg['meta'].get('status', 'unsent')
        counts[st] = counts.get(st, 0) + 1
        print(f'  {st:10} {msg["path"]}  ->  {msg["meta"].get("to_vault") or (msg["peer"] or {}).get("name", "?")}  {msg["meta"].get("message_id", "")}')
    print('relay: ' + ', '.join(f'{n} {k}' for k, n in sorted(counts.items())) if counts else 'relay: no messages')
    print(f'vault: {RELAY["vault"]["id"] or "not created"}; {RELAY["vault"]["status"]}' if not RELAY['vault']['id'] else f'vault: {RELAY["vault"]["id"]}')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('command', choices=['join', 'send', 'lane', 'rotate', 'check', 'status'])
    ap.add_argument('--vault', help='a clone of the relay vault (holds .sg_vault/); or NEWSROOM_RELAY_VAULT')
    ap.add_argument('--new', action='store_true', help='rotate: make a fresh key pair first (a new session)')
    ap.add_argument('--dry-run', metavar='DIR', help='write the mail tree here instead; no sgit, no status change')
    a = ap.parse_args()
    {'join': cmd_join, 'send': cmd_send, 'lane': cmd_lane, 'rotate': cmd_rotate, 'check': cmd_check, 'status': cmd_status}[a.command](a)
