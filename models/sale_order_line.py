# InvoiceLines/models/account_move_line.py
from odoo import models, fields, api

class SaleOrderLineCustom(models.Model):
    _inherit = 'sale.order.line'

    colour = fields.Char(string="Colour")
    meters = fields.Float(string="Meters")
    computed_amount = fields.Float(string="Amount", compute="_compute_amount", store=True)

    @api.depends('meters', 'product_uom_qty', 'price_unit')
    def _compute_amount(self):
        for line in self:
            line.computed_amount = line.meters * line.product_uom_qty * line.price_unit
            line.price_subtotal = line.computed_amount  # Set price_subtotal to computed_amount


