# -*- coding: utf-8 -*-

# 1. Standard library imports:

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class AccountJournal(models.Model):
    
    # 1. Private attributes
    _inherit = 'account.journal'

    # 2. Fields declaration

    # 3. Default methods

    # 4. Compute and search fields, in the same order that fields declaration

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods

    # 8. Business methods
    @api.model
    def _sale_journal_allow_cancel(self):
        # Set sale journal(s) as cancellable

        sale_journals = self.search([('type', '=', 'sale')])

        sale_journals.write({'update_posted': True})


