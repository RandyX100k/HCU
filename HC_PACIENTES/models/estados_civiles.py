# -*- coding:utf-8 -*-
from  odoo import  models,fields

class EstadosCiviles(models.Model):
    _name = "estados.civiles"
    name = fields.Char(string="Estado civil")