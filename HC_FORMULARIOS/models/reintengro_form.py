# -*- coding:utf-8 -*-
from  odoo import  models ,fields , api

class ReitengroForm(models.Model):
    _name = "reintegro.form"

    name = fields.Char(string="Numero",default="Borrador")

    paciente_id = fields.Many2one("pacientes.hc",string="Paciente")

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
    puesto_trabajo_id = fields.Many2one("puestos.names", string="Puesto de trabajo")

    fecha_ultimo = fields.Date(string="Fecha ultimo dia laboral")
    fecha_reingreso = fields.Date(string="Fecha de reingro")
    total = fields.Integer(string="Total (dias)")
    causa_salida = fields.Text(string="Causa salida")

    #motivo consulta
    motivo_consulta = fields.Char(string="Motivo de consulta")
    #enfermedad actual
    enfermedad_actual = fields.Char(string="Enfermedad actual")

    #constantes vitales
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
    examen_region_ids = fields.One2many("regiones.examen", "reintegro_id",
                                        string="Examen fisico regional")
    observaciones = fields.Text(string="Observaciones")
    #colunmas y extremidades
    columna_extremidades_ids = fields.One2many("columna.extremidades", "reintegro_id",
                                               string="Columna y Extremidades")

    resultado_examen_ids = fields.One2many("resultado.examenes", "reintegro_id",
                                           string="RESULTADOS DE EXAMENES GENERALES Y ESPECIFICOS DE ACUERDO AL RIESGO Y PUESTO DE TRABAJO")

    # examen diagnosticos
    examens_diagnosticos_ids = fields.One2many("motivo.diagnostico", "reintegro_id",
                                               string="K.DIAGNOSTICO")

    # aptitud medica para el trabajo
    aptidudes_medicas_ids = fields.One2many("actitud.medica", "reintegro_id",
                                            string="L. APTITUD MÉDICA PARA EL TRABAJO")
    # recomendaciones
    recomendaciones_ids = fields.One2many("recomendaciones.tratamientos",
                                          "reintegro_id", string="Recomendaciones")

    # datos del profesional
    fecha_datos = fields.Date(string="Fecha", default=fields.Date.today())
    hora = fields.Char(string="Hora")

    profesional_id = fields.Many2one("profesionales.doctores", string="Nombre y apellidos")
    codigo = fields.Char(string="Codigo")
    firma_sello = fields.Binary(string="Firma y sello")

    # firma del usuario
    firma_user = fields.Binary(string="Firma usuario")

    @api.onchange('paciente_id')
    def _onchange_periodica_id(self):
        if not self.paciente_id:
            return

        p1 = self.env['periodica.1'].search([
            ('paciente_id', '=', self.paciente_id.id)
        ],
        order='id desc',
        limit=1
        )

        # Datos institucionales
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

        # Constantes vitales
        self.enfermedad_actual = p1.enfermedad_actual
        self.presion_arterial = p1.presion_arterial
        self.temperatura = p1.temperatura
        self.frecuencia_cardiaca = p1.frecuencia_cardiaca
        self.saturacion_oxigeno = p1.saturacion_oxigeno
        self.frecuencia_respiratoria = p1.frecuencia_respiratoria
        self.peso = p1.peso
        self.talla = p1.talla
        self.indice_masa_corporal = p1.indice_masa_corporal
        self.perimetro_abdominal = p1.perimetro_abdominal

        # Observaciones
        self.observaciones = p1.observaciones

        # Examen físico regional
        self.examen_region_ids = [(5, 0, 0)] + [
            (0, 0, {
                'type_region': r.type_region.id,
                'type_subregion': r.type_subregion.id,
                'patologia': r.patologia,
                'descripcion': r.descripcion
            }) for r in p1.examen_region_ids
        ]

        # Columna y extremidades
        self.columna_extremidades_ids = [(5, 0, 0)] + [
            (0, 0, {
                'signos_ids': c.signos_ids.id,
                'patologia': c.patologia,
                'descripcion': c.descripcion
            }) for c in p1.columna_extremidades_ids
        ]

        # Resultados de exámenes
        self.resultado_examen_ids = [(5, 0, 0)] + [
            (0, 0, {
                'examen_id': r.examen_id.id,
                'fecha': r.fecha,
                'resultado': r.resultado
            }) for r in p1.resultado_examen_ids
        ]

        # Diagnósticos
        self.examens_diagnosticos_ids = [(5, 0, 0)] + [
            (0, 0, {
                'cie_id': d.cie_id.id,
                'motivo': d.motivo,
                'pref': d.pref,
                'def_': d.def_
            }) for d in p1.examens_diagnosticos_ids
        ]

        # Aptitud médica
        self.aptidudes_medicas_ids = [(5, 0, 0)] + [
            (0, 0, {
                'apto': a.apto,
                'apto_observacion': a.apto_observacion,
                'apto_limitaciones': a.apto_limitaciones,
                'no_apto': a.no_apto,
                'observacion': a.observacion,
                'limitacion': a.limitacion
            }) for a in p1.aptidudes_medicas_ids
        ]

        # Recomendaciones
        self.recomendaciones_ids = [(5, 0, 0)] + [
            (0, 0, {
                'recomendacion': r.recomendacion
            }) for r in p1.recomendaciones_ids
        ]

        # Datos del profesional
        self.fecha_datos = p1.fecha_datos
        self.hora = p1.hora
        self.profesional_id = p1.profesional_id.id
        self.codigo = p1.codigo
        self.firma_sello = p1.firma_sello
        self.firma_user = p1.firma_user

    @api.model
    def create(self, vals_list):
        if vals_list.get('name', 'Borrador') == 'Borrador':
            vals_list['name'] = self.env['ir.sequence'].next_by_code('REIN') or 'Borrador'
        return super().create(vals_list)