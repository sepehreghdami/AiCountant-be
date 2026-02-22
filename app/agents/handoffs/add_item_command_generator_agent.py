
from app.application.commands.item import CreateItemPayload
from agents import Agent
from typing import Union



add_item_command_generator_agent_instructions = """
given users request text, your task is to generate a structured json command. if any needed info is missing, ask user about it
"""
add_item_command_generator_agent = Agent(
    name="add item command generator agent",
    instructions=add_item_command_generator_agent_instructions,
    model="gpt-4o",
    output_type=CreateItemPayload
)