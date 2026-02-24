from agents import Agent,function_tool,RunContextWrapper

from app.application.commands.person import CreatePersonPayload
from app.application.commands.command import CommandMeta
from app.schemas.send_message_request import SendMessageRequest

@function_tool
async def create_person(
    wrapper: RunContextWrapper[SendMessageRequest], command: CreatePersonPayload
):

    meta = CommandMeta(
        idempotency_key="",
        tenant_id=wrapper.context.tenant_id,
        actor_id=wrapper.context.actor_id,
        timestamp="",#TODO
        source_text="",#TODO
        confidence="",#TODO
        metadata="",#TODO
    )

    result = "add person is handled"

    return result
create_person_agent_instructions = """
given users request text, your task is to generate a structured json command. if any needed info is missing, ask user about it
"""
create_person_agent = Agent(
    name="create person command generator agent",
    instructions=create_person_agent_instructions,
    model="gpt-4o-mini",
    tools=[create_person]
) 