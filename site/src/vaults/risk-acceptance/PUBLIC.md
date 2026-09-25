# PUBLIC.md

Every byte in this vault is already public. It is published with a read key on sgit.ai, and it is written so that somebody who is not us can take it and build the company it describes.

Three rules, and the reasons for them:

1. **Nothing private committed.** No real organisation's risks, no real people, no credentials, no API keys, no tokens. The organisation, the people and the risk in the replay are invented, and every address uses the reserved `.example` domain.
2. **No write token.** This vault carries no credential that could change it. The read key that opens it grants read and only read, and the vault key stays with the publisher.
3. **No metered capability.** `app.json` requests `"permissions": {}`. The app calls no LLM, writes no file and opens no network connection. It replays the record it was shipped with, in your browser, and verifies the hash chain there.

The plan is offered on the same terms as the code behind it: take it, run it, change it. If you build a company on it, the most useful thing you can send back is how often executives refused to accept, and what changed their minds.
