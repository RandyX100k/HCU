# -*- coding:utf-8 -*-
from  odoo import  models , fields

class MotivosDiagnosticos(models.Model):
    _name = "motivos.diagnosticos"

    name = fields.Char(string="Motivo diagnostico")
