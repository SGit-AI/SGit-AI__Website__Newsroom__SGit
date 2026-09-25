[← Prototypes](README.md) · [Index](../plan/00-START-HERE.md)

# Six change requests, worked

From the customer's words to the commit. The businesses are invented; the shape of each request is not.

## 1. "We're closed on Monday the 5th for the bank holiday, can you put that on the site?"

- **Session:** customer's
- **Playbook rule:** a notice, and hours, on pages the customer owns → straight to live
- **What the agent does:** adds a one-line notice to the top of `index.html` and `pages/contact.html`, dated to remove itself after the 5th; updates `site.json` hours for that date
- **Commit:** `Add bank holiday closure notice for Monday 5 May`
- **Change log:** `2026-05-01 · Closed Monday 5 May, notice added to home and contact`
- **Live in:** about a minute

## 2. "Can you put these three photos from Saturday on the gallery page?"

- **Session:** customer's
- **Playbook rule:** adding photos already provided, on a page the customer owns → live; images resized first
- **What the agent does:** resizes three phone photos to 1600 px WebP, adds them to `pages/gallery.html` with alt text taken from the customer's message
- **Commit:** `Add three photos from the Saturday market to the gallery`
- **Live in:** a couple of minutes

## 3. "Our prices went up. Haircut is now £32, colour from £75."

- **Session:** customer's
- **Playbook rule:** prices on the services page → live
- **What the agent does:** edits `pages/services.html`; notices the home page also quotes the old haircut price and asks: *"The home page also says £28 for a haircut. Change that too?"* Waits for yes.
- **Commit:** `Update haircut to £32 and colour from £75 on services and home`
- **What to notice:** the agent asked before touching the home page, because the playbook marks the home page hero as preview-only. Prices in the hero were content, so a question rather than a refusal.

## 4. "I want a new page about the wedding cakes, with the photos I sent and a form to ask for a quote."

- **Session:** customer's
- **Playbook rule:** a new page, and a form → preview, operator notified
- **What the agent does:** builds `pages/wedding-cakes.html` from the photos and the customer's notes on `preview`, adds it to the navigation on `preview` only, drafts the quote form as a placeholder, and tells the customer: *"It is on the preview site for you to look at. The form needs the webmaster to connect it, so I have flagged it."*
- **Operator's session, next day:** connects the form to the provider under the customer's account, records it in the playbook's embed table, checks the page on a phone, merges to `main`.
- **Commit (operator):** `Add wedding cakes page with quote form`
- **Charged as:** a Silver-package change, or £120 on demand

## 5. "The site looks weird on my phone since yesterday."

- **Session:** operator's, notified by the customer
- **What the agent does:** reads the last three commits, finds a photo committed at 6,000 px wide by the customer's session (a rule was missed), reverts that commit so live is restored in a minute, resizes the image properly on `preview`, checks the phone viewport, merges.
- **Playbook change:** rule 6 was already there; the agent in the customer's session had skipped it. The operator adds a line to the customer's session instructions to confirm image sizes before committing, and notes the incident in the operator's vault.
- **Change log:** `2026-06-12 · Fixed home page layout on phones (oversized photo), photo re-added at the right size`

## 6. "Can we get more people finding us on Google and on ChatGPT?"

- **Session:** operator's
- **What the agent does:** this is not a change, it is an upsell. The operator replies with what the basics would be (titles, descriptions, structured data for the business, a page per service, the accessibility statement, being clear and citable), what it costs as an on-demand piece of work, and what to expect. If yes, it is done on `preview` and merged.
- **What to notice:** the change log produced the sale. This is the pattern the business model section describes.

---

[← Prototypes](README.md) · [Index](../plan/00-START-HERE.md)
