# db/models/person_phone.py
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base, UUIDMixin


class PersonPhone(Base, UUIDMixin):
    __tablename__ = "person_phones"

    person_id: Mapped[str] = mapped_column(
        ForeignKey("persons.id", ondelete="CASCADE"),
        index=True,
    )

    phone: Mapped[str] = mapped_column(String, nullable=False)
    label: Mapped[str | None] = mapped_column(String)
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False)

    person: Mapped["Person"] = relationship(back_populates="phones")
