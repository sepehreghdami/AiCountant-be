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
    business_id: Mapped[str] = mapped_column(
        ForeignKey("businesses.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )
    description: Mapped[str] = mapped_column(String)

    entries: Mapped[list["LedgerEntry"]] = relationship(
        back_populates="transaction",
        cascade="all, delete-orphan",
    )
    business: Mapped["Business"] = relationship(back_populates="ledger_transactions")