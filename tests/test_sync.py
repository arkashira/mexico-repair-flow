from src.sync import SyncManager, WorkOrder, Inventory, Invoice

def test_sync_data():
    sync_manager = SyncManager()
    work_order = WorkOrder(1, "Test work order")
    inventory = Inventory(1, 10)
    invoice = Invoice(1, 100.0)
    sync_manager.add_local_change("work_order", work_order)
    sync_manager.add_local_change("inventory", inventory)
    sync_manager.add_local_change("invoice", invoice)
    sync_manager.sync_data()
    cloud_store = sync_manager.get_cloud_store()
    assert len(cloud_store["work_orders"]) == 1
    assert len(cloud_store["inventory"]) == 1
    assert len(cloud_store["invoices"]) == 1

def test_resolve_conflicts():
    sync_manager = SyncManager()
    work_order1 = WorkOrder(1, "Test work order 1")
    work_order2 = WorkOrder(1, "Test work order 2")
    sync_manager.add_local_change("work_order", work_order1)
    sync_manager.add_local_change("work_order", work_order2)
    sync_manager.sync_data()
    cloud_store = sync_manager.get_cloud_store()
    assert len(cloud_store["work_orders"]) == 2

def test_detect_network_status():
    sync_manager = SyncManager()
    assert sync_manager.detect_network_status() == True
