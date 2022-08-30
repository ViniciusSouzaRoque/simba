# Copyright (c) 2022, Vinicius Roque and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class CadastrodeColaboradores(Document):
	def before_save(self):
		self.full_name = f'{self.nome} {self.sobrenome or ""}'
	pass
