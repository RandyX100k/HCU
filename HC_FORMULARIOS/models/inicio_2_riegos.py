# -*- coding:utf-8 -*-
from  odoo import  models , fields

class Inicio_2_Riesgos(models.Model):
    _name = "inicio.2.riesgos"

    form_id = fields.Many2one("inicio.2",string="form")
    periodica_id = fields.Many2one("periodica.1")
    form_id_1 = fields.Many2one("inicio.1")

    puesto_id = fields.Many2one("puestos.names",string="Puesto de trabajo")
    actividades = fields.Char(string="Actividades")
    typo_riesgos = fields.Many2one("tipos.riesgos",string="Tipo riesgo")
    riesgo = fields.Many2many("riesgos.inicio_2",string="Riesgo")