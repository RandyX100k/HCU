# -*- coding:utf-8 -*-
from odoo import  models , fields

class ResultadoExamenes(models.Model):
    _name = "resultado.examenes"
    form_id = fields.Many2one("inicio.3",string="Form")
    form_id_1 = fields.Many2one("inicio.1")
    periodica_2_id_ = fields.Many2one("periodica.1")
    reintegro_id = fields.Many2one("reintegro.form")
    retiro_2_id = fields.Many2one("retiro.2")

    examen_id = fields.Many2one("examenes.types",string="Examen")
    fecha = fields.Date(string="Fecha",default=fields.Date.today())
    resultado = fields.Text(string="Resultado")