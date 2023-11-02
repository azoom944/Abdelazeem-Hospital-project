from odoo import models,fields,api


class Create_wizard(models.TransientModel):
    _name = "create.appointment"


    name = fields.Char(required=True)
    patient = fields.Many2one("hms.patient", required=True)


    def create_appointment_action(self):
        print("Done!")


