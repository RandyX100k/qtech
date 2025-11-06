from odoo import models, fields, api

class SaleCustom(models.Model):
    _inherit = "sale.order"

    view_btn_apply_change = fields.Boolean(string="View Apply Change", default=False)

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for record in res:
            record.apply_margen()
        return res

    def write(self, vals):
        res = super().write(vals)
        self.apply_margen()
        return res

    def apply_margen(self):
        for record in self:
            margen = record.pricelist_id.margen or 0.0
            for line in record.order_line:
                base_price = line.product_id.list_price
                line.price_unit = base_price * (1 + margen / 100)
            record.view_btn_apply_change = False
