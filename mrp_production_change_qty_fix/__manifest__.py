# Copyright 2020 Sergio Corato <https://github.com/sergiocorato>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'MRP Production Change Qty Fix',
    'version': '12.0.1.0.0',
    'development_status': 'Beta',
    'license': 'AGPL-3',
    'category': 'Manufacturing',
    'author': 'Sergio Corato, '
              'Odoo Community Association (OCA)',
    'website': 'https://github.com/OCA/manufacture',
    'description': 'Fix non-removed lines in MO where sub-bom or its components are '
                   'removed.',
    'depends': [
        'mrp',
    ],
    'installable': True,
}
