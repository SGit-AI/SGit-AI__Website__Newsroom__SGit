# PUBLIC.md

Every byte in this vault is already public. It is published with a read key on sgit.ai, and it is written so that somebody who is not us can take it and run the business it describes.

Three rules, and the reasons for them:

1. **Nothing private committed.** No customer data, no credentials, no email addresses of real people, no API keys, no tokens. The mock-ups use invented businesses. If a file would need permission to publish, it does not belong here.
2. **No write token.** This vault carries no credential that could change it. The read key that opens it grants read and only read, and the vault key stays with the publisher.
3. **No metered capability.** `app.json` requests `"permissions": {}`. The app calls no LLM, writes no file, and opens no network connection, so a published read key in front of it costs nobody anything.

The plan itself is offered on the same terms as the code behind it: take it, run it, change it. If you build a company on it, the most useful thing you can send back is what broke.
