<!-- generated from views/index.html by admin/build/gen_markdown.py — do not edit by hand -->

*[open-source.sgit.ai](/index.md) · site v0.2.2 · canonical: https://open-source.sgit.ai/views/index.html*

> Technology is not the moat; lock-in relocates to quality, certification and maintainability; lock-in degrades your own architecture; and open source frees you to cannibalise your own code. The full position, each argument with its counter-case attached.

---

# The position

Most arguments for open source are arguments about generosity. This is not one. The claim here is narrower, harder, and more useful to anyone actually deciding: **open source is a strategy that wins on economics and structure**, and the reasons it wins have almost nothing to do with whether anyone contributes back.

> "the power of open source is not for the community, it is not because it is nice for others, and it is not to give back."

That sentence is deliberately unfashionable. It is also the load-bearing one, because everything downstream depends on which framing you accept. If open source is a gift, its funding crisis is a moral failure and the remedy is to shame people into paying. If it is a strategy, the funding crisis is an **externality** — and externalities are corrected by structure and market forces, never by virtue. [cURL is where that stops being theory](../funding/curl.md).

## 1. Not free. Freedom — and somebody is always paying

> "open source is not free, somebody is always paying for it. What you get from open source is freedom, that is different… We play the game of empowering the user and being the reputable source of trust. **We are selling trust.**"

The second half of that is the part people skip. If the code is free and the freedom is the product, then what remains to sell is *trust* — being the reputable source, the party who knows the thing, the one you call when it breaks at 3am. That is a real commercial position and it is not a weaker one than owning the copyright.

And the first half is measurable rather than rhetorical:

> "It is not free to take a piece of open source and run it in your environment, because somebody is always paying for people… They will not fully understand it, and the more time they spend, the more it costs."

> **The counter-case.** This framing is comfortable for a vendor and uncomfortable for a maintainer. A solo maintainer of a package with a million downloads is "always paying" in the sense that *they* pay and nobody else does. The argument describes the cost honestly and then locates the remedy in market design rather than obligation — which is right, and which is also very convenient for the people who currently benefit. [The funding page takes that objection seriously →](../funding/index.md)

## 2. Technology is not the moat, and pretending otherwise is expensive

> "it allows for the removal of the idea that technology is the moat, more and more technology and software is not the moat, technology gets recreated, gets customised."

This is now close to a consensus view among people who have watched a competitor rebuild their differentiator in a quarter. What is *not* consensus is where the moat goes instead, and the answer here is specific rather than vague:

> "the lock-in is not on the technology, the lock-in is in **the quality and the services and the new versions and the maintainability and the certification of versions**."

Note what that list has in common. Every item is something you have to keep being good at. None of them can be acquired once and held. That is the difference between a moat that decays into rent extraction and one that requires you to stay useful — which is why the same document is blunt about the alternative:

> "As soon as you move into rent extraction, you lose sight of it: you are playing the game of making it less expensive to keep you than to leave, and then they leave with pain. I do not want us to fall into that."

## 3. The moat is a rate, not a wall

The obvious objection to publishing everything is that a competitor takes it. The answer is the sharpest formulation the author has given:

> "A competitor who forks our code today gets our position as of today. **They do not get our velocity.**" / "The code is open source. The execution is not forkable."

And the related claim, which is more contestable:

> "Anyone competing closed-source can copy and re-implement and leverage the LLM capabilities, but they will not have the users and the adoption."

> **Where this is weakest.** "They do not get our velocity" is true right up until they do. It is an empirical claim about a specific team at a specific moment, dressed as a structural one. A fork by a party with more engineers than you is exactly the scenario where it fails — and the honest version of the argument is that *velocity is a defensible moat only while you actually have more of it*. That is a reason to keep shipping, not a licence to relax.

## 4. Lock-in degrades your own architecture

This is the most unusual argument on the site, because it makes the case against lock-in on *engineering* grounds rather than ethical ones:

