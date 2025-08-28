# -*-coding:utf-8 -*-
from odoo import  models , fields

class SignosClinicos(models.Model):
    _name = "signos.clinicos"

    name = fields.Char(string="Signos clinicos")