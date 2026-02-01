# db/models/ledger_transaction.py
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base, UUIDMixin, TimestampMixin


class LedgerTransaction(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "ledger_transactions"

    invoice_id: Mapped[str | None] = mapped_column(
        ForeignKey("invoices.id"),
        index=True,
    )

    description: Mapped[str] = mapped_column(String)

    entries: Mapped[list["LedgerEntry"]] = relationship(
        back_populates="transaction",
        cascade="all, delete-orphan",
    )
