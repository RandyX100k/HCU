# -*- coding:utf-8 -*-
from  odoo import  models , fields , api
# -*- coding:utf-8 -*-
from odoo import models, fields

class ColumnaExtremidades(models.Model):
    _name = "columna.extremidades"
    _description = "Evaluación de Columna y Extremidades"

    form_id = fields.Many2one("inicio.3", string="Formulario clínico")
    form_id_1 = fields.Many2one("inicio.1", string="Formulario clínico")
    periodica_2_id_ = fields.Many2one("periodica.1")
    reintegro_id = fields.Many2one("reintegro.form")
    retiro_2_id = fields.Many2one("retiro.2")

    signos_ids = fields.Many2one("signos.clinicos",string="Signos clinicos")
    patologia = fields.Boolean(string="Patologia?")
    descripcion = fields.Text(string="Descripcion")


    @api.onchange('patologia')
    def _onchage_patologia(self):
        if not self.patologia:
            self.descripcion = "SIN PATLOLOGIA"
        else:
            self.descripcion = "TIENE PATOLOGIA"