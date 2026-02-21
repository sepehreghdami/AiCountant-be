from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel


class PhonePayload(BaseModel):
    phone: str
    label: Optional[str] = None
    is_primary: Optional[bool] = False

class AddressPayload(BaseModel):
    address_text: str
    label: Optional[str] = None
    is_primary: Optional[bool] = False

class CreatePersonPayload(BaseModel):
    name: str
    normalized_name: Optional[str] = None
    phones: Optional[List[PhonePayload]] = None
    addresses: Optional[List[AddressPayload]] = None

class UpdatePersonPayload(BaseModel):
    person_id: UUID
    name: Optional[str] = None
    normalized_name: Optional[str] = None
    phones: Optional[List[PhonePayload]] = None
    addresses: Optional[List[AddressPayload]] = None