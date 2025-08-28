# -*- coding:utf-8 -*-
from odoo import  models , fields

class GruposSanguineros(models.Model):
    _name = "grupos.sanguineos"

    name = fields.Char(string="Grupo sanguineo")