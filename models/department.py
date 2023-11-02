from odoo import models,fields

class Department(models.Model):
    _name = "hms.department"

    name = fields.Char(string="Department Name")
    capacity = fields.Integer(string="Department Capacity")
    is_opend = fields.Boolean()
    patient_id = fields.One2many("hms.patient", "department_id")