"""Quote generation module for Mexico Repair Flow.

Provides in‑memory management of repair quotes with automatic total price
calculation and basic validation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class ServiceItem:
    """A single service line item."""
    description: str
    price: float

    def __post_init__(self) -> None:
        if not self.description:
            raise ValueError("Service item description must be non‑empty")
        if not isinstance(self.price, (int, float)):
            raise ValueError("Service item price must be a number")
        if self.price < 0:
            raise ValueError("Service item price cannot be negative")


@dataclass(frozen=True)
class Quote:
    """A repair quote."""
    id: int
    vehicle_make: str
    vehicle_model: str
    vehicle_year: int
    service_items: List[ServiceItem] = field(default_factory=list)
    total_price: float = 0.0


class QuoteManager:
    """In‑memory store for quotes."""

    def __init__(self) -> None:
        self._quotes: List[Quote] = []
        self._next_id: int = 1

    def create_quote(
        self,
        vehicle_make: str,
        vehicle_model: str,
        vehicle_year: int,
        service_items: List[dict | ServiceItem],
    ) -> Quote:
        """Validate input, calculate total, store and return a new Quote.

        Args:
            vehicle_make: Manufacturer name.
            vehicle_model: Model name.
            vehicle_year: Production year (int, 1886‑2100).
            service_items: List of dicts ``{'description': str, 'price': float}``
                or ``ServiceItem`` instances.

        Returns:
            The created ``Quote`` instance.

        Raises:
            ValueError: If any validation fails.
        """
        # Basic vehicle validation
        if not vehicle_make or not vehicle_model:
            raise ValueError("Vehicle make and model are required")
        if not isinstance(vehicle_year, int) or not (1886 <= vehicle_year <= 2100):
            raise ValueError("Vehicle year must be an integer between 1886 and 2100")

        # Service items validation and conversion
        if not service_items:
            raise ValueError("At least one service item is required")

        items: List[ServiceItem] = []
        for raw in service_items:
            if isinstance(raw, ServiceItem):
                item = raw
            else:
                # Expect a mapping with description and price
                try:
                    description = raw["description"]
                    price = raw["price"]
                except (TypeError, KeyError) as exc:
                    raise ValueError("Service item must have 'description' and 'price'") from exc
                item = ServiceItem(description=description, price=price)
            items.append(item)

        total = sum(item.price for item in items)

        quote = Quote(
            id=self._next_id,
            vehicle_make=vehicle_make,
            vehicle_model=vehicle_model,
            vehicle_year=vehicle_year,
            service_items=items,
            total_price=total,
        )
        self._quotes.append(quote)
        self._next_id += 1
        return quote

    def list_quotes(self) -> List[Quote]:
        """Return a shallow copy of all stored quotes."""
        return list(self._quotes)
