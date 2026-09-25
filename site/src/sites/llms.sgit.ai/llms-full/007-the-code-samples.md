# The code samples

For surface 3, the only one that needs code. Before you write any of it, read [the decision table](index.md#decide): two of the three surfaces need none.

**Which half is a contract and which half is an example.** Every `sg.llm.*` call below is the **shipped API**, quoted from a contract that is [generated on this site from its canonical source](../api/index.md) and licensed Apache-2.0 with the product. The surrounding UI code is an **example**, written for this site and released CC BY 4.0. Copy the calls with confidence; treat the DOM around them as one way of many.

## 0. No code — surfaces 1 and 2

**Grants:** none

The vault chat panel and the app-side panel are host chrome. The only thing an app author expresses is a chrome preference:

```
{
 "entry": "index.html",
 "hud": { "show": { "llm": true } }
}
```

`false` hides the button if it would clash with your own UI; `true` forces it on in `minimal` mode, where it is off by default. It is a preference about chrome and not authority.

## 1. The minimum viable chat pane

**Grants:** llm.chat

```
{
 "entry": "index.html",
 "permissions": { "llm": { "chat": true } }
}
```

```
<div id="chat" hidden>
 <div id="log" role="log" aria-live="polite"></div>
 <form id="composer">
 <input id="q" type="text" autocomplete="off" aria-label="Message">
 <button type="submit">Send</button>
 </form>
</div>
<div id="fallback" hidden></div>
```

```
const chat = document.getElementById('chat')
const fallback = document.getElementById('fallback')
const log = document.getElementById('log')
const composer = document.getElementById('composer')
const q = document.getElementById('q')

const messages = []

// 1. ALWAYS check availability before rendering a chat UI.
// It depends on runtime state: key configured, read-only session, budget spent.
const a = await sg.llm.available()
if (!a.ok) {
 fallback.hidden = false
 fallback.textContent = {
 ENOKEY: 'No AI key configured for this vault - Settings > AI models.',
 EPERM: 'This app was not granted AI access.',
 EREADONLY: 'The AI key is owner-sealed and this is a read-only session.',
 }[a.reason] ?? `AI unavailable (${a.reason})`
} else {
 chat.hidden = false
}

composer.addEventListener('submit', async (e) => {
 e.preventDefault()
 const text = q.value.trim()
 if (!text) return
 q.value = ''

 messages.push({ role: 'user', content: text })
 append('user', text)

 const bubble = append('assistant', '')
 try {
 // 2. The terminal reply is authoritative. onToken is a UX affordance.
 const res = await sg.llm.chat({ messages }, (delta, acc) => { bubble.textContent = acc })
 bubble.textContent = res.content
 messages.push({ role: 'assistant', content: res.content })
 } catch (err) {
 // 3. Branch on err.code, never on message text.
 bubble.textContent = `[${err.code}] ${errorText(err.code)}`
 }
})

function append(role, text) {
 const el = document.createElement('div')
 el.className = `msg ${role}`
 el.textContent = text
 log.append(el)
 log.scrollTop = log.scrollHeight
 return el
}

function errorText(code) {
 return {
 EBUDGET: 'Spend cap reached for this session.',
 ECONSENT: 'You declined the request.',
 EMODEL: 'That model cannot handle this request.',
 EABORT: 'Cancelled.',
 EPROTO: 'The provider failed. Try again.',
 }[code] ?? 'Something went wrong.'
}
```

**Three rules are load-bearing and all three are in the comments:** check `available()` before drawing, treat the terminal reply as the truth, and branch on `err.code`.

## 2. Adding cancel

**Grants:** llm.chat

The promise carries its own request id:

```
let inFlight = null

async function send(messages, bubble) {
 const p = sg.llm.chat({ messages }, (delta, acc) => { bubble.textContent = acc })
 inFlight = p.requestId
 stopBtn.hidden = false
 try {
 return await p
 } catch (e) {
 if (e.code === 'EABORT') return null // partial text is already rendered
 throw e
 } finally {
 inFlight = null
 stopBtn.hidden = true
 }
}

stopBtn.onclick = () => { if (inFlight) sg.llm.cancel(inFlight) }
```

## 3. A cost meter that does not lie

**Grants:** llm.chat llm.usage

```
async function refreshMeter() {
 const u = await sg.llm.usage()
 meter.textContent =
 `${u.calls} calls - $${u.cost.toFixed(4)} - ${u.remaining.cost ?? '∞'} left`
}
```

And per call. **The `~` is the rule, not a nicety:**

```
const res = await sg.llm.chat({ messages })
costPill.textContent = res.cost.estimated
 ? `~$${res.cost.value.toFixed(4)}` // computed from tokens x list price - NOT billed
 : `$${res.cost.value.toFixed(4)}` // reconciled against /generation
```

> `estimated: true` means it was computed from token counts times list price, not billed. Render estimates with a `~`. Never show one as a bill.

`usage()` covers the **whole session**, including the host panel's own calls: one bill per session, not one per surface. A meter you draw in your app is therefore the true total, which is the right default and not the obvious one.

## 4. A model picker that cannot be wrong

**Grants:** llm.chat llm.models

```
const models = await sg.llm.models() // already filtered by the vault's allow-list
picker.append(...models.map(m => {
 const o = document.createElement('option')
 o.value = m.id
 o.textContent = m.name ?? m.id
 return o
}))

// then pass it per call
await sg.llm.chat({ model: picker.value, messages })
```

**You do not filter this list.** The host returns only what the vault allows, so a picker built from it is automatically correct, including after the allow-list changes.

## 5. Attaching an image

**Grants:** llm.chat an image is an ordinary chat call, not a new grant

```
dropZone.addEventListener('paste', async (e) => {
 const item = [...e.clipboardData.items].find(i => i.type.startsWith('image/'))
 if (!item) return

 const part = await sg.llm.imagePart(item.getAsFile()) // Blob | Uint8Array | ArrayBuffer | data: URL
 const res = await sg.llm.chat({
 messages: [...messages, { role: 'user', content: [
 { type: 'text', text: q.value || 'What is in this image?' },
 part,
 ] }]
 })
 append('assistant', res.content)
})
```

**Use `imagePart()`. Do not encode it yourself.** It runs in your frame with no host round trip, and it chunks base64 at **8190, not 8192**, because `8192 % 3 === 2`, so a 8192-sized chunk emits `=` padding mid-string and `atob()` rejects it. *"This codebase has shipped that exact bug three times."* [The arithmetic, in full](../api/traps.md#chunking).

png, jpeg, webp and gif only. Not svg: it is a scriptable document rather than a bitmap, and no provider takes it. An `EMODEL` error will **name the model** that cannot see. **And clear the attachment after sending** — the host panel does, deliberately, because an image left attached would silently re-send and re-bill on every turn.

## 6. Voice input

**Grants:** llm.chat llm.listen listen is never implied by chat

```
{ "permissions": { "llm": { "chat": true, "listen": true } } }
```

```
micBtn.onclick = async () => {
 try {
 micBtn.disabled = true
 const { text, cost } = await sg.llm.listen() // opts: {maxMs, model, prompt}
 q.value = text
 q.focus()
 } catch (e) {
 if (e.code === 'ECONSENT') return // declined - not worth showing
 if (e.code === 'ENOMIC') showTypeInstead()
 else showError(e.code)
 } finally {
 micBtn.disabled = false
 }
}
```

**Your frame never touches audio.** A sandboxed frame has no `navigator.mediaDevices` at all. The host records, shows the indicator on its own chrome, transcribes with the vault's key, and hands you text. That is also [why the indicator is trustworthy](../security/index.md#indicator): it is not the app's to draw, so it is not the app's to fake.

## 7. A file-grounded pane, following the host panel's own rules

**Grants:** llm.chat plus whatever vfs read grant your app already has

If you attach vault files to the prompt, copy the three honesty mechanisms the host panel uses. They are the difference between a demo and something you can trust:

```
const BUDGET = 24_000 // ONE budget shared across all files

async function buildContext(paths) {
 const parts = []
 let spent = 0
 for (const path of paths) {
 const text = await sg.vfs.readText(path)
 const share = Math.max(0, Math.floor(BUDGET / paths.length) - 64)
 const clip = text.length > share
 parts.push(
 `--- ${path}${clip ? ' (TRUNCATED)' : ''} ---\n` + // the MODEL sees TRUNCATED
 text.slice(0, share)
 )
 spent += share
 }
 return parts.join('\n\n')
}
```

1. **One budget shared across all files**, not one each, so a second file cannot silently double the bill.
1. **`TRUNCATED` goes in the text the model sees**, so it cannot pretend to have read the whole file.
1. **Re-adding a file replaces its contents**, so it refreshes after an edit instead of duplicating.

**These are honesty mechanisms, not injection defences, and the difference matters here.** The moment you attach file contents to a prompt, you are putting untrusted text in front of the model. The shipped vault chat wraps such content in an explicit **untrusted-data fence** and tells the model in its system prompt to treat anything inside it as data rather than instructions. If you are building your own grounded pane, [read what that mechanism does and does not promise](../security/index.md#injection) before you rely on the budget and the marker to protect you, because they do not.

## 8. The checklist before you ship

| | Check |
|---|---|
| ☐ | `available()` called **before** any chat UI is rendered |
| ☐ | Every `catch` branches on `err.code`, never on message text |
| ☐ | All nine error codes have user-facing text: `EPERM` `ECONSENT` `ENOKEY` `EREADONLY` `EBUDGET` `EMODEL` `EABORT` `EIMGSIZE` `EPROTO` |
| ☐ | Estimated costs rendered with `~`, never shown as a bill |
| ☐ | Image attachments cleared after one send |
| ☐ | File context under one shared budget, with `TRUNCATED` visible to the model |
| ☐ | Model picker built from `models()` and not filtered locally |
| ☐ | Only the grants you use are declared, and `listen` only if you actually record |
| ☐ | You have checked whether **surface 1 or 2 would have done the job with no code at all** |

**These samples are read rather than run, and that is a weakness this site names.** The brief's recommendation was to ship them as a real vault app that exercises every call, published as both the demo and the test, so they are verified by existing rather than by review. That app is not built. It also cannot be published casually: [a vault with an LLM key configured carries a credential](../security/index.md#storing), so the demo needs either hard spend caps chosen deliberately for publication or a bring-your-own-key flow. [The decision is open and it belongs to the project lead](../admin/comms.md#needs).

 [← Adding a chat pane](index.md) [The reference →](../api/index.md)


==============================================================================
/api/index.md
==============================================================================
