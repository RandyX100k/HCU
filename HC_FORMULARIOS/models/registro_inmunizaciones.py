# -*- coding:utf-8 -*-
from  odoo import  models , fields , api

class RegistroInmunizacion(models.Model):
    _name = "registro.inmunizacion"

    name = fields.Char(string="Name",default="Borrador")

    retiro_2_id = fields.Many2one("retiro.2")

    # institucion
    institucion_name = fields.Many2one(
        "companys.hc",
        string="Institucion del sistema o empresa"
    )

    ruc = fields.Char(string="RUC")
    ciiu = fields.Char(string="CIIU")
    establecimiento_salud = fields.Many2one("res.company", string="Establecimiento de Salud")
    historia_clinica = fields.Char(string="Número de Historia Clínica")
    numero_archivo = fields.Char(string="Número de Archivo")

    # paciente
    primer_apellido = fields.Char(string="Primer apellido")
    segundo_apellido = fields.Char(string="Segundo apellido")
    primer_nombre = fields.Char(string="Primer nombre")
    segundo_nombre = fields.Char(string="Segundo nombre")
    sexo = fields.Selection([('M', 'Masculino'), ('F', 'Femenino')], string="Sexo")
    fecha_inicio = fields.Date(string="Fecha inicio labores")
    fecha_salida = fields.Date(string="Fecha de salida")
    tiempo = fields.Integer(string="Tiempo(meses)")
    puesto_trabajo_id = fields.Many2one("puestos.names", string="Puesto de trabajo")


    inmunizaciones_ids = fields.One2many("inmunizaciones.ids","inmunizacion_id",
                                         string="INMUNIZACIONES")

    @api.onchange('retiro_2_id')
    def _onchange_retiro_2_id(self):
        if self.retiro_2_id:
            retiro_id = self.retiro_2_id.retiro_1_id
            self.institucion_name = retiro_id.institucion_name.id
            self.ruc = retiro_id.ruc
            self.ciiu = retiro_id.ciiu
            self.establecimiento_salud = retiro_id.establecimiento_salud.id
            self.historia_clinica = retiro_id.historia_clinica
            self.numero_archivo = retiro_id.numero_archivo
            self.primer_apellido = retiro_id.primer_apellido
            self.segundo_apellido = retiro_id.segundo_apellido
            self.primer_nombre = retiro_id.primer_nombre
            self.segundo_nombre = retiro_id.segundo_nombre
            self.sexo = retiro_id.sexo
            self.fecha_inicio = retiro_id.fecha_inicio
            self.fecha_salida = retiro_id.fecha_salida
            self.puesto_trabajo_id = retiro_id.puesto_trabajo_id.id


    @api.model
    def create(self, vals_list):
        if vals_list.get('name', 'Borrador') == 'Borrador':
            vals_list['name'] = self.env['ir.sequence'].next_by_code('INM') or 'Borrador'
        return super().create(vals_list)
