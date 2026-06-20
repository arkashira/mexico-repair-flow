import json
from dataclasses import dataclass
from datetime import datetime
from typing import Dict

@dataclass
class Customer:
    name: str
    email: str

@dataclass
class Vehicle:
    make: str
    model: str
    year: int

@dataclass
class Invoice:
    customer: Customer
    vehicle: Vehicle
    parts: Dict[str, float]
    labor: float
    taxes: float
    status: str = "Unpaid"

    def to_dict(self):
        return {
            "customer": self.customer.__dict__,
            "vehicle": self.vehicle.__dict__,
            "parts": self.parts,
            "labor": self.labor,
            "taxes": self.taxes,
            "status": self.status,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

    def export_to_pdf(self):
        # Simulate PDF export
        return json.dumps(self.to_dict(), indent=4)

    def update_status(self, status: str):
        self.status = status

    def email_to_customer(self, email_body: str):
        # Simulate email sending
        print(f"Email sent to {self.customer.email} with body: {email_body}")
