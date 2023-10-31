# -*- coding: utf-8 -*-
{
    'name': 'Employee Contact',
    'version': '16.0.1.0',
    'author': 'Tag Hassan',
    "support": "tag.hassann@gmail.com",
    'category': 'Human Resources',
    'depends': ['hr'],
    'summary': 'Employee Contact',
    'description': """
        Employee Contact
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/hr_employee_views.xml',
        'views/hr_views.xml',
    ],
    'application': True,
    "auto_install": False,
    'installable': True,
    "images": ["static/description/icon.png"],
}
