{
    "name": "Besial Erp System",
    "version": "1.0",
    "category": "Custom/ERP",
    "summary": "Integrate Odoo ERP with Shopify for performance tracking, task management, and more.",
    "description": """
        This module integrates Odoo's ERP capabilities with Shopify e-commerce stores to enhance performance tracking, task management, and profitability analysis.
    """,
    "author": "Ahmed Warid - Emsi - Encadrée par Mme. REMMACH",

    "license": "AGPL-3",
    "depends": ["base",
                "sale",
                "hr",
                'base_setup',
                'mail',
                'resource',
                'web',
                'project',
                'pragtech_odoo_shopify_connector',
                ],
    "data": ['security/ir.model.access.csv',
             'data/sequence.xml',
             'views/menu.xml',
             'views/employee.xml',
             'views/stores.xml',
             'views/project.xml',
             'views/instance.xml',
             'views/product.xml',
             'views/operation.xml'],
    "demo": [],
    "installable": True,
    "application": True,
    "auto_install": False,
}

