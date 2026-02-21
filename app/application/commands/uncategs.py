#TODO: FIX MY NAME

from typing import Optional, List, Dict, Any
from uuid import UUID
from pydantic import BaseModel, condecimal
from datetime import date
from app.application.commands.common_types import CounterpartyType




class BankTransactionPayload(BaseModel):
    external_id: str
    date: date
    description: Optional[str] = None
    amount: condecimal(decimal_places=2, max_digits=18)
    currency: Currency = "USD"
    bank_account: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None

class ImportBankTransactionsPayload(BaseModel):
    transactions: List[BankTransactionPayload]

class ReconcilePayload(BaseModel):
    ledger_entry_id: UUID
    bank_tx_external_id: str
    reconciled_on: Optional[date] = None

class FindOrCreateCounterpartyPayload(BaseModel):
    tenant_id: UUID
    name: str
    type: Optional[CounterpartyType] = CounterpartyType.customer

class CreateCorrectionPayload(BaseModel):
    original_ledger_transaction_id: Optional[UUID] = None
    description: Optional[str] = None
    entries: List[Dict[str, Any]]

Currency = str