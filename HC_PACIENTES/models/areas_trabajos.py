# -*- coding:utf-8 -*-
from  odoo import  models , fields

class AreasTrabajos(models.Model):
    _name = "areas.trabajos"

    name = fields.Char(string="Areas trabajos")