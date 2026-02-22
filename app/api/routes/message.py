from fastapi import APIRouter
from agents import Runner

from app.schemas.send_message_request import SendMessageRequest
from app.agents.main_agent import main_agent

router = APIRouter(prefix="/message")


@router.post("")
async def send_otp(request: SendMessageRequest):
    # with trace:
    agent_final_response = await Runner.run(
        main_agent, input = request.source_text
    )
    return {"response": agent_final_response.final_output}
