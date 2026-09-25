# 10. Open questions

1. **When should the journal be processed?** On a timer, on a threshold, on demand, or all three. It needs real usage to answer, not more design. `prototypes/processor-schedule.md` sets out the options.
2. **How much of the prompt should be captured?** The instruction and the agent's own summary are cheap and valuable. The full model context is expensive and far more sensitive. The default here is the first, with the second as an opt-in.
3. **Does an API deletion appear in Calendar's trash?** Google's help says deleted events stay in trash for 30 days; this plan has not tested an API deletion. Until it is tested, the revert plan uses the twin's captured copy.
4. **Which connectors after Gmail and Calendar?** Drive and Slack are the obvious next two, each with its own list of actions that cannot be undone. Each needs its own view and its own revert rules.
5. **What does an insurer actually want in the evidence pack?** The Assured tier is a guess until one insurer has read one pack.
6. **Should the revert be executable by an agent?** Probably yes, under the same capture and with a person's approval, which makes the revert itself subject to the twin. Not in the first ninety days.
