# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
import openerp.addons.decimal_precision as dp

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class AccountFollowupPrint(models.TransientModel):
    
    # 1. Private attributes
    _inherit = 'account_followup.print'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.model
    def process_partners(self, partner_ids, data):
        res = super(AccountFollowupPrint, self).process_partners(partner_ids=partner_ids, data=data)

        overdue_invoices_created = 0

        for partner in self.env['account_followup.stat.by.partner'].browse(partner_ids):
            if partner.max_followup_id.overdue_invoice:
                overdue_invoices_created += partner.partner_id.do_overdue_invoices()

        res['resulttext'] += "<p>%s overdue invoices created</p>" % overdue_invoices_created

        return res
