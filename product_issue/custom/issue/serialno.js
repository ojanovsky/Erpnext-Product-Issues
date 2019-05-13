/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

frappe.ui.form.on("Serial No", "refresh", function (frm, page) {
    $.each(frm.doc.issues, function (i, d) {
        //read all related issues and set subject and status in table
        frappe.call({
            method: "frappe.client.get",
            args: {
                doctype: "Issue",
                name: d.issue,
            },
            async: false,
            callback(r) {
                if (r.message) {
                    var task = r.message;
                    frappe.model.set_value(d.doctype, d.name, "subject", r.message.subject);
                    frappe.model.set_value(d.doctype, d.name, "status", r.message.status);
                    frappe.model.set_value(d.doctype, d.name, "idx", i + 1);
                }
            }
        });
    });
});
