# Copyright (c) 2022, Vinicius Roque and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
#test

class CadastrodeColaboradores(Document):
	def before_save(self):
		self.full_name = f'{self.first_name} {self.last_name or ""}'
	pass
