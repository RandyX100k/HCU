# -*- coding:utf-8 -*-
from email.policy import default

from odoo import models, fields, api


class Certificado(models.Model):
    _name = "certificado.model"

    name = fields.Char(string="Numero", default="Borrador")
    form_id = fields.Many2one("inicio.3", string="Inicio3")

    #institucion
    institucion_name = fields.Many2one(
        "companys.hc",
        string="Institucion del sistema o empresa"
    )

    ruc = fields.Char(string="RUC")
    ciiu = fields.Char(string="CIIU")
    establecimiento_salud = fields.Many2one("res.company", string="Establecimiento de Salud")
    historia_clinica = fields.Char(string="Número de Historia Clínica")
    numero_archivo = fields.Char(string="Número de Archivo")

    #paciente
    primer_apellido = fields.Char(string="Primer apellido")
    segundo_apellido = fields.Char(string="Segundo apellido")
    primer_nombre = fields.Char(string="Primer nombre")
    segundo_nombre = fields.Char(string="Segundo nombre")
    sexo = fields.Selection([('M', 'Masculino'), ('F', 'Femenino')], string="Sexo")
    puesto_trabajo_id = fields.Many2one("puestos.names",string="Puesto de trabajo")

    #DATOS GENERALES
    fecha_emision = fields.Date(string="Fecha de emision",default=fields.Date.today())

    #evaluaciones
    evaluacion_id = fields.One2many("certificado.evaluacion","form_id",
                                    string="Evaluacion")

    #aptitud medica laboral
    aptitudes_ids = fields.One2many("actitud.medica","certificado_id",
                                    string="APTITUD MÉDICA LABORAL")

    evaluacion_retiro_ids = fields.One2many(
        "evaluacion.medica",
        "certificado_id",
        string="Evaluación médica de retiro"
    )

    #recomendaciones
    recomendaciones_ids = fields.One2many("recomendaciones.tratamientos",
                                          "certificado_id",string="Recomendaciones")

    # datos del profesional
    fecha_datos = fields.Date(string="Fecha", default=fields.Date.today())
    hora = fields.Char(string="Hora")

    profesional_id = fields.Many2one("profesionales.doctores",string="Nombre y apellidos")
    codigo = fields.Char(string="Codigo")
    firma_sello = fields.Binary(string="Firma y sello")

    # firma del usuario
    firma_user = fields.Binary(string="Firma usuario")


    #llenado automatico
    @api.onchange('form_id')
    def _onchange_form_id(self):
        inicio1 = (
            self.form_id.form_inicio_2_id.form_01_id
            if self.form_id and self.form_id.form_inicio_2_id and self.form_id.form_inicio_2_id.form_01_id
            else None
        )
        if inicio1:
            # Institución
            self.institucion_name = inicio1.company_id
            self.ruc = inicio1.ruc
            self.ciiu = inicio1.ciiu
            self.establecimiento_salud = inicio1.establecimiento_salud
            self.historia_clinica = inicio1.historia_clinica
            self.numero_archivo = inicio1.numero_archivo

            # Paciente
            self.primer_apellido = inicio1.primer_apellido
            self.segundo_apellido = inicio1.segundo_apellido
            self.primer_nombre = inicio1.primer_nombre
            self.segundo_nombre = inicio1.segundo_nombre
            self.sexo = inicio1.sexo
            self.puesto_trabajo_id = inicio1.puesto_trabajo_id
        else:
            # Limpiar si no hay valores
            self.institucion_name = False
            self.ruc = False
            self.ciiu = False
            self.establecimiento_salud = False
            self.historia_clinica = False
            self.numero_archivo = False
            self.primer_apellido = False
            self.segundo_apellido = False
            self.primer_nombre = False
            self.segundo_nombre = False
            self.sexo = False
            self.puesto_trabajo_id = False

        # Copiar actitudes desde el form original
        nuevas_actitudes = []
        for actitud in self.form_id.actitudes_ids:
            nuevas_actitudes.append((0, 0, {
                'apto': actitud.apto,
                'apto_observacion': actitud.apto_observacion,
                'apto_limitaciones': actitud.apto_limitaciones,
                'no_apto': actitud.no_apto,
                'observacion': actitud.observacion,
                'limitacion': actitud.limitacion,
            }))
        self.aptitudes_ids = [(5, 0, 0)] + nuevas_actitudes

        # Copiar recomendaciones desde el form original
        nuevas_recomendaciones = []
        for rec in self.form_id.recomendaciones_ids:
            nuevas_recomendaciones.append((0, 0, {
                'recomendacion': rec.recomendacion
            }))
            self.recomendaciones_ids = [(5, 0, 0)] + nuevas_recomendaciones

        # Copiar recomendaciones desde el form original
        nuevas_recomendaciones = []
        for rec in self.form_id.recomendaciones_ids:
            nuevas_recomendaciones.append((0, 0, {
                'recomendacion': rec.recomendacion
            }))
        self.recomendaciones_ids = [(5, 0, 0)] + nuevas_recomendaciones

        # Copiar datos del profesional y firmas
        self.fecha_datos = self.form_id.fecha_datos
        self.hora = self.form_id.hora
        self.profesional_id = self.form_id.profesional_id.id
        self.codigo = self.form_id.codigo
        self.firma_sello = self.form_id.firma_sello
        self.firma_user = self.form_id.firma_user

    #LLENAR EL NAME
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Borrador') == 'Borrador':
                vals['name'] = self.env['ir.sequence'].next_by_code('CERT') or 'Borrador'
        return super().create(vals_list)

