"""Team collaboration example with Agno.

Run:
    python examples/02_team_collaboration.py
"""

from __future__ import annotations

import os

from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.team import Team


def build_agent(name: str, role_instruction: str) -> Agent:
    return Agent(
        name=name,
        model=OpenAIChat(id="gpt-4o-mini"),
        instructions=[
            role_instruction,
            "Provide structured, concise output.",
            "Avoid speculation; label assumptions clearly.",
        ],
        markdown=True,
    )


def main() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("Set OPENAI_API_KEY before running this script.")

    researcher = build_agent(
        "Researcher",
        "Gather key arguments, trends, and concrete examples relevant to the question.",
    )
    analyst = build_agent(
        "Analyst",
        "Turn evidence into trade-offs: pros, cons, risks, and mitigations.",
    )
    reviewer = build_agent(
        "Reviewer",
        "Challenge weak assumptions and highlight missing information.",
    )

    coordinator = Team(
        name="StrategyTeam",
        mode="coordinate",
        model=OpenAIChat(id="gpt-4o-mini"),
        members=[researcher, analyst, reviewer],
        instructions=[
            "Delegate to members when useful.",
            "Synthesize a final recommendation at the end.",
            "Use headings: Context, Opportunities, Risks, Recommendation.",
        ],
        markdown=True,
    )

    prompt = "Analyze remote-first hiring in SaaS: opportunities, risks, and a recommendation."
    response = coordinator.run(prompt)
    print(response.content)


if __name__ == "__main__":
    main()
