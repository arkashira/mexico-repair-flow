import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Customer:
    id: int
    name: str
    email: str

class CustomerManager:
    def __init__(self):
        self.customers = []

    def create_customer(self, name: str, email: str) -> Customer:
        customer_id = len(self.customers) + 1
        customer = Customer(customer_id, name, email)
        self.customers.append(customer)
        return customer

    def get_customer(self, customer_id: int) -> Customer:
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        raise ValueError("Customer not found")

    def update_customer(self, customer_id: int, name: str = None, email: str = None) -> Customer:
        customer = self.get_customer(customer_id)
        if name:
            customer.name = name
        if email:
            customer.email = email
        return customer

    def search_customers(self, name: str = None, email: str = None) -> List[Customer]:
        results = []
        for customer in self.customers:
            if (name and customer.name == name) or (email and customer.email == email):
                results.append(customer)
        return results

    def save_to_json(self, filename: str) -> None:
        data = [customer.__dict__ for customer in self.customers]
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load_from_json(self, filename: str) -> None:
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.customers = [Customer(**customer) for customer in data]
        except FileNotFoundError:
            pass
