# -*- coding:utf-8 -*-
from  odoo import  models, fields

class Regiones_types(models.Model):
    _name = "subregiones.types"
    name = fields.Char(string="Region")
    region_id = fields.Many2one("regiones.types", string="Región padre")