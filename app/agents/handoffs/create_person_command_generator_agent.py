from agents import Agent
from app.application.commands.person import CreatePersonPayload

create_person_command_generator_agent_instructions = """
given users request text, your task is to generate a structured json command. if any needed info is missing, ask user about it
"""
create_person_command_generator_agent = Agent(
    name="create person command generator agent",
    instructions=create_person_command_generator_agent_instructions,
    model="gpt-4o-mini",
    output_type=CreatePersonPayload
)