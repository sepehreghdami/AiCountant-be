# db/models/item.py
import enum
from sqlalchemy import String, Enum, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from db.base import Base, UUIDMixin, TimestampMixin


class ItemType(str, enum.Enum):
    service = "Service"
    good = "Good"


class Item(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "items"

    type: Mapped[ItemType] = mapped_column(Enum(ItemType))
    category: Mapped[str | None] = mapped_column(String)
    unit: Mapped[str] = mapped_column(String)
    per_unit_price: Mapped[float] = mapped_column(Numeric(12, 2))
