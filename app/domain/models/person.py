# db/models/person.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from db.base import Base, UUIDMixin

class Person(Base, UUIDMixin):
    __tablename__ = "persons"

    counter_parties: Mapped[list["CounterParty"]] = relationship(
        back_populates="person",
        cascade="all, delete-orphan",
    )

    phones: Mapped[list["PersonPhone"]] = relationship(
        back_populates="person",
        cascade="all, delete-orphan",
    )

    addresses: Mapped[list["PersonAddress"]] = relationship(
        back_populates="person",
        cascade="all, delete-orphan",
    )
