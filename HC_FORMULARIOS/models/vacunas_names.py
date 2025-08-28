# -*- coding:utf-8 -*-
from  odoo import  models , fields

class Vacunas(models.Model):
    _name = "vacunas.names"

    _rec_name = "vacuna_name"

    vacuna_name = fields.Char(string="Vacuna")