# 06 — OWASP, the summits, and the interview that has to happen

**The site's strongest human asset is its least documented.** Everything below is real, sourced and checkable — and almost all of it is written in the third person, from public sources, about him. There is no first-person account of any of it.

---

## 1. What the record establishes

| Claim | Source | Confidence |
|---|---|---|
| **Former OWASP Board member** | Founder profile: *"**Former OWASP Board member** — the Open Web Application Security Project, the global standard-setting body for application security"*, evidence column *"Public record, founder biography"* | Repeated across six documents |
| *"20+ years application security, former OWASP Board member"* | Investor one-pager | |
| *"30+ years dev, 20+ years AppSec, OWASP board, multiple CISO positions"* | Ambassador review | |
| *"**OWASP Leader** — Contributed to multiple OWASP projects and **organized global security summits**"* | `docs.diniscruz.ai/about` — **his own published bio** | Self-stated |
| Email of record is **`dinis.cruz@owasp.org`** | `docs.diniscruz.ai/pyproject.toml`, authors field | Hard artefact |
| The entire Issues-FS estate lives under the **`owasp-sbot`** GitHub org | `Issues-FS__Dev/README.md` | Hard artefact |
| **MGraph-DB publicly credited to OWASP** | *"an open source, serverless graph database… published by the OWASP community… available in the OWASP SBot GitHub repositories (within `owasp-sbot/MGraph-DB`)"* | Published article |

**Note what those last three mean.** This is not a historical affiliation being cited for credibility — the current work ships under the OWASP organisation, under an OWASP email, with at least one project publicly credited to the OWASP community. **The OWASP thread is live, and the site should present it as present tense.**

---

## 2. The summits — the only fully-researched history in the corpus

From the 5,615-word summit history (7 Jun 2025), which is the corpus's single primary-source historical document:

**2008 · OWASP European Summit · Algarve, Portugal · 4–7 November.** ~80 attendees. Theme: *"Setting the Web Application Security Agenda for 2009"*. And a striking detail: *"the OWASP Foundation **covered travel and accommodation costs for all participants (~80 people)** using OWASP funds."* Outcomes: **OWASP's core principles and a formal code of ethics**, and the creation of **six new global committees**.

**2009 · Washington D.C. · 11 November.** One day, leadership only. *"review 2009 & decide directions for 2010"*.

**2011 · OWASP Global Summit · Lisbon · 8–11 February.** *"**Over 150–180 attendees from more than 20 countries and 120 companies**."* **Named as an organiser:** *"A dedicated organizing team (led by OWASP volunteers **including Dinis Cruz** and others) spent months preparing working session topics."* Format: *"**designed in a working session style format**"*, with *"**no vendor booths, no purely lecture-style talks to a passive audience**."* Attendees from Google, Mozilla, Microsoft, PayPal, Facebook, Apache, Verizon, Dell. Outcomes: board elections by membership, the first full-time Executive Director, the Browser Security Report 2011, OpenSAMM v1.1, the seeds of the OWASP Mobile Top Ten. And: *"reportedly 'thousands' joined some sessions remotely via live streams or IRC, **a forward-thinking move in 2011**."*

**2017 · Woburn Forest, UK · 12–16 June.** Five days, ***"173 sessions in total across the week"***, attendance in the low hundreds. **Named as primary organiser:** *"organized by OWASP community leaders (with **Dinis Cruz, a long-time OWASP contributor, acting as a primary organizer and evangelist**)."* Open planning: *"proposed working sessions were gathered on a public wiki and interested participants could sign up."* Tracks: Threat Modeling, SAMM, DevSecOps, Education, Mobile, CISO, Research. Ethos: ***"no spectators, only participants"***.

**2018 onward · the Open Security Summit.** *"the concept of an open, working-session-based security summit was embraced outside the strict OWASP umbrella… **The Open Security Summit series explicitly built on the OWASP Summit 2017 model**, using the same 5-day intensive format for broader security topics."*

