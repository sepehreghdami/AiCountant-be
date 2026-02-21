from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from app.application.commands.common_types import CounterpartyType


class CreateCounterpartyPayload(BaseModel):
    person_id: Optional[UUID] = None       
    person_name: Optional[str] = None      
    type: CounterpartyType
    description: Optional[str] = None
    is_active: Optional[bool] = True

class UpdateCounterpartyPayload(BaseModel):
    counterparty_id: UUID
    type: Optional[CounterpartyType] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None