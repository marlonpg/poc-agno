# Agno Multi-Agent POC

This repository is a **proof of concept (POC)** for building multi-agent systems with the [Agno framework](https://docs.agno.com/).

It includes:
- A practical project structure you can extend.
- Simple, runnable examples of common multi-agent capabilities.
- Documentation to understand when to use Agent, Team, and Workflow patterns.

---

## What this POC demonstrates

### 1) Single-purpose specialist agents
Agents with focused responsibilities (for example, researcher, summarizer, or risk reviewer).

### 2) Multi-agent collaboration with `Team`
A coordinator agent delegates tasks to specialist agents and synthesizes the final answer.

### 3) Routing and deterministic orchestration
A lightweight workflow script routes prompts to the right specialist based on simple intent rules.

### 4) Stateful sessions
Examples show how to use session IDs for continuity across multiple interactions.

---

## Project layout

```text
.
├── docs/
│   ├── architecture.md
│   └── examples.md
├── examples/
│   ├── 01_single_agent.py
│   ├── 02_team_collaboration.py
│   └── 03_router_workflow.py
├── requirements.txt
└── README.md
```

---

## Prerequisites

- Python 3.10+
- An OpenAI API key (or replace model provider in code)

```bash
export OPENAI_API_KEY="your_api_key_here"
```

---

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Run examples

```bash
python examples/01_single_agent.py
python examples/02_team_collaboration.py
python examples/03_router_workflow.py
```

---

## Common functionality examples covered

- **Tool-enabled research** (web search via DuckDuckGo tools).
- **Role-based decomposition** (planner + analyst + reviewer).
- **Final-answer synthesis** (team lead merges specialist outputs).
- **Prompt routing** (finance-like, engineering-like, and generic paths).

See [`docs/examples.md`](docs/examples.md) for prompt ideas and expected behavior.

---

## Next steps to productionize

1. Add evals and regression tests for answer quality.
2. Add guardrails and input validation for tool usage.
3. Add persistent memory storage per user/session.
4. Containerize and expose as FastAPI endpoints.
5. Add observability (token usage, latency, tool traces).

