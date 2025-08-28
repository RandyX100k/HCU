# -*- coding:utf-8 -*-
from  odoo import  models , fields

class ProfesionNames(models.Model):
    _name = "profesion.names"

    name = fields.Char(string="Nombre de la profesion")