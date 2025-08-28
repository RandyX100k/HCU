# -*- coding:utf-8 -*-
from odoo import models, fields, api
from  datetime import  date

class PacientesHC(models.Model):
    _name = "pacientes.hc"
    _description = "Historial Clínico del Paciente"
    _rec_name = "nombre_completo"

    nombre_completo = fields.Char(string="Nombre completo", compute="_compute_nombre_completo", store=True)
    primer_apellido = fields.Char(string="Primer apellido", tracking=True)
    segundo_apellido = fields.Char(string="Segundo apellido")
    primer_nombre = fields.Char(string="Primer nombre")
    segundo_nombre = fields.Char(string="Segundo nombre")
    sexo = fields.Selection([
        ('M', 'Masculino'),
        ('F', 'Femenino')
    ], string="Sexo")
    edad = fields.Integer(string="Edad", compute="_compute_edad", store=True)
    religion_id = fields.Many2one("religiones.hc", string="Religión")
    grupo_sanguineo = fields.Many2one("grupos.sanguineos", string="Grupo sanguíneo")

    lateralidad = fields.Selection(
        [
            ('derecho','Derecho'),
            ('zurdo','Zurdo'),
            ('ambidextro','Ambidextro')
        ],
        string="Lateralidad")

    instruccion_id = fields.Many2one("instruccion.names",string="Instrucción")
    estado_civil = fields.Many2one("estados.civiles", string="Estado civil")
    profesion_id = fields.Many2one("profesion.names",string="Profesión")
    lugar_nacimiento = fields.Char(string="Lugar de nacimiento")
    fecha_nacimieto = fields.Date(string="Fecha de nacimiento")
    ocupacion_id = fields.Many2one("ocupaciones.names",string="Ocupación")
    tel = fields.Char(string="Número de celular")
    direccion = fields.Text(string="Dirección")
    orientacion_sexual = fields.Many2one("orientacion.sexual", string="Orientación sexual")
    identidad_genero = fields.Many2one("identidad.genero", string="Identidad de género")

    discapacidad = fields.Selection([
        ('si', 'Sí'),
        ('no', 'No')
    ], string="¿Tiene discapacidad?")
    tipo_discapacidad = fields.Char(string="Tipo de discapacidad")
    porcentaje = fields.Integer(string="% de discapacidad")
    fecha_ingreso = fields.Date(string="Fecha de ingreso al trabajo")
    puesto_trabajo_id = fields.Many2one("puestos.names",string="Puesto de trabajo (CIUO)")
    area_trabajo_id = fields.Many2one("areas.trabajos",string="Área de trabajo")
    actividades_trabajo = fields.Char(string="Actividades relevantes del puesto")
    antecedente_trabajo_ids = fields.One2many(
        "antecedente.trabajo",
        "paciente_id",
        string="Antecedentes laborales"
    )

    @api.depends('fecha_nacimieto')
    def _compute_edad(self):
        for rec in self:
            if rec.fecha_nacimieto:
                today = date.today()
                rec.edad = today.year - rec.fecha_nacimieto.year - (
                        (today.month, today.day) < (rec.fecha_nacimieto.month, rec.fecha_nacimieto.day)
                )
            else:
                rec.edad = 0

    @api.depends('primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido')
    def _compute_nombre_completo(self):
        for rec in self:
            nombres = filter(None, [rec.primer_nombre, rec.segundo_nombre])
            apellidos = filter(None, [rec.primer_apellido, rec.segundo_apellido])
            rec.nombre_completo = " ".join(apellidos) + ", " + " ".join(
                nombres) if rec.primer_apellido or rec.segundo_apellido else " ".join(nombres)

    def form_inicios(self):
        return{
            'type': 'ir.actions.act_window',
            'name': 'Evaluación Médica',
            'res_model': 'inicio.1',
            'view_mode': 'form',
            'view_id': self.env.ref('HC_FORMULARIOS.view_form_inicio_1').id,
            'target': 'current',
            'context':{'default_paciente_id':self.id}
        }

    def certificado(self):
        return {
        'type': 'ir.actions.act_window',
        'name': 'Certficados',
        'res_model': 'certificado.model',
        'view_mode':'form',
        'view_id': self.env.ref('HC_FORMULARIOS.view_certificado_model_form').id,
        'target': 'current',
        }

    def periodica(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Periodica',
            'res_model':'periodica.1',
            'view_mode': 'form',
            'view_id': self.env.ref('HC_FORMULARIOS.view_form_periodica_1').id,
            'target': 'current',
            'context': {'default_paciente_id': self.id}
        }

    def reintegro(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Reintegro',
            'res_model': 'reintegro.form',
            'view_mode':'form',
            'view_id': self.env.ref('HC_FORMULARIOS.view_form_reintegro_form').id,
            'target': 'current',
        }

    def retiro(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Retiro',
            'res_model': 'retiro.1',
            'view_mode': 'form',
            'view_id': self.env.ref('HC_FORMULARIOS.retiro_1_form_view').id,
            'target': 'current'
        }

    def inmunizaciones(self):
        return {
            'type' : 'ir.actions.act_window',
            'name': 'inmunizaciones',
            'res_model': 'registro.inmunizacion',
            'view_mode': 'form',
            'view_id': self.env.ref('HC_FORMULARIOS.view_registro_inmunizacion_form').id,
            'target': 'current'
        }