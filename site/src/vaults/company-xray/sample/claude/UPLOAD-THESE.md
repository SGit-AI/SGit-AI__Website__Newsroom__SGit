# Setting up Claude to keep asking questions

Ten minutes, once.

1. **Create a Claude Project.** In Claude, open *Projects* and create one called "Northgate X-ray". Projects are available on every Claude plan, including free accounts, which can have up to five. Sharing a project with colleagues needs a Team or Enterprise plan; otherwise each person sets up their own.
2. **Paste the instructions.** Copy the text below the line in `PROJECT-INSTRUCTIONS.md` into the project's instructions.
3. **Upload the files.** Add these to the project's knowledge:
   - every file in `inbox/`
   - `xray/X-RAY.md`, `xray/findings.json`, `xray/board-pack.md`, `xray/questions-for-you.md`, `xray/next-90-days.md`
   - every file in `xray/evidence/`
4. **Ask your first question.** `TRY-ASKING.md` has twelve to start with.

**In ChatGPT** the same steps work with a ChatGPT Project: paste the instructions into the project's instructions and upload the same files.

**If you use Claude Code or another agent that runs `sgit`,** skip the upload: clone the vault, and the agent reads the files where they are, including anything added since.

**Which account.** Use a company account on business terms, not a personal one. By default Anthropic does not use inputs or outputs from its commercial products, such as Claude for Work (Team and Enterprise) and the API, to train models. On consumer plans the account holder chooses. Check the current terms on the day you set this up.

**When the documents change,** upload the new versions and remove the old ones, or clone the vault again.