> "you introduce attrition, and by introducing attrition you create much worse architectures, because there is a lot of simplicity when you do not have copyrights, licensing, and restrictions."

Anyone who has watched a codebase grow a licensing boundary knows the shape of this. The boundary is never where the engineering wants it. Modules get split to keep something proprietary, interfaces get widened to avoid exposing an internal, a clean refactor gets vetoed because it would move code across the line. The licence stops being a legal artefact and starts being an architectural constraint — and it is a constraint chosen for reasons that have nothing to do with the system.

## 5. Open source frees you to delete your own code

> "it makes you more motivated, and with less false sense of ownership, to cannibalise your own code or remove code you had, because it is open source, the code does not particularly have value"

Short, original, and true. Sunk-cost attachment to code is partly an ownership illusion, and open sourcing dissolves some of it: the code is out there, it is not going anywhere, anyone who wants the old version has it. What is left is the question of whether it should still be in your tree — which is the only question that was ever worth asking.

## 6. It is the right strategy even with zero contributions

> "even if there are no contributions, no external people submitting code and patches, and there is a lot of AI slop now, with even open-source repos not accepting submissions because of the mess… open source is still the right strategy"

> "even with zero contributions, being open dramatically simplifies the tech stack… If you are the creator and maintainer of the core technology, the core ideas, the core standards, there is crazy value, and that is where we want to play."

This is the position at its most consistent, and it is what makes the rest coherent: if you never expected contributions, then the collapse of the contribution model is not an argument against you. It is also the position's largest cost, and the site states it as one rather than hiding it.

> **The tension, named.** A project that expects no contributions has less to say about running one — governance, review, codes of conduct, DCO-versus-CLA *in practice*. And the [survivability argument turns on exactly that distinction](../survivability/index.md). It is why that argument is shipped as a test answerable from public artefacts rather than as advice about community, and why [the community question is on the open list](../roadmap/index.md#community).

## 7. Burden of proof sits with the sceptic

> "I am yet to see evidence that open source is a deterrent to the business. All the evidence is that it is only a problem when companies shoot themselves in the foot."

Stated that way it is a challenge rather than a proof, and it should be read as one. The [success stories](../history/stories.md) are the evidence offered; [the relicensing wave](../history/index.md#reversals) is the strongest evidence against, and the site's answer to it is [structural rather than dismissive](../survivability/index.md) — those companies did not fail because they were open, they moved because a single copyright holder could.

## 8. The rising tide, and its unresolved version

> "you want to build a model where the better your competitors are, the better you become, and open source is the key element of that strategy."

Applied to hyperscalers, the author argues this both ways *in one document* and leaves it open — *"you want the hyperscalers to adopt and embrace these technologies, because they open up the market"* against *"Hyperscalers could commoditise it. Their embrace opens the market but could also absorb it."*

Left unresolved here too, deliberately. It is a genuine open question about scale, not a rhetorical balance: the same adoption that creates your market can eat it, and which one happens depends on facts not yet in evidence. [It is on the open-questions list →](../roadmap/index.md#open)

## The arguments that carry their own pages

### [Sovereignty requires open source](sovereignty.md)

*Four steps*

One SLA away from losing access, schemas that matter as much as code, and jurisdiction as the thing you actually lose. Necessary, but not sufficient.

### [Open core, or packaging?](open-core.md)

*Position moved*

"There should be nothing proprietary" and "customers only have a subset" — five weeks apart. The test that settles which one this is.

### [Somebody has to be the villagers](villagers.md)

*The market*

Maintaining the non-functional requirements as a market, and both of its counter-arguments — including the one that says some of this should be retired rather than hardened.

### [Survivability is not a licence property](../survivability/index.md)

*The best idea*

It is a property of the copyright and trademark structure — and the evidence is every relicensing between 2018 and 2024.

[← Front page](../index.md)[Sovereignty →](sovereignty.md)

---

*This page is released under the Creative Commons Attribution 4.0 International licence (CC BY 4.0).*
