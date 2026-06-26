# Mexico Repair Flow – Quote Generation

A tiny, pure‑Python library that lets a technician create a repair quote,
automatically calculates the total price, and keeps the quote in an
in‑memory list.

## Features

* **Vehicle details** – make, model, year validation.
* **Service items** – description and price, with validation (no negative
  prices, description required).
* **Automatic total** – summed from all service items.
* **In‑memory storage** – `QuoteManager` holds created quotes and can list them.

## Installation
