# -*- coding:utf-8 -*-
from  odoo import models , fields , api

class ActividadesLaborales(models.Model):
    _name = "actividades.laborales"

    form_id = fields.Many2one("inicio.2")
    form_id_1 = fields.Many2one("inicio.1")

    actividad = fields.Char("Actividad")