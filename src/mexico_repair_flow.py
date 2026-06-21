from dataclasses import dataclass
from typing import List

@dataclass
class User:
    name: str
    role: str

@dataclass
class Quote:
    id: int
    revenue: float

class MexicoRepairFlow:
    def __init__(self):
        self.users = []
        self.quotes = []
        self.tier = 'Basic'

    def upgrade_to_team_tier(self):
        if self.tier == 'Basic' and len(self.quotes) >= 5:
            self.tier = 'Team'
            self.users.extend([User('Collaborator 1', 'Collaborator'), User('Collaborator 2', 'Collaborator'), User('Admin', 'Admin')])

    def add_quote(self, quote: Quote):
        self.quotes.append(quote)

    def get_reporting_dashboard(self):
        if self.tier == 'Team':
            revenue = sum(quote.revenue for quote in self.quotes)
            return {'revenue': revenue, 'quote_stats': len(self.quotes)}
        else:
            return None

    def get_user_seats(self):
        return len(self.users)
