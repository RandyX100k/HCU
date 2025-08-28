# -*- coding:utf-8 -*-
from  odoo import  models, fields

class Regiones_types(models.Model):
    _name = "regiones.types"
    name = fields.Char(string="Region")
