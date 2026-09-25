[← Why invest](08-why-invest.md) · [Index](00-START-HERE.md) · [Next →](10-open-source.md)

# 9 · The risks

Stated plainly, with what to do about each.

| Risk | How real | What to do |
|---|---|---|
| **The agent breaks a site** | Certain to happen, occasionally | This is what branches and commits are for. Small changes go live; anything structural goes to preview. Every change is a revert away from undone. Put the revert in the playbook and practise it on the first customer. |
| **A customer's session does something odd** | Likely, at scale | The playbook scopes what the customer's session may touch. Anything outside scope goes to preview and notifies the operator. Review the change log weekly. |
| **GitHub Pages terms or limits** | Real, must be checked | Pages is for static sites and has usage limits and terms about commercial use. Read them before customer one, keep sites within them, and keep a second static host (a bucket behind a CDN, Netlify, Cloudflare Pages) ready as the fallback. The sites are plain files; moving them is a copy. |
| **Public repositories** | A feature, but a discipline | Nothing secret ever goes in the repository. Forms, bookings and payments are third-party embeds whose credentials live with the third party. The customer's private material lives in their vault. Say this to every customer at setup. |
| **Token costs rise or a provider changes terms** | Possible | Two providers are named for a reason. The playbook is provider-neutral. Meter usage from day one so a change in price is a line on an invoice, not a surprise. |
| **Commoditisation: anybody can do this** | True, and accepted | Anybody could; most will not. The moat is fifty happy customers, a playbook with the mistakes already in it, and referrals. The plan being public makes more operators, which makes the category, which is the Wide path. |
| **Customer expectations** | The usual one | Publish what each package includes. Agree changes in the chat before doing them. The monthly note manages expectations by making the work visible. |
| **Accessibility, privacy and cookie law** | Real obligations on the customer's site | Every template ships with an accessibility statement, a privacy page and a cookie posture (no cookies, ideally). Keep them current as part of maintenance. This is also an upsell, but it is a duty first. |
| **The operator is the bottleneck** | Yes, by design | Time every setup and every maintenance task. Move anything repeatable into the playbook and the templates. Hire the second operator at fifty, or stay at fifty and be profitable. Both are the plan working. |
| **Key-person risk for the customer** | The customer's risk, and our answer to it | The repository is theirs, the playbook is in it, the vault is openable with their read key. If the operator vanishes, the customer has everything. Say so in the sales pitch; it is the honest answer to "what if you disappear". |

## What is not a risk

- **Hosting cost.** There is none.
- **Building the product.** The product is a process and a playbook. It exists on day one.
- **The technology going away.** Static files, git and a chat session. All of it is boring, which is the point.

---

[← Why invest](08-why-invest.md) · [Index](00-START-HERE.md) · [Next →](10-open-source.md)
