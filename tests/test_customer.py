import json
from customer import Customer, CustomerManager

def test_create_customer():
    manager = CustomerManager()
    customer = manager.create_customer("John Doe", "john@example.com")
    assert customer.id == 1
    assert customer.name == "John Doe"
    assert customer.email == "john@example.com"

def test_get_customer():
    manager = CustomerManager()
    customer = manager.create_customer("John Doe", "john@example.com")
    retrieved_customer = manager.get_customer(1)
    assert retrieved_customer == customer

def test_update_customer():
    manager = CustomerManager()
    customer = manager.create_customer("John Doe", "john@example.com")
    updated_customer = manager.update_customer(1, name="Jane Doe", email="jane@example.com")
    assert updated_customer.name == "Jane Doe"
    assert updated_customer.email == "jane@example.com"

def test_search_customers():
    manager = CustomerManager()
    manager.create_customer("John Doe", "john@example.com")
    manager.create_customer("Jane Doe", "jane@example.com")
    results = manager.search_customers(name="John Doe")
    assert len(results) == 1
    assert results[0].name == "John Doe"

def test_save_to_json():
    manager = CustomerManager()
    manager.create_customer("John Doe", "john@example.com")
    manager.save_to_json("customers.json")
    with open("customers.json", 'r') as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["name"] == "John Doe"

def test_load_from_json():
    manager = CustomerManager()
    manager.create_customer("John Doe", "john@example.com")
    manager.save_to_json("customers.json")
    manager.load_from_json("customers.json")
    assert len(manager.customers) == 1
    assert manager.customers[0].name == "John Doe"
