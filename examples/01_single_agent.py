"""Simple single-agent example with Agno.

Run:
    python examples/01_single_agent.py
"""

from __future__ import annotations

import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY before running this script.")

    specialist = Agent(
        name="OrchestrationCoach",
        model=OpenAIChat(id="gpt-4o-mini"),
        instructions=[
            "You are an AI engineering coach.",
            "Respond in concise bullets with practical actions.",
            "Keep output under 180 words unless explicitly asked for more.",
        ],
        markdown=True,
    )

    prompt = "Give me a 5-bullet summary of AI agent orchestration best practices."
    response = specialist.run(prompt)
    print(response.content)


if __name__ == "__main__":
    main()
