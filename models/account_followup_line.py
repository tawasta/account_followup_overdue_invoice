# -*- coding: utf-8 -*-

# 1. Standard library imports:
from datetime import date
from datetime import datetime

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
import openerp.addons.decimal_precision as dp

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class AccountFollowupLine(models.Model):
    
    # 1. Private attributes
    _inherit = 'account_followup.followup.line'

    # 2. Fields declaration
    overdue_invoice = fields.Boolean(
        "Create overdue invoice",
        help="Create invoice with selected extra payment rows",
        default=False,
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
