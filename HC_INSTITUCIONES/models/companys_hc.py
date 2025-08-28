# -*- coding:utf-8 -*-
from  odoo import  models , fields
from odoo.api import ValuesType, Self


class Companyshc(models.Model):
    _name = "companys.hc"
    imagen = fields.Binary(string="Logo / Imagen")
    name = fields.Char(string="Institucion o nombre de la empresa")
    ruc = fields.Char(string="Numero RUC")
    ciiu = fields.Char("Numero CIIU")
    establecimiento = fields.Many2one("res.company",string="Establecimiento de saludo",
                                      default= lambda self: self.env.company)
    numero_historia_clinica = fields.Char("Numero de historia clinica")
    numero_archivo = fields.Char(string="Numero de archivo")


    def create(self, vals_list: list[ValuesType]) -> Self:
        if vals_list['name']:
            self.env['res.partner'].create({
                'name': vals_list['name'],
                'vat': vals_list['vat'] if 'vat' in vals_list else ''
            })

        return super().create(vals_list)

    def write(self, vals):
        for rec in self:
            # Buscar partner con el mismo nombre y RUC si existe
            partner = self.env['res.partner'].search([
                ('name', '=', rec.name),
                ('vat', '=', rec.ruc)
            ], limit=1)

            if partner:
                partner.write({
                    'name': vals.get('name', rec.name),
                    'vat': vals.get('ruc', rec.ruc)
                })
        return super().write(vals)
