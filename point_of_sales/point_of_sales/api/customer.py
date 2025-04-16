import frappe
from frappe import _
import json

@frappe.whitelist(allow_guest=False)  # or remove this line if you want to restrict access
def get_customers():
    """
    Fetches all customers from the database.
    """
    customers = frappe.get_all("Customer", fields=["name", "customer_name", "email","phone", "address"])
    return customers


@frappe.whitelist(allow_guest=False)  # or remove this line if you want to restrict access
def create_customer():
    """
    Creates a new customer in the database.
    """
    data = frappe.request.get_json()
    customer = frappe.get_doc({
        "doctype": "Customer",
        "customer_name": data.get("customer_name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "address": data.get("address")
    })
    
    customer.insert()
    frappe.db.commit()
    return {
        "status": "success",
        "message": _("Customer created successfully"),
        "customer_id": customer.name
    }
    
@frappe.whitelist(allow_guest=False)  # or remove this line if you want to restrict access
def get_customer_by_name():
    # gets the customer by name from query param
    customer_name = frappe.request.args.get('customer_name')
    if not customer_name:
        return {
            "status": "error",
            "message": _("Customer name is required")
        }
    customer = frappe.get_all("Customer", filters={"customer_name": customer_name}, fields=["name", "customer_name", "email","phone", "address"])
    if not customer:
        return {
            "status": "error",
            "message": _("Customer not found")
        }
    return {
        "status": "success",
        "customer": customer[0]
    }
    
    