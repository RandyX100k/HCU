# -*- coding:utf-8 -*-
from  odoo import  models , fields

class EvaluacionMedica(models.Model):
    _name = "evaluacion.medica"

    certificado_id = fields.Many2one("certificado.model", string="Certificado")

    realizo_evaluacion = fields.Selection([
        ('si', 'Sí'),
        ('no', 'No'),
    ], string="¿Se realizó la evaluación?")

    condicion_diagnostico = fields.Selection([
        ('presuntiva', 'Presuntiva'),
        ('definitiva', 'Definitiva'),
        ('no_aplica', 'No aplica'),
    ], string="Condición del diagnóstico")

    relacionada_trabajo = fields.Selection([
        ('si', 'Sí'),
        ('no', 'No'),
        ('no_aplica', 'No aplica'),
    ], string="¿Relacionado con el trabajo?")