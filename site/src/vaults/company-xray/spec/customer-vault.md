# The customer vault

One vault per customer. It starts as the drop box and ends as the delivery, so the customer's documents, the X-ray and every later change sit in one encrypted history.

```
README.md            what is here, and where to start
inbox/               the customer's documents, and intake.md
xray/                X-RAY.md, board-pack.md, questions-for-you.md, next-90-days.md,
                     findings.json, evidence/
claude/              PROJECT-INSTRUCTIONS.md, UPLOAD-THESE.md, TRY-ASKING.md
tools/               recompute.py: the arithmetic, re-runnable
```

## The life of the vault

| Step | What happens | Who holds the key |
|---|---|---|
| 1. Create | The operator creates the vault with `inbox/intake.md` and the README. | Operator |
| 2. Hand over the key | The key goes to the customer by a separate channel from the link to the intake page. Never on a web page, never in the same email as the instructions. | Operator and customer |
| 3. Drop in | The customer adds documents to `inbox/` with `sgit` from a folder on their machine, or through a browser vault interface where one is available to them, and fills in `intake.md`. | Both |
| 4. Run | The operator's agents clone the vault, run the catalogue, and commit `xray/`, `claude/` and `tools/`. | Both |
| 5. Review | A person runs `tools/recompute.py`, reads every inferred finding against its evidence, and commits the review note. | Both |
| 6. Deliver | The handover call. The customer's first clone is the delivery; done is a commit in their history. | Both |
| 7. Leave | The operator deletes its working copies, and records that it has. The customer can copy the content into a fresh vault whose key only they hold. | Customer |
| 8. Re-X-ray | Months later, the customer adds new documents and shares a key again. The new X-ray lands as a new commit; the difference is a diff. | Both, for the run |

## What the host sees

The vault is encrypted on the device before anything is uploaded, so the host holds ciphertext and never a readable document. The operator's agents do see the documents, because reading them is the service; `plan/03-architecture.md` says where that happens and on what terms.
