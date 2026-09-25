[← Prototypes](README.md) · [Index](../plan/00-START-HERE.md)

# The setup, step by step

What the operator's session does for a new customer, in order. About an hour the first time, twenty minutes by the tenth.

## 1. The repository

- Create a **public** repository under the customer's own GitHub account (create the account with them on the call if they do not have one; it is theirs, not yours). Name it after the domain: `example-bakery-co-uk`.
- Add the operator as a collaborator. The customer owns; the operator works.
- Initialise with `README.md`, `PLAYBOOK.md` (from the template), `CHANGELOG.md`, and a `.gitignore`.

## 2. The site

- Plain HTML with one shared stylesheet, or a very small static generator the agent can maintain. Plain HTML is the default; it has no build to break.
- One file per page under `pages/`, the home page at `index.html`, images under `images/`, the brand assets (logo, colours, fonts) under `assets/brand/`.
- `site.json` holds the structured content the pages repeat: name, address, hours, phone, social links. Pages read it at build or the agent keeps them in step; either way there is one source for the facts that change most.
- Every template ships with `privacy.html`, `accessibility.html` and a no-cookie posture. No analytics unless the customer asks and the playbook records it.

## 3. The branches

```
main       the live site
preview    what the customer looks at before it goes live
```

Protect `main` so that only the operator and the customer's own account can push. Set the default branch for the customer's session to `preview` for anything the playbook marks as needing a look.

## 4. The deploy

- GitHub Pages, source: GitHub Actions. The standard static deploy workflow, unchanged.
- Two environments: `main` to the production Pages site, `preview` to a second Pages deployment or a preview host. If Pages will not deploy two branches for this account, the preview branch deploys to a bucket behind a CDN or to Netlify; the files are the same.
- Confirm the deploy runs on push and the site is up before touching the domain.

## 5. The domain

- The customer owns the domain and pays for it. If they do not have one, register it in their name, not yours.
- CNAME (or A records for the apex) pointing at GitHub Pages, set at the customer's registrar. Enforce HTTPS in the Pages settings once the certificate is issued.
- `preview.<domain>` as a CNAME to the preview deployment, if the customer wants a friendly preview address.

## 6. The agent

- The operator's session: a project with the repository connected and the playbook loaded.
- The customer's session: a separate project under the customer's own account, with the same repository connected and the playbook loaded, and a one-page guide on how to ask for a change.
- Test both: make a content change from the customer's session and watch it go live; ask for a layout change and watch it go to preview.

## 7. The vault

- Create the customer's vault: the setup notes, the materials they sent, the brand pack, the playbook, and the handover page. Commit, push, and give the customer the read key.
- The customer now holds everything: the repository, the domain, the vault. Say so in the handover.

## 8. The checklist, to keep in the operator's vault

- [ ] Repository public, under the customer's account, operator as collaborator
- [ ] `PLAYBOOK.md` filled in, every blank
- [ ] `privacy.html`, `accessibility.html` present and correct for this business
- [ ] Images resized; no phone originals committed
- [ ] `main` protected; `preview` deploying
- [ ] Domain pointed, HTTPS enforced
- [ ] Customer's session tested with one live change and one preview change
- [ ] Customer vault created, read key handed over
- [ ] First line in `CHANGELOG.md`: "Site launched"
- [ ] Setup time recorded

---

[← Prototypes](README.md) · [Index](../plan/00-START-HERE.md)
