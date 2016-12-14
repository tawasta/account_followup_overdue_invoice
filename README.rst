.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========================
Overdue invoices management
===========================

Add overdue payments and fees to customer invoices.


Installation
============

Install the module form Settings->Local Modules

Configuration
=============
After installation you should decide the payments that will be used.

Default follow-up payments
--------------------------
1. Go to Accounting->Configuration->Follow-up->Follow-up Levels
2. Select (or create) the record for your company
3. Select the desired default payments for overdue invoices:
    - **Use overdue interest**: add an interest invoice total amount, based on the selected interest percent, invoice total amount and overdue days.
    - **Use overdue payment**: add a fixed overdue payment for overdue invoice.
    - **Use debt collection fee**: add a fixed deb collection fee for overdue invoice.
    - The *overdue payment* and *debt collection fee* are functionally the same, and can be used simultaneously.
4. Set up the desired "Payment term on followups"
    - Immediate payment is recommended here
    - This will be used on reminder invoices and to calculate the new due date
    - Leave this empty to use the original payment term on the invoice
5. Setup the desired Follow-Up Actions, if you want to make use of automated/mass follow-up collection.

.. image:: account_followup_overdue_invoice/static/description/settings.png
   :alt: Followup settings


The configuration above is optional. You can also setup the follow-up payments in each invoice.
Using any of these additional payments should be informed to the customer in the original invoice.

Invoice-specific follow-up payments
-----------------------------------
The follow-up payments can be added and edited in each invoice separately.

After payment terms, there are selections for each supported follow-up payment.
These are fetched automatically from your default follow-up payments, but can be enabled or disabled for specific invoices. The amount can also be altered, but this isn't recommended because the payment must be informed to the customer in the original invoice.

.. image:: account_followup_overdue_invoice/static/description/invoice.png
   :alt: Invoice settings


Invoice templates
-----------------
**Important:** You should inform your customers about using any of these additional payments in the original invoice or in the contract conditions. This may also be required by the laws in the operating country. This module **will not** add any conditions to be shown to the customer about the payment of your invoices.

**Please follow all laws and regulations in your country when using follow-up payments.**

Usage
=====
You can create overdue payments for invoices manually, or with automated wizard. The manual approach is recommended to prevent unintended operations.

Creating reminder invoices manually
-----------------------------------
1. Go to Accounting -> Customer Invoices Overdue
    - Here you can see all the invoices that are overdue.
2. Click an invoice
3. Click "Reminder invoice" to create reminder invoice lines
    - You can't create a reminder invoice if the payment is less than 15 days late
4. Two things should happen:
    - Follow-up fees are added as invoice lines
    - Invoice due date is updated

.. image:: account_followup_overdue_invoice/static/description/reminder.png
   :alt: Invoice reminder

Creating reminder invoices automatically
----------------------------------------
1. Go to Accounting -> Payment Follow-up -> Send Letters and Emails
2. Click "Send emails and generate letters"
3. This should do the configured follow-up actions

Note that this action will also create all the other selected follow-up actions.
**Use with caution!**


Known issues / Roadmap
======================
- Support multi-currencies
- Allow other "overdue"-settings than 15 days after due date
- Allow mass-create for reminder invoices

Credits
=======

Contributors
------------

* Aleksi Savijoki <aleksi.savijoki@tawasta.fi>
* Jarmo Kortetjärvi <jarmo.kortetjarvi@tawasta.fi>
* Kirsi Hirvonen <kirsi.hirvonen@tawasta.fi>
* Teemu Parto <teemu.parto@mindpolis.com>

Sponsors
--------
* Fuugin säätiö <https://fuug.fi/saatio/>

Images
------
Module icon made by `Gregor Cresnar <http://www.flaticon.com/authors/gregor-cresnar/>`_ from `www.flaticon.com <http://www.flaticon.com>`_. Licenced by `Creative Commons BY 3.0 <http://creativecommons.org/licenses/by/3.0/>`_


Maintainer
----------

.. image:: http://tawasta.fi/templates/tawastrap/images/logo.png
   :alt: Oy Tawasta OS Technologies Ltd.
   :target: http://tawasta.fi/

This module is maintained by Oy Tawasta OS Technologies Ltd.
