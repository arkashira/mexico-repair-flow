import json
from dataclasses import dataclass
from typing import List

@dataclass
class Part:
    name: str
    stock: int
    threshold: int
    notify: bool

class Inventory:
    def __init__(self):
        self.parts = []

    def add_part(self, part: Part):
        self.parts.append(part)

    def set_threshold(self, part_name: str, threshold: int):
        for part in self.parts:
            if part.name == part_name:
                part.threshold = threshold
                break

    def check_low_stock(self):
        low_stock_parts = []
        for part in self.parts:
            if part.stock < part.threshold:
                low_stock_parts.append(part)
        return low_stock_parts

    def send_notification(self, part: Part):
        if part.notify:
            print(f"Low stock alert: {part.name} is below threshold")

    def update_stock(self, part_name: str, quantity: int):
        for part in self.parts:
            if part.name == part_name:
                part.stock += quantity
                break

    def get_part(self, part_name: str):
        for part in self.parts:
            if part.name == part_name:
                return part
        return None
