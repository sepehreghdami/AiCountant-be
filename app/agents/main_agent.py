from agents import Agent

from app.agents.handoffs.create_person_agent import create_person_agent
from app.agents.handoffs.add_item_agent import add_item_agent


main_agent_instructions = (
    main_agent_instructions
) = """
you are a helpfull assistant. your task is the following:
    1-read the users requst text and find the best and only one appropriate handoff to call.
    2-call the appropriate handoff with the users input.
    3-report to user based on handoff's result
"""
main_agent = Agent(
    name="users request analyser",
    instructions=main_agent_instructions,
    model="gpt-4o",  # TODO:read it from config
    handoffs=[add_item_agent, create_person_agent],
)
