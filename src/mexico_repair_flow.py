from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Customer:
    name: str
    phone: str

@dataclass
class Vehicle:
    make: str
    model: str
    year: int

@dataclass
class ServiceType:
    name: str
    description: str

@dataclass
class WorkOrder:
    customer: Customer
    vehicle: Vehicle
    service_type: ServiceType
    notes: str
    created_at: datetime

class MexicoRepairFlow:
    def __init__(self):
        self.work_orders = []

    def create_work_order(self, customer_name: str, customer_phone: str, vehicle_make: str, vehicle_model: str, vehicle_year: int, service_type_name: str, service_type_description: str, notes: str) -> WorkOrder:
        if not self.validate_work_order(customer_name, customer_phone, vehicle_make, vehicle_model, vehicle_year, service_type_name, service_type_description, notes):
            raise ValueError("Invalid work order data")
        customer = Customer(customer_name, customer_phone)
        vehicle = Vehicle(vehicle_make, vehicle_model, vehicle_year)
        service_type = ServiceType(service_type_name, service_type_description)
        work_order = WorkOrder(customer, vehicle, service_type, notes, datetime.now())
        self.work_orders.append(work_order)
        return work_order

    def get_work_orders(self) -> List[WorkOrder]:
        return self.work_orders

    def validate_work_order(self, customer_name: str, customer_phone: str, vehicle_make: str, vehicle_model: str, vehicle_year: int, service_type_name: str, service_type_description: str, notes: str) -> bool:
        if not customer_name or not customer_phone or not vehicle_make or not vehicle_model or vehicle_year < 1900 or not service_type_name or not service_type_description or not notes:
            return False
        return True
