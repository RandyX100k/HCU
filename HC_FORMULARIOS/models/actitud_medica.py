# -*- coding:utf-8 -*-
from  odoo import  models , fields


class EvaluacionMedica(models.Model):
    _name = 'actitud.medica'
    _description = 'Evaluación médica del trabajador'

    #form_id
    form_id = fields.Many2one("inicio.3",string="Form")
    form_id_1 = fields.Many2one("inicio.1")
    certificado_id = fields.Many2one("certificado.model",string="Certificado")
    periodica_2_id_ = fields.Many2one("periodica.1")
    reintegro_id = fields.Many2one("reintegro.form")

    # Aptitud - Solo uno puede ser True
    apto = fields.Boolean(string="Apto")
    apto_observacion = fields.Boolean(string="Apto en observación")
    apto_limitaciones = fields.Boolean(string="Apto con limitaciones")
    no_apto = fields.Boolean(string="No apto")

    # Comentarios
    observacion = fields.Text(string="Observación")
    limitacion = fields.Text(string="Limitación")
