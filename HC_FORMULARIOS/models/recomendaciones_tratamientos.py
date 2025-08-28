# -*- coding:utf-8 -*-

from  odoo import  models , fields

class RecomendacionesTratamientos(models.Model):
    _name = "recomendaciones.tratamientos"
    form_id = fields.Many2one("inicio.3",string="Form")
    form_id_1 = fields.Many2one("inicio.1")
    certificado_id = fields.Many2one("certificado.model",string="Certificado")
    periodica_2_id_ = fields.Many2one("periodica.1")
    reintegro_id = fields.Many2one("reintegro.form")
    retiro_2_id = fields.Many2one("retiro.2")

    recomendacion = fields.Text(string="Recomendacion")
    observacion = fields.Text(string="Observacion")


