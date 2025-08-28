# -*- coding:utf-8 -*-
from  odoo import  models , fields

class Inicio_2_Riesgos_2(models.Model):
    _name = "inicio.2.riesgos.2"

    form_id = fields.Many2one("inicio.2",string="form")
    form_id_1 = fields.Many2one("inicio.1")

    periodica_1_id = fields.Many2one("periodica.1")
    puesto_id = fields.Many2one("puestos.names",string="Puesto de trabajo")
    actividades = fields.Char(string="Actividades")
    #tipo
    typo_riesgos = fields.Many2one("tipos.riesgos",string="Tipo riesgo")
    #riesgos
    riesgo = fields.Many2many("riesgos.inicio_2",string="Riesgo")
    medidas_preventiva = fields.Text(string="Medidas preventiva")