from mexico_repair_flow import MexicoRepairFlow, Quote
import pytest

def test_upgrade_to_team_tier():
    flow = MexicoRepairFlow()
    flow.add_quote(Quote(1, 100.0))
    flow.add_quote(Quote(2, 200.0))
    flow.add_quote(Quote(3, 300.0))
    flow.add_quote(Quote(4, 400.0))
    flow.add_quote(Quote(5, 500.0))
    flow.upgrade_to_team_tier()
    assert flow.tier == 'Team'
    assert flow.get_user_seats() == 3

def test_get_reporting_dashboard():
    flow = MexicoRepairFlow()
    flow.add_quote(Quote(1, 100.0))
    flow.add_quote(Quote(2, 200.0))
    flow.add_quote(Quote(3, 300.0))
    flow.add_quote(Quote(4, 400.0))
    flow.add_quote(Quote(5, 500.0))
    flow.upgrade_to_team_tier()
    dashboard = flow.get_reporting_dashboard()
    assert dashboard['revenue'] == 1500.0
    assert dashboard['quote_stats'] == 5

def test_get_user_seats():
    flow = MexicoRepairFlow()
    flow.add_quote(Quote(1, 100.0))
    flow.add_quote(Quote(2, 200.0))
    flow.add_quote(Quote(3, 300.0))
    flow.add_quote(Quote(4, 400.0))
    flow.add_quote(Quote(5, 500.0))
    flow.upgrade_to_team_tier()
    assert flow.get_user_seats() == 3

def test_upgrade_to_team_tier_before_5_quotes():
    flow = MexicoRepairFlow()
    flow.add_quote(Quote(1, 100.0))
    flow.add_quote(Quote(2, 200.0))
    flow.add_quote(Quote(3, 300.0))
    flow.add_quote(Quote(4, 400.0))
    flow.upgrade_to_team_tier()
    assert flow.tier == 'Basic'
    assert flow.get_user_seats() == 0
