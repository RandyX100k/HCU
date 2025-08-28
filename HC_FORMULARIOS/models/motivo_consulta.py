# -*- coding:utf-8 -*-
from  odoo import  models , fields

class MotivoConsulta(models.Model):
    _name = "motivo.consulta"
    periodica_id = fields.Many2one("periodica.1")
    motivo = fields.Text(string="Motivo Consulta")