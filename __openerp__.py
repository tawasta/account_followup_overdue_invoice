# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Oy Tawasta OS Technologies Ltd.
#    Copyright 2016 Oy Tawasta OS Technologies Ltd. (http://www.tawasta.fi)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see http://www.gnu.org/licenses/agpl.html
#
##############################################################################

{
    'name': 'Overdue invoices management',
    'summary': 'Add overdue payments and fees to customer invoices',
    'version': '8.0.1.0.0',
    'category': 'Accounting & Finance',
    'website': 'http://www.tawasta.fi',
    'author': 'Oy Tawasta Technologies Ltd.',
    'license': 'AGPL-3',
    'application': False,
    'installable': True,
    'external_dependencies': {
        'python': [],
        'bin': [],
    },
    'depends': [
        'account',
        'account_cancel',
        'account_followup',
    ],
    'data': [
        'data/account_journal.xml',
        'data/product_template.xml',

        'views/account_followup_line_form.xml',
        'views/account_followup_line_tree.xml',
        'views/account_invoice_followup_form.xml',
        'views/account_invoice_form.xml',
        'views/account_invoice_tree.xml',
    ],
    'demo': [
    ],
}
