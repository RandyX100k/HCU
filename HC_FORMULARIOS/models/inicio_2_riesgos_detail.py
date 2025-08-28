# -*- coding:utf-8 -*-
from  odoo import  models , fields

class RiesgosDetails(models.Model):
    _name = "riesgos.inicio_2"

    name = fields.Char(string="Riesgo")