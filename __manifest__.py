# -*- coding: utf-8 -*-
{
    "name": "Caravans history",
    "description": """
        Интерфейс взаимодействия с внешними приложениями
    """,
    "author": "Dessan Hemrayev",
    "website": "https://erpsmart.ru",
    "category": "",
    "version": "15.0.1.0.0",
    "license": "LGPL-3",
    "depends": ["website_sale", "website_blog", "components"], 
    "data": [
        'security/ir.model.access.csv',
        'views/history_add.xml',
        'views/history_edit.xml',
        'views/blog_post.xml',
    ],
    "assets": {
        'web.assets_frontend': [
            "/caravans_history/src/js/add_history.js"
        ],
    },
    "auto_install": False,
    "installable": True,
    "application": False,
}
