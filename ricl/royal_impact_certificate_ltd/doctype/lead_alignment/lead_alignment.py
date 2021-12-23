# -*- coding: utf-8 -*-
# Copyright (c) 2021, RICL and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class LeadAlignment(Document):
	pass

@frappe.whitelist()
def getAddress(lead):
	data = frappe.db.sql("""select ts.address_line1,ts.address_line2,ts.city,ts.state,
		ts.country,ts.pincode from `tabDynamic Link` tdl 
		left join `tabAddress` ts on tdl.parent=ts.name 
		WHERE tdl.link_name = '{0}';""".format(lead), as_dict = True)
	if data[0]["address_line1"]:
		address_line1 = data[0]["address_line1"]
	else:
		address_line1 = ''	
	if data[0]["address_line2"]:	
		address_line2 = ', '+data[0]["address_line2"]
	else:
		address_line2 = ''
	if data[0]["city"]:		
		city = ', '+data[0]["city"]
	else:
		city = ''
	if data[0]["state"]: 		
		state = ', '+data[0]["state"]
	else:
		state = ''
	if data[0]["country"]:		
		country = ', '+data[0]["country"]
	else:
		country = ''
	if data[0]["pincode"]:		
		pincode = ', '+data[0]["pincode"]
	else:
		pincode = ''	
	
	final_address = address_line1+address_line2+city+state+country+pincode
	return final_address
