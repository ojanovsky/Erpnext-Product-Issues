frappe.ui.form.on("Issue", "after_save", function (frm, page) {    
    frappe.call({
        method: "product_issue.product_issue.doctype.product_issues.api.save_serial_connect",
        args: {
            "serialno": frm.doc.product_serial_no,
            "issue": frm.doc.name
        },
        callback: function (r) {
            if (r.message==0) {
                msgprint("U hlášení problému nelze změnit sériové číslo výrobku!","Pozor");
            }
        }
    });
    if (frm.doc.product_serial_no!=null && frm.doc.product_serial_no.length>0)cur_frm.set_df_property("product_serial_no","read_only",1);
})

frappe.ui.form.on("Issue","refresh", function (frm, page){
    
    if(frm.doc.product_serial_no!=null && frm.doc.product_serial_no.length>0) cur_frm.set_df_property("product_serial_no","read_only",1);
})

