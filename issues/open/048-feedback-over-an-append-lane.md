---
title: Send the reader's feedback from the browser to the newsroom over an append lane
created: 2026-09-25T17:00:00Z
priority: high
type: task
owner: build.desk
source: admin/inbox/2026-09-25__feedback-over-an-append-lane.md
parent: 002-personalised-site
estimated_effort: medium
---

# Send the reader's feedback from the browser to the newsroom over an append lane

The reader's feedback log (local storage) gains a second way out beside "Copy for Claude": a Send button that encrypts
the unsent events to the newsroom's published public key and appends them to a lane on a vault the newsroom owns. The
append token is given to the browser by the editor of record (a link with the token in the fragment, or pasted into
settings) and kept in local storage; without it, nothing can be sent.

Checked on 25 September, before any build:
- CORS: both send.sgraph.ai and dev.send.sgraph.ai answer the preflight with `access-control-allow-origin: *` and allow
  `Content-Type`; a page on this site can POST and read `{"ok": true}`. The route is live on dev; send.sgraph.ai
  answered 404 on /api/vault/append/*.
- Envelope: a batch encrypted with Web Crypto (RSA-OAEP SHA-256 wrapping AES-256-GCM, sgit's v2 envelope) and signed
  with a non-extractable ECDSA P-256 device key decrypted with `sgit pki decrypt`, which reported "Signature verified".
- Vault apps framed on this site run in sandboxed iframes without allow-same-origin, so they cannot read local storage.

Design (to confirm with the editor of record): one token per device; a device signing key so a copied token alone
cannot forge feedback; sent/unsent cursors and an outbox that waits for the network; manual send by default, optional
auto-send in batches; the batch is the "Copy for Claude" content; a receiver in the daily run (list, fetch, decrypt,
verify, mark processed) that files each batch in admin/inbox/ as a paste would be.

Done when: a batch sent from a browser on the live site lands, verified, in admin/inbox/ on the next run.
