# -*- coding:utf-8 -*-

from  odoo import  models , fields

class FactoresRiesgos(models.Model):
    _inherit = "actividades.laborales"

    retiro_1_id = fields.Many2one("retiro.1")

    factores_riesgos_id = fields.Many2one("factores.riesgos.types",string="Factores riesgos")
