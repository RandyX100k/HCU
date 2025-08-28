# -*- coding:utf-8 -*-
from odoo import  models , fields, api

class MotivoDiagnostico(models.Model):
    _name = "motivo.diagnostico"

    form_id = fields.Many2one("inicio.3",string="Form")
    periodica_2_id_ = fields.Many2one("periodica.1")
    reintegro_id = fields.Many2one("reintegro.form")
    retiro_2_id = fields.Many2one("retiro.2")
    form_id_1 = fields.Many2one("inicio.1")

    motivo = fields.Char(string="Motivo diagnostico", compute="_compute_motivo", store=True)


    cie_id = fields.Many2one("ciie.10",string="Ciie")

    pref = fields.Boolean(string="PREF")

    def_ = fields.Boolean(string="DEF")

    @api.depends('cie_id')
    def _compute_motivo(self):
        for record in self:
            record.motivo = record.cie_id.enfermedad if record.cie_id else False


