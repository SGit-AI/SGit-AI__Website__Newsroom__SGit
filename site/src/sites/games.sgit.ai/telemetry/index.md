# What our games send

> What Can It Do? sends anonymous usage events over two write-only append lanes; Which Agent Is It? sends nothing. What is in an event, what is deliberately absent, what it proves, and how to stop it.

*Source: <https://games.sgit.ai/telemetry/index.html> · site v0.5.0 · this file is generated from the same content
as the page, so the two cannot drift. Every page on this site has a `.md` twin; internal links
below point at them.*

---

[Home](../index.md) / What our games send

# What our games send

> *What Can It Do?* counts usage anonymously while you play — which screens people reach, which answers are common. No cookies, no analytics script, no id, nothing that identifies you, and a pause switch on every screen. *Which Agent Is It?* and the games vault's home page send nothing (since 9 September 2026). [What is sent, and why a vault doing it at all is unusual](../telemetry/index.md).

## The default this breaks — and the one it does not

Opening a vault does not normally send anything anywhere. That is the platform default and every other vault this family publishes honours it — including, since 9 September 2026 (v0.26.0), the games vault that holds *Which Agent Is It?*, which sends nothing and asks for no permissions. *What Can It Do?*, in its own vault, does send, which is why the fact is stated wherever that game appears rather than left to a privacy page nobody opens.

**Browser signals are off.** From v0.21.0 to v0.25.0 the sender could also carry three browser fingerprints and a country, region and connection type from an IP lookup, behind a `signals` switch that shipped on. The game's own vault ships that switch **off** since v1.0.0 (9 September 2026); the vault's `telemetry/index.html` and its *What this page knows* screen (inside the game since v1.2.0) say so, and the locked branch is the record of what shipped before.

**It is worth being proportionate about the size of this.** What leaves is a count of how far people got and which answers are common. There is no cookie, no analytics script, no account, no id, no fingerprint, no URL and no referrer — which is **less than a default web-server access log**, and considerably less than the analytics running on almost every site a reader will visit today. The reason it is disclosed at all is not that it is invasive; it is that a vault sending anything is a departure from a platform promise, and departures get stated.

## What is in an event

| Carried | Deliberately absent |
|---|---|
| which screen you reached | your name, or any id for you |
| the answers you gave, and the points | any fingerprint |
| the profile you picked from the public list | the URL, and the referrer |
| a 16-hex session id, minted in memory when the page opened and gone when the tab closes | your IP, as far as the payload is concerned |
| a coarse form factor, a language and a host | your user-agent string and screen size |

The `profile` field is which **public** profile you picked from a list of nine. It is not a description of your setup — the scoring is arithmetic over a published profile, and the schema is blunt about it: *"Not a count of people (sessions are tabs). Not evidence."*

## How it travels

Batched: one batch per flush, at most every 4 seconds, at most 40 flushes and 50 events per flush in a session. The payload is an `sgit pki` v2 envelope — RSA-OAEP-SHA256 wrapping AES-256-GCM — built with Web Crypto in the browser against a public key that ships in the vault. **If there is no secure context there is no Web Crypto, and the sender disables itself rather than falling back to plaintext.**

It goes to a separate private vault over an append lane. The games hold a **write-only token**: it cannot read, list or decrypt anything on that lane, including what it just wrote.

## What it proves — which is the part most analytics pages never write

> **Nothing about anyone.** Anyone holding the games' read key holds the append token too — it is published with them, because it has to be — and could forge or flood the lane. So the receiving end treats every event as a claim, not as a fact. Counts from this lane are a lower bound on activity and evidence of nothing else.

## Two lanes, not one

Anonymous counters travel on one token; **feedback you deliberately write** — the 👍/👎 and the form behind *say more* — travels on a second, never batched with the counters. Different retention, and the counters can be purged without losing the feedback. Nothing is sent from the feedback lane without a press.

What comes back out of it is [the ideas graph](../games/ideas.md): paraphrased, keyed to the question rather than to the person, naming nobody.

## How to stop it

Every page in the game's vault carries a **pause switch** next to the notice, and it works before the first question. `telemetry/index.html` inside that vault is the authoritative statement — it is reachable from every screen and it is more detailed than this page. This page exists so that a reader who never opens the vault still gets told.

This site itself sends nothing. It is static files on GitHub Pages with no analytics and no server to receive anything — the only thing that sends is the game, in its frame, on its own lanes.

---

*[Site index for agents](../llms.txt) · [HTML version](https://games.sgit.ai/telemetry/index.html)*
