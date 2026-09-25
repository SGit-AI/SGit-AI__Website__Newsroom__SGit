# chrome-extensions.sgit.ai — the expensive bugs do not throw

Site version: v0.1.0 (9 September 2026). Full machine-readable index: [llms.txt](llms.txt).

Guidance and worked examples for building Chrome extensions, written for the agent that
reads them before writing one. Four guides from five weeks building a Manifest V3 browser
extension that records a web application's own network traffic, against an undocumented
target that changed its entire API stack mid-project.

## If you read nothing else

1. **Build a deliberately stupid recorder first.** No parsers, no domain model — just keep
   the bodies.
2. **Verify every derived fact against an artefact the system itself produced.**
3. **The expensive bugs do not throw.**
4. **Missing is `null`, and `null` never becomes `0`, `''` or `{}`.**
5. **Leave the corrections in.**

## A narrow instrument, stated before the code

This is an instrument for observing your own session and your own data, on an account you
hold, recording only what the service already sent to your browser. It originates no
requests, transmits nothing, and captures no message content in any mode. Never originates a
request; never blocks, delays or alters a response; never throws into the page; never
transmits. See [about/participant.html](about/participant.html).

## One shipped, four specified

One extension has been built — the recorder, v0.16.0. Four more were specified across six
months and never shipped: a Key Vault, risk cards on extensions, the Scribe, and a secrets
manager, plus two smaller proposals (the manifest as a published profile, and the vault as
the extension's storage layer). See [the arc](the-arc/index.md) and [the unbuilt](unbuilt/index.md).

## The four guides — read 01 first

- [01 · The method](method/index.html)
- [02 · The extension](architecture/index.html)
- [03 · Reading payloads nobody documented](payloads/index.html)
- [04 · Vaults, scoped to this project](vaults/index.html)

## Built from the guides

- [The six silent failures](silent-failures/index.html)
- [The checklist](checklist/index.html)
- [The quality rubric](rubric/index.html) and [rubric.json](rubric/rubric.json)
- [The documents](documents/index.html)

## What this site does not cover

The guides are written from one extension: a passive recorder that never originates a
request. No page-modifying extensions, injected UI, `declarativeNetRequest`, OAuth flows,
multi-origin content scripts, or Chrome Web Store publishing guide. The recorder's original
target is never named.

CC BY 4.0 (site text, rubric, guides); code snippets CC0/MIT.
