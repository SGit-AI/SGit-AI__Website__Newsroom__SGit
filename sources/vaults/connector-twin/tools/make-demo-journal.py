#!/usr/bin/env python3
"""Generate the demo journal: one invented agent session against Gmail and Google Calendar.

Run from the vault root:

    python3 tools/make-demo-journal.py

Writes journal/session-2026-09-22.jsonl, one entry per line, hash-chained.

Everything here is invented. The people, the companies and the email addresses use the reserved
.example domain. The request and response shapes follow the Gmail API v1 and Google Calendar API v3,
abbreviated to the fields the replay needs. Message bodies are stored decoded (body_text) for
readability; the real API returns them base64url-encoded in payload.body.data.

Each line is what an append lane would receive for one tool call: the MCP call the agent made,
the upstream HTTP request the connector sent, and the response it got back. The Authorization
header is never captured. `prev` and `hash` chain the entries so a missing or edited line shows.
"""
import hashlib, json, os

SESSION   = 'sess-2026-09-22-a'
AGENT     = 'scheduling-assistant'
PRINCIPAL = 'maya@harbourfinch.example'
GMAIL     = 'https://gmail.googleapis.com/gmail/v1/users/me'
CAL       = 'https://www.googleapis.com/calendar/v3/calendars/primary'
TZ        = 'Europe/London'

PROMPTS = [
    {'id': 'p1', 'role': 'user', 'ts': '2026-09-22T09:14:00.000Z',
     'text': 'Sort out next week for me. Move the Northwind review to Thursday morning, decline anything '
             'that clashes with the offsite on Friday, clear out the newsletter clutter, and reply to Sam '
             'about the proposal with a time for a call.'},
    {'id': 'a1', 'role': 'agent', 'ts': '2026-09-22T09:16:41.000Z',
     'text': 'Done. Northwind review moved to Thursday 1 October at 10:00. Declined the studio sync and '
             'removed the supplier call, both clashed with the offsite. Archived three newsletters and '
             'deleted an old reminder. Replied to Sam and booked a call for Wednesday at 15:00.'},
]

def h(name, value):
    return {'name': name, 'value': value}

def msg(mid, thread, labels, frm, to, subject, date, snippet, body=None, fmt='full'):
    m = {'id': mid, 'threadId': thread, 'labelIds': labels, 'snippet': snippet,
         'payload': {'headers': [h('From', frm), h('To', to), h('Subject', subject), h('Date', date)]}}
    if fmt == 'full' and body is not None:
        m['payload']['body_text'] = body
    return m

def ev(eid, summary, start, end, attendees, organizer, location=None, description=None):
    e = {'id': eid, 'status': 'confirmed', 'summary': summary,
         'start': {'dateTime': start, 'timeZone': TZ}, 'end': {'dateTime': end, 'timeZone': TZ},
         'organizer': {'email': organizer, 'self': organizer == PRINCIPAL},
         'attendees': attendees}
    if location:    e['location'] = location
    if description: e['description'] = description
    return e

def att(email, status, self_=False):
    a = {'email': email, 'responseStatus': status}
    if self_: a['self'] = True
    return a

