# -*- coding:utf-8 -*-
from  odoo import  models , fields,api

class RegionesExamen(models.Model):
    _name = "regiones.examen"

    form_id = fields.Many2one("inicio.3",string="Form")
    form_id_1 = fields.Many2one("inicio.1")
    periodica_2_id_ = fields.Many2one("periodica.1")
    reintegro_id = fields.Many2one("reintegro.form")
    retiro_id = fields.Many2one("retiro.1")

    type_region = fields.Many2one("regiones.types",string="Region")
    type_subregion = fields.Many2one("subregiones.types",string="Subregion")
    patologia = fields.Boolean(string="Patologia?")
    descripcion = fields.Text(string="Observaciones")



    @api.onchange('patologia')
    def _onchage_patologia(self):
        if not self.patologia:
            self.descripcion = "SIN PATOLOGIA"

        else:
            self.descripcion = "TIENE PATOLOGIA"
