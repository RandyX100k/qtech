from odoo import models , fields, api

class SaleCustom(models.Model):
    _inherit = "sale.order"
    
    view_btn_apply_change = fields.Boolean()
        
    @api.onchange("pricelist_id")
    def _onchange_pricelist(self):
        for record in self:
            if record.pricelist_id:
                if record.pricelist_id.margen > 0:
                    record.view_btn_apply_change = True
                
                else:
                    record.view_btn_apply_change = False
    
    
    def apply_margen(self):
        for record in self:
            margen = record.pricelist_id.margen
            for line in record.order_line:
                without_itbis = (line.price_unit / 100) * margen +  line.price_unit
                line.price_unit = without_itbis

        self.view_btn_apply_change = False
