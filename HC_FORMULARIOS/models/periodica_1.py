# -*- coding:utf-8 -*-
from  odoo import  models , fields , api

class Periodica_1(models.Model):
    _name = "periodica.1"

    name = fields.Char(string="Numero", default="Borrador")
    paciente_id = fields.Many2one("pacientes.hc", string="Paciente")

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


    #motivo consulta
    motivo_consulta = fields.One2many(
        "motivo.consulta",
        "periodica_id",
        string="Motivo Consulta")
    

    #antecedentes personales
    antecedentes_clinicos = fields.Text(string="APP Clínicos")
    antecedentes_quirurgicos = fields.Text(string="APP Quirúrgicos")
    antecedentes_trauma = fields.Text(string="APP Traumáticos")
    antecedentes_hospitalizacion = fields.Text(string="Hospitalización")
    antecedentes_alergias = fields.Text(string="Alergias")


    #paciente
    lugar_nacimiento = fields.Char(string="Lugar de nacimiento")
    fecha_nacimieto = fields.Date(string="Fecha de nacimiento")
    instruccion_id = fields.Many2one("instruccion.names",string="Instrucción")
    ocupacion_id = fields.Many2one("ocupaciones.names",string="Ocupación")
    tel = fields.Char(string="Número de celular")



    # HÁBITOS TÓXICOS
    tabaco = fields.Boolean(string="Tabaco")
    tiempo_tabaco = fields.Char(string="¿Cuánto tiempo? (meses)", help="Indicar el tiempo de consumo en meses")
    ex_consumo_tabaco = fields.Boolean(string="Ex consumidor")
    cantidad_tabaco = fields.Char(string="Cantidad tabaco")
    tiempo_abs = fields.Integer(string="Tiempo abstiencia (meses)")
    #alcohol
    alcohol = fields.Boolean(string="Alcohol")
    tiempo_alcohol = fields.Char(string="¿Cuánto tiempo? (meses)", help="Indicar el tiempo de consumo en meses")
    ex_consumo_alcohol = fields.Boolean(string="Ex consumidor")
    tiempo_alcohol_abs = fields.Integer(string="Tiempo abstiencia (meses)")
    cantidad_alcohol = fields.Char(string="Cantidad alcohol")

    otras_drogas = fields.Boolean(string="Otras drogas")
    otras_drogas_detalle = fields.Char(string="Especificar drogas")

    # ESTILO DE VIDA
    actividad_fisica = fields.Boolean(string="Actividad física")
    medicacion_habitual = fields.Boolean(string="Medicación habitual")
    estilo_vida_cual = fields.Char(string="¿Cuál?")
    medicacion_cual = fields.Char(string="Medicacion cual")

    #incidentes
    incidentes = fields.Char(string="Incidentes")




    #accidentes de trabajo
    # ACCIDENTES DE TRABAJO
    calificado_accidente = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Fue calificado por el IESS")
    especificacion_accidente = fields.Char(string="Especificar accidente")
    fecha_accidente = fields.Date(string="Fecha calificación accidente")
    observaciones_accidente_trabajo = fields.Text("Observaciones")

    # ENFERMEDADES PROFESIONALES
    descripcion_enfermedad = fields.Text(string="Descripción enfermedad profesional")
    calificado_enfermedad = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Fue calificada por el IESS")
    especificacion_enfermedad = fields.Char(string="Especificar enfermedad")
    fecha_enfermedad = fields.Date(string="Fecha calificación enfermedad")
    observaciones_enfermades = fields.Text("Observaciones")


    #antecedentes familiares
    # ANTECEDENTES FAMILIARES
    enfermedad_cardio = fields.Boolean(string="Enferrmedad cardio-vascular")
    enfermedad_metabolidca = fields.Boolean(string="Enfermedad metabolica")
    enfermedad_neurologica = fields.Boolean(string="Enfermedad neurologica")
    enfermedad_oncologica = fields.Boolean(string="Enfermedad oncologica")

    # infeciosa . # hereditaria , discapacidades , otros
    enfermedad_infecciosa = fields.Boolean(string="Enfermedad infecciosa")
    enfermedad_hereditaria = fields.Boolean(string="Enfermedad hereditaria")
    discapacidad = fields.Boolean(string="Discapacidad")
    otra_enfermedad = fields.Boolean(string="Otras enfermedades")
    refiere = fields.Char(string="Refire")

    #factores de riesgos del puesto de trabajo
    riesgos_ids = fields.One2many("inicio.2.riesgos", "periodica_id",
                                  string="Riesgos-1")

    #otros riesgos
    riesgos_ids_2 = fields.One2many("inicio.2.riesgos.2", "periodica_1_id",
                                    string="Riesgos-2")

    #periodica 2
    # enfermedad actual
    enfermedad_actual = fields.Char(string="Enfermedad actual")
    # revisiones de organos y sistemas
    organos_sistemas_ids = fields.One2many("organos.sistemas", "periodica_2_id_",
                                           string="Revision de organos y sistemas")

    observaciones_organos = fields.Char(string="Observaciones organos")
    refiere = fields.Char(string="REFIERE")

    # contantes vitales
    presion_arterial = fields.Char(string="Presión Arterial")
    temperatura = fields.Float(string="Temperatura (°C)")
    frecuencia_cardiaca = fields.Integer(string="Frecuencia Cardíaca (lat/min)")
    saturacion_oxigeno = fields.Integer(string="Saturación de Oxígeno (%)")
    frecuencia_respiratoria = fields.Integer(string="Frecuencia Respiratoria (resp/min)")
    peso = fields.Float(string="Peso (kg)")
    talla = fields.Float(string="Talla (cm)")
    indice_masa_corporal = fields.Float(
        string="Índice de Masa Corporal (kg/m²)",
        compute = "_compute_imc",
        store=True
    )
    perimetro_abdominal = fields.Float(string="Perímetro Abdominal (cm)")

    # examen fisico regional
    examen_region_ids = fields.One2many("regiones.examen", "periodica_2_id_",
                                        string="Examen fisico regional")

    observaciones_examen_regional = fields.One2many("recomendaciones.tratamientos","periodica_2_id_",string="Observaciones")

    observaciones = fields.Text(string="Observaciones")
    # columna y extremidades

    columna_extremidades_ids = fields.One2many("columna.extremidades", "periodica_2_id_",
                                               string="Columna y Extremidades")
    # resultado de examenes generales
    resultado_examen_ids = fields.One2many("resultado.examenes", "periodica_2_id_",
                                           string="RESULTADOS DE EXAMENES GENERALES Y ESPECIFICOS DE ACUERDO AL RIESGO Y PUESTO DE TRABAJO")

    # examen diagnosticos
    examens_diagnosticos_ids = fields.One2many("motivo.diagnostico", "periodica_2_id_", string="K.DIAGNOSTICO")

    # aptitud medica para el trabajo
    aptidudes_medicas_ids = fields.One2many("actitud.medica", "periodica_2_id_",
                                            string="L. APTITUD MÉDICA PARA EL TRABAJO")

    # recomendaciones
    recomendaciones_ids = fields.One2many("recomendaciones.tratamientos",
                                          "periodica_2_id_", string="Recomendaciones")

    # datos usuario
    # datos del profesional
    fecha_datos = fields.Date(string="Fecha", default=fields.Date.today())
    hora = fields.Char(string="Hora")

    profesional_id = fields.Many2one("profesionales.doctores", string="Nombre y apellidos")
    codigo = fields.Char(string="Codigo")
    firma_sello = fields.Binary(string="Firma y sello")

    # firma del usuario
    firma_user = fields.Binary(string="Firma usuario")

    @api.onchange('paciente_id')
    def _onchange_form_id(self):
        if not self.paciente_id:
            return

        ultimo_inicio_1 = self.env['inicio.1'].search(
            [('paciente_id', '=', self.paciente_id.id)],
            order='id desc',
            limit=1
        )

        if not ultimo_inicio_1:
            return

        # --- Datos del paciente
        self.primer_apellido = self.paciente_id.primer_apellido
        self.segundo_apellido = self.paciente_id.segundo_apellido
        self.primer_nombre = self.paciente_id.primer_nombre
        self.segundo_nombre = self.paciente_id.segundo_nombre
        self.sexo = self.paciente_id.sexo
        self.lugar_nacimiento = self.paciente_id.lugar_nacimiento
        self.fecha_nacimieto = self.paciente_id.fecha_nacimieto
        self.instruccion_id = self.paciente_id.instruccion_id.id
        self.ocupacion_id = self.paciente_id.ocupacion_id.id
        self.tel = self.paciente_id.tel
        self.puesto_trabajo_id = self.paciente_id.puesto_trabajo_id.id

        #datos del establecimiento

        self.institucion_name = ultimo_inicio_1.company_id.id
        self.ruc = ultimo_inicio_1.ruc
        self.ciiu = ultimo_inicio_1.ciiu
        self.establecimiento_salud = ultimo_inicio_1.establecimiento_salud
        self.historia_clinica = ultimo_inicio_1.historia_clinica
        self.numero_archivo = ultimo_inicio_1.numero_archivo

        # --- Antecedentes y enfermedad
        self.antecedentes_clinicos = ultimo_inicio_1.antecedentes_clinicos
        self.antecedentes_quirurgicos = ultimo_inicio_1.antecedentes_quirurgicos
        self.antecedentes_trauma = ultimo_inicio_1.antecedentes_trauma
        self.antecedentes_hospitalizacion = ultimo_inicio_1.antecedentes_hospitalizacion
        self.antecedentes_alergias = ultimo_inicio_1.antecedentes_alergias
        self.calificado_accidente = ultimo_inicio_1.calificado_accidente
        self.especificacion_accidente = ultimo_inicio_1.especificacion_accidente
        self.fecha_accidente = ultimo_inicio_1.fecha_accidente
        self.descripcion_enfermedad = ultimo_inicio_1.descripcion_enfermedad
        self.calificado_enfermedad = ultimo_inicio_1.calificado_enfermedad
        self.especificacion_enfermedad = ultimo_inicio_1.especificacion_enfermedad
        self.fecha_enfermedad = ultimo_inicio_1.fecha_enfermedad
        self.enfermedad_cardio = ultimo_inicio_1.enfermedad_cardio
        self.enfermedad_metabolidca = ultimo_inicio_1.enfermedad_metabolidca
        self.enfermedad_neurologica = ultimo_inicio_1.enfermedad_neurologica
        self.enfermedad_oncologica = ultimo_inicio_1.enfermedad_oncologica
        self.enfermedad_infecciosa = ultimo_inicio_1.enfermedad_infecciosa
        self.enfermedad_hereditaria = ultimo_inicio_1.enfermedad_hereditaria
        self.discapacidad = ultimo_inicio_1.discapacidad_
        self.otra_enfermedad = ultimo_inicio_1.otra_enfermedad
        self.refiere = ultimo_inicio_1.refiere
        self.enfermedad_actual = ultimo_inicio_1.enfermedad_actual
        self.observaciones = ultimo_inicio_1.observaciones

        #datos profesional

        self.profesional_id = ultimo_inicio_1.profesional_id.id
        self.codigo = ultimo_inicio_1.codigo
        self.firma_sello  = ultimo_inicio_1.firma_sello
        self.firma_user = ultimo_inicio_1.firma_user



        # --- Riesgos 1
        self.riesgos_ids = [(5, 0, 0)] + [
            (0, 0, {
                'puesto_id': r.puesto_id.id,
                'actividades': r.actividades,
                'typo_riesgos': r.typo_riesgos.id,
                'riesgo': [(6, 0, r.riesgo.ids if r.riesgo else [])],
            }) for r in ultimo_inicio_1.riesgos_ids
        ]

        # --- Riesgos 2
        self.riesgos_ids_2 = [(5, 0, 0)] + [
            (0, 0, {
                'puesto_id': r.puesto_id.id,
                'actividades': r.actividades,
                'typo_riesgos': r.typo_riesgos.id,
                'riesgo': [(6, 0, r.riesgo.ids if r.riesgo else [])],
                'medidas_preventiva': r.medidas_preventiva,
            }) for r in ultimo_inicio_1.riesgos_ids_2
        ]

        # --- Órganos y sistemas
        self.organos_sistemas_ids = [(5, 0, 0)] + [
            (0, 0, {
                'organo_sistema_': o.organo_sistema_,
                'patologia': o.patologia,

            }) for o in ultimo_inicio_1.organos_sistemas_ids
        ]

        # --- Examen físico regional
        self.examen_region_ids = [(5, 0, 0)] + [
            (0, 0, {
                'type_region': ex.type_region.id if ex.type_region else False,
                'type_subregion': ex.type_subregion.id if ex.type_subregion else False,
                'patologia': ex.patologia,
                'descripcion': ex.descripcion,
            }) for ex in ultimo_inicio_1.regiones_ids
        ]

        # --- Columna y extremidades
        self.columna_extremidades_ids = [(5, 0, 0)] + [
            (0, 0, {
                'signos_ids': c.signos_ids.id if c.signos_ids else False,
                'patologia': c.patologia,
                'descripcion': c.descripcion,
            }) for c in ultimo_inicio_1.columna_extremidades_ids
        ]

        # --- Resultados de exámenes
        self.resultado_examen_ids = [(5, 0, 0)] + [
            (0, 0, {
                'examen_id': re.examen_id.id,
                'resultado': re.resultado,
                'fecha': re.fecha,
            }) for re in ultimo_inicio_1.resultados_ids
        ]

        # --- Diagnósticos
        self.examens_diagnosticos_ids = [(5, 0, 0)] + [
            (0, 0, {
                'cie_id': d.cie_id.id if d.cie_id else False,
                'pref': d.pref,
                'def_': d.pref
            }) for d in ultimo_inicio_1.motivos_diagnosticos_ids
        ]

        # --- Aptitudes médicas
        self.aptidudes_medicas_ids = [(5, 0, 0)] + [
            (0, 0, {
                'apto': a.apto,
                'apto_observacion': a.apto_observacion,
                'apto_limitaciones': a.apto_limitaciones,
                'no_apto': a.no_apto,
                'observacion': a.observacion,
                'limitacion': a.limitacion
            }) for a in ultimo_inicio_1.actitudes_ids
        ]

        # --- Recomendaciones
        self.recomendaciones_ids = [(5, 0, 0)] + [
            (0, 0, {
                'recomendacion': r.recomendacion,
            }) for r in ultimo_inicio_1.recomendaciones_ids
        ]

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == 'Borrador':
                vals['name'] = self.env['ir.sequence'].next_by_code('PERO1') or 'PER1/BORRADOR'
        return super().create(vals_list)

    # imc

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