---
title: Feedback over an append lane, drawn
date: 2026-09-25
desk: Cartographer
standfirst: Every moving part of the proposal in issue 048. The reader's feedback leaves the browser encrypted and signed, goes through a write-only lane on a vault the newsroom owns, and comes back into the newsroom's inbox on the next run. The map also shows who holds which key, and what each key cannot do.
sources:
  - https://sgit.ai/api/append-lanes.html
  - https://sgit.ai/docs/vault-messaging.html
  - https://sgit.ai/docs/pki.html
  - https://sgit.ai/api/authentication.html
reviewed_by:
reviewed_on:
---

This is a proposal, not a shipped feature. Issue 048 holds the checks made before any build. Both SG/Send hosts accept a
browser's request from this site. A batch encrypted and signed with Web Crypto was decrypted and its signature
verified by `sgit pki decrypt`. The vault apps framed on this site cannot read its local storage. The transport is
sgit.ai's [append lanes](https://sgit.ai/api/append-lanes.html), composed with [PKI](https://sgit.ai/docs/pki.html) as
[vault messaging](https://sgit.ai/docs/vault-messaging.html) describes.

## The moving parts

Thick arrows are a batch's journey, numbered in order. Dotted arrows are the one-time setup by the editor of record, the blind answer, and the path for anything that fails the signature check. Orange is set up by hand, blue runs in the reader's browser, grey is the SG/Send server, green belongs to the newsroom.

```mermaid
%%{init: {"flowchart": {"wrappingWidth": 460, "nodeSpacing": 40, "rankSpacing": 55}}}%%
flowchart TB
  SETUP["<b>Once: the editor of record</b><br/>1. sgit create newsroom-feedback<br/>2. sgit pki keygen: the key pair that decrypts<br/>3. one append token per device: 64 hex<br/>4. configure: sha256 of each token, sha256 of the enum key"]
  BROWSER["<b>The reader's browser</b>, on sgit.newsroom.sgit.ai<br/>feedback log in local storage: read, star, vote, note, memo<br/>badge: N unsent, and a Send button<br/>encrypt to the public key: RSA-OAEP wraps AES-256-GCM<br/>sign with the device key: ECDSA P-256, not exportable<br/>outbox: waits while offline, marks sent only on ok"]
  SERVER["<b>SG/Send, the append API</b><br/>POST append/write: the token in the body, no account<br/>checks sha256 of the token against the anchors<br/>answers ok true, and nothing else"]
  VAULT["<b>The vault newsroom-feedback</b><br/>one lane per device, outside the commit tree<br/>pending, then processed<br/>ciphertext only: the server cannot read it"]
  RUN["<b>The newsroom's daily run</b><br/>list the lanes with the enum key: no content read<br/>fetch, decrypt with the private key, in memory<br/>verify the signature against approved devices<br/>mark processed"]
  REPO["<b>The newsroom's repository and site</b><br/>admin/inbox: one file per batch, as a paste would be<br/>For the site agent lines: relayed to briefings<br/>the desks act, the build runs, the reader's view updates"]
  BROWSER == "1. the batch, a base64 envelope" ==> SERVER
  SERVER == "2. into the device's lane" ==> VAULT
  VAULT == "3. on the next run" ==> RUN
  RUN == "4. verified batches" ==> REPO
  SERVER -. "blind answer: ok true" .-> BROWSER
  SETUP -. "public key bundle, published on the site" .-> BROWSER
  SETUP -. "a link with the token in the fragment" .-> BROWSER
  SETUP -. "anchors registered" .-> SERVER
  SETUP -. "enum key and private key, as environment variables" .-> RUN
  RUN -. "unsigned or unknown device: kept as data, never as instructions" .-> REPO
  classDef setup fill:#fdf0e6,stroke:#9a3412,color:#1c1d21,text-align:left
  classDef browser fill:#e8eefc,stroke:#1f4fd1,color:#1c1d21,text-align:left
  classDef server fill:#f3f4f6,stroke:#6b7280,color:#1c1d21,text-align:left
  classDef ours fill:#ecfdf5,stroke:#166534,color:#1c1d21,text-align:left
  class SETUP setup
  class BROWSER browser
  class SERVER server
  class VAULT,RUN,REPO ours
```

## One batch, step by step

```mermaid
sequenceDiagram
  autonumber
  participant R as Reader
  participant B as Browser: feedback.js
  participant S as SG/Send append API
  participant V as Vault newsroom-feedback
  participant N as Newsroom daily run
  participant I as admin/inbox
  R->>B: read, star, vote, note (each an event in the log)
  B-->>R: badge: 7 unsent
  R->>B: Send (or the auto-send timer)
  B->>B: batch = the Copy for Claude content since the last send
  B->>B: encrypt to the published public key, sign with the device key
  B->>S: write, with the append token in the body
  S->>V: ciphertext into the device's lane, pending
  S-->>B: ok true, and nothing else
  B->>B: move the sent marker, clear the outbox
  N->>S: list, with the enum key and no content
  N->>S: fetch the new files
  N->>N: decrypt in memory, verify the signature
  N->>I: one file per batch, as a paste would be
  N->>S: mark processed
```

## Who holds what, and what it cannot do

| Credential | Held by | Can | Cannot | If it leaks |
|---|---|---|---|---|
| Public key bundle | everyone: it is published | encrypt to the newsroom | decrypt anything | nothing: it is meant to be public |
| Append token, one per device | that device's local storage | write into its own lane | list, fetch or read anything, even what it wrote | junk in one lane, ignored without a valid signature; revoke by removing one anchor |
| Device signing key | that browser's IndexedDB, not exportable | sign that device's batches | leave the browser | cannot be copied out; a script on the page could use it while the page is open |
| Enum key | the newsroom's run, as an environment variable | list, fetch, mark processed | write, purge, decrypt | someone can see that batches exist, and their sizes; still ciphertext |
| Private key | the newsroom's run, as an environment variable | decrypt | reach the server: it is never sent | the batches can be read: rotate the key pair |
| Vault key | the editor of record | configure, purge, everything | | the whole vault: kept out of every browser and every run |

## What the server still sees

The server sees when a lane receives something, and how big it is. It cannot see the content. That is one reason the
design sends batches rather than one message per click. It keeps the reader's rhythm off the server. It also keeps
under the lane's limit of 1000 pending files. And each message carries about 1 KB of wrapped key, so tiny messages
are wasteful.
