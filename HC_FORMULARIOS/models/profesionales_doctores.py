# -*- coding:utf-8 -*-
from  odoo import models, fields

class ProfesionalesDoctores(models.Model):
    _name = "profesionales.doctores"
    _rec_name = "name_full"

    name_full = fields.Char("Nombre y Apellido")
    code = fields.Char(string="Codigo")