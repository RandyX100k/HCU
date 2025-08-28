# -*- coding:utf-8 -*-
from odoo import  models,fields


class OrganosSistemasNames(models.Model):
    _name = "organos.sistemas_names"
    _rec_name = "name_organo_sistema"

    name_organo_sistema = fields.Char(string="Organo o sistema")
