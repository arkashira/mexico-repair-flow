import json
from dataclasses import dataclass
from typing import List

@dataclass
class WorkOrder:
    id: int
    description: str

@dataclass
class Inventory:
    id: int
    quantity: int

@dataclass
class Invoice:
    id: int
    amount: float

class SyncManager:
    def __init__(self):
        self.local_changes = {
            "work_orders": [],
            "inventory": [],
            "invoices": []
        }
        self.cloud_store = {
            "work_orders": [],
            "inventory": [],
            "invoices": []
        }

    def detect_network_status(self):
        # Simulate network status detection
        return True

    def sync_data(self):
        if self.detect_network_status():
            self.merge_local_changes_with_cloud_store()

    def merge_local_changes_with_cloud_store(self):
        for work_order in self.local_changes["work_orders"]:
            self.cloud_store["work_orders"].append(work_order)
        for inventory in self.local_changes["inventory"]:
            self.cloud_store["inventory"].append(inventory)
        for invoice in self.local_changes["invoices"]:
            self.cloud_store["invoices"].append(invoice)

    def resolve_conflicts(self):
        # Simulate conflict resolution using 'last write wins' strategy
        pass

    def add_local_change(self, change_type, change):
        if change_type == "work_order":
            self.local_changes["work_orders"].append(change)
        elif change_type == "inventory":
            self.local_changes["inventory"].append(change)
        elif change_type == "invoice":
            self.local_changes["invoices"].append(change)

    def get_cloud_store(self):
        return self.cloud_store
