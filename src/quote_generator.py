import json
from dataclasses import dataclass
from typing import List

@dataclass
class Quote:
    customer_name: str
    repair_description: str
    price: float

class QuoteGenerator:
    def __init__(self):
        self.quotes = []

    def create_quote(self, customer_name: str, repair_description: str, price: float) -> Quote:
        quote = Quote(customer_name, repair_description, price)
        self.quotes.append(quote)
        return quote

    def get_quote(self, index: int) -> Quote:
        if index < len(self.quotes):
            return self.quotes[index]
        else:
            raise IndexError("Quote not found")

    def update_quote(self, index: int, customer_name: str = None, repair_description: str = None, price: float = None) -> Quote:
        if index < len(self.quotes):
            quote = self.quotes[index]
            if customer_name:
                quote.customer_name = customer_name
            if repair_description:
                quote.repair_description = repair_description
            if price:
                quote.price = price
            return quote
        else:
            raise IndexError("Quote not found")

    def delete_quote(self, index: int) -> None:
        if index < len(self.quotes):
            del self.quotes[index]
        else:
            raise IndexError("Quote not found")

    def generate_quote(self, index: int) -> str:
        if index < len(self.quotes):
            quote = self.quotes[index]
            return json.dumps({
                "customer_name": quote.customer_name,
                "repair_description": quote.repair_description,
                "price": quote.price
            })
        else:
            raise IndexError("Quote not found")
