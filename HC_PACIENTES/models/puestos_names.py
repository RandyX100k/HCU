# -*- coding:utf-8 -*-

from  odoo import  models , fields

class PuestosNames(models.Model):
    _name = "puestos.names"

    name = fields.Char("Nombre del puesto")