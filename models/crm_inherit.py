from odoo import models, fields, api
from odoo.exceptions import UserError


class CustomerWithPatient(models.Model):
    _inherit = "res.partner"

    related_patient_id = fields.Many2one('hms.patient')
    vat = fields.Char(required=True)
    # web_sit = fields.String()
    patient_email = fields.Char(related="related_patient_id.email")

    def unlink(self):
        for record in self:
            if len(self.related_patient_id) != 0:
                raise UserError('you cant remove that')
            else:
                return super().unlink()

    # @api.constrains('email')
    # def email_validation(self):
    #     if 'email' in self:
    #         search = self.search['patient_email', '=', 'email']
    #         if search:
    #             raise UserError('the email is existed')
