# -*- coding:utf-8 -*-
from  odoo import  models,fields

class OrganosSistema(models.Model):
    _name = "organos.sistemas"
    form_id = fields.Many2one("inicio.2",string="Form_id")
    form_id_1 = fields.Many2one("inicio.1")
    periodica_2_id_ = fields.Many2one("periodica.1")

    organo_sistema_ = fields.Many2one("organos.sistemas_names",string="Organo o sistema")
    patologia = fields.Boolean(string="Con patologia?")
