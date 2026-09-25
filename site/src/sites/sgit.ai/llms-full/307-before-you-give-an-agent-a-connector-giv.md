# Before you give an agent a connector, give the connector a twin, sgit.ai

> When an AI agent is given a Gmail or Google Calendar connector, it can read, send, move, decline and permanently delete on somebody's behalf, and for several of those actions the platform itself documents that there is no way back. This article argues that a twin of the connector is the minimum requirement for deploying an agent with confidence. The twin is a journal of every request and response the agent makes, appended as it happens to a write-only lane, processed later, and replayed into the inbox and calendar as the agent saw them, with a before and after for every change and a revert plan for each one. It gives provenance, explanation and a named list of what can and cannot be undone, and it changes the agent's behaviour policy from a hope into a list. Every claim about Gmail and Calendar is taken from Google's own documentation and linked. A working replay of an invented session, and a business plan for the service, are published alongside it as a vault.
>
> Page: https://sgit.ai/articles/connector-twin-before-you-deploy-an-agent.html

[Home](../index.md) / [Articles](index.md) / Before you give an agent a connector, give the connector a twin
