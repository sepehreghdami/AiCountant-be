from typing import Optional, Dict, Any
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field


class CommandMeta(BaseModel):
    idempotency_key: Optional[str] = None
    tenant_id: UUID
    actor_id: Optional[UUID] = None
    timestamp: Optional[datetime] = None
    source_text: Optional[str] = None
    confidence: Optional[float] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class Command(BaseModel):
    type: str
    meta: CommandMeta
    data: Dict[str, Any]

    class Config:
        extra = "forbid"
