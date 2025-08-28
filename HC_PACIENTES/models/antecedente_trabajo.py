# -*- coding:utf-8 -*-
from  odoo import  models , fields

class AntecedenteTrabajo(models.Model):
    _name = "antecedente.trabajo"
    _description = "Antecedentes laborales del paciente"

    paciente_id = fields.Many2one("pacientes.hc", string="Paciente", ondelete="cascade")

    empresa = fields.Many2one("companys.hc",string="Empresa")
    puesto_trabajo = fields.Many2one("puestos.names",string="Puesto de trabajo")
    actividades = fields.Text(string="Actividades que desempeñaba")
    tiempo = fields.Integer(string="Tiempo de trabajo (meses)")

    riesgo_fisico = fields.Boolean(string="Físico")
    riesgo_mecanico = fields.Boolean(string="Mecánico")
    riesgo_quimico = fields.Boolean(string="Químico")
    riesgo_biologico = fields.Boolean(string="Biológico")
    riesgo_ergonomico = fields.Boolean(string="Ergonómico")
    riesgo_psicosocial = fields.Boolean(string="Psicosocial")

    observaciones = fields.Text(string="Observaciones")
