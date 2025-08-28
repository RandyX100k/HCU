# -*- coding:utf-8 -*-

from  odoo import  models , fields

class OcupacionesNames(models.Model):
    _name = "ocupaciones.names"

    name = fields.Char(string="Ocupaciones")