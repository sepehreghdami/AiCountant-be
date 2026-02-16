# db/models/invoice.py
import enum
from datetime import date
from sqlalchemy import String, Enum, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base, UUIDMixin, TimestampMixin


class InvoiceStatus(str, enum.Enum):
    draft = "draft"
    issued = "issued"
    partially_paid = "partially_paid"
    paid = "paid"
    cancelled = "cancelled"


class Invoice(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "invoices"

    invoice_number: Mapped[str] = mapped_column(String, unique=True, index=True)
    counter_party_id: Mapped[str] = mapped_column(
        ForeignKey("counter_parties.id"),
        index=True,
    )
    business_id: Mapped[str] = mapped_column(
        ForeignKey("businesses.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    issue_date: Mapped[date] = mapped_column(Date)
    due_date: Mapped[date | None] = mapped_column(Date)
    status: Mapped[InvoiceStatus] = mapped_column(Enum(InvoiceStatus))
    currency: Mapped[str] = mapped_column(String(3))
    notes: Mapped[str | None] = mapped_column(String)

    counter_party: Mapped["CounterParty"] = relationship(back_populates="invoices")
    lines: Mapped[list["InvoiceLine"]] = relationship(
        back_populates="invoice",
        cascade="all, delete-orphan",
    )
    business: Mapped["Business"] = relationship(back_populates="invoices")
