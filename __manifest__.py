{
"name":"HMS Project",
"description":"Odoo project for hospital",
"depends": ["crm"],
"data":[
     "security/hms_security.xml",
      "security/ir.model.access.csv",
    "wizard/create_appointment_view.xml",
    "views/hms_patient_view.xml",
    "views/hms_department.xml",
     "views/hms_doctors.xml",
    "views/crm_inherit.xml"
     "reports/hms_patient_templet.xml",
     "reports/hms_patient_report.xml"
     ]

}