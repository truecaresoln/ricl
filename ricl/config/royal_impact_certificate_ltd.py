from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
    return[
        {
            "label": _("Human Resource"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Employee",
                    "onboard": 1,
                    "label": _("Employee"),
                    "description": _("Employee"),
                },
                {
                    "type": "doctype",
                    "name": "Employment Type",
                    "onboard": 1,
                    "label": _("Employment Type"),
                    "description": _("Employment Type"),
                },
                {
                    "type": "doctype",
                    "name": "Branch",
                    "onboard": 1,
                    "label": _("Branch"),
                    "description": _("Branch"),
                },
                {
                    "type": "doctype",
                    "name": "Department",
                    "onboard": 1,
                    "label": _("Department"),
                    "description": _("Department"),
                },
                {
                    "type": "doctype",
                    "name": "Designation",
                    "onboard": 1,
                    "label": _("Designation"),
                    "description": _("Designation"),
                },                          
            ]
        },
         {
            "label": _("CRM"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Lead",
                    "onboard": 1,
                    "label": _("Lead"),
                    "description": _("Lead"),
                },
                {
                    "type": "doctype",
                    "name": "Lead Alignment",
                    "onboard": 1,
                    "label": _("Lead Alignment"),
                    "description": _("Lead Alignment"),
                },
                {
                    "type": "doctype",
                    "name": "Quotation",
                    "onboard": 1,
                    "label": _("Quotation"),
                    "description": _("Quotation"),
                },
                {
                    "type": "doctype",
                    "name": "Lead Source",
                    "onboard": 1,
                    "label": _("Lead Source"),
                    "description": _("Lead Source"),
                },                  
                                        
            ]
        },
        {
            "label": _("Customer Information"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Customer Information Form",
                    "onboard": 1,
                    "label": _("CIF"),
                    "description": _("Customer Information Form"),
                },
                {
                    "type": "doctype",
                    "name": "Customer",
                    "onboard": 1,
                    "label": _("Customer"),
                    "description": _("Customer"),
                },
                {
                    "type": "doctype",
                    "name": "Contact",
                    "onboard": 1,
                    "label": _("Contact"),
                    "description": _("Contact"),
                },            
                                        
            ]
        },
        {
            "label": _("Accounting"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Company",
                    "onboard": 1,
                    "label": _("Company"),
                    "description": _("Company"),
                },
                {
                    "type": "doctype",
                    "name": "Bank",
                    "onboard": 1,
                    "label": _("Bank"),
                    "description": _("Bank"),
                },
                {
                    "type": "doctype",
                    "name": "Bank Account",
                    "onboard": 1,
                    "label": _("Bank Account"),
                    "description": _("Bank Account"),
                },            
                                        
            ]
        },        
    ]                     