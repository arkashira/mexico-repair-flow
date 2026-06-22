from mexico_repair_flow import MexicoRepairFlow, Customer, Vehicle

def test_add_customer():
    flow = MexicoRepairFlow()
    customer = Customer(id=1, name='John Doe', contact_details='john@example.com', vehicles=[])
    flow.add_customer(customer)
    assert flow.get_customer(1) == customer

def test_add_vehicle():
    flow = MexicoRepairFlow()
    vehicle = Vehicle(id=1, make='Toyota', model='Corolla', year=2015, service_history=[])
    flow.add_vehicle(vehicle)
    assert flow.get_vehicle(1) == vehicle

def test_get_customer():
    flow = MexicoRepairFlow()
    customer = Customer(id=1, name='John Doe', contact_details='john@example.com', vehicles=[])
    flow.add_customer(customer)
    assert flow.get_customer(1) == customer
    assert flow.get_customer(2) is None

def test_get_vehicle():
    flow = MexicoRepairFlow()
    vehicle = Vehicle(id=1, make='Toyota', model='Corolla', year=2015, service_history=[])
    flow.add_vehicle(vehicle)
    assert flow.get_vehicle(1) == vehicle
    assert flow.get_vehicle(2) is None

def test_filter_customers():
    flow = MexicoRepairFlow()
    customer1 = Customer(id=1, name='John Doe', contact_details='john@example.com', vehicles=[])
    customer2 = Customer(id=2, name='Jane Doe', contact_details='jane@example.com', vehicles=[])
    flow.add_customer(customer1)
    flow.add_customer(customer2)
    filtered_customers = flow.filter_customers(name='John Doe')
    assert len(filtered_customers) == 1
    assert filtered_customers[0] == customer1

def test_sort_customers():
    flow = MexicoRepairFlow()
    customer1 = Customer(id=1, name='John Doe', contact_details='john@example.com', vehicles=[])
    customer2 = Customer(id=2, name='Jane Doe', contact_details='jane@example.com', vehicles=[])
    flow.add_customer(customer1)
    flow.add_customer(customer2)
    sorted_customers = flow.sort_customers(key='name')
    assert len(sorted_customers) == 2
    assert sorted_customers[0].name == 'Jane Doe'
    assert sorted_customers[1].name == 'John Doe'

def test_get_dashboard():
    flow = MexicoRepairFlow()
    customer = Customer(id=1, name='John Doe', contact_details='john@example.com', vehicles=[])
    flow.add_customer(customer)
    dashboard = flow.get_dashboard(customer_id=1)
    assert dashboard['customer'] == customer
    assert 'vehicles' in dashboard
