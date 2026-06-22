import json
from quote_generator import QuoteGenerator, Quote

def test_create_quote():
    generator = QuoteGenerator()
    quote = generator.create_quote("John Doe", "Repair car", 100.0)
    assert quote.customer_name == "John Doe"
    assert quote.repair_description == "Repair car"
    assert quote.price == 100.0

def test_get_quote():
    generator = QuoteGenerator()
    generator.create_quote("John Doe", "Repair car", 100.0)
    quote = generator.get_quote(0)
    assert quote.customer_name == "John Doe"
    assert quote.repair_description == "Repair car"
    assert quote.price == 100.0

def test_update_quote():
    generator = QuoteGenerator()
    generator.create_quote("John Doe", "Repair car", 100.0)
    updated_quote = generator.update_quote(0, customer_name="Jane Doe", price=200.0)
    assert updated_quote.customer_name == "Jane Doe"
    assert updated_quote.repair_description == "Repair car"
    assert updated_quote.price == 200.0

def test_delete_quote():
    generator = QuoteGenerator()
    generator.create_quote("John Doe", "Repair car", 100.0)
    generator.delete_quote(0)
    try:
        generator.get_quote(0)
        assert False, "Quote not found exception expected"
    except IndexError:
        assert True

def test_generate_quote():
    generator = QuoteGenerator()
    generator.create_quote("John Doe", "Repair car", 100.0)
    quote = generator.generate_quote(0)
    assert json.loads(quote) == {
        "customer_name": "John Doe",
        "repair_description": "Repair car",
        "price": 100.0
    }

def test_get_quote_out_of_range():
    generator = QuoteGenerator()
    try:
        generator.get_quote(0)
        assert False, "Quote not found exception expected"
    except IndexError:
        assert True

def test_update_quote_out_of_range():
    generator = QuoteGenerator()
    try:
        generator.update_quote(0)
        assert False, "Quote not found exception expected"
    except IndexError:
        assert True

def test_delete_quote_out_of_range():
    generator = QuoteGenerator()
    try:
        generator.delete_quote(0)
        assert False, "Quote not found exception expected"
    except IndexError:
        assert True

def test_generate_quote_out_of_range():
    generator = QuoteGenerator()
    try:
        generator.generate_quote(0)
        assert False, "Quote not found exception expected"
    except IndexError:
        assert True
