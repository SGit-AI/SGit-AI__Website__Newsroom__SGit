---
title: The key management call names one business plan; two more depend on it
date: 2026-09-24
desk: Architect
standfirst: sgit.ai's key management call cites one business plan, Agent as Webmaster, as its case that keys are multiplying; two more plans published on sgit.ai the same day, Lesson Loop and Company X-Ray, depend on easy key handover, and the call does not mention either.
from_site: sgit.ai
to_site: sgit.ai
status: new
action: give the authors of sgit.ai's key management call the Lesson Loop and Company X-Ray pages as evidence of demand, and give the X-Ray plan the call's link
sources:
  - https://sgit.ai/partnerships/vault-key-management.md
  - https://sgit.ai/demos/vaults/lesson-loop/index.md
  - src:vaults/lesson-loop/plan/03-architecture.md
  - src:vaults/lesson-loop/plan/04-what-exists-today.md
  - https://sgit.ai/demos/vaults/company-xray/index.md
  - src:vaults/company-xray/plan/03-architecture.md
reviewed_by:
reviewed_on:
---

**sgit.ai's key management call cites one business plan, Agent as Webmaster, as its case that keys are multiplying; two more plans published on sgit.ai the same day, Lesson Loop and Company X-Ray, depend on easy key handover, and the call does not mention either.**

Lesson Loop says so and links the call; Company X-Ray relies on it without linking it.

## Side A: the call

[Who holds the keys?](https://sgit.ai/partnerships/vault-key-management.md), published on 24 September 2026 in sgit.ai v0.6.2, says "We are looking for a key manager, not building one." Its evidence that keys are multiplying includes agents that hand work over as vaults. It names Agent as Webmaster, "a business plan built on exactly that. Every one of those hand-overs is a key that has to go to a person, safely".

It asks for a way to "share a vault with someone else by sending a short name in plain words rather than the key", and for revocation.

## Side B: two plans that need it

**Lesson Loop** (sgit.ai v0.6.6, [vault page](https://sgit.ai/demos/vaults/lesson-loop/index.md)). Its architecture file, [03-architecture.md](src:vaults/lesson-loop/plan/03-architecture.md), has a section called "The one hard part":

> "Key management. A player has to keep a vault key safe, hand out read keys to coaches, and take them back. That is the problem sgit.ai's call for collaboration with password managers and identity providers exists to solve."

Its table of [what exists today](src:vaults/lesson-loop/plan/04-what-exists-today.md) lists "Easy key handling for players and coaches" as "Open", with the call's address.

**Company X-Ray** (sgit.ai v0.6.8, [vault page](https://sgit.ai/demos/vaults/company-xray/index.md)). Its [architecture file](src:vaults/company-xray/plan/03-architecture.md) hands keys out at two points: after delivery, "The customer can copy the content into a fresh vault whose key only they hold", and read-only keys "let the customer give their accountant or chair a view without giving them the ability to change anything." It does not mention the key management call.

## What we checked

- Searched the key management page for "Lesson", "X-Ray" and "Connector": the only business plan it names is Agent as Webmaster.
- Searched all five plan vaults for "key management", "key manager", "password manager" and the call's address. Only Lesson Loop links it. Company X-Ray's one hit for "password manager" is inside its invented sample company's staff handbook.
- The call went out at 09:30 on 24 September; Lesson Loop at 15:04 and Company X-Ray at 23:26 (sgit.ai git log). The call could not have cited them when it was written. The signal is that it can now.
- Noticed on the same page, and small: the call says both "thirty-six published vaults to test against" and "Thirty-five vaults are published on this site alone". sgit.ai's published-vaults list in the seed has 36 entries.
