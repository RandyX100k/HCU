# -*- coding:utf-8 -*-
from email.policy import default

from  odoo import  models , fields , api

class Retiro_2(models.Model):
    _name = "retiro.2"

    name = fields.Char(string="Numero",default="Borrador")

    retiro_1_id = fields.Many2one("retiro.1",string="Retiro 1")

    columna_extremidades_ids = fields.One2many("columna.extremidades", "retiro_2_id",
                                               string="Columna y Extremidades")

    #resultados examenes
    resultado_examen_ids = fields.One2many("resultado.examenes", "retiro_2_id",
                                           string="RESULTADOS DE EXAMENES")

    # examen diagnosticos
    examens_diagnosticos_ids = fields.One2many("motivo.diagnostico", "retiro_2_id",
                                               string="K.DIAGNOSTICO")
    observaciones_evaluacion = fields.Char(string="Observaciones")

    #evaluacion_medica
    realizo_evaluacion = fields.Selection([
        ('si', 'Sí'),
        ('no', 'No'),
    ], string="¿Se realizó la evaluación?")

    observaciones_examen = fields.Char(string="Observaciones")

    # recomendaciones
    recomendaciones_ids = fields.One2many("recomendaciones.tratamientos",
                                          "retiro_2_id", string="Recomendaciones")

    # datos del profesional
    fecha_datos = fields.Date(string="Fecha", default=fields.Date.today())
    hora = fields.Char(string="Hora")
    profesional_id = fields.Many2one("profesionales.doctores", string="Nombre y apellidos")
    codigo = fields.Char(string="Codigo", compute="_check_profesional_id", store=True)
    firma_sello = fields.Binary(string="Firma y sello")

    # firma del usuario
    firma_user = fields.Binary(string="Firma usuario")


    @api.onchange('retiro_1_id')
    def _onchange_retiro_id(self):

        if not self.retiro_1_id.reintegro_id:
            return

        reintegro = self.retiro_1_id.reintegro_id
        self.profesional_id = reintegro.profesional_id
        self.firma_sello = reintegro.firma_sello

        self.firma_user = reintegro.firma_user

        self.columna_extremidades_ids = [(5,0,0)]

        colums = []

        for colum in reintegro.columna_extremidades_ids:
            colums.append((0,0,{
                'signos_ids': colum.signos_ids.id,
                'patologia':colum.patologia,
                'descripcion': colum.descripcion
            }))

        self.columna_extremidades_ids = colums

    @api.model_create_multi
    def create(self, vals):
        for record in vals:
            if not record.get('name') or record['name'] == 'Borrador':
                record['name'] = self.env['ir.sequence'].next_by_code('RETI2')
        return super().create(vals)

    @api.depends('profesional_id')
    def _check_profesional_id(self):
        for record in self:
            record.codigo = record.profesional_id.code