# Copyright (c) 2025, Yash Gholap and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Expense(Document):
	def validate(self):
		self.set("splits",[])

		group = frappe.get_doc("Expense Group", self.group)
		members = [row.users for row in group.members]
		
		if not members:
			frappe.throw("Expnse Group must have atleast one member")
		per_head = self.amount / len(members)
		
		for user in members:
			self.append("splits", {
				"user": user,
				"share_amount": per_head
			})
