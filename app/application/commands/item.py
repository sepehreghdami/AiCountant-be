from typing import Optional
from uuid import UUID
from pydantic import BaseModel, condecimal
from app.application.commands.common_types import ItemType

class CreateItemPayload(BaseModel):
    name: str
    type: ItemType = ItemType
    category: Optional[str] = None
    unit: Optional[str] = None
    default_unit_price: Optional[condecimal(decimal_places=2, max_digits=18)] = None

class UpdateItemPayload(BaseModel):
    item_id: UUID
    name: Optional[str] = None
    type: Optional[ItemType] = None
    category: Optional[str] = None
    unit: Optional[str] = None
    default_unit_price: Optional[condecimal(decimal_places=2, max_digits=18)] = None