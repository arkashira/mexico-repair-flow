import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Part:
    upc: str
    name: str
    quantity: int

class Inventory:
    def __init__(self):
        self.parts: Dict[str, Part] = {}
        self.work_orders: Dict[str, List[Part]] = {}

    def add_part(self, upc: str, name: str, quantity: int):
        self.parts[upc] = Part(upc, name, quantity)

    def add_part_to_work_order(self, work_order_id: str, upc: str):
        if upc not in self.parts:
            raise ValueError("Part not found in inventory")
        if work_order_id not in self.work_orders:
            self.work_orders[work_order_id] = []
        self.work_orders[work_order_id].append(self.parts[upc])
        self.parts[upc].quantity -= 1

    def get_work_order_parts(self, work_order_id: str) -> List[Part]:
        return self.work_orders.get(work_order_id, [])

    def get_part(self, upc: str) -> Part:
        return self.parts.get(upc)

    def update_inventory(self, upc: str, quantity: int):
        if upc not in self.parts:
            raise ValueError("Part not found in inventory")
        self.parts[upc].quantity = quantity
