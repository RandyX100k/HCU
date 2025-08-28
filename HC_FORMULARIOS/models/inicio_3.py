# -*- coding:utf-8 -*-
from  odoo import  models , fields , api

class FormInicio3(models.Model):
    _name =  "inicio.3"

    name = fields.Char(string="Numero",default="Borrador")

    form_inicio_2_id = fields.Many2one("inicio.2",string="Inicio2")

    regiones_ids = fields.One2many("regiones.examen","form_id",
                                   string="Examen fisico y regional")
    #columnas y extremidades
    columna_extremidades_ids = fields.One2many(
        "columna.extremidades",
        "form_id",
        string="Columna y Extremidades"
    )

    #resultado de examamenes
    resultados_ids = fields.One2many("resultado.examenes",
                                     "form_id",string="Resultado examenes")



    #MOTIVO DIAGNOSTICO
    motivos_diagnosticos_ids = fields.One2many("motivo.diagnostico","form_id",
                                               string="Motivos diagnosticos")
    observaciones = fields.Text(string="Observaciones")
    #actitud medica
    actitudes_ids = fields.One2many("actitud.medica","form_id",
                                   string="Actitud medica para el trabajo")

    #recomendaciones o tratamientos
    recomendaciones_ids = fields.One2many("recomendaciones.tratamientos",
                                          "form_id",string="Recomendaciones o tratamientos")

    #datos del profesional
    fecha_datos = fields.Date(string="Fecha",default=fields.Date.today())
    hora = fields.Char(string="Hora")

    profesional_id = fields.Many2one("profesionales.doctores",string="Nombre y apellidos")
    codigo = fields.Char(string="Codigo",compute="_check_profesional_id",store=True)
    firma_sello = fields.Binary(string="Firma y sello")

    #firma del usuario
    firma_user = fields.Binary(string="Firma usuario")

    #create method
    @api.model
    def create(self, vals_list):
        if vals_list.get('name', 'Borrador') == 'Borrador':
            vals_list['name'] = self.env['ir.sequence'].next_by_code('FORM003') or 'Borrador'

        if vals_list.get('hora'):
            vals_list['hora'] = vals_list.get('hora') + 'HORAS'
        return super().create(vals_list)

    @api.depends('profesional_id')
    def _check_profesional_id(self):
        for record in self:
            record.codigo = record.profesional_id.code