# ---- the mailbox as the agent will see it --------------------------------------------------
M = {
 'm1': msg('18c2a91f0e1a0001', 't-sam', ['INBOX', 'UNREAD', 'IMPORTANT'],
           'Sam Reyes <sam@reyesarchitects.example>', PRINCIPAL, 'Proposal: studio fit-out, v2',
           'Mon, 21 Sep 2026 17:42:10 +0100',
           'Maya, attached is v2 of the fit-out proposal with the revised joinery costs...',
           'Maya,\n\nAttached is v2 of the fit-out proposal with the revised joinery costs. The main change '
           'is the reception desk, which comes down by about eight per cent if we use the oak veneer.\n\n'
           'Could we talk it through this week or early next? Any afternoon works for me.\n\nSam'),
 'm2': msg('18c2a91f0e1a0002', 't-northwind', ['INBOX', 'CATEGORY_UPDATES'],
           'Priya Nair <priya@northwind.example>', PRINCIPAL, 'Northwind quarterly review: agenda',
           'Mon, 21 Sep 2026 11:05:44 +0100',
           'Hi Maya, agenda for the quarterly review below. If Tuesday no longer suits...',
           'Hi Maya,\n\nAgenda for the quarterly review below. If Tuesday no longer suits, Thursday morning '
           'works on our side too.\n\n1. Brand refresh status\n2. Q4 campaign scope\n3. Invoicing\n\nPriya'),
 'm3': msg('18c2a91f0e1a0003', 't-dw', ['INBOX', 'CATEGORY_PROMOTIONS'],
           'Design Weekly <news@designweekly.example>', PRINCIPAL, 'Design Weekly #212: the return of serif',
           'Sun, 20 Sep 2026 07:00:00 +0100', 'This week: the return of serif, three studios on pricing...',
           fmt='metadata'),
 'm4': msg('18c2a91f0e1a0004', 't-cn', ['INBOX', 'CATEGORY_PROMOTIONS'],
           'Colour Notes <hello@colournotes.example>', PRINCIPAL, 'Colour Notes, September',
           'Sat, 19 Sep 2026 08:30:00 +0100', 'Autumn palettes, and a note on accessible contrast...',
           fmt='metadata'),
 'm5': msg('18c2a91f0e1a0005', 't-offsite', ['INBOX'],
           'Harbour & Finch Office <office@harbourfinch.example>', 'team@harbourfinch.example',
           'Offsite logistics: Friday 2 October', 'Fri, 18 Sep 2026 15:20:02 +0100',
           'All, the offsite runs 09:00 to 17:00 on Friday 2 October at the boathouse...',
           'All,\n\nThe offsite runs 09:00 to 17:00 on Friday 2 October at the boathouse. Please keep the '
           'whole day clear.\n\nOffice'),
 'm6': msg('18c2a91f0e1a0006', 't-inv', ['INBOX'],
           'Coastline Print Accounts <accounts@coastlineprint.example>', PRINCIPAL,
           'Invoice INV-2291: payment reminder', 'Tue, 8 Sep 2026 10:12:31 +0100',
           'This is a reminder that invoice INV-2291 for the brochure print run is now due...',
           'Hello,\n\nThis is a reminder that invoice INV-2291 for the brochure print run is now due. '
           'The amount outstanding and our bank details are on the attached invoice.\n\nIf this has '
           'already been paid, please ignore this message.\n\nCoastline Print Accounts'),
 'm7': {'id': '18c2a91f0e1a0007', 'threadId': 't-lunch'},
 'm8': msg('18c2a91f0e1a0008', 't-cb', ['INBOX', 'CATEGORY_UPDATES'],
           'CloudBox <noreply@cloudbox.example>', PRINCIPAL, 'Your storage is almost full',
           'Thu, 17 Sep 2026 06:01:09 +0100', 'You have used 92% of your storage...', fmt='metadata'),
}

# ---- the calendar as the agent will see it -------------------------------------------------
E = {
 'e1': ev('evt0northwindq3', 'Northwind quarterly review', '2026-09-29T14:00:00+01:00', '2026-09-29T15:00:00+01:00',
          [att(PRINCIPAL, 'accepted', True), att('priya@northwind.example', 'accepted'),
           att('tom@harbourfinch.example', 'accepted')], PRINCIPAL, 'Video call'),
 'e2': ev('evt0studiosync', 'Weekly studio sync', '2026-10-02T09:30:00+01:00', '2026-10-02T10:00:00+01:00',
          [att(PRINCIPAL, 'accepted', True), att('tom@harbourfinch.example', 'accepted'),
           att('lee@harbourfinch.example', 'accepted')], 'tom@harbourfinch.example', 'Studio'),
 'e3': ev('evt0offsite', 'Team offsite', '2026-10-02T09:00:00+01:00', '2026-10-02T17:00:00+01:00',
          [att(PRINCIPAL, 'accepted', True), att('team@harbourfinch.example', 'accepted')],
          'office@harbourfinch.example', 'The boathouse'),
 'e4': ev('evt0coastline', 'Supplier call: Coastline Print', '2026-10-02T16:00:00+01:00', '2026-10-02T16:30:00+01:00',
          [att(PRINCIPAL, 'accepted', True), att('accounts@coastlineprint.example', 'accepted')], PRINCIPAL,
          'Phone', 'Agree the reprint schedule and settle INV-2291.'),
 'e5': ev('evt0dentist', 'Dentist', '2026-09-30T08:30:00+01:00', '2026-09-30T09:15:00+01:00',
          [att(PRINCIPAL, 'accepted', True)], PRINCIPAL, 'High Street'),
}

