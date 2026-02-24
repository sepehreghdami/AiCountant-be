from fastapi import APIRouter
from agents import Runner
from app.schemas.send_message_request import SendMessageRequest
from app.agents.main_agent import main_agent

router = APIRouter(prefix="/message")


@router.post("")
async def send_otp(request: SendMessageRequest):
    # with trace:
    context = SendMessageRequest(
        tenant_id="e8c3346f-98f0-47a2-87cf-6260a22a3f86",
        actor_id="d2378c62-4261-4300-bafd-6e1228cc3ec4",
        idempotency_key="74a34c13-eb9e-450a-9d4f-eaa9b380190f",
        source_text=request.source_text
    )
    agent_final_response = await Runner.run(
        main_agent, input=context.source_text, context=context
    )
    return {"response": agent_final_response.final_output}



