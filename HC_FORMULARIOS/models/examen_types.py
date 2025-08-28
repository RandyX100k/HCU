# -*-coding:utf-8 -*-
from  odoo import  models,fields

class ExamanesTypes(models.Model):
    _name = "examenes.types"

    name = fields.Char(string="Examen")