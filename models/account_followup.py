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


class AccountFollowup(models.Model):
    
    # 1. Private attributes
    _inherit = 'account_followup.followup'

    # 2. Fields declaration
    use_overdue_interest = fields.Boolean("Use overdue interest", default=False)
    overdue_interest = fields.Float("Overdue interest %", digits=dp.get_precision('Discount'), default=8.50,)
    use_overdue_payment = fields.Boolean("Use overdue payment", default=False)
    overdue_payment = fields.Float("Overdue payment", digits=dp.get_precision('Product Price'), default=5.00)
    use_debt_collection_fee = fields.Boolean("Use debt collection fee", default=False)
    debt_collection_fee = fields.Float("Debt collection fee", digits=dp.get_precision('Product Price'), default=5.00)

    followup_payment_term = fields.Many2one(
        'account.payment.term',
        string='Payment term on followups',
        help='Leave empty to use the original payment term'
    )

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
