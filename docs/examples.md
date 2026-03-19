# Example Prompts and Expected Behavior

## Example 1: Single specialist agent
Script: `examples/01_single_agent.py`

Prompt:
> "Give me a 5-bullet summary of AI agent orchestration best practices."

Expected behavior:
- Agent uses concise output formatting.
- Produces actionable bullet points.

## Example 2: Team collaboration
Script: `examples/02_team_collaboration.py`

Prompt:
> "Analyze remote-first hiring in SaaS: opportunities, risks, and a recommendation."

Expected behavior:
- Researcher collects key facts.
- Analyst structures trade-offs.
- Reviewer critiques assumptions.
- Team lead produces a final recommendation.

## Example 3: Router workflow
Script: `examples/03_router_workflow.py`

Prompts:
- "Compare NVDA and AMD valuation risk."
- "How should we design retries in distributed jobs?"
- "Give me a short marketing launch checklist."

Expected behavior:
- Finance-style prompt routes to finance agent.
- Engineering-style prompt routes to engineering agent.
- Everything else routes to generalist agent.

## Tips

- Keep specialist instructions narrow.
- Start with deterministic routing before adding probabilistic dispatch.
- Log route decisions for debugging and audits.
