# -*- coding:utf-8 -*-
from email.policy import default

from  odoo import  models , fields

class Inmunizaciones(models.Model):
    _name = "inmunizaciones.ids"

    inmunizacion_id = fields.Many2one("registro.inmunizacion")

    vacuna_id = fields.Many2one("vacunas.names",string="Vacuna")
    dosis = fields.Char(string="Dosis")

    fecha = fields.Date(string="Fecha",default=fields.Date.today())
    lote = fields.Char(string="Lote")
    esquema_full = fields.Boolean(string="ESQUEMA COMPLETO MARCAR")
    responsable_id = fields.Many2one("profesionales.doctores"
                                     ,string="Nombres completos de la responsable")
    establecimiento_salud = fields.Many2one("res.company",string="Establecimiento salud",
                                            default=lambda self: self.env.user.company_id.id)

    observaciones = fields.Char(string="Observaciones")