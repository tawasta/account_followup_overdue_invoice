# -*- coding: utf-8 -*-

# 1. Standard library imports:
from datetime import date
from datetime import datetime

# 2. Known third party imports:

# 3. Odoo imports (openerp):
from openerp import api, fields, models
from openerp import _
import openerp.addons.decimal_precision as dp

# 4. Imports from Odoo modules:

# 5. Local imports in the relative form:

# 6. Unknown third party imports:


class AccountInvoice(models.Model):
    
    # 1. Private attributes
    _inherit = 'account.invoice'

    # 2. Fields declaration
    overdue = fields.Boolean("Overdue", compute='_compute_overdue', default=False)
    date_due_count = fields.Integer("Overdue days", compute='_compute_date_due_count')

    use_overdue_interest = fields.Boolean(
        "Use overdue interest",
        compute='compute_use_overdue_interest',
        default=lambda self: self.compute_use_overdue_interest(),
        store=True
    )
    overdue_interest = fields.Float(
        "Overdue interest",
        digits=dp.get_precision('Discount'),
        default=lambda self: self._default_overdue_interest()
    )

    use_overdue_payment= fields.Boolean(
        "Use overdue payment",
        compute='compute_use_overdue_payment',
        default=lambda self: self.compute_use_overdue_payment(),
        store=True
    )
    overdue_payment = fields.Float(
        "Overdue payment",
        digits=dp.get_precision('Product price'),
        default=lambda self: self._default_overdue_payment()
    )

    use_debt_collection_fee = fields.Boolean(
        "Use debt collection fee",
        compute='compute_use_debt_collection_fee',
        default=lambda self: self.compute_use_debt_collection_fee(),
        store=True
    )
    debt_collection_fee = fields.Float(
        "Debt collection fee",
        digits=dp.get_precision('Product price'),
        default=lambda self: self._default_debt_collection_fee()
    )

    # 3. Default methods
    def _default_overdue_interest(self):
        followup = self.get_account_followup()

        return followup.overdue_interest

    def _default_overdue_payment(self):
        followup = self.get_account_followup()

        return followup.overdue_payment

    def _default_debt_collection_fee(self):
        followup = self.get_account_followup()

        return followup.debt_collection_fee

    # 4. Compute and search fields, in the same order that fields declaration
    @api.depends('date_due_count')
    def _compute_overdue(self):
        for record in self:
            if record.state == 'open' and record.date_due_count >= 15:
                record.overdue = True
            else:
                record.overdue = False

            return record.overdue

    @api.depends('date_due', 'state')
    def _compute_date_due_count(self):
        for record in self:
            if not record.date_due:
                return False

            due_date = datetime.strptime(record.date_due, "%Y-%m-%d").date()
            today = date.today()

            overdue = (today - due_date).days

            if overdue > 0:
                record.date_due_count = overdue

    @api.depends('payment_term')
    def compute_use_overdue_interest(self):
        followup = self.get_account_followup()

        for record in self:
            if record.payment_term and followup.use_overdue_interest:
                record.use_overdue_interest = True

    @api.depends('payment_term')
    def compute_use_overdue_payment(self):
        followup = self.get_account_followup()

        for record in self:
            if record.payment_term and followup.use_overdue_payment:
                record.use_overdue_payment = True

    @api.depends('payment_term')
    def compute_use_debt_collection_fee(self):
        followup = self.get_account_followup()

        for record in self:
            if record.payment_term and followup.use_debt_collection_fee:
                record.use_debt_collection_fee = True

    # 5. Constraints and onchanges

    # 6. CRUD methods

    # 7. Action methods
    @api.multi
    def action_overdue_invoice(self):
        invoice_line = self.env['account.invoice.line']

        for record in self:
            record.action_cancel()
            record.action_cancel_draft()

            product_overdue_interest = self.env.ref('account_followup_overdue_invoice.overdue_interest') or False
            product_overdue_payment = self.env.ref('account_followup_overdue_invoice.overdue_payment') or False
            product_deb_collection_fee = self.env.ref('account_followup_overdue_invoice.deb_collection_fee') or False

            if record.use_overdue_interest:
                daily_interest = record.overdue_interest / 365 / 100
                price_unit = daily_interest * record.date_due_count * record.amount_untaxed

                # Write existing overdue interest line to prevent invoicing the same interest multiple times
                existing_line = record.invoice_line.search([
                    ('invoice_id', '=', record.id),
                    ('product_id', '=', product_overdue_interest.id)],
                )
                if existing_line:
                    invoice_line.write({'price_unit': price_unit})
                else:
                    invoice_line_values = {
                        'invoice_id': record.id,
                        'product_id': product_overdue_interest.id,
                        'name': product_overdue_interest.name,
                        'price_unit': price_unit,
                    }

                    invoice_line.create(invoice_line_values)

            if record.use_overdue_payment:
                quantity = 1

                # Remove existing overdue payment and add it to new line quantity
                existing_line = record.invoice_line.search([
                    ('invoice_id', '=', record.id),
                    ('product_id', '=', product_overdue_payment.id)
                ], limit=1)

                invoice_line_values = {
                    'price_unit': record.overdue_payment,
                    'quantity': quantity
                }

                if existing_line:
                    quantity += existing_line.quantity
                    invoice_line_values['quantity'] = quantity

                    invoice_line.write(invoice_line_values)
                else:
                    invoice_line_values['invoice_id'] = record.id
                    invoice_line_values['product_id'] = product_overdue_payment.id
                    invoice_line_values['name'] = product_overdue_payment.name

                    invoice_line.create(invoice_line_values)

            if record.use_debt_collection_fee:
                quantity = 1

                # Remove existing debt collection fee and add it to new line quantity
                existing_line = record.invoice_line.search([
                    ('invoice_id', '=', record.id),
                    ('product_id', '=', product_deb_collection_fee.id)
                ], limit=1)

                invoice_line_values = {
                    'price_unit': record.debt_collection_fee,
                    'quantity': quantity
                }

                if existing_line:
                    quantity += existing_line.quantity
                    invoice_line_values['quantity'] = quantity

                    invoice_line.write(invoice_line_values)
                else:
                    invoice_line_values['invoice_id'] = record.id
                    invoice_line_values['product_id'] = product_deb_collection_fee.id
                    invoice_line_values['name'] = product_deb_collection_fee.name

                    invoice_line.create(invoice_line_values)

            account_followup = record.env['account_followup.followup'].search([
                ('company_id', '=', record.company_id.id)
            ], limit=1)

            if account_followup.followup_payment_term:
                record.payment_term = account_followup.followup_payment_term

            try:
                date_due = record.payment_term.compute(value=1)[0][0][0]
                record.date_due = date_due
            except:
                # Can't update due date. This shouldn't happen
                continue

            record.invoice_validate()

    # 8. Business methods
    def get_account_followup(self):
        followup = self.env['account_followup.followup'].search(
            [('company_id', '=', self.default_get(['company_id'])['company_id'])],
            limit=1,
        )

        return followup
