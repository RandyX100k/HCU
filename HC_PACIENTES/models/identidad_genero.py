# -*- coding:utf-8 -*-
from  odoo import  models , fields

class IdentidadGenero(models.Model):
    _name = "identidad.genero"

    name = fields.Char(string="Identidad Genero")