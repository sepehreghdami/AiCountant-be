# db/models/ledger_entry.py
import enum
from sqlalchemy import String, Enum, ForeignKey, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base, UUIDMixin


class LedgerDirection(str, enum.Enum):
    debit = "debit"
    credit = "credit"


class LedgerEntry(Base, UUIDMixin):
    __tablename__ = "ledger_entries"

    ledger_transaction_id: Mapped[str] = mapped_column(
        ForeignKey("ledger_transactions.id", ondelete="CASCADE"),
        index=True,
    )
    business_id: Mapped[str] = mapped_column(
        ForeignKey("businesses.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    account: Mapped[str] = mapped_column(String)
    amount: Mapped[float] = mapped_column(Numeric(14, 2))
    direction: Mapped[LedgerDirection] = mapped_column(Enum(LedgerDirection))

    item_id: Mapped[str | None] = mapped_column(ForeignKey("items.id"))
    quantity: Mapped[float | None] = mapped_column(Numeric(12, 4))

    transaction: Mapped["LedgerTransaction"] = relationship(back_populates="entries")
    business: Mapped["Business"] = relationship(back_populates="ledger_entries")
