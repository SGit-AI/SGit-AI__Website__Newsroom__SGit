## Who takes the card, and where

**One rail, and it is a payment link on Stripe's own pages.** Six products are
priced there, three coupons exist, and the store reconciles both against its own
data on every release. A second rail was planned and **came off on 16 September
for the first end-to-end store** — a rail that is half set up is a second thing to
explain here and a second thing to keep true, and neither is worth it while the
first one is not live. The plan for it is kept rather than deleted.

**Nothing on this site collects anything.** No form, no input, no select, no account,
no cookie. The provider takes your name, your contact and your card on its own pages,
which is the only place a card number should ever be typed. A build check holds every
page here to that, and a second one holds every page to opening no network connection
at all.

**One page can be typed into: [the partner review](/review/).** It has reason boxes on it
because it exists to be answered, and the rule moved by ruling in v0.1.15 to allow exactly
that and nothing else. There is still no `<form>` on this domain — that is the element that
submits — and still no `<input>` or `<select>`, which is where a card number would go. What
somebody types there stays in their own browser until they copy it out.
{{claim:review-is-the-one-typing-surface}}

**What reaches the provider is the amount and your order reference.** The
reference carries the product codes for everything you picked, so matching it
against the name and contact the provider captured gives the whole order.
[How that works, in three steps](/how-it-works/).

### Every level is one price, so every level can hold a link

The four levels are £5, £50, £500 and £1,500 — **single prices, not bands**, which
is what a standing payment link needs. The banded tiers and the deposit that this
page used to describe belonged to the offer line replaced on 15 September: there is
no band left to fix and no engagement left to deposit against.
{{claim:checkout-bands-have-no-standing-link}}

**No link has been created on either rail.** [Your order](/cart/) renders the
button as unissued and names the rail that is missing, rather than showing
something that looks live: **a greyed-out button is a lie about which half of the
work is done.** Pasting one line into `data/checkout.yml` turns a rail on, and the
build holds whatever lands there to that provider's own checkout hosts over HTTPS.
{{claim:checkout-links-not-issued}}

### Why the catalogue is not inside either provider

**Sixty-two product codes maintained in two places is sixty-two codes that will one
day disagree.** The catalogue lives here, in one file, checked on every build; the
provider takes an amount and a reference; neither side has to know about the other.
It also means adding a product is a build rather than a build plus a console.
