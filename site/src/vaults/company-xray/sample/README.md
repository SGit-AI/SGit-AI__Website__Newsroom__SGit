# Northgate Facilities Ltd: the X-ray vault, as delivered

*This is what a customer receives at the Standard level. Northgate Facilities Ltd, its people, customers and suppliers are invented.*

| Folder | What is in it | Who wrote it |
|---|---|---|
| `inbox/` | The 12 documents the customer dropped in, and `intake.md`: their three questions and what they chose not to send. | The customer |
| `xray/` | `X-RAY.md`, the full report with 14 findings; `board-pack.md`, one page; `questions-for-you.md`; `next-90-days.md`; `findings.json`, the source the others are generated from; and `evidence/`, the derived tables. | The operator's agents, reviewed by a person |
| `claude/` | Everything needed to keep asking questions of the same documents in Claude, or in ChatGPT: the project instructions, the files to upload and questions to start with. | The operator |

In a real delivery the vault also holds `tools/recompute.py`, which re-runs every computed figure. In this demo it sits at the root of the plan vault.

**Start with `xray/board-pack.md`**, then `xray/X-RAY.md`.

**The vault is yours.** It is encrypted before it leaves the device, so the host holds only ciphertext. You hold the key. The history shows what was dropped in, when the X-ray was committed, and what changed after. A Re-X-ray lands in the same vault as a new commit, so the difference between two X-rays is a diff.
