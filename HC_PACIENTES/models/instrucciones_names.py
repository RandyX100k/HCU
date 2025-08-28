# -*- coding:utf-8 -*-
from  odoo import  models,fields

class InstruccionesNames(models.Model):
    _name = "instruccion.names"

    name = fields.Char(string="Nombre")