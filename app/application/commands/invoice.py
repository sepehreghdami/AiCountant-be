
from typing import Optional, List, Dict, Any
from uuid import UUID
from decimal import Decimal
from datetime import date
from pydantic import BaseModel, Field, condecimal, field_validator
from app.application.commands.common_types import InvoiceStatus


class InvoiceLinePayload(BaseModel):
    item_id: Optional[UUID] = None
    description: Optional[str] = None
    quantity: condecimal(max_digits=18, decimal_places=4) = Field(default=1)
    unit_price: condecimal(decimal_places=2, max_digits=18)
    unit: Optional[str] = None
    line_total: Optional[condecimal(decimal_places=2, max_digits=18)] = None

    @field_validator("line_total", always=True)
    def compute_line_total(cls, v, values):
        if v is None:
            q = values.get("quantity", 1)
            p = values.get("unit_price", Decimal("0.00"))
            return (Decimal(q) * Decimal(p)).quantize(Decimal("0.01"))
        return v

class CreateInvoicePayload(BaseModel):
    invoice_number: Optional[str] = None
    counterparty_id: Optional[UUID] = None
    counterparty_name: Optional[str] = None
    issue_date: date = Field(default_factory=date.today)
    due_date: Optional[date] = None
    status: InvoiceStatus = InvoiceStatus.draft
    currency: Currency = "USD"
    notes: Optional[str] = None
    lines: List[InvoiceLinePayload]
    auto_payment: Optional[Dict[str, Any]] = None

class UpdateInvoicePayload(BaseModel):
    invoice_id: UUID
    status: Optional[InvoiceStatus] = None
    due_date: Optional[date] = None
    notes: Optional[str] = None

class AddInvoiceLinePayload(BaseModel):
    invoice_id: UUID
    line: InvoiceLinePayload

class RemoveInvoiceLinePayload(BaseModel):
    invoice_id: UUID
    line_id: UUID


Currency = str 
