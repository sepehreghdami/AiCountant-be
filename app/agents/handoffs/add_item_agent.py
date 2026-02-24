from app.application.commands.item import CreateItemPayload
from agents import Agent, function_tool, RunContextWrapper
from typing import Union, Dict
from app.schemas.send_message_request import SendMessageRequest
from app.application.commands.command import CommandMeta, Command


@function_tool
async def create_item(
    wrapper: RunContextWrapper[SendMessageRequest], command: CreateItemPayload
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

    result = f"add item is handled with command: {command}"

    return result


add_item_agent = Agent(
    name="item agent",
    instructions="If user wants to create an item, call create_item tool.",
    model="gpt-4o",
    tools=[create_item],
)
