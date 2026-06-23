from customer import Customer, Vehicle, CustomerDatabase

def test_customer_creation():
    customer = Customer("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
    assert customer.name == "John Doe"
    assert customer.phone == "1234567890"
    assert customer.email == "johndoe@example.com"
    assert customer.address == "123 Main St"

def test_vehicle_creation():
    vehicle = Vehicle("Toyota", "Camry", 2020, "1234567890", "ABC123")
    assert vehicle.make == "Toyota"
    assert vehicle.model == "Camry"
    assert vehicle.year == 2020
    assert vehicle.vin == "1234567890"
    assert vehicle.license_plate == "ABC123"

def test_add_vehicle_to_customer():
    customer = Customer("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
    vehicle = Vehicle("Toyota", "Camry", 2020, "1234567890", "ABC123")
    customer.add_vehicle(vehicle)
    assert len(customer.vehicles) == 1
    assert customer.vehicles[0].make == "Toyota"

def test_customer_to_dict():
    customer = Customer("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
    vehicle = Vehicle("Toyota", "Camry", 2020, "1234567890", "ABC123")
    customer.add_vehicle(vehicle)
    customer_dict = customer.to_dict()
    assert customer_dict["name"] == "John Doe"
    assert customer_dict["phone"] == "1234567890"
    assert customer_dict["email"] == "johndoe@example.com"
    assert customer_dict["address"] == "123 Main St"
    assert len(customer_dict["vehicles"]) == 1
    assert customer_dict["vehicles"][0]["make"] == "Toyota"

def test_customer_from_dict():
    customer_data = {
        "name": "John Doe",
        "phone": "1234567890",
        "email": "johndoe@example.com",
        "address": "123 Main St",
        "vehicles": [
            {"make": "Toyota", "model": "Camry", "year": 2020, "vin": "1234567890", "license_plate": "ABC123"}
        ]
    }
    customer = Customer.from_dict(customer_data)
    assert customer.name == "John Doe"
    assert customer.phone == "1234567890"
    assert customer.email == "johndoe@example.com"
    assert customer.address == "123 Main St"
    assert len(customer.vehicles) == 1
    assert customer.vehicles[0].make == "Toyota"

def test_customer_database_add_customer():
    database = CustomerDatabase()
    customer = Customer("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
    database.add_customer(customer)
    assert len(database.customers) == 1
    assert database.customers[0].name == "John Doe"

def test_customer_database_get_customer():
    database = CustomerDatabase()
    customer = Customer("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
    database.add_customer(customer)
    retrieved_customer = database.get_customer(name="John Doe")
    assert retrieved_customer.name == "John Doe"

def test_customer_database_search_customers():
    database = CustomerDatabase()
    customer1 = Customer("John Doe", "1234567890", "johndoe@example.com", "123 Main St")
    customer2 = Customer("Jane Doe", "9876543210", "janedoe@example.com", "456 Elm St")
    database.add_customer(customer1)
    database.add_customer(customer2)
    results = database.search_customers("Doe")
    assert len(results) == 2
    assert results[0].name == "John Doe"
    assert results[1].name == "Jane Doe"
