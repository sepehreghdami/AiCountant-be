from typing import Optional
from enum import Enum
from uuid import UUID
from pydantic import BaseModel, condecimal


class InventoryAdjustmentReason(str, Enum):
    count = "count"
    correction = "correction"
    sale = "sale"
    purchase = "purchase"
    transfer = "transfer"


class InventoryAdjustmentPayload(BaseModel):
    item_id: UUID
    quantity_delta: condecimal(max_digits=18, decimal_places=4)
    reason: InventoryAdjustmentReason
    note: Optional[str] = None
    related_invoice_id: Optional[UUID] = None