def rid(n):
    return f'req-{n:03d}'

entries = []
def add(ts, connector, effect, tool, args, method, url, body, status, resp):
    entries.append({
        'seq': len(entries) + 1, 'ts': ts, 'session': SESSION, 'agent': AGENT, 'principal': PRINCIPAL,
        'connector': connector, 'capture': 'broker', 'prompt_ref': 'p1', 'effect': effect,
        'mcp': {'jsonrpc': '2.0', 'id': len(entries) + 1, 'method': 'tools/call',
                'params': {'name': tool, 'arguments': args}},
        'request': {'method': method, 'url': url, 'headers': {'authorization': '[never captured]'},
                    'body': body},
        'response': {'status': status, 'body': resp},
    })

import copy
ids = [M[k]['id'] for k in ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8']]

add('2026-09-22T09:14:03.120Z', 'gmail', 'read', 'gmail_search_messages', {'q': 'in:inbox newer_than:14d'},
    'GET', f'{GMAIL}/messages?q=in%3Ainbox%20newer_than%3A14d&maxResults=20', None, 200,
    {'messages': [{'id': M[k]['id'], 'threadId': M[k]['threadId']} for k in ['m1','m2','m3','m4','m5','m6','m7','m8']],
     'resultSizeEstimate': 8})
for k, fmt, t in [('m1','full','09:14:04.310'), ('m2','full','09:14:04.902'), ('m3','metadata','09:14:05.377'),
                  ('m4','metadata','09:14:05.801'), ('m5','full','09:14:06.244'), ('m6','full','09:14:06.790'),
                  ('m8','metadata','09:14:07.153')]:
    add(f'2026-09-22T{t}Z', 'gmail', 'read', 'gmail_read_message', {'messageId': M[k]['id']},
        'GET', f"{GMAIL}/messages/{M[k]['id']}?format={fmt}", None, 200, M[k])

add('2026-09-22T09:14:09.610Z', 'calendar', 'read', 'calendar_list_events',
    {'timeMin': '2026-09-28T00:00:00+01:00', 'timeMax': '2026-10-03T00:00:00+01:00'},
    'GET', f'{CAL}/events?timeMin=2026-09-28T00%3A00%3A00%2B01%3A00&timeMax=2026-10-03T00%3A00%3A00%2B01%3A00&singleEvents=true',
    None, 200, {'kind': 'calendar#events', 'items': [E[k] for k in ['e1','e5','e3','e2','e4']]})

e1_after = copy.deepcopy(E['e1'])
e1_after['start']['dateTime'] = '2026-10-01T10:00:00+01:00'
e1_after['end']['dateTime']   = '2026-10-01T11:00:00+01:00'
add('2026-09-22T09:15:02.018Z', 'calendar', 'write', 'calendar_update_event',
    {'eventId': E['e1']['id'], 'start': '2026-10-01T10:00', 'end': '2026-10-01T11:00', 'notify': True},
    'PATCH', f"{CAL}/events/{E['e1']['id']}?sendUpdates=all",
    {'start': e1_after['start'], 'end': e1_after['end']}, 200, e1_after)

e2_after = copy.deepcopy(E['e2'])
e2_after['attendees'][0]['responseStatus'] = 'declined'
add('2026-09-22T09:15:20.455Z', 'calendar', 'write', 'calendar_respond_to_event',
    {'eventId': E['e2']['id'], 'response': 'declined', 'notify': True},
    'PATCH', f"{CAL}/events/{E['e2']['id']}?sendUpdates=all",
    {'attendees': e2_after['attendees']}, 200, e2_after)

add('2026-09-22T09:15:31.902Z', 'calendar', 'write', 'calendar_delete_event',
    {'eventId': E['e4']['id'], 'notify': True},
    'DELETE', f"{CAL}/events/{E['e4']['id']}?sendUpdates=all", None, 204, None)

add('2026-09-22T09:15:48.270Z', 'gmail', 'write', 'gmail_modify_labels',
    {'messageIds': [M['m3']['id'], M['m4']['id'], M['m8']['id']], 'removeLabels': ['INBOX']},
    'POST', f'{GMAIL}/messages/batchModify',
    {'ids': [M['m3']['id'], M['m4']['id'], M['m8']['id']], 'removeLabelIds': ['INBOX']}, 204, None)

m3_trashed = {'id': M['m3']['id'], 'threadId': M['m3']['threadId'], 'labelIds': ['TRASH', 'CATEGORY_PROMOTIONS']}
add('2026-09-22T09:15:55.731Z', 'gmail', 'write', 'gmail_trash_message', {'messageId': M['m3']['id']},
    'POST', f"{GMAIL}/messages/{M['m3']['id']}/trash", None, 200, m3_trashed)

add('2026-09-22T09:16:03.118Z', 'gmail', 'write', 'gmail_delete_message', {'messageId': M['m6']['id']},
    'DELETE', f"{GMAIL}/messages/{M['m6']['id']}", None, 204, None)

reply_body = ('Sam,\n\nThanks for v2. The oak veneer change makes sense. Could we talk it through on a call on '
              'Wednesday 30 September at 15:00? I have sent an invite.\n\nMaya')
add('2026-09-22T09:16:20.664Z', 'gmail', 'write', 'gmail_send_message',
    {'to': 'sam@reyesarchitects.example', 'subject': 'Re: Proposal: studio fit-out, v2', 'threadId': M['m1']['threadId'],
     'body': reply_body},
    'POST', f'{GMAIL}/messages/send',
    {'threadId': M['m1']['threadId'], 'raw_decoded': {'to': 'sam@reyesarchitects.example',
     'subject': 'Re: Proposal: studio fit-out, v2', 'body_text': reply_body}}, 200,
    {'id': '18c2a91f0e1a0009', 'threadId': M['m1']['threadId'], 'labelIds': ['SENT']})

new_ev = ev('evt0samcall', 'Call with Sam Reyes: fit-out proposal', '2026-09-30T15:00:00+01:00', '2026-09-30T15:30:00+01:00',
            [att(PRINCIPAL, 'accepted', True), att('sam@reyesarchitects.example', 'needsAction')], PRINCIPAL, 'Phone')
add('2026-09-22T09:16:38.940Z', 'calendar', 'write', 'calendar_create_event',
    {'summary': new_ev['summary'], 'start': '2026-09-30T15:00', 'end': '2026-09-30T15:30',
     'attendees': ['sam@reyesarchitects.example'], 'notify': True},
    'POST', f'{CAL}/events?sendUpdates=all',
    {k: new_ev[k] for k in ['summary', 'start', 'end', 'attendees', 'location']}, 200, new_ev)

# ---- chain -----------------------------------------------------------------------------------
prev = '0' * 64
for e in entries:
    e['prev'] = prev
    canon = json.dumps({k: v for k, v in e.items() if k != 'hash'}, sort_keys=True, separators=(',', ':'),
                       ensure_ascii=False)
    e['hash'] = hashlib.sha256(canon.encode('utf-8')).hexdigest()
    prev = e['hash']

os.makedirs('journal', exist_ok=True)
with open('journal/session-2026-09-22.jsonl', 'w') as f:
    for e in entries:
        f.write(json.dumps(e, ensure_ascii=False, separators=(',', ':')) + '\n')
with open('journal/prompts-2026-09-22.json', 'w') as f:
    json.dump({'session': SESSION, 'capture': 'on', 'prompts': PROMPTS}, f, indent=2, ensure_ascii=False)
print(f'{len(entries)} entries, head {prev[:12]}')
