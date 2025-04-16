# Copyright (c) 2025, Hendro Steven and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _


class Customer(Document):
	def validate(self):
		# validate email if email is set with frappe email validator
		if self.email and not frappe.utils.validate_email_address(self.email):
			frappe.throw(_("Email {0} is not valid").format(self.email))
			
		
