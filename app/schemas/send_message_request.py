from pydantic import BaseModel
from typing import Optional
from uuid import UUID



class SendMessageRequest(BaseModel):
    idempotency_key: Optional[str] = None
    tenant_id: UUID
    actor_id: Optional[UUID] = None
    source_text: Optional[str] = None

