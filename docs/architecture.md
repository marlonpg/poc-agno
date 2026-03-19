# Architecture Notes: Agno Multi-Agent POC

## Goal

Design a simple, understandable multi-agent system that demonstrates:
- specialist behavior,
- delegation,
- orchestration,
- and composability.

## Core building blocks

### Agent
A single autonomous component with:
- instructions,
- model,
- optional tools.

Use when one role can solve the task end-to-end.

### Team
A collaborative unit of multiple agents under a coordinator.

Use when a task benefits from decomposition into specialized steps.

### Workflow / Router
Deterministic orchestration logic in Python that decides *which* agent or team should execute based on input characteristics.

Use when you need predictable behavior and clear control paths.

## POC flow

1. User prompt comes in.
2. Router classifies intent (finance, engineering, generic).
3. Appropriate specialist agent is selected.
4. For broader tasks, coordinator team is used instead.
5. Output is returned with concise structure.

## Why this pattern works

- Keeps agent prompts focused.
- Makes behavior explainable.
- Makes debugging easier than a single giant prompt.
- Scales naturally with additional specialist agents.

## Extension points

- Add persistent storage for conversation memory.
- Add an evaluation harness with golden prompts.
- Add asynchronous parallel specialist calls for latency reduction.
- Add policy agent for safety and compliance checks.
