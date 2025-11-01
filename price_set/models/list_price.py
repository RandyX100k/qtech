from odoo import models , fields

class ListPriceCustom(models.Model):
    _inherit = "product.pricelist"
    
    margen = fields.Float(string="Margen %")
    
    
    