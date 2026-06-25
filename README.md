# Mexico Repair Flow
A simple customer information management system.

## Usage
1. Create a customer: `customer_manager.create_customer("John Doe", "john@example.com")`
2. Get a customer: `customer_manager.get_customer(1)`
3. Update a customer: `customer_manager.update_customer(1, name="Jane Doe", email="jane@example.com")`
4. Search customers: `customer_manager.search_customers(name="John Doe")`
5. Save customers to JSON: `customer_manager.save_to_json("customers.json")`
6. Load customers from JSON: `customer_manager.load_from_json("customers.json")`
