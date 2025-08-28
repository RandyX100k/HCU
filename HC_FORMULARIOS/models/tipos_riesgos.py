# -*- coding:utf-8 -*-
from  odoo import  models , fields

class Tipos_riegos(models.Model):
    _name = "tipos.riesgos"
    name = fields.Char(string="Tipo riesgo")