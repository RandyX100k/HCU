# -*- coding:utf-8 -*-
from odoo import  models , fields

class OrientacionSexual(models.Model):
    _name = "orientacion.sexual"

    name = fields.Char(string="Orientacion sexual")