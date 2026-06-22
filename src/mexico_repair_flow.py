from dataclasses import dataclass
from typing import List

@dataclass
class Vehicle:
    id: int
    make: str
    model: str
    year: int
    service_history: List[str]

@dataclass
class Customer:
    id: int
    name: str
    contact_details: str
    vehicles: List[Vehicle]

class MexicoRepairFlow:
    def __init__(self):
        self.customers = []
        self.vehicles = []

    def add_customer(self, customer: Customer):
        self.customers.append(customer)

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def get_customer(self, customer_id: int):
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def get_vehicle(self, vehicle_id: int):
        for vehicle in self.vehicles:
            if vehicle.id == vehicle_id:
                return vehicle
        return None

    def filter_customers(self, name: str = None, contact_details: str = None):
        filtered_customers = []
        for customer in self.customers:
            if (name is None or customer.name == name) and (contact_details is None or customer.contact_details == contact_details):
                filtered_customers.append(customer)
        return filtered_customers

    def sort_customers(self, key: str = 'name'):
        if key == 'name':
            return sorted(self.customers, key=lambda x: x.name)
        elif key == 'id':
            return sorted(self.customers, key=lambda x: x.id)
        else:
            raise ValueError("Invalid sort key")

    def get_dashboard(self, customer_id: int = None):
        dashboard = {}
        if customer_id:
            customer = self.get_customer(customer_id)
            if customer:
                dashboard['customer'] = customer
                dashboard['vehicles'] = customer.vehicles
            else:
                return None
        else:
            dashboard['customers'] = self.customers
            dashboard['vehicles'] = self.vehicles
        return dashboard
