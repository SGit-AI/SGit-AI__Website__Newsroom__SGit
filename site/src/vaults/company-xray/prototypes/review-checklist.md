# The reviewer's checklist

The person who reviews an X-ray before it is delivered. This is the step that makes it a professional's work rather than a model's output, and it is where most of the operator's time goes.

1. **Run `tools/recompute.py`.** Every check passes, or the X-ray does not go out.
2. **Read every inferred finding against its evidence.** Open the file, find the place, and ask: would the customer's own team read it the same way? Downgrade, reword or delete.
3. **Read the titles alone.** Do they tell the story? Is the first one the one that matters most?
4. **Check the customer's questions are answered first**, in plain words, each pointing at findings.
5. **Look for what is missing.** Is there an obvious question the documents answer that the X-ray does not ask?
6. **Check tone.** The X-ray describes documents and numbers. It never judges people, and it never names an individual as the cause of a problem.
7. **Check nothing private has leaked into findings**: no personal data, no credentials, nothing the intake says was removed.
8. **Write the review note** in `xray/REVIEW.md`: what changed, what was deleted and why, and the reviewer's name and date. Commit it.

Target time: 90 minutes for a Standard X-ray; three hours for a Tailored one.
