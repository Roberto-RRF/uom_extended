from odoo import models, fields, api
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = 'stock.move.line'

    ref = fields.Char(string='Lote Fabricación')
    fecha_de_fabricacion = fields.Date(string="Fecha de fabricacion")
    metro_lineal_original = fields.Float(string="Metro Lineal Original")


    # Metodo re-definido para que se creen los valores nuevos en el lote
    def _prepare_new_lot_vals(self):
        self.ensure_one()
        return {
            'name': self.lot_name,
            'product_id': self.product_id.id,
            'company_id': self.company_id.id,
            'ref':self.ref,
            'fecha_de_fabricacion':self.fecha_de_fabricacion,
            'metro_lineal_original':self.metro_lineal_original,
        }