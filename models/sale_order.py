from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('order_line.computed_amount')
    def _compute_amount_total(self):
        for order in self:
            order.amount_total = sum(line.computed_amount for line in order.order_line)