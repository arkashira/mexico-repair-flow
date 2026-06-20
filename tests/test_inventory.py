from inventory import Inventory, Part

def test_add_part():
    inventory = Inventory()
    inventory.add_part("1234567890", "Test Part", 10)
    assert inventory.get_part("1234567890").name == "Test Part"
    assert inventory.get_part("1234567890").quantity == 10

def test_add_part_to_work_order():
    inventory = Inventory()
    inventory.add_part("1234567890", "Test Part", 10)
    inventory.add_part_to_work_order("work_order_1", "1234567890")
    assert len(inventory.get_work_order_parts("work_order_1")) == 1
    assert inventory.get_part("1234567890").quantity == 9

def test_update_inventory():
    inventory = Inventory()
    inventory.add_part("1234567890", "Test Part", 10)
    inventory.update_inventory("1234567890", 5)
    assert inventory.get_part("1234567890").quantity == 5

def test_get_work_order_parts():
    inventory = Inventory()
    inventory.add_part("1234567890", "Test Part", 10)
    inventory.add_part_to_work_order("work_order_1", "1234567890")
    assert len(inventory.get_work_order_parts("work_order_1")) == 1

def test_get_part():
    inventory = Inventory()
    inventory.add_part("1234567890", "Test Part", 10)
    assert inventory.get_part("1234567890").name == "Test Part"

def test_add_part_to_work_order_part_not_found():
    inventory = Inventory()
    try:
        inventory.add_part_to_work_order("work_order_1", "1234567890")
        assert False
    except ValueError as e:
        assert str(e) == "Part not found in inventory"

def test_update_inventory_part_not_found():
    inventory = Inventory()
    try:
        inventory.update_inventory("1234567890", 5)
        assert False
    except ValueError as e:
        assert str(e) == "Part not found in inventory"
