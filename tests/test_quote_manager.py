import pytest

from quote_manager import QuoteManager, ServiceItem, Quote


@pytest.fixture
def manager():
    return QuoteManager()


def test_create_quote_happy_path(manager):
    service_items = [
        {"description": "Oil change", "price": 29.99},
        {"description": "Brake pads", "price": 120.0},
    ]
    quote = manager.create_quote(
        vehicle_make="Toyota",
        vehicle_model="Corolla",
        vehicle_year=2020,
        service_items=service_items,
    )
    assert isinstance(quote, Quote)
    assert quote.id == 1
    assert quote.vehicle_make == "Toyota"
    assert quote.vehicle_model == "Corolla"
    assert quote.vehicle_year == 2020
    assert len(quote.service_items) == 2
    assert quote.total_price == pytest.approx(149.99)
    # Ensure it is stored
    stored = manager.list_quotes()
    assert stored == [quote]


def test_create_quote_with_serviceitem_objects(manager):
    items = [
        ServiceItem(description="Tire rotation", price=40),
        ServiceItem(description="Battery check", price=15.5),
    ]
    quote = manager.create_quote(
        vehicle_make="Ford",
        vehicle_model="Focus",
        vehicle_year=2018,
        service_items=items,
    )
    assert quote.total_price == pytest.approx(55.5)
    assert manager.list_quotes()[0] is quote


def test_create_quote_invalid_year_raises(manager):
    with pytest.raises(ValueError) as exc:
        manager.create_quote(
            vehicle_make="Honda",
            vehicle_model="Civic",
            vehicle_year=1800,  # too early
            service_items=[{"description": "Filter", "price": 20}],
        )
    assert "Vehicle year" in str(exc.value)


def test_create_quote_empty_service_items_raises(manager):
    with pytest.raises(ValueError) as exc:
        manager.create_quote(
            vehicle_make="Nissan",
            vehicle_model="Sentra",
            vehicle_year=2022,
            service_items=[],
        )
    assert "At least one service item" in str(exc.value)


def test_create_quote_negative_price_raises(manager):
    with pytest.raises(ValueError) as exc:
        manager.create_quote(
            vehicle_make="Chevrolet",
            vehicle_model="Impala",
            vehicle_year=2019,
            service_items=[{"description": "Engine tune", "price": -50}],
        )
    assert "cannot be negative" in str(exc.value)
