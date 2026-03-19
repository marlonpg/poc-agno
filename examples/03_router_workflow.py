"""Deterministic prompt router for multiple specialist agents.

Run:
    python examples/03_router_workflow.py
"""

from __future__ import annotations

import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat


class PromptRouter:
    def __init__(self) -> None:
        model = OpenAIChat(id="gpt-4o-mini")

        self.finance_agent = Agent(
            name="FinanceSpecialist",
            model=model,
            instructions=[
                "You analyze business and finance questions.",
                "Focus on valuation, risk, and assumptions.",
                "Use short bullet points and plain language.",
            ],
            markdown=True,
        )

        self.engineering_agent = Agent(
            name="EngineeringSpecialist",
            model=model,
            instructions=[
                "You answer software architecture and engineering operations questions.",
                "Prefer practical implementation guidance.",
                "Use concise sections and action items.",
            ],
            markdown=True,
        )

        self.generalist_agent = Agent(
            name="Generalist",
            model=model,
            instructions=[
                "You answer broad strategy and planning questions clearly.",
                "When uncertain, state assumptions.",
            ],
            markdown=True,
        )

    def route(self, prompt: str) -> Agent:
        lower = prompt.lower()

        finance_terms = ["stock", "valuation", "revenue", "profit", "market cap", "financial"]
        engineering_terms = ["api", "architecture", "distributed", "latency", "retry", "queue"]

        if any(term in lower for term in finance_terms):
            return self.finance_agent
        if any(term in lower for term in engineering_terms):
            return self.engineering_agent
        return self.generalist_agent


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY before running this script.")

    router = PromptRouter()

    prompts = [
        "Compare NVDA and AMD valuation risk in the current cycle.",
        "How should we design retries in distributed background jobs?",
        "Give me a short marketing launch checklist for a new B2B feature.",
    ]

    for idx, prompt in enumerate(prompts, start=1):
        agent = router.route(prompt)
        result = agent.run(prompt)
        print(f"\n=== Example {idx}: {agent.name} ===")
        print(result.content)


if __name__ == "__main__":
    main()
