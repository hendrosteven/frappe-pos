# Copyright (c) 2025, Hendro Steven and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Order(Document):
    def on_submit(self):
        for line in self.order_line:
            product = frappe.get_doc("Product", line.product)
            if product.stock < line.quantity:
                frappe.throw(f"Not enough stock for {product.name}. Only {product.stock} left.")
            
            product.stock -= line.quantity
            product.save()