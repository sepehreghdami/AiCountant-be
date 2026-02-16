class Business(Base, UUIDMixin):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String)

    counter_parties: Mapped[list["CounterParty"]] = relationship(
        back_populates="Business",
        cascade="all, delete-orphan",
    )
    invoices: Mapped[list["Invoice"]] = relationship(
        back_populates="Business",
        cascade="all, delete-orphan",
    )
    invoice_lines: Mapped[list["InvoiceLine"]] = relationship(
        back_populates="Business",
        cascade="all, delete-orphan",
    )
    ledger_transactions: Mapped[list["LedgerTransaction"]] = relationship(
        back_populates="Business",
        cascade="all, delete-orphan",
    )
    ledger_entries: Mapped[list["LedgerEntry"]] = relationship(
        back_populates="Business",
        cascade="all, delete-orphan",
    )
    items: Mapped[list["Item"]] = relationship(
        back_populates="Business",
        cascade="all, delete-orphan",
    )
    persons: Mapped[list["Person"]] = relationship(
        back_populates="Business",
        cascade="all, delete-orphan",
    )
    person_phones: Mapped[list["PersonPhone"]] = relationship(
        back_populates="Business",
        cascade="all, delete-orphan",
    )
    person_addresses: Mapped[list["PersonAddress"]] = relationship(
        back_populates="Business",
        cascade="all, delete-orphan",
    )

