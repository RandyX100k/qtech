from odoo import models , fields,api

class SaleCustom(models.Model):
    _inherit = "sale.order"
    
    
    def write(self,vals):
        if "pricelist_id" in vals:
            price_list = vals.get("pricelist_id")
            
            list_price = self.env["product.pricelist"].browse(price_list)
            margen = list_price.margen
            
            if margen > 0:
                #calculate the price in order
                for record in self:
                    for line in record.order_line:
                        without_itbis = (line.price_unit / 100) * margen +  line.price_unit
                        # with_itbis = without_itbis * 1.18
                        line.price_unit = without_itbis
                        
            
        return super().write(vals)