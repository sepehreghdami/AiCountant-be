1. Person
Purpose

Represents a real human being.
A person may appear as:

a customer

a supplier

an employee
(via CounterParty)

This separation avoids duplication when the same person plays multiple roles.

Person
------
id

Fields

id (UUID, PK)
Unique identifier for a real person.
Used to attach phones, addresses, and multiple counter-party roles.

2. CounterParty
Purpose

Represents a business relationship with a person.
Same person can be:

customer in one context

supplier in another

CounterParty
------------
id
person_id
name
normalized_name
type
description
is_active
created_on
updated_on

Fields

id (UUID, PK)
Unique identifier for this business role.

person_id (FK → Person.id)
Links the counter-party role to a real person.

name (string)
Display name used in invoices, chats, and UI.
Example: "James Drywall Services"

normalized_name (string)
Lowercased / cleaned version of name.
Used for:

LLM matching

fuzzy search

duplicate detection

type (enum: supplier | employee | customer)
Defines how this counter-party participates in transactions.

description (string)
Free-form notes.
Useful for LLM context:

“Usually pays late”, “Friend of Ali”, etc.

is_active (boolean)
Soft-delete flag.
Inactive counter-parties remain in history but are not suggested.

created_on (datetime)
Audit timestamp.

updated_on (datetime)
Last modification time.

3. PersonPhone
Purpose

Stores multiple phone numbers per person with labels.

PersonPhone
-----------
id
person_id
phone
label
is_primary

Fields

id (UUID, PK)
Unique phone record.

person_id (FK → Person.id)
Owner of the phone number.

phone (string)
Raw phone number.
Normalization can be added later.

label (string)
Human label:

"mobile"

"work"

"shop"

is_primary (boolean)
Marks default phone number.

4. PersonAddress
Purpose

Stores multiple addresses per person.

PersonAddress
-------------
id
person_id
address_text
label
is_primary

Fields

id (UUID, PK)
Unique address record.

person_id (FK → Person.id)
Owner of the address.

address_text (string)
Free-form address text (LLM-friendly).

label (string)
Example:

"home"

"shop"

"billing"

is_primary (boolean)
Default address.

5. Item
Purpose

Represents reusable catalog items:

goods

services

Items are templates, not historical truth.

Item
-------------
id
Type : Service|Good
category
Unit
perUnitPrice
createdAt
updatedAt

Fields

id (UUID, PK)
Unique item identifier.

type (enum: Service | Good)
Determines whether inventory is involved.

category (string)
Logical grouping:

"Construction"

"Cosmetics"

unit (string)
Measurement unit:

"hour"

"piece"

"kg"

perUnitPrice (decimal)
Default price suggestion.
⚠️ NOT authoritative — invoice lines override this.

createdAt (datetime)
Audit timestamp.

updatedAt (datetime)
Audit timestamp.

6. Invoice
Purpose

A human-readable document describing a charge.
Invoices do not store balances.

Invoice
-------
id
invoice_number
counter_party_id
issue_date
due_date
status
currency
notes
created_at
updated_at

Fields

id (UUID, PK)
Internal invoice identifier.

invoice_number (string, unique)
Human-friendly identifier.
Example: "INV-2026-001"

counter_party_id (FK → CounterParty.id)
Who the invoice is issued to.

issue_date (date)
When the invoice is created.

due_date (date, nullable)
Payment deadline.

status (enum)
Document lifecycle:

draft

issued

partially_paid

paid

cancelled

⚠️ Status is derived from ledger, not authoritative.

currency (string)
ISO code, e.g. "USD".

notes (string)
Free-form notes for user or LLM.

created_at (datetime)
Audit timestamp.

updated_at (datetime)
Audit timestamp.

7. InvoiceLine
Purpose

Represents individual items/services on an invoice.

InvoiceLine
-----------
id
invoice_id
item_id
description
quantity
unit_price
unit
line_total

Fields

id (UUID, PK)
Unique invoice line.

invoice_id (FK → Invoice.id)
Parent invoice.

item_id (FK → Item.id)
Reference item (optional logic).

description (string)
Snapshot description at invoice time.

quantity (decimal)
Amount sold or worked.

unit_price (decimal)
Price per unit at invoice time.

unit (string)
Snapshot of unit (do not rely on Item).

line_total (decimal)
quantity × unit_price
Stored for immutability & performance.

8. LedgerTransaction
Purpose

Represents one real-world financial event.
Acts as a header for ledger entries.

LedgerTransaction
-----------------
id
invoice_id
description
created_at

Fields

id (UUID, PK)
Unique transaction identifier.

invoice_id (FK → Invoice.id, nullable)
Optional link to invoice that caused this transaction.

description (string)
Human explanation of what happened.

created_at (datetime)
Event timestamp.

9. LedgerEntry
Purpose

Represents one effect of a transaction.
A single transaction produces multiple entries.

LedgerEntry
-----------
id
ledger_transaction_id
account
amount
direction
item_id
quantity

Fields

id (UUID, PK)
Unique ledger entry.

ledger_transaction_id (FK → LedgerTransaction.id)
Parent transaction.

account (string | enum)
Logical bucket:

Cash

Revenue

AccountsReceivable

Inventory

amount (decimal)
Monetary value (always positive).

direction (enum: debit | credit)
Determines sign and accounting meaning.

item_id (FK → Item.id, nullable)
Used for inventory tracking.

quantity (decimal, nullable)
Inventory movement amount.

Final mental model (Cursor-friendly)

Invoice = document

LedgerTransaction = event

LedgerEntry = effect

Item = catalog

CounterParty = role

Person = human



===================================================================================================================================
install poetry command:

(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

poetry init

poetry add --group dev pytest ruff mypy httpx


 C:\Users\Asus\AppData\Local\pypoetry\Cache\virtualenvs\aicountant-be-Kk8vlHwv-py3.14\Scripts\Activate.ps1
==================================================================================================================================