The article's own sources note cites *"Dinis Cruz's 2017 summit announcements"* as a primary source — **which means the primary sources for this history are his, and he has not written the account.**

---

## 3. The lesson, and the thing nobody has connected

The article states the lesson in the third person:

> *"the **format became more purely collaborative over time**… OWASP learned that maximal value came from letting experts 'roll up their sleeves' together rather than having people passively watch slide decks."*

> *"even in an era of constant virtual communication, **face-to-face collaboration can significantly accelerate progress on complex security problems**."*

> *"OWASP maintained its stance that sponsor involvement should not compromise the neutrality of the content — sponsors contributed to logistical costs but did not get speaking slots or marketing displays at summits, preserving the collaborative, **vendor-neutral** atmosphere."*

**And here is the connection nobody has made.** The current agentic-team operating model — briefs with named outcomes, cross-team reviews, day-indexes, acceptance criteria on every brief, *"no spectators"* as an implicit rule for agents — **is the OWASP working-session format applied to a company, and then to a set of AI agents.**

That is a real, traceable line from 2008 Algarve to a 2026 agent team, and it is one page. It is also the most interesting thing on this site for a reader who came for open source and did not expect a governance argument.

---

## 4. ⚠️ The interview — the site cannot ship without it

Everything above is third-person, from public sources. **There is no memoir, no first-person account, no board-tenure dates, no list of the OWASP projects he led, and no Open Security Summit founding story.** The site's strongest human asset is undocumented, and no amount of research fixes it — it is not on the public record.

**Questions that need answering. These are the interview.**

*On OWASP:*
1. What years were you on the OWASP board, and what did the role actually involve?
2. Which OWASP projects did you lead or contribute to, and which one mattered most?
3. Why is the current estate under `owasp-sbot` rather than a personal or company org? Was that a deliberate statement?
4. What did OWASP get right that other foundations got wrong — and what did it get wrong?
5. Applying your own Change-of-Control Stress Test (`04__` §2) to OWASP: who holds the trademark, what is the copyright structure, would it survive a hostile change of control?

*On the summits:*
6. Why did the 2017 summit leave the OWASP umbrella and become the Open Security Summit? What changed?
7. Does it still run? What is its current state?
8. *"No spectators, only participants"* — where did that come from, and did it work?
9. The 2008 summit paid travel and accommodation for all ~80 attendees. Would that be possible now? What did it buy?
10. What did running four summits teach you that shows up in how you run the agent team today?

*On the projects:*
11. **O2 Platform, MGraph-DB, OSBot, memory_fs, sgit-ai, Issues-FS — why was each open-sourced?** There is not one document explaining any of these decisions.
12. Did anyone ever contribute to them? What happened when they did?
13. What would you do differently?

**The O2 Platform article (11 Feb 2025, 5,620 words) is the honourable exception in the corpus** — a real retrospective on his own 2010–2012 OWASP SAST engine. Use it as the model for what the other five need, and as evidence that he can write these when he chooses to.

---

## 5. The OWASP monetisation thread — a live, unclaimed argument

Two documents carry it, and it belongs on this site rather than a commercial one:

> *"say you are an OWASP leader or member with a good reputation for a certain set of application-security skills… **One of the challenges today is that you do not have good revenue streams easily, apart from working for companies or doing consulting.** That is where skills come into play, because you should be selling those skills."*

And the sharper diagnosis, from *Semantic OWASP*: organisations *"either use the broad standards as-is… or **fork them into static custom guides, losing the benefit of OWASP's ongoing improvements**."* The proposal — an OWASP Knowledge Graph Working Group, an OWASP ontology, machine-readable releases — is a finished argument that has never been executed.

**This is the same shape as `04__` §4's funding problem, applied to a specific community he belongs to.** It connects the OWASP thread to the site's central argument rather than leaving it as biography, and it is a proposal made from inside rather than a critique from outside — which is the only position from which it lands.

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
