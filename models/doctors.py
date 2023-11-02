from odoo import models,fields

class Doctors(models.Model):
    _name = "hms.doctor"

    first_name = fields.Char(string="Fname")
    last_name = fields.Char(string="Lname")
    image = fields.Binary()