# Code samples — adding an LLM chat pane

Runnable samples for the commission's *"code samples of how to add an LLM chat pane."* Every API call here is from the shipped `sg.llm.*` contract (`02__`); the surrounding UI code is written for this pack.

**Before you write any of this, read `01__` §1.** Two of the three surfaces need no code at all.

---

## 0. No code — surfaces 1 and 2

The vault chat panel (`/vault` → **✨ AI Chat**) and the app-side panel (`/en-gb/app/` → **✨ AI**) are host chrome. Nothing to build.

The only thing an app author can express is a chrome preference in `app.json`:

```json
{
  "entry": "index.html",
  "hud": { "show": { "llm": true } }
}
```

`false` hides the button if it would clash with your own UI; `true` forces it on in `minimal` mode, where it is off by default. It is a preference about chrome, not authority.

---

## 1. The minimum viable chat pane

`app.json`:

```json
{
  "entry": "index.html",
  "permissions": { "llm": { "chat": true } }
}
```

`index.html`:

```html
<div id="chat" hidden>
    <div id="log" role="log" aria-live="polite"></div>
    <form id="composer">
        <input id="q" type="text" autocomplete="off" aria-label="Message">
        <button type="submit">Send</button>
    </form>
</div>
<div id="fallback" hidden></div>
```

`chat.js`:

```js
const chat     = document.getElementById('chat')
const fallback = document.getElementById('fallback')
const log      = document.getElementById('log')
const composer = document.getElementById('composer')
const q        = document.getElementById('q')

const messages = []

// 1. ALWAYS check availability before rendering a chat UI.
//    It depends on runtime state: key configured, read-only session, budget spent.
const a = await sg.llm.available()
if (!a.ok) {
    fallback.hidden      = false
    fallback.textContent = {
        ENOKEY:    'No AI key configured for this vault — Settings → AI models.',
        EPERM:     'This app was not granted AI access.',
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
    el.className   = `msg ${role}`
    el.textContent = text
    log.append(el)
    log.scrollTop = log.scrollHeight
    return el
}

function errorText(code) {
    return {
        EBUDGET:  'Spend cap reached for this session.',
        ECONSENT: 'You declined the request.',
        EMODEL:   'That model cannot handle this request.',
        EABORT:   'Cancelled.',
        EPROTO:   'The provider failed. Try again.',
    }[code] ?? 'Something went wrong.'
}
```

**Three rules are load-bearing and all three are in the comments:** check `available()` before drawing, treat the terminal reply as the truth, branch on `err.code`.

---

## 2. Adding cancel

The promise carries its own request id:

```js
let inFlight = null

async function send(messages, bubble) {
    const p   = sg.llm.chat({ messages }, (delta, acc) => { bubble.textContent = acc })
    inFlight  = p.requestId
    stopBtn.hidden = false
    try {
        return await p
    } catch (e) {
        if (e.code === 'EABORT') return null       // partial text is already rendered
        throw e
    } finally {
        inFlight = null
        stopBtn.hidden = true
    }
}

stopBtn.onclick = () => { if (inFlight) sg.llm.cancel(inFlight) }
```

---

## 3. A cost meter that does not lie

```json
{ "permissions": { "llm": { "chat": true, "usage": true } } }
```

```js
async function refreshMeter() {
    const u = await sg.llm.usage()
    meter.textContent =
        `${u.calls} calls · $${u.cost.toFixed(4)} · ${u.remaining.cost ?? '∞'} left`
}
```

And per call — **the `~` is the rule, not a nicety**:

```js
const res = await sg.llm.chat({ messages })
costPill.textContent = res.cost.estimated
    ? `~$${res.cost.value.toFixed(4)}`     // computed from tokens × list price — NOT billed
    :  `$${res.cost.value.toFixed(4)}`     // reconciled against /generation
```

> *"`estimated: true` means it was computed from token counts × list price, not billed. Render estimates with a `~`. **Never show one as a bill.**"*

Note that `usage()` covers the **whole session**, including the host panel's own calls — one bill per session, not one per surface.

---

## 4. A model picker that cannot be wrong

```json
{ "permissions": { "llm": { "chat": true, "models": true } } }
```

