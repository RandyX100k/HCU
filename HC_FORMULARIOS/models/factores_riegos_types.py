# -*- coding:utf-8 -*-
from  odoo import  models , fields

class Factores_Riesgos_Types(models.Model):
    _name = "factores.riesgos.types"


    name = fields.Char(string="Tipo riesgo")