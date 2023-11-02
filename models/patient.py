sfrom odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import re
from datetime import date, datetime

class HmsStudent(models.Model):
    _name = "hms.patient"

    first_name = fields.Char(string="Fname")
    last_name = fields.Char(string="Lname")
    birth_date = fields.Date(string="BD")
    history = fields.Html(string="Your illnes history")
    cr_ratio = fields.Float()
    blood_type = fields.Selection([('a', "A"), ('b', "B"), ('o+', "O+"), ('o-', "O-"), ('ab', "AB")])
    pcr = fields.Selection([('p', "positive"), ('n', "negative")])
    image = fields.Binary()
    adress = fields.Text()
    age = fields.Integer(compute="calc_age" , store=True)
    department_id = fields.Many2one("hms.department")
    doctor_id = fields.Many2many("hms.doctor")
    department_capacity = fields.Integer(related="department_id.capacity")
    created_by = fields.Char(default=lambda self: self.env.user.name,readonly=True)
    created_date = fields.Date(default=datetime.today(), readonly=True)
    describtion = fields.Text()
    states = fields.Selection([('u', 'Undetermined'), ('g', 'Good'), ('f', 'Fair'), ('s', 'Serious')], defult='u')
    pcr_check = fields.Boolean()
    email = fields.Char()




    @api.onchange("age")
    def _azoom(self):
     if self.age < 30 and self.age is not None :
        self.pcr_check = True
        return {
                'warning': {'title': "hello",
                               'message': "the pcr has checked"},
                 }

    @api.model
    def create(self, vals):
        if 'email' in vals:
            search = self.search([('email', '=', vals['email'])])
            if search:
                raise UserError('the email is existed')
            else:
                 if not re.match('(\w+[.|\w])*@(\w+[.])*\w+',vals['email'] ):
                   raise ValidationError("Wrong mail")
        return super().create(vals)


    def write(self, vals):
          if 'email' in vals:
            search = self.search([('email', '=', vals['email'])])
            if search:
                raise UserError('the email is existed')
            else:
                if not re.match('(\w+[.|\w])*@(\w+[.])*\w+', vals['email']):
                    raise ValidationError("Wrong mail")
          return super().write(vals)


    @api.depends("birth_date")
    def calc_age(self):
        if self.birth_date:
         today = date.today()
         self.age = today.year - self.birth_date.year -((today.month, today.day) < (self.birth_date.month, self.birth_date.day))



    def first_case(self):
         self.states = 'u'

    def second_case(self):
        self.states = 'g'

    def third_case(self):
        self.states = 'f'

    def fourth_case(self):
        self.states = 's'