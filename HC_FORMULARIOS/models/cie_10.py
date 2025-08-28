# -*- coding:utf-8 -*-
from  odoo import models , fields

class Ciie_10(models.Model):
    _name = "ciie.10"
    _rec_name = "code"

    code = fields.Char(string="Ciie")
    enfermedad = fields.Char(string="Enfermedad")