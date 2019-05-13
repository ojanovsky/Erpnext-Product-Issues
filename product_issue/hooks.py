# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "product_issue"
app_title = "Product Issue"
app_publisher = "Alarex-Group s.r.o."
app_description = "Add connection between Issue and product entity with serial number"
app_icon = "octicon octicon-file-directory"
app_color = "orange"
app_email = "ondrej.janovsky@alarex.cz"
app_license = "MIT"

fixtures = [
    {
	"doctype": "Custom Field",
        "filters":{
	    "name": ["in", ("Issue-product_serial_no",
                            "Serial No-issues",
                            "Serial No-section_break_12")]
	}
    }
#    {
#	"doctype": "Custom Script",
#	"filters": {
#	    "name":["in", "Issue-Client"]
#	}
#    },
]



# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/product_issue/css/product_issue.css"
# app_include_js = "/assets/product_issue/js/product_issue.js"

# include js, css files in header of web template
# web_include_css = "/assets/product_issue/css/product_issue.css"
# web_include_js = "/assets/product_issue/js/product_issue.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
#zde se uvadi odkazy na jednotlive doctype a k nim lze pripojit javascripty s uzivatelskymi funkcemi misto definice v custom_script
#vyhodou je, ze muze byt k jednomu doctype jeden customscript, ale tato metoda to neomezuje, takze ruzne aplikace
#mohou definovat ke stejnemu doctype sve funkce
#!!!!nutno provest pri zmenach bench restart
doctype_js = {"Issue" : "custom/issue/issue.js","Serial No" : "custom/issue/serialno.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "product_issue.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "product_issue.install.before_install"
# after_install = "product_issue.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "product_issue.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"product_issue.tasks.all"
# 	],
# 	"daily": [
# 		"product_issue.tasks.daily"
# 	],
# 	"hourly": [
# 		"product_issue.tasks.hourly"
# 	],
# 	"weekly": [
# 		"product_issue.tasks.weekly"
# 	]
# 	"monthly": [
# 		"product_issue.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "product_issue.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "product_issue.event.get_events"
# }

