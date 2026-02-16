# db/models/counter_party.py
import enum
from sqlalchemy import String, Boolean, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base, UUIDMixin, TimestampMixin


class CounterPartyType(str, enum.Enum):
    supplier = "supplier"
    employee = "employee"
    customer = "customer"


class CounterParty(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "counter_parties"

    person_id: Mapped[str] = mapped_column(
        ForeignKey("persons.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    business_id: Mapped[str] = mapped_column(
        ForeignKey("businesses.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    name: Mapped[str] = mapped_column(String, nullable=False)
    normalized_name: Mapped[str] = mapped_column(String, index=True)
    type: Mapped[CounterPartyType] = mapped_column(Enum(CounterPartyType))
    description: Mapped[str | None] = mapped_column(String)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    person: Mapped["Person"] = relationship(back_populates="counter_parties")
    invoices: Mapped[list["Invoice"]] = relationship(back_populates="counter_party")
    business: Mapped["Business"] = relationship(back_populates="counter_parties")

