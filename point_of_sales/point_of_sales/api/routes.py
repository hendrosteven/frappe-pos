import frappe
from frappe import _

def get_customers():
    """
    Fetches all customers from the database.
    """
    customers = frappe.get_all("Customer", fields=["name", "customer_name", "email","phone", "address"])
    return customers

def hello():
    return {"message": "Hello from custom API"}