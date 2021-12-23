//Copyright (c) 2021, RICL and contributors
//For license information, please see license.txt

frappe.ui.form.on('Lead Alignment', {
	
	//refresh: function(frm) {
	//	frm.trigger("set_label");
	//},
	
	onload: function(frm) {
		if(frm.is_new()){
			var lead = frm.doc.lead;
			set_lead_details(frm,lead);
			if(lead){
				return frappe.call({
						method: 'ricl.royal_impact_certificate_ltd.doctype.lead_alignment.lead_alignment.getAddress',
						args: {
							"lead": lead,
						},
						callback: function(r){
							if(r.message){
								cur_frm.set_value("customer_address", r.message);
							}
						}	
				});
			}
		}
	},


});

const set_lead_details = function(frm,lead){
	const options = {name: lead};
	const fields = ['lead_name','designation','department','email_id','contact_number','notes'];
	frappe.db.get_value('Lead', options, fields).then(({ message }) => {
		if(message){
			alert(message.lead_name);
			frm.set_value('lead_name', message.lead_name);
			frm.set_value('designation', message.designation);
			frm.set_value('department', message.department);
			frm.set_value('email_id', message.email_id);
			frm.set_value('contact_number', message.contact_number);
			frm.set_value('notes', message.notes);
		}
	});
}