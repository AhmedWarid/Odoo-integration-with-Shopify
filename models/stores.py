from odoo import api , fields, models, _
from odoo.exceptions import ValidationError
import re
from random import randint

class ShopifyStore(models.Model):

    _name = "besial.store"
    _inherit = ['mail.thread', 'avatar.mixin', 'resource.mixin']
    _description = "stores records"
    def _get_default_color(self):
        return randint(1, 11)


    user_id = fields.Many2one('res.users', 'User', related='resource_id.user_id', store=True, readonly=False)

    name = fields.Char(string='name', required=True, tracking=True)
    store_url = fields.Char(string='URL', tracking=True)
    store_type = fields.Selection(
        [('fashion', 'Fashion'), ('electronics', 'Electronics'), ('other', 'Other')],
        string='Niche',
    )
    status = fields.Selection(
        [('active', 'Active'), ('inactive', 'Inactive'), ('maintenance', 'Under Maintenance'),
         ('pending', 'Pending Shopify Approval')],
        string='Status',
        default='active',
    )
    active = fields.Boolean(default='True')
    ref = fields.Char(string='Reference', default=lambda self: _('New'))
    shopify_instance_id = fields.Many2one('shopify.instance', string='Shopify Instance')
    color = fields.Integer(string='Color Index', default=_get_default_color)


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('besial.store')
        return super(ShopifyStore, self).create(vals_list)
    @api.depends('name', 'user_id.avatar_128', 'image_128')
    def _compute_avatar_128(self):
        super()._compute_avatar_128()

    @api.depends('name', 'user_id.avatar_1920', 'image_1920')
    def _compute_avatar_1920(self):
        super()._compute_avatar_1920()

    @api.depends('name', 'user_id.avatar_1024', 'image_1024')
    def _compute_avatar_1024(self):
        super()._compute_avatar_1024()

    @api.depends('name', 'user_id.avatar_512', 'image_512')
    def _compute_avatar_512(self):
        super()._compute_avatar_512()

    @api.constrains('store_url')
    def _check_store_url(self):
        for record in self:
            # Define the regex pattern for a valid URL (this is a basic example)
            pattern = r'^[a-zA-Z0-9.-]+\.[a-z]{2,}$'

            # Check if the URL matches the regex pattern
            if record.store_url and not re.match(pattern, record.store_url):
                raise models.ValidationError('Invalid URL format. Please use a valid URL.')
