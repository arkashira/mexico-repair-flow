from mexico_repair_flow import MexicoRepairFlow, Customer, Vehicle, ServiceType, WorkOrder
import pytest

def test_create_work_order():
    flow = MexicoRepairFlow()
    work_order = flow.create_work_order("John Doe", "123-456-7890", "Toyota", "Camry", 2020, "Oil Change", "Change oil and filter", "Notes")
    assert work_order.customer.name == "John Doe"
    assert work_order.vehicle.make == "Toyota"
    assert work_order.service_type.name == "Oil Change"
    assert work_order.notes == "Notes"

def test_get_work_orders():
    flow = MexicoRepairFlow()
    flow.create_work_order("John Doe", "123-456-7890", "Toyota", "Camry", 2020, "Oil Change", "Change oil and filter", "Notes")
    work_orders = flow.get_work_orders()
    assert len(work_orders) == 1

def test_validate_work_order():
    flow = MexicoRepairFlow()
    assert flow.validate_work_order("John Doe", "123-456-7890", "Toyota", "Camry", 2020, "Oil Change", "Change oil and filter", "Notes") == True
    assert flow.validate_work_order("", "", "", "", 0, "", "", "") == False

def test_create_work_order_with_empty_fields():
    flow = MexicoRepairFlow()
    with pytest.raises(ValueError):
        flow.create_work_order("", "", "", "", 0, "", "", "")

def test_create_work_order_with_invalid_vehicle_year():
    flow = MexicoRepairFlow()
    with pytest.raises(ValueError):
        flow.create_work_order("John Doe", "123-456-7890", "Toyota", "Camry", -1, "Oil Change", "Change oil and filter", "Notes")
