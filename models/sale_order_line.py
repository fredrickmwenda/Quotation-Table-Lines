# InvoiceLines/models/account_move_line.py
from odoo import models, fields, api

class SaleOrderLineCustom(models.Model):
    _inherit = 'sale.order.line'


    color = fields.Char(string="Colour")
    meters = fields.Float(string="Meters")
    vat = fields.Float(string="VAT (%)")
    discount = fields.Float(string="Discount (%)")
    computed_amount = fields.Float(string="Amount", compute="_compute_amount")

    @api.depends('meters', 'quantity', 'price_unit', 'discount')
    def _compute_amount(self):
        for line in self:
            base_amount = line.meters * line.quantity * line.price_unit
            discount_amount = base_amount * (line.discount / 100)
            line.computed_amount = base_amount - discount_amount

