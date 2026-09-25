# How it is built

## The pieces

| Piece | What it does | What exists today |
|---|---|---|
| **The customer vault** | One per customer. Documents in `inbox/`, the X-ray in `xray/`, the Claude setup in `claude/`, the arithmetic in `tools/`. Encrypted on the device; the host holds ciphertext only. | sgit vaults, versioned and encrypted, with read-only keys for sharing. |
| **The catalogue** | Twelve standard analyses, the finding format and the rules. | `spec/analysis-catalogue.md` and `spec/finding.md` in this vault. |
| **The agents** | Claude Code (or another agent that runs `sgit` and Python) clones the vault, runs the catalogue, writes the arithmetic as a script, and commits the X-ray. | `prototypes/run-the-xray.md`, ready to paste. |
| **The reviewer** | A person runs the script, reads every inferred finding against its evidence, and commits a review note. | `prototypes/review-checklist.md`. |
| **The handover** | Project instructions and files for a Claude Project, or a ChatGPT Project. | Claude Projects are available on every plan, including free accounts (up to five); sharing a project needs a Team or Enterprise plan. |
| **The store** | Four standing payment links, one per level, and a page after payment that says what happens next. | The same pattern RiskMandate.ai uses at store.sgit.ai. |

## Where the documents are read

This is the question every customer should ask, and the answer has to be plain.

- **At rest and in transit**, the documents are encrypted in the vault. The host never sees them.
- **During the run**, the operator's agents read them. That is the service. The model provider processes them under the operator's account.
- **The operator's account must be on business terms.** By default Anthropic does not use inputs or outputs from its commercial products, such as Claude for Work and the API, to train models. Check the current terms before the first customer, and state them on the intake page.
- **After delivery**, the operator deletes its working copies and records that it has done so. The customer can copy the content into a fresh vault whose key only they hold.

## Data protection

The documents will often contain personal data, even after the intake checklist: names in minutes, roles in an org chart. Under UK and EU GDPR the operator is then a processor for the customer, and needs a processing agreement, a record of the model provider as a sub-processor, and a deletion step it can evidence. The intake checklist keeps the personal data to the minimum; it does not make it zero. Take advice before the first paid customer.

## Why a vault and not a shared drive

- **Encrypted end to end**, so the storage provider is not a party to the customer's documents.
- **One history for the whole engagement**: what was sent, when the X-ray landed, what was corrected after. "Done" is a commit the customer can see.
- **Re-X-rays are diffs.** Next quarter's X-ray lands in the same vault, and the difference is the report.
- **Read-only keys** let the customer give their accountant or chair a view without giving them the ability to change anything.
