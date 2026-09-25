# Briefing for sgit-cli-team



## Signals


## Loose ends
- Two CLI transport bugs found while publishing the Agent as Webmaster vault (a fresh vault's first push flipped to the read-only static transport, and push, pull, fetch, status and delete ignored --transport) are described as fixed in the CLI repository. No source says whether the fixes have reached a released CLI version.
- The CLI did not accept the canonical prefixed read-key form that the web loader accepts: given the prefixed key it derived the wrong ref and failed, while the bare form worked.
- Four older cross-team asks from sgit.ai have no recorded answer: serial transfer mode for sgit under WebAssembly, a history-preserving vault rekey, first-class serialised diffs with ignore support, and the SG/Send API's CORS allow-list missing x-api-key.
