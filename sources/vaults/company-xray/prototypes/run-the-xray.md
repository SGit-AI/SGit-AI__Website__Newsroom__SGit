# Run the X-ray: the operator's agent prompt

For Claude Code, or any agent that can run `sgit` and Python, on the operator's machine. Replace the angle brackets. The vault key is given to the agent in the session, never written into a file.

```
You are running a Standard X-ray for <company>. Read spec/analysis-catalogue.md, spec/finding.md and
spec/customer-vault.md in the X-ray plan vault first.

1. Clone the customer vault. Read inbox/intake.md: their questions, what they sent, what they removed.
2. List every file in inbox/ with one line on what it contains and its date range. If a file holds
   personal data the intake checklist says not to send, stop and tell me which file and which columns.
3. For each analysis A1 to A12, say whether the inbox supports it. Skip the ones it does not, and
   record each skip for "not covered".
4. Write tools/recompute.py first: one function per computed figure, reading only inbox/. Then write
   xray/findings.json, with every computed figure in "checks". Run recompute.py until every check
   passes. Never type a computed figure by hand.
5. Look hardest at A7, say and do: where the minutes, the plan, the logs and the numbers disagree.
6. Every finding names its evidence: file, and row, line or section. Label each read, computed or
   inferred. Where the documents cannot settle a point, write a question, not a finding.
7. Answer the customer's own questions first, each pointing at findings.
8. Render X-RAY.md, board-pack.md, questions-for-you.md and next-90-days.md from findings.json.
9. Write claude/PROJECT-INSTRUCTIONS.md, UPLOAD-THESE.md and TRY-ASKING.md for this customer.
10. Commit with the message "X-ray, draft for review". Do not push until I have reviewed it.

Do not search the web about the customer. Public facts, such as a wage rate or a regulation, may be
used as context with their URL. Do not name individuals in findings unless the customer's own
document names them and the finding needs it.
```
