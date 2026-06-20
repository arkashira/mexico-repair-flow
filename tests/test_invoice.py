import pytest
import json
from invoice import Customer, Vehicle, Invoice

def test_invoice_creation():
    customer = Customer("John Doe", "john@example.com")
    vehicle = Vehicle("Toyota", "Camry", 2020)
    invoice = Invoice(customer, vehicle, {"Oil": 10.0, "Filter": 5.0}, 50.0, 8.0)
    assert invoice.customer.name == "John Doe"
    assert invoice.vehicle.make == "Toyota"
    assert invoice.parts == {"Oil": 10.0, "Filter": 5.0}
    assert invoice.labor == 50.0
    assert invoice.taxes == 8.0
    assert invoice.status == "Unpaid"

def test_invoice_export_to_pdf():
    customer = Customer("John Doe", "john@example.com")
    vehicle = Vehicle("Toyota", "Camry", 2020)
    invoice = Invoice(customer, vehicle, {"Oil": 10.0, "Filter": 5.0}, 50.0, 8.0)
    pdf_content = invoice.export_to_pdf()
    assert json.loads(pdf_content)["customer"]["name"] == "John Doe"
    assert json.loads(pdf_content)["vehicle"]["make"] == "Toyota"
    assert json.loads(pdf_content)["parts"] == {"Oil": 10.0, "Filter": 5.0}
    assert json.loads(pdf_content)["labor"] == 50.0
    assert json.loads(pdf_content)["taxes"] == 8.0
    assert json.loads(pdf_content)["status"] == "Unpaid"

def test_invoice_update_status():
    customer = Customer("John Doe", "john@example.com")
    vehicle = Vehicle("Toyota", "Camry", 2020)
    invoice = Invoice(customer, vehicle, {"Oil": 10.0, "Filter": 5.0}, 50.0, 8.0)
    invoice.update_status("Paid")
    assert invoice.status == "Paid"

def test_invoice_email_to_customer():
    customer = Customer("John Doe", "john@example.com")
    vehicle = Vehicle("Toyota", "Camry", 2020)
    invoice = Invoice(customer, vehicle, {"Oil": 10.0, "Filter": 5.0}, 50.0, 8.0)
    invoice.email_to_customer("Your invoice is attached.")
    # No assertion, just testing that the method runs without errors

def test_invoice_edge_case_empty_parts():
    customer = Customer("John Doe", "john@example.com")
    vehicle = Vehicle("Toyota", "Camry", 2020)
    invoice = Invoice(customer, vehicle, {}, 50.0, 8.0)
    assert invoice.parts == {}
