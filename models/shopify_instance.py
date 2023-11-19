from odoo import api, fields, models, _
from odoo.exceptions import UserError
import logging
import requests

_logger = logging.getLogger(__name__)


class ShopifyInstance(models.Model):
    _inherit = 'shopify.instance'

    besial_store_id = fields.One2many('besial.store', 'shopify_instance_id', string='Besial Store')

    def create_store_record(self):
        for instance in self:
            if instance.besial_store_id:
                # Store record already exists for this instance, do nothing
                continue

            # Create a new store record with the same name and URL as the Shopify instance
            store_obj = self.env['besial.store']
            store_vals = {
                'name': instance.name,
                'store_url': instance.shopify_host + '.myshopify.com',
                # You can set other fields as needed
                'shopify_instance_id': instance.id,
            }
            print('create multi method')
            store = store_obj.create(store_vals)

    @api.model
    def create(self, values):
        # Call the original create method
        instance = super(ShopifyInstance, self).create(values)

        # Create a store record
        print('create method')
        instance.create_store_record()

        return instance


