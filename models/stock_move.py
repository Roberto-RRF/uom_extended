from odoo import models, fields, api
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = 'stock.move'


    millares = fields.Float(string='Millar(es)', compute='_compute_millares', store=False)
    millares_visible = fields.Boolean(string="Field Millar(es) invisible", compute="_compute_millares_visible", store=False)

    @api.depends('product_uom_qty','product_id')
    def _compute_millares(self):
        for record in self:
            if record.product_id.product_cosal == 'hoja':
                for uom in record.product_id.secondary_uom_ids:
                    if uom:
                        record.millares = uom.factor_inv/ record.product_uom_qty
                        break
            else:
                record.millares = None

    @api.depends('product_id')
    def _compute_millares_visible(self):
        for record in self:
            if record.product_id.product_cosal == 'hoja':
                record.millares_visible= True
            else:
                record.millares_visible= False