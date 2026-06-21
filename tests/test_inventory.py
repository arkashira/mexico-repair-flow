import pytest
from inventory import Inventory, Part

def test_add_part():
    inventory = Inventory()
    part = Part("Test Part", 10, 5, True)
    inventory.add_part(part)
    assert len(inventory.parts) == 1

def test_set_threshold():
    inventory = Inventory()
    part = Part("Test Part", 10, 5, True)
    inventory.add_part(part)
    inventory.set_threshold("Test Part", 3)
    assert inventory.get_part("Test Part").threshold == 3

def test_check_low_stock():
    inventory = Inventory()
    part1 = Part("Test Part 1", 10, 5, True)
    part2 = Part("Test Part 2", 3, 5, True)
    inventory.add_part(part1)
    inventory.add_part(part2)
    low_stock_parts = inventory.check_low_stock()
    assert len(low_stock_parts) == 1
    assert low_stock_parts[0].name == "Test Part 2"

def test_send_notification():
    inventory = Inventory()
    part = Part("Test Part", 3, 5, True)
    inventory.add_part(part)
    inventory.send_notification(part)
    # No assertion, just checking it runs without error

def test_update_stock():
    inventory = Inventory()
    part = Part("Test Part", 10, 5, True)
    inventory.add_part(part)
    inventory.update_stock("Test Part", 5)
    assert inventory.get_part("Test Part").stock == 15

def test_get_part():
    inventory = Inventory()
    part = Part("Test Part", 10, 5, True)
    inventory.add_part(part)
    retrieved_part = inventory.get_part("Test Part")
    assert retrieved_part.name == "Test Part"

def test_check_low_stock_edge_case():
    inventory = Inventory()
    part = Part("Test Part", 5, 5, True)
    inventory.add_part(part)
    low_stock_parts = inventory.check_low_stock()
    assert len(low_stock_parts) == 0
