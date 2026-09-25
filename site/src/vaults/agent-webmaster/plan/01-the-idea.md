[← Start here](00-START-HERE.md) · [Index](00-START-HERE.md) · [Next →](02-architecture.md)

# 1 · The idea

## What most businesses actually want from a website

Not much, and not what they are usually sold. A business of a certain size wants a website that has some images, looks fine, says what they do and how to reach them, and, more than anything, **that they can update and use regularly**. Opening hours change. A new service starts. A photo from last week's event should go up. A price changes. The menu changes every Friday.

Today that business has three options, and all of them fail the same test:

| Option | What goes wrong |
|---|---|
| An agency built it | Every change is an email, a quote, a wait, an invoice. So nothing changes, and the site becomes a brochure from the year it was built. |
| A template builder (Wix, Squarespace, and the rest) | They pay rent forever for a tool they touch twice a year, fight the editor when they do, and the site is locked to the platform. |
| A relative did it in WordPress | It is out of date, nobody remembers the login, and the plugins have opinions. |

The thing they wanted, a site they can change by saying what they want changed, did not exist at a price they could pay.

## What changed

The agents did. Claude and ChatGPT, given access to a repository, can now maintain a website end to end: write and edit the pages, adjust the layout, add a section, resize the images, fix what broke, and push the commit that publishes it. Not a demo of that. The thing itself, reliably, at the quality a small business needs, which is not the quality of a launch site for a consumer brand.

That is how the author builds his own sites, and the point of this plan is that it is **super straightforward, super efficient and super simple**, so straightforward that the interesting question is no longer how to build a website but how to run a business that gives this to people who would never open a terminal.

## The product

**A website with a webmaster, where the webmaster is an agent.**

The customer gets a real website on a real domain, built from their materials in days, and after that they get a way to change it that works like asking a person: they describe the change, in chat, and it happens. Behind that is a chat session with access to their site's repository, which publishes to GitHub Pages on every push. The operator, the person running this business, sets it up, keeps it healthy, and steps in when a change needs an expert.

Three things make this a business rather than a trick:

1. **The setup is expert work and is charged as such.** Understanding what the customer actually wants, choosing the structure, getting their brand into a design that looks right, and teaching the agent their site. That is a call, some materials, and a few hours of directed work. It is worth £300 to £1,200 depending on the size of the site, and the customer sees value within days.
2. **The maintenance is rent that is earned.** Somebody keeps an eye on the site, makes the small tweaks, updates the agent's instructions as the site evolves, and makes sure the customer does not break anything they cannot undo. That is worth £50 to £200 a month, and unlike most subscriptions the customer can see the work being done, because every change is a commit with a message.
3. **The changes are priced by the interaction.** A new section, a seasonal campaign, a translation, a rewrite: these are charged when they happen, by the change or by the tokens they cost, so the customer pays for what they use and the operator is paid for what they deliver.

## Why this is empowering rather than another dependency

Because the customer holds everything. The repository is theirs, and it is public, so there is nothing to hide and nothing to lose. The site is plain files. The history of every change is in the commits. If they fall out with the operator, they take the repository and find another one, or run the agent themselves. The service is not a lock-in. It is a person who is good at this, plus an agent, looking after something the customer owns.

That is also why the plan is open. The next section is the architecture.

---

[← Start here](00-START-HERE.md) · [Index](00-START-HERE.md) · [Next →](02-architecture.md)
