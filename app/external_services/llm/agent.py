# from statistics import mode
# from agents import Agent, Runner,InputGuardrail, GuardrailFunctionOutput
# from dotenv import load_dotenv
# from pydantic import BaseModel
# load_dotenv()  # loads .env into os.environ

# # instructions = """
# # identify the sentiment of the text from the categories below:
# # 1-positive
# # 2-negative
# # """
# # agent = Agent(name="AI Accountant", instructions=instructions)


# # result = Runner.run_sync(agent, "امروز روی خوبیه")
# # print(result.final_output)
# from agents import Agent, Runner
# from dotenv import load_dotenv

# load_dotenv()  # loads .env into os.environ

# record_save_request_analysis_instructions = """
# given a user's record save request, you generate (a list of) appropriate json with the following format:
# [
#     {
#         "counter_party":"counter party name",
#         "quantity":"quantity of service or goods sold to or bought from counter party",
#         "price":"the price on which the record is going to be kept",
#         "action": "sell|buy"
#     }
# ]

# """
# record_save_request_analyser_agent = Agent(
#     name="Record Save Request Analyser",
#     handoff_description="Specialist agent for parsing user record save request to a structured json",
#     instructions=record_save_request_analysis_instructions
# )

# ###################################################################################################################
# report_request_analysis_instructions = """
# given a user's report request, you generate (a list of) appropriate json with the following format:
# [
#     {
#     "report_type":"sales|debt|item_inventoroy|income",
#     "filters":[
#         "date":[
#             "date_from":"",
#             "date_to":""
#         ],
#         "counterparties(s)":[
#             "Ali",
#             "Hossein"
#             ]
#     ]

#     }
# ]

# """
# report_request_analyser_agent = Agent(
#     name="Report Request Analyser",
#     instructions=report_request_analysis_instructions,
#     handoff_description="Specialist agent for parsing user report request to a structured json",

# )

# ##########################################################################################


# class AccouningOutput(BaseModel):
#     is_related: bool
#     reasoning: str

# guardrail_agent = Agent(
#     name="Guardrail check",
#     instructions="Check if the user is requesting either an accounting report or a record save",
#     output_type=AccouningOutput,
# )

# async def accounting_guardrail(ctx, agent, input_data):
#     result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
#     final_output = result.final_output_as(AccouningOutput)
#     return GuardrailFunctionOutput(
#         output_info=final_output,
#         tripwire_triggered=not final_output.is_related,
#     )

# from agents import Runner


# triage_agent_instructions = """
# You determine which agent to use based on the user's request
# """
# triage_agent = Agent(
#     name="Triage Agent",
#     instructions=triage_agent_instructions,
#     handoffs=[record_save_request_analyser_agent, report_request_analyser_agent],
#         input_guardrails=[
#         InputGuardrail(guardrail_function=accounting_guardrail),
#     ],
# )
# # async def main():
# result =  Runner.run_sync(triage_agent, "امسال درآمد چقدر بود؟")
# print("================")
# print(result.final_output)


from dotenv import load_dotenv
from agents import Agent, Runner, trace
from pydantic import BaseModel, Field, condecimal, validator
from typing import Optional, List, Dict, Any, Union
from enum import Enum



load_dotenv(override=True)


class PhonePayload(BaseModel):
    phone: str
    label: Optional[str] = None
    is_primary: Optional[bool] = False


class AddressPayload(BaseModel):
    address_text: str
    label: Optional[str] = None
    is_primary: Optional[bool] = False


class CreatePersonPayload(BaseModel):
    name: str
    normalized_name: Optional[str] = None
    phones: List[PhonePayload]
    addresses: List[AddressPayload]

create_person_command_generator_agent_instructions = """
given users request text, your task is to generate a structured json command. if any needed info is missing, ask user about it
"""
create_person_command_generator_agent = Agent(
    name="create person command generator agent",
    instructions=create_person_command_generator_agent_instructions,
    model="gpt-4o-mini",
    output_type=CreatePersonPayload
)
########################################################################################################################################

class ItemType(str, Enum):
    good = "good"
    service = "service"
class CreateItemPayload(BaseModel):
    name: str
    type: ItemType = ItemType.good
    category: Optional[str] = None
    unit: Optional[str] = None
    default_unit_price: Optional[condecimal(decimal_places=2, max_digits=18)] = None

add_item_command_generator_agent_instructions = """
given users request text, your task is to generate a structured json command. if any needed info is missing, ask user about it
"""
add_item_command_generator_agent = Agent(
    name="add item command generator agent",
    instructions=add_item_command_generator_agent_instructions,
    model="gpt-4o-mini",
    output_type=CreateItemPayload
)
########################################################################################################################################

main_agent_instructions = """
you are a helpfull assistant. your task is the following:
    1-read the users requst text and find the best and only one appropriate handoff to call.
    2-call the appropriate handoff with the users input.
    3-report to user based on handoff's result
"""
main_agent = Agent(
    name="users request analyser",
    instructions=main_agent_instructions,
    model="gpt-4o-mini",
    handoffs= [add_item_command_generator_agent, create_person_command_generator_agent]
)


with trace("blah balh "):
    result = Runner.run_sync(main_agent, "یک کالای جدبد داربم . مایع ظرف شویی پریل. تعریفش کن")
    print(result.final_output)
