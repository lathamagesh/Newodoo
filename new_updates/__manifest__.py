{
    'name': 'new updates',
    'version': '1.0.0',
    'sequence': -10,
    'summary': 'Removing tax for Sale and Purchase, inventory adjustment serial number auto generator',
    'description': """  This module helps to Removing tax for Sale and Purchase,
                        Inventory adjustment reference Number auto generating,
                        if store quantity greater than on hand Quantity will rise validation error. 
                        """,
    'license': 'OPL-1',
    'category': 'Stock',
    'author': 'Jagadish-->JETZERP',
    'website': '',
    'images': [],
    "depends": [
        "mrp", "sale",
        "sale_stock",
        "report_xlsx",
        "purchase",'stock', 'account', "mrp",
    ],
    'data': [
        'data/data.xml',
        'views/remove_tax_in_sale.xml',
        'views/web_backend_css.xml',
    ],
    'images': [
        'static/description//home/icon.png',
        'static/description//home/banner.png',
    ],
    # 'pre_init_hook':'pre_init_check',
    'installable': True,
    'application': True,
    'auto_install': False,
}