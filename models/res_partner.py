# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
import openerp.addons.decimal_precision as dp

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class ResPartner(models.Model):
    
    # 1. Private attributes
    _inherit = 'res.partner'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.model
    def do_overdue_invoices(self):
        overdue_invoices_count = 0
        for record in self:
            overdue_invoices = self.env['account.invoice'].search([
                ('partner_id', '=', record.id),
                ('date_due', '<', 'now()')
            ])

            for invoice in overdue_invoices:
                if not invoice.overdue:
                    continue

                invoice.action_overdue_invoice()
                overdue_invoices_count += 1

        return overdue_invoices_count
