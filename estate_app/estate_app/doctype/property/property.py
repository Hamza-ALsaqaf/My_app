# Copyright (c) 2023, Hamza Alsaqaf and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Property(Document):
	def before_submit(self):
		pass
		# frappe.throw(_("Theis is an error Maseges"))
		# frappe.throw(f"you are not allowed to save this {self.name} ")
	def before_save(self):
		pass

