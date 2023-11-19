from odoo import api, fields, models

from odoo import api, fields, models, _


class besialemployee(models.Model):
    _inherit = 'hr.employee'
    _description = "Besial Employees"

    store_ids = fields.Many2many('besial.store', string='Concerned stores', groups="hr.group_hr_user")
    # extending the odoo base model hr.employee to add a Many2many for Stores

    # When an employee is created it creates a user and assigns it the concerned group
    @api.model_create_multi
    def create(self, values):
        employee = super(besialemployee, self).create(values)

        # Check if the employee already has a user
        if not employee.user_id:
            user_values = {
                'name': employee.name,
                'login': employee.work_email,
                'employee_ids': [(6, 0, [employee.id])],
                'groups_id': [(4, self.env.ref('base.group_user').id)]
            }

            user = self.env['res.users'].create(user_values)
            employee.write({'user_id': user.id})

        return employee

'''
    # Redefine the stores_ids_shops field with the same structure as hr.employee
    stores_ids_shops = fields.Many2many(
        'besial.store',  # Replace 'besial.store' with the actual model name
        string="Stores"
    )
'''


