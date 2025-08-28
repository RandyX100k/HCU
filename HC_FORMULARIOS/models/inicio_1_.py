# -*- coding:utf-8 -*-
from odoo import  models , fields,api

class Inicio_1(models.Model):
    _name = "inicio.1"
    _rec_name = "name"
    name = fields.Char(string="Inicio1", default="Borrador", copy=False, readonly=True)
    # DATOS DE LA INSTITUCION
    company_id = fields.Many2one("companys.hc", string="Empresa o Institución")
    ruc = fields.Char(string="RUC")
    ciiu = fields.Char(string="CIIU")
    establecimiento_salud = fields.Many2one("res.company", string="Establecimiento de Salud")
    historia_clinica = fields.Char(string="Número de Historia Clínica")
    numero_archivo = fields.Char(string="Número de Archivo")

    # DATOS DEL PACIENTE
    paciente_id = fields.Many2one("pacientes.hc", string="Nombre del paciente")
    primer_apellido = fields.Char(string="Primer apellido")
    segundo_apellido = fields.Char(string="Segundo apellido")
    primer_nombre = fields.Char(string="Primer nombre")
    segundo_nombre = fields.Char(string="Segundo nombre")
    sexo = fields.Selection([('M', 'Masculino'), ('F', 'Femenino')], string="Sexo")
    edad = fields.Integer(string="Edad")
    religion_id = fields.Many2one("religiones.hc", string="Religión")
    grupo_sanguineo = fields.Many2one("grupos.sanguineos", string="Grupo Sanguíneo")
    lateralidad = fields.Selection(
        [
            ('derecho', 'Derecho'),
            ('zurdo', 'Zurdo'),
            ('ambidextro', 'Ambidextro')
        ],
        string="Lateralidad")
    intruccion_id = fields.Many2one("instruccion.names",string="Instrucción")
    estado_civil = fields.Many2one("estados.civiles", string="Estado civil")
    profesion_id = fields.Many2one("profesion.names",string="Profesión")
    lugar_nacimiento = fields.Char(string="Lugar de nacimiento")
    fecha_nacimieto = fields.Date(string="Fecha de nacimiento")
    ocupacion_id = fields.Many2one("ocupaciones.names",string="Ocupación")
    tel = fields.Char(string="Teléfono")
    direccion = fields.Text(string="Dirección")
    orientacion_sexual = fields.Many2one("orientacion.sexual", string="Orientación sexual")
    identidad_genero = fields.Many2one("identidad.genero", string="Identidad de género")
    discapacidad = fields.Selection([('si', 'Sí'), ('no', 'No')], string="¿Tiene discapacidad?")
    tipo_discapacidad = fields.Char(string="Tipo de discapacidad")
    porcentaje = fields.Integer(string="Porcentaje de discapacidad")
    fecha_ingreso = fields.Date(string="Fecha de ingreso")
    puesto_trabajo_id = fields.Many2one("puestos.names",string="Puesto de trabajo")
    area_trabajo_id = fields.Many2one("areas.trabajos",string="Área de trabajo")
    actividades_trabajo = fields.Char(string="Actividades de trabajo")

    # MOTIVO DE CONSULTA
    motivo_consulta = fields.Text(string="Motivo de consulta")
    evaluacion_ocupacional = fields.Char(string="Causa del problema")

    # ANTECEDENTES CLÍNICOS Y QUIRÚRGICOS
    antecedentes_clinicos = fields.Text(string="APP Clínicos")
    antecedentes_quirurgicos = fields.Text(string="APP Quirúrgicos")
    antecedentes_trauma = fields.Text(string="APP Traumáticos")
    antecedentes_hospitalizacion = fields.Text(string="Hospitalización")
    antecedentes_alergias = fields.Text(string="Alergias")

    # GINECO OBSTÉTRICOS
    menarquia = fields.Char(string="Menarquía")
    ciclos = fields.Char(string="Ciclos")
    fecha_ultima_menstruacion = fields.Date(string="Fecha de última menstruación")
    gestas = fields.Integer(string="Gestas")
    partos = fields.Integer(string="Partos")
    cesareas = fields.Integer(string="Cesáreas")
    abortos = fields.Integer(string="Abortos")
    hijos_vivos = fields.Integer(string="Hijos vivos")
    hijos_muertos = fields.Integer(string="Hijos muertos")
    vida_sexual_activa = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Vida sexual activa")
    usa_planificacion = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Usa planificación familiar")
    tipo_planificacion = fields.Char(string="Tipo de método")

    # EXÁMENES GINECOLÓGICOS
    papanicolaou = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Papanicolaou realizado")
    resultado_papanicolaou = fields.Text(string="Resultado Papanicolaou")
    colposcopia = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Colposcopia realizada")
    resultado_colposcopia = fields.Text(string="Resultado Colposcopia")

    eco_mamario = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Eco mamario realizado")
    eco_mamario_fecha = fields.Char(string="Fecha Eco Mamario")
    resultado_eco_mamario = fields.Text(string="Resultado Eco Mamario")

    mamografia = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Mamografía realizada")
    resultado_mamografia = fields.Text(string="Resultado Mamografía")

    # ANTECEDENTES REPRODUCTIVOS MASCULINOS
    antigeno_prostatico = fields.Selection([('si', 'Sí'), ('no', 'No'), ('na', 'N/A')], string="Antígeno Prostático")
    resultado_antigeno = fields.Text(string="Resultado Antígeno")
    eco_prostatico = fields.Selection([('si', 'Sí'), ('no', 'No'), ('na', 'N/A')], string="Eco Prostático")
    resultado_eco_prostatico = fields.Text(string="Resultado Eco Prostático")

    usa_planificacion_m = fields.Selection([('si', 'Sí'), ('no', 'No'), ('na', 'N/A')], string="Usa planificación (M)")
    tipo_planificacion_m = fields.Char(string="Tipo planificación (M)")
    hijos_vivos_m = fields.Integer(string="Hijos vivos (M)")
    hijos_muertos_m = fields.Integer(string="Hijos muertos (M)")


    # HÁBITOS TÓXICOS
    tabaco = fields.Boolean(string="Tabaco")
    tiempo_tabaco = fields.Char(string="¿Cuánto tiempo? (meses)", help="Indicar el tiempo de consumo en meses")
    ex_consumo_tabaco = fields.Boolean(string="Ex consumidor")
    cantidad_tabaco = fields.Char(string="Cantidad tabaco")
    tiempo_abs = fields.Integer(string="Tiempo abstiencia (meses)")
    # alcohol
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

    # incidentes
    incidentes = fields.Char(string="Incidentes")

    antecedente_trabajo_ids = fields.One2many(
        'antecedente.trabajo',
        'paciente_id',
        string="Antecedentes laborales",
        related='paciente_id.antecedente_trabajo_ids',
        store=False
    )

    # ACCIDENTES DE TRABAJO
    descripcion_accidente = fields.Text(string="Descripción de accidente de trabajo")
    calificado_accidente = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Fue calificado por el IESS")
    especificacion_accidente = fields.Char(string="Especificar accidente")
    fecha_accidente = fields.Date(string="Fecha calificación accidente")

    # ENFERMEDADES PROFESIONALES
    descripcion_enfermedad = fields.Text(string="Descripción enfermedad profesional")
    calificado_enfermedad = fields.Selection([('si', 'Sí'), ('no', 'No')], string="Fue calificada por el IESS")
    especificacion_enfermedad = fields.Char(string="Especificar enfermedad")
    fecha_enfermedad = fields.Date(string="Fecha calificación enfermedad")
    res_company_id = fields.Many2one('res.company', string="Compañía", default=lambda self: self.env.company)



    #inicio 2- 2
    # ANTECEDENTES FAMILIARES
    enfermedad_cardio = fields.Boolean(string="Enferrmedad cardio-vascular")
    enfermedad_metabolidca = fields.Boolean(string="Enfermedad metabolica")
    enfermedad_neurologica = fields.Boolean(string="Enfermedad neurologica")
    enfermedad_oncologica = fields.Boolean(string="Enfermedad oncologica")

    # infeciosa . # hereditaria , discapacidades , otros
    enfermedad_infecciosa = fields.Boolean(string="Enfermedad infecciosa")
    enfermedad_hereditaria = fields.Boolean(string="Enfermedad hereditaria")
    discapacidad_ = fields.Boolean(string="Discapacidad")
    otra_enfermedad = fields.Boolean(string="Otras enfermedades")

    refiere = fields.Char(string="Refire")

    actividades_extras_laborales = fields.One2many("actividades.laborales", "form_id_1",
                                                   string="Actividades Extras laborales")

    enfermedad_actual = fields.Char(string="Enfermedad actual")

    # riegos
    riesgos_ids = fields.One2many("inicio.2.riesgos", "form_id_1", string="Riesgos-1")
    riesgos_ids_2 = fields.One2many("inicio.2.riesgos.2", "form_id_1", string="Riesgos-2")

    # actividades extras laborales
    # enfermedad_actual
    enfermedad_actual = fields.Text(string="Enfermedad actual")
    # revision actual
    organos_sistemas_ids = fields.One2many("organos.sistemas", "form_id_1",
                                           string="Organos y sistemas")

    observacion_organos = fields.Char(string="SIN PATOLOGIA APARENTE")

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
        compute="_compute_imc",
        store=True
    )
    perimetro_abdominal = fields.Float(string="Perímetro Abdominal (cm)")


    #inicio 3-3

    regiones_ids = fields.One2many("regiones.examen","form_id_1",
                                   string="Examen fisico y regional")

    observaciones_examen_regional = fields.One2many("recomendaciones.tratamientos", "form_id_1",
                                                    string="Observaciones")
    #columnas y extremidades
    columna_extremidades_ids = fields.One2many(
        "columna.extremidades",
        "form_id_1",
        string="Columna y Extremidades"
    )

    #resultado de examamenes
    resultados_ids = fields.One2many("resultado.examenes",
                                     "form_id_1",string="Resultado examenes")



    #MOTIVO DIAGNOSTICO
    motivos_diagnosticos_ids = fields.One2many("motivo.diagnostico","form_id_1",
                                               string="Motivos diagnosticos")
    observaciones = fields.Text(string="Observaciones")
    #actitud medica
    actitudes_ids = fields.One2many("actitud.medica","form_id_1",
                                   string="Actitud medica para el trabajo")

    #recomendaciones o tratamientos
    recomendaciones_ids = fields.One2many("recomendaciones.tratamientos",
                                          "form_id_1",string="Recomendaciones o tratamientos")

    #datos del profesional
    fecha_datos = fields.Date(string="Fecha",default=fields.Date.today())
    hora = fields.Char(string="Hora")

    profesional_id = fields.Many2one("profesionales.doctores",string="Nombre y apellidos")
    codigo = fields.Char(string="Codigo",compute="_check_profesional_id",store=True)
    firma_sello = fields.Binary(string="Firma y sello")

    #firma del usuario
    firma_user = fields.Binary(string="Firma usuario")

    #sequencias
    @api.model
    def create(self, vals):
        if vals.get('name', 'Borrador') == 'Borrador':
            vals['name'] = self.env['ir.sequence'].next_by_code('FORM001') or 'Borrador'
        return super().create(vals)

    @api.onchange('company_id')
    def _onchange_company_id(self):
        if self.company_id:
            self.ruc = self.company_id.ruc
            self.ciiu = self.company_id.ciiu
            self.establecimiento_salud = self.company_id.establecimiento.id
            self.historia_clinica = self.company_id.numero_historia_clinica
            self.numero_archivo = self.company_id.numero_archivo

    @api.onchange('paciente_id')
    def _onchange_paciente_id(self):
        if self.paciente_id:
            self.primer_apellido = self.paciente_id.primer_apellido
            self.segundo_apellido = self.paciente_id.segundo_apellido
            self.primer_nombre = self.paciente_id.primer_nombre
            self.segundo_nombre = self.paciente_id.segundo_nombre
            self.sexo = self.paciente_id.sexo
            self.edad = self.paciente_id.edad
            self.religion_id = self.paciente_id.religion_id
            self.grupo_sanguineo = self.paciente_id.grupo_sanguineo
            self.lateralidad = self.paciente_id.lateralidad
            self.intruccion_id = self.paciente_id.instruccion_id
            self.estado_civil = self.paciente_id.estado_civil
            self.profesion_id = self.paciente_id.profesion_id
            self.lugar_nacimiento = self.paciente_id.lugar_nacimiento
            self.fecha_nacimieto = self.paciente_id.fecha_nacimieto
            self.ocupacion_id = self.paciente_id.ocupacion_id
            self.tel = self.paciente_id.tel
            self.direccion = self.paciente_id.direccion
            self.orientacion_sexual = self.paciente_id.orientacion_sexual
            self.identidad_genero = self.paciente_id.identidad_genero
            self.discapacidad = self.paciente_id.discapacidad
            self.tipo_discapacidad = self.paciente_id.tipo_discapacidad
            self.porcentaje = self.paciente_id.porcentaje
            self.fecha_ingreso = self.paciente_id.fecha_ingreso
            self.puesto_trabajo_id = self.paciente_id.puesto_trabajo_id
            self.area_trabajo_id = self.paciente_id.area_trabajo_id
            self.actividades_trabajo = self.paciente_id.actividades_trabajo

            # Limpiar regiones previas
            self.regiones_ids = [(5, 0, 0)]

            # Obtener todas las regiones con sus subregiones
            regiones = self.env['regiones.types'].search([])
            nuevas_regiones = []

            for region in regiones:
                subregiones = self.env['subregiones.types'].search([('region_id', '=', region.id)])
                for sub in subregiones:
                    nuevas_regiones.append((0, 0, {
                        'type_region': region.id,
                        'type_subregion': sub.id,
                        'patologia': False,
                        'descripcion': 'SIN PATOLOGIA',
                    }))

            self.regiones_ids = nuevas_regiones


            self.columna_extremidades_ids = [(5,0,0)]
            columns_new = []
            columnas = self.env['columna.extremidades'].search([])

            for col in columnas:
                columns_new.append((0,0,{
                    'signos_ids': col.signos_ids.id,
                    'patologia': False,
                    'descripcion': 'SIN PATOLOGIA'
                }))

            self.columna_extremidades_ids = columns_new

            # Limpiar columna_extremidades
            self.columna_extremidades_ids = [(5, 0, 0)]
            columns_new = []

            # Este es el origen correcto: los signos clínicos
            signos = self.env['signos.clinicos'].search([])

            for signo in signos:
                columns_new.append((0, 0, {
                    'signos_ids': signo.id,
                    'patologia': False,
                    'descripcion': 'SIN PATOLOGIA'
                }))

            self.columna_extremidades_ids = columns_new

    #imc
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


    @api.depends('profesional_id')
    def _check_profesional_id(self):
        for record in self:
            record.codigo = record.profesional_id.code