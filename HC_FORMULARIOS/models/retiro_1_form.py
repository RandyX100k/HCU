# -*- coding:utf-8 -*-
from  odoo import  models ,fields, api


class Retiro_1(models.Model):
    _name = "retiro.1"
    name = fields.Char(string="Numero",default="Borrador")

    reintegro_id = fields.Many2one("reintegro.form",string="Periodica 2")
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

    #factores riesgos

    factores_ids = fields.One2many("actividades.laborales","retiro_1_id",
                                   string="Factores riesgos")

    # ANTECEDENTES CLÍNICOS Y QUIRÚRGICOS
    antecedentes_clinicos = fields.Text(string="APP Clínicos")
    antecedentes_quirurgicos = fields.Text(string="APP Quirúrgicos")
    antecedentes_trauma = fields.Text(string="APP Traumáticos")
    antecedentes_hospitalizacion = fields.Text(string="Hospitalización")
    antecedentes_alergias = fields.Text(string="Alergias")

    # ACCIDENTES DE TRABAJO
    descripcion_accidente = fields.Text(string="Observaciones")
    calificado_accidente = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Fue calificado por el IESS")
    especificacion_accidente = fields.Char(string="Especificar accidente")
    fecha_accidente = fields.Date(string="Fecha calificación accidente")

    # ENFERMEDADES PROFESIONALES
    descripcion_enfermedad = fields.Text(string="Observaciones")
    calificado_enfermedad = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Fue calificada por el IESS")
    especificacion_enfermedad = fields.Char(string="Especificar enfermedad")
    fecha_enfermedad = fields.Date(string="Fecha calificación enfermedad")

    # constantes vitales
    presion_arterial = fields.Char(string="Presión Arterial")
    temperatura = fields.Float(string="Temperatura (°C)")
    frecuencia_cardiaca = fields.Integer(string="Frecuencia Cardíaca (lat/min)")
    saturacion_oxigeno = fields.Integer(string="Saturación de Oxígeno (%)")
    frecuencia_respiratoria = fields.Integer(string="Frecuencia Respiratoria (resp/min)")
    peso = fields.Float(string="Peso (kg)")
    talla = fields.Float(string="Talla (cm)")
    indice_masa_corporal = fields.Float(
        string="Índice de Masa Corporal (kg/m²)",
        store=True
    )
    perimetro_abdominal = fields.Float(string="Perímetro Abdominal (cm)")

    # examen fisico regional
    examen_region_ids = fields.One2many("regiones.examen", "retiro_id",
                                        string="Examen fisico regional")

    #observaciones examenes
    observaciones_examen = fields.Char(string="Observaciones")

    @api.onchange('reintegro_id')
    def _onchange_periodica_2_id(self):
        if not self.reintegro_id.periodica_2_id:
            return

        p1 = self.reintegro_id.periodica_2_id.periodica_1_id
        f1 = self.reintegro_id.periodica_2_id.periodica_1_id.certificado_id.form_id.form_inicio_2_id.form_01_id
        f2 = self.reintegro_id.periodica_2_id.periodica_1_id.certificado_id.form_id.form_inicio_2_id
        p2 = self.reintegro_id.periodica_2_id

        # Datos de institución
        self.institucion_name = p1.institucion_name
        self.ruc = p1.ruc
        self.ciiu = p1.ciiu
        self.establecimiento_salud = p1.establecimiento_salud
        self.historia_clinica = p1.historia_clinica
        self.numero_archivo = p1.numero_archivo

        # Datos del paciente
        self.primer_apellido = p1.primer_apellido
        self.segundo_apellido = p1.segundo_apellido
        self.primer_nombre = p1.primer_nombre
        self.segundo_nombre = p1.segundo_nombre
        self.sexo = p1.sexo
        self.puesto_trabajo_id = p1.puesto_trabajo_id


        #antecedentes
        self.antecedentes_clinicos = p1.antecedentes_clinicos
        self.antecedentes_quirurgicos = p1.antecedentes_clinicos
        self.antecedentes_trauma = p1.antecedentes_trauma
        self.antecedentes_hospitalizacion = p1.antecedentes_hospitalizacion
        self.antecedentes_alergias = p1.antecedentes_alergias
        #accidentes
        self.calificado_accidente = p1.calificado_accidente
        self.fecha_accidente = p1.fecha_accidente
        self.descripcion_accidente = p1.observaciones_accidente_trabajo
        self.especificacion_accidente = p1.especificacion_accidente

        #enfermedades profesionales
        self.descripcion_enfermedad = p1.descripcion_enfermedad
        self.calificado_enfermedad = p1.calificado_enfermedad
        self.especificacion_enfermedad = p1.especificacion_enfermedad
        self.fecha_enfermedad = p1.fecha_enfermedad
        self.descripcion_enfermedad = p1.descripcion_enfermedad

        #constantes vitales
        # constantes vitales desde f2
        self.presion_arterial = f2.presion_arterial
        self.temperatura = f2.temperatura
        self.frecuencia_cardiaca = f2.frecuencia_cardiaca
        self.saturacion_oxigeno = f2.saturacion_oxigeno
        self.frecuencia_respiratoria = f2.frecuencia_respiratoria
        self.peso = f2.peso
        self.talla = f2.talla
        self.indice_masa_corporal = f2.indice_masa_corporal
        self.perimetro_abdominal = f2.perimetro_abdominal

        #examen regional
        # Examen físico regional desde p2
        self.examen_region_ids = [(5, 0, 0)]  # Limpiar primero
        lineas_nuevas = []
        for linea in p2.examen_region_ids:
            lineas_nuevas.append((0, 0, {
                'type_region': linea.type_region.id,
                'type_subregion': linea.type_subregion.id,
                'patologia': linea.patologia,
                'descripcion': linea.descripcion,
            }))
        self.examen_region_ids = lineas_nuevas

    @api.model
    def create(self, vals_list):
        if vals_list.get('name', 'Borrador') == 'Borrador':
            vals_list['name'] = self.env['ir.sequence'].next_by_code('RETI') or 'Borrador'
        return super().create(vals_list)


