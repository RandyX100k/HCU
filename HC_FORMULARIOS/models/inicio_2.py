# -*- coding:utf-8 -*-
from odoo import  models , fields , api
from odoo.api import ValuesType, Self


class Inicio_2(models.Model):
    _name = "inicio.2"
    _rec_name = "name"
    name = fields.Char(string="Numero",default="Borrador", readonly=True)
    #form01_id
    form_01_id = fields.Many2one("inicio.1",string="Inicio1")
    #ANTECEDENTES FAMILIARES
    enfermedad_cardio = fields.Boolean(string="Enferrmedad cardio-vascular")
    enfermedad_metabolidca = fields.Boolean(string="Enfermedad metabolica")
    enfermedad_neurologica = fields.Boolean(string="Enfermedad neurologica")
    enfermedad_oncologica = fields.Boolean(string="Enfermedad oncologica")

    #infeciosa . # hereditaria , discapacidades , otros
    enfermedad_infecciosa = fields.Boolean(string="Enfermedad infecciosa")
    enfermedad_hereditaria = fields.Boolean(string="Enfermedad hereditaria")
    discapacidad = fields.Boolean(string="Discapacidad")
    otra_enfermedad = fields.Boolean(string="Otras enfermedades")

    refiere = fields.Char(string="Refire")

    actividades_extras_laborales = fields.One2many("actividades.laborales","form_id_1",
                                                   string="Actividades Extras laborales")

    enfermedad_actual  = fields.Char(string="Enfermedad actual")

    #riegos
    riesgos_ids = fields.One2many("inicio.2.riesgos","form_id",string="Riesgos-1")
    riesgos_ids_2 = fields.One2many("inicio.2.riesgos.2","form_id",string="Riesgos-2")

    #actividades extras laborales
    #enfermedad_actual
    enfermedad_actual = fields.Text(string="Enfermedad actual")
    #revision actual
    organos_sistemas_ids = fields.One2many("organos.sistemas","form_id",
                                       string="Organos y sistemas")

    observacion_organos = fields.Char(string="SIN PATOLOGIA APARENTE")

    #contantes vitales
    presion_arterial = fields.Char(string="Presión Arterial")
    temperatura = fields.Float(string="Temperatura (°C)")
    frecuencia_cardiaca = fields.Integer(string="Frecuencia Cardíaca (lat/min)")
    saturacion_oxigeno = fields.Integer(string="Saturación de Oxígeno (%)")
    frecuencia_respiratoria = fields.Integer(string="Frecuencia Respiratoria (resp/min)")
    peso = fields.Float(string="Peso (kg)")
    talla = fields.Float(string="Talla (cm)")
    indice_masa_corporal = fields.Float(
        string="Índice de Masa Corporal (kg/m²)",
        compute="_compute_imc",
        store=True
    )
    perimetro_abdominal = fields.Float(string="Perímetro Abdominal (cm)")

    @api.depends('peso', 'talla')
    def _compute_imc(self):
        for record in self:
            if record.peso and record.talla:
                try:
                    talla_metros = record.talla / 100  # Convertir cm a metros
                    record.indice_masa_corporal = round(record.peso / (talla_metros ** 2), 2)
                except ZeroDivisionError:
                    record.indice_masa_corporal = 0
            else:
                record.indice_masa_corporal = 0

    @api.onchange('form_01_id')
    def _onchange_form_01(self):
        if self.form_01_id:
            self.riesgos_ids = [
                (5, 0, 0),
                (0, 0, {
                    'puesto_id': self.form_01_id.puesto_trabajo_id,
                    'actividades': self.form_01_id.actividades_trabajo,
                })
            ]
            self.riesgos_ids_2 = [
                (5, 0, 0),
                (0, 0, {
                    'puesto_id': self.form_01_id.puesto_trabajo_id,
                    'actividades': self.form_01_id.actividades_trabajo,
                })
            ]

    @api.model
    def create(self, vals_list: list[ValuesType]) -> Self:
        if vals_list.get('name', 'Borrador') == 'Borrador':
            vals_list['name'] = self.env['ir.sequence'].next_by_code('FORM002') or 'Borrador'
        return super().create(vals_list)


    def get_report_values(self, docids, data=None):
        docs = self.env['inicio.2'].browse(docids)

        riesgos_agrupados = {}

        for doc in docs:
            for r in doc.riesgos_ids:
                key = (r.puesto_id.name, r.actividades)
                if key not in riesgos_agrupados:
                    riesgos_agrupados[key] = {'FISICO': [], 'MECANICO': [], 'QUIMICO': []}
                tipo = r.typo_riesgos.name
                if tipo in riesgos_agrupados[key] and r.riesgo:
                    riesgos_agrupados[key][tipo].append(r.riesgo.name)

        return {
            'doc_ids': docids,
            'doc_model': 'inicio.2',
            'docs': docs,
            'riesgos_agrupados': riesgos_agrupados,
        }

