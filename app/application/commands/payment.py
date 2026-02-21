from typing import Optional, List, Dict, Any
from uuid import UUID
from datetime import date
from pydantic import BaseModel, Field, condecimal


class QuickSalePayload(BaseModel):
    counterparty_id: Optional[UUID] = None
    counterparty_name: Optional[str] = None
    item_id: Optional[UUID] = None
    item_name: Optional[str] = None
    quantity: condecimal(max_digits=18, decimal_places=4) = Field(default=1)
    total_amount: condecimal(decimal_places=2, max_digits=18)
    currency: Currency = "USD"
    payment_method: Optional[str] = "cash"  
    create_invoice: Optional[bool] = False
    invoice_number: Optional[str] = None
    line_unit_price: Optional[condecimal(decimal_places=2, max_digits=18)] = None

class RecordServiceDebtPayload(BaseModel):
    counterparty_id: Optional[UUID] = None
    counterparty_name: Optional[str] = None
    service_description: str
    amount: condecimal(decimal_places=2, max_digits=18)
    currency: Currency = "USD"
    due_date: Optional[date] = None
    invoice_if_any: Optional[Dict[str, Any]] = None

class RecordPaymentPayload(BaseModel):
    counterparty_id: Optional[UUID] = None
    counterparty_name: Optional[str] = None
    amount: condecimal(decimal_places=2, max_digits=18)
    currency: Currency = "USD"
    payment_method: str  # e.g. cash|card|bank_transfer
    applied_to_invoice_ids: Optional[List[UUID]] = None
    reference: Optional[str] = None
    received_on: Optional[date] = None

class RecordRefundPayload(BaseModel):
    counterparty_id: Optional[UUID] = None
    counterparty_name: Optional[str] = None
    amount: condecimal(decimal_places=2, max_digits=18)
    currency: Currency = "USD"
    refund_method: str
    reason: Optional[str] = None
    original_invoice_id: Optional[UUID] = None


Currency = str