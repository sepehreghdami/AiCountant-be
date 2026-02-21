from typing import Optional, List, Dict, Any
from uuid import UUID
from pydantic import BaseModel,field_validator


class CreateLedgerTransactionPayload(BaseModel):
    description: Optional[str] = None
    invoice_id: Optional[UUID] = None
    entries: List[Dict[str, Any]]


    @field_validator("entries", each_item=True)
    def check_entry_shape(cls, v):
        required = {"account", "direction", "amount"}
        if not required.issubset(set[Any](v.keys())):
            raise ValueError(f"ledger entry must include {required}")
        return v