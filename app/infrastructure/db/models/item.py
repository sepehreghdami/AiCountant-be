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

    business_id: Mapped[str] = mapped_column(
        ForeignKey("businesses.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    title: Mapped[str] = mapped_column(String)
    description: Mapped[str | None] = mapped_column(String)
    image: Mapped[str | None] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    type: Mapped[ItemType] = mapped_column(Enum(ItemType))
    category: Mapped[str | None] = mapped_column(String)
    unit: Mapped[str] = mapped_column(String)
    per_unit_price: Mapped[float] = mapped_column(Numeric(12, 2))

    business: Mapped["Business"] = relationship(back_populates="items")