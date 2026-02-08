# db/models/person_address.py
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base, UUIDMixin


class PersonAddress(Base, UUIDMixin):
    __tablename__ = "person_addresses"

    person_id: Mapped[str] = mapped_column(
        ForeignKey("persons.id", ondelete="CASCADE"),
        index=True,
    )
    business_id: Mapped[str] = mapped_column(
        ForeignKey("businesses.id", ondelete="CASCADE"),
        index=True,
        nullable=False,
    )

    address_text: Mapped[str] = mapped_column(String, nullable=False)
    label: Mapped[str | None] = mapped_column(String)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False)

    person: Mapped["Person"] = relationship(back_populates="addresses")
    business: Mapped["Business"] = relationship(back_populates="person_addresses")
