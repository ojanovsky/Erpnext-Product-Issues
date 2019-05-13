from __future__ import unicode_literals
import frappe

from product_issues import ProductIssues
@frappe.whitelist()
def mojefunc():
    return "hellooooooooooooooooooooooooooooo"
@frappe.whitelist()
def save_serial_connect(issue, serialno=None):
    """
    it save pair info serial no. and issue name
    """
    
    #doc = frappe.get_doc("Product Issues", "howno") 
    if (serialno != None):
        
            
            if (frappe.db.count("Product Issues", filters={"issue":issue})==0):                   
                doc = frappe.get_doc({
                         "doctype": "Product Issues",
                         "issue":issue,
                         "parent": serialno,
                         "parenttype":"Serial No",
                         "parentfield":"issues"
                         })
                doc.insert(ignore_permissions=True)        
                return 1
            else:            
                old_serial = frappe.get_value("Product Issues",filters={"issue":issue},fieldname=["parent"])

                if (old_serial==serialno):
                    return 1                
                return 0
      