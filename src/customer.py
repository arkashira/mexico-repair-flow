import json
from dataclasses import dataclass, field
from typing import List

@dataclass
class Vehicle:
    make: str
    model: str
    year: int
    vin: str
    license_plate: str

@dataclass
class Customer:
    name: str
    phone: str
    email: str
    address: str
    vehicles: List[Vehicle] = field(default_factory=list)

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
            "vehicles": [v.__dict__ for v in self.vehicles]
        }

    @classmethod
    def from_dict(cls, data: dict):
        customer = cls(
            name=data["name"],
            phone=data["phone"],
            email=data["email"],
            address=data["address"]
        )
        for vehicle_data in data.get("vehicles", []):
            customer.add_vehicle(Vehicle(**vehicle_data))
        return customer

class CustomerDatabase:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def get_customer(self, name: str = None, phone: str = None):
        for customer in self.customers:
            if (name and customer.name == name) or (phone and customer.phone == phone):
                return customer
        return None

    def search_customers(self, query: str):
        return [customer for customer in self.customers if query in customer.name or query in customer.phone]
