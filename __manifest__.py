# -*- coding: utf-8 -*-
{
    'name': "fichier",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',

                'crm',
                'hr',
                'calendar',
                'sale',


                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/templates.xml',
        'views/patient.xml',
        'views/calendar_meetings.xml',
        'views/payement.xml',
        'views/consultation.xml',
        'views/menu.xml',
        'views/acte.xml',
        'views/medicament.xml',
        'views/ordonnance.xml',
        'reports/report.xml',
        'reports/report_ordonnance.xml',
     

        'reports/template_header.xml',

        'views/ordonnanceligne.xml',









    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}