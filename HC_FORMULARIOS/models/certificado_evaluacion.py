# -*- coding:utf-8 -*-
from  odoo import  models , fields,api

class CertificadoEvaluacio(models.Model):
    _name = "certificado.evaluacion"
    #form_id
    form_id = fields.Many2one("certificado.model",string="Form")

    #evaluaciones
    ingreso = fields.Boolean(string="Ingreso")
    periodico = fields.Boolean(string="Periodico")
    reintegro = fields.Boolean(string="Reintegro")
    retiro = fields.Boolean(string="Retiro")