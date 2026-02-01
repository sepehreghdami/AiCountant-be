# db/models/invoice_line.py
from sqlalchemy import String, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base, UUIDMixin


class InvoiceLine(Base, UUIDMixin):
    __tablename__ = "invoice_lines"

    invoice_id: Mapped[str] = mapped_column(
        ForeignKey("invoices.id", ondelete="CASCADE"),
        index=True,
    )

    item_id: Mapped[str | None] = mapped_column(ForeignKey("items.id"))
    description: Mapped[str] = mapped_column(String)

    quantity: Mapped[float] = mapped_column(Numeric(12, 4))
    unit_price: Mapped[float] = mapped_column(Numeric(12, 2))
    unit: Mapped[str] = mapped_column(String)
    line_total: Mapped[float] = mapped_column(Numeric(12, 2))

    invoice: Mapped["Invoice"] = relationship(back_populates="lines")