```js
const models = await sg.llm.models()          // already filtered by the vault's allow-list
picker.append(...models.map(m => {
    const o = document.createElement('option')
    o.value = m.id
    o.textContent = m.name ?? m.id
    return o
}))

// then pass it per call
await sg.llm.chat({ model: picker.value, messages })
```

**You do not filter this list.** The host returns only what the vault allows, so a picker built from it is automatically correct — including when the allow-list changes.

---

## 5. Attaching an image

```js
dropZone.addEventListener('paste', async (e) => {
    const item = [...e.clipboardData.items].find(i => i.type.startsWith('image/'))
    if (!item) return

    const part = await sg.llm.imagePart(item.getAsFile())   // Blob | Uint8Array | ArrayBuffer | data: URL
    const res  = await sg.llm.chat({
        messages: [...messages, { role: 'user', content: [
            { type: 'text', text: q.value || 'What is in this image?' },
            part,
        ] }]
    })
    append('assistant', res.content)
})
```

**Use `imagePart()`. Do not encode it yourself.** It runs in your frame with no host round trip, and it chunks base64 at **8190, not 8192** — because `8192 % 3 === 2`, so a 8192-sized chunk emits `=` padding mid-string and `atob()` rejects it. *"This codebase has shipped that exact bug three times."*

png / jpeg / webp / gif only. Not svg. An `EMODEL` error will **name the model** that cannot see.

**And clear the attachment after sending.** The host panel does, deliberately: an image left attached would silently re-send and re-bill on every turn.

---

## 6. Voice input

```json
{ "permissions": { "llm": { "chat": true, "listen": true } } }
```

```js
micBtn.onclick = async () => {
    try {
        micBtn.disabled = true
        const { text, cost } = await sg.llm.listen()      // opts: {maxMs, model, prompt}
        q.value = text
        q.focus()
    } catch (e) {
        if (e.code === 'ECONSENT') return                  // declined — not worth showing
        if (e.code === 'ENOMIC')   showTypeInstead()
        else                       showError(e.code)
    } finally {
        micBtn.disabled = false
    }
}
```

**Your frame never touches audio** — a sandboxed frame has no `navigator.mediaDevices` at all. The host records, shows the indicator on its own chrome, transcribes with the vault's key, and hands you text. `listen` is a **separate grant, never implied by `chat`**, and asks for consent every time by default.

---

## 7. A file-grounded pane, following the host panel's own rules

If you attach vault files to the prompt, copy the three honesty mechanisms the host panel uses. They are the difference between a demo and something you can trust:

```js
const BUDGET = 24_000                                    // ONE budget shared across all files

async function buildContext(paths) {
    const parts = []
    let spent   = 0
    for (const path of paths) {
        const text  = await sg.vfs.readText(path)
        const share = Math.max(0, Math.floor(BUDGET / paths.length) - 64)
        const clip  = text.length > share
        parts.push(
            `--- ${path}${clip ? ' (TRUNCATED)' : ''} ---\n` +   // the MODEL sees TRUNCATED
            text.slice(0, share)
        )
        spent += share
    }
    return parts.join('\n\n')
}
```

1. **One budget shared across all files**, not one each — so a second file cannot silently double the bill.
2. **`TRUNCATED` goes in the text the model sees**, so it cannot pretend to have read the whole file.
3. **Re-adding a file replaces its contents**, so it refreshes after an edit instead of duplicating.

---

## 8. The checklist before you ship

- [ ] `available()` called **before** any chat UI is rendered
- [ ] Every `catch` branches on `err.code`, never on message text
- [ ] All nine error codes have user-facing text: `EPERM` `ECONSENT` `ENOKEY` `EREADONLY` `EBUDGET` `EMODEL` `EABORT` `EIMGSIZE` `EPROTO`
- [ ] Estimated costs rendered with `~`; never shown as a bill
- [ ] Image attachments cleared after one send
- [ ] File context under one shared budget, with `TRUNCATED` visible to the model
- [ ] Model picker built from `models()` and not filtered locally
- [ ] Only the grants you use are declared — and `listen` only if you actually record
- [ ] You have checked whether **surface 1 or 2 would have done the job with no code at all**

---

This document is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).
