# -*- coding: utf-8 -*-
from  odoo import  models,fields

class Religiones(models.Model):
    _name = "religiones.hc"

    name = fields.Char(string="Religion")