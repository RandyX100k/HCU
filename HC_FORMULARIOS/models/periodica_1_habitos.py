# -*- coding:utf-8 -*-
from  odoo import  models , fields

class PeriodicaHabitos(models.Model):
    _name = "periodica.habitos"

    periodica_id = fields.Many2one("periodica.1")


    tabaco = fields.Boolean(string="Tabaco")
    alcohol = fields.Boolean(string="Alcohol")
    otras_drogas = fields.Char(string="Otras drogas detalles")
    tiempo_consumo = fields.Integer(string="Tiempo de consumo (meses)")
    cantidad = fields.Integer(string="Cantidad")
    ex_consumidor = fields.Boolean(string="Ex consumidor")
    tiempo_abstinencia = fields.Integer(string="Tiempo abstiencia(meses)")

    #estilos
    actividad_fisica = fields.Boolean(string="Actividad fisica")
    mediciacion_habitual = fields.Boolean(string="Medicación habitual")
    estilo_vida_cual = fields.Char(string="¿Cuál?")
    tiempo_cantidad = fields.Integer(string="Tiempo / Cantidad")
