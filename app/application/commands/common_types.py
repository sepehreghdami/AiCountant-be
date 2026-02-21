
from typing import Enum

class Direction(str, Enum):
    debit = "debit"
    credit = "credit"

class ItemType(str, Enum):
    good = "good"
    service = "service"

class CounterpartyType(str, Enum):
    customer = "customer"
    supplier = "supplier"
    both = "both"

class InvoiceStatus(str, Enum):
    draft = "draft"
    issued = "issued"
    paid = "paid"
    partially_paid = "partially_paid"
    cancelled = "cancelled"