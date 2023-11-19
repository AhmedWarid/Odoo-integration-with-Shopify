from odoo import api , fields, models, _
from odoo.exceptions import ValidationError
import re
from random import randint


class project(models.Model):

    _inherit = ['project.task',]
    _description = "Project Management"

    employees_assigned = fields.Many2many('hr.employee')
    Store_concerned = fields.Many2one('besial.store')
