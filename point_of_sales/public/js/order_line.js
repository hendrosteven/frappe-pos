frappe.ui.form.on('OrderLine', {
    product: function (frm, cdt, cdn) {
        let row = locals[cdt][cdn];
        if (row.product) {
            frappe.db.get_doc('Product', row.product).then(product => {
                // Set price
                frappe.model.set_value(cdt, cdn, 'price', product.price);
            });
        }
    }
});
