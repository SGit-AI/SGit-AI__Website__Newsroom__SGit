---
title: Experiment: a JSON twin with a semantic graph for each new piece
created: 2026-09-25T12:05:00Z
priority: medium
type: task
owner: journalist.desk
source: admin/inbox/2026-09-25__notes-from-the-flight.md
parent: 004-content-and-editorial
estimated_effort: medium
---

# Experiment: a JSON twin with a semantic graph for each new piece

For new pieces only (the next batch), the desk also writes `<piece>.json`: the markdown, the sources and
images it depends on, and a graph of typed nodes (Evidence, Idea, Question, Statement, Fact, Hypothesis,
Observation, Comment) with edges (supports, contradicts, asks, answers, cites), the graph the prose was
written from (fractal semantic graphs). The build renders the graph beside the piece and validates the
schema. Two rounds, then decide.
