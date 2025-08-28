# -*- coding:utf-8 -*-
from  odoo import  models,fields , api

class Periodica_2(models.Model):
    _name = "periodica.2"

    name = fields.Char(string="Numero",default="Borrador")
    #periodica1_id
    periodica_1_id = fields.Many2one("periodica.1")

    #enfermedad actual
    enfermedad_actual = fields.Char(string="Enfermedad actual")
    #revisiones de organos y sistemas
    organos_sistemas_ids = fields.One2many("organos.sistemas","periodica_2",
                                           string="Revision de organos y sistemas")
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
        store=True
    )
    perimetro_abdominal = fields.Float(string="Perímetro Abdominal (cm)")


    #examen fisico regional
    examen_region_ids = fields.One2many("regiones.examen","periodica_2_id",
                                        string="Examen fisico regional")
    observaciones = fields.Text(string="Observaciones")
    #columna y extremidades

    columna_extremidades_ids = fields.One2many("columna.extremidades","periodica_2_id",
                                               string="Columna y Extremidades")
    #resultado de examenes generales
    resultado_examen_ids = fields.One2many("resultado.examenes","periodica_2_id",
                                           string="RESULTADOS DE EXAMENES GENERALES Y ESPECIFICOS DE ACUERDO AL RIESGO Y PUESTO DE TRABAJO")

    #examen diagnosticos
    examens_diagnosticos_ids = fields.One2many("motivo.diagnostico","periodica_2_id",string="K.DIAGNOSTICO")

    #aptitud medica para el trabajo
    aptidudes_medicas_ids = fields.One2many("actitud.medica","periodica_2_id",
                                            string="L. APTITUD MÉDICA PARA EL TRABAJO")

    #recomendaciones
    recomendaciones_ids = fields.One2many("recomendaciones.tratamientos",
                                          "periodica_2_id", string="Recomendaciones")


    #datos usuario
    # datos del profesional
    fecha_datos = fields.Date(string="Fecha", default=fields.Date.today())
    hora = fields.Char(string="Hora")

    profesional_id = fields.Many2one("profesionales.doctores",string="Nombre y apellidos")
    codigo = fields.Char(string="Codigo")
    firma_sello = fields.Binary(string="Firma y sello")

    # firma del usuario
    firma_user = fields.Binary(string="Firma usuario")

    @api.onchange('periodica_1_id')
    def _onchange_periodica_1_id(self):
        if self.periodica_1_id:
            inicio2 = self.periodica_1_id.certificado_id.form_id.form_inicio_2_id
            #llenar los campos
            self.presion_arterial = inicio2.presion_arterial
            self.temperatura = inicio2.temperatura
            self.frecuencia_cardiaca = inicio2.frecuencia_cardiaca
            self.saturacion_oxigeno = inicio2.saturacion_oxigeno
            self.frecuencia_respiratoria = inicio2.frecuencia_cardiaca
            self.peso = inicio2.peso
            self.talla = inicio2.talla
            self.indice_masa_corporal = inicio2.indice_masa_corporal
            self.perimetro_abdominal = inicio2.perimetro_abdominal

            inicio3 = self.periodica_1_id.certificado_id.form_id
            self.examen_region_ids = [(5, 0, 0)]
            nuevos_valores = []

            if inicio3.regiones_ids:
                for examen in inicio3.regiones_ids:
                    nuevos_valores.append((0, 0, {
                        'type_region': examen.type_region.id,
                        'type_subregion': examen.type_subregion.id,
                        'patologia': examen.patologia,
                        'descripcion': examen.descripcion
                    }))
            self.examen_region_ids = nuevos_valores

            #columnas y extemidades
            self.columna_extremidades_ids = [(5,0,0)]
            columnas_nuevas_valores = []
            if inicio3.columna_extremidades_ids:
                for col_extremidades in inicio3.columna_extremidades_ids:
                    columnas_nuevas_valores.append((0,0,{
                        'signos_ids':col_extremidades.signos_ids.id,
                        'patologia':col_extremidades.patologia,
                        'descripcion':col_extremidades.descripcion
                    }))

            self.columna_extremidades_ids = columnas_nuevas_valores

            #organos sistemas
            self.organos_sistemas_ids = [(5,0,0)]
            nuevos_valores_organos = []

            if inicio2.organos_sistemas_ids:
                for exame_organo in inicio2.organos_sistemas_ids:
                    nuevos_valores_organos.append((0,0,{
                        'organo_sistema_': exame_organo.organo_sistema_.id,
                        'patologia': exame_organo.patologia
                    }))
            self.organos_sistemas_ids = nuevos_valores_organos

            #aptidudes medias
            self.aptidudes_medicas_ids = [(5,0,0)]

            nuevas_aptitudes = []

            for aptitudes in inicio3.actitudes_ids:
                nuevas_aptitudes.append((0,0,{
                    'apto':aptitudes.apto,
                    'apto_observacion':aptitudes.apto_observacion,
                    'apto_limitaciones': aptitudes.apto_limitaciones,
                    'no_apto':aptitudes.no_apto,
                    'observacion':aptitudes.observacion,
                    'limitacion':aptitudes.limitacion
                }))

            self.aptidudes_medicas_ids = nuevas_aptitudes


            #certificado
            certificado = self.periodica_1_id.certificado_id

            self.recomendaciones_ids = [(5,0,0)]
            recomendaciones = []

            if inicio3.recomendaciones_ids:
                for recomendacion in inicio3.recomendaciones_ids:
                    recomendaciones.append((0,0,{
                        'recomendacion': recomendacion.recomendacion,
                    }))
            self.recomendaciones_ids = recomendaciones

            self.fecha_datos = certificado.fecha_datos
            self.hora = certificado.hora
            self.profesional_id = certificado.profesional_id.id
            self.codigo = certificado.codigo
            self.firma_sello = certificado.firma_sello
            self.firma_user = certificado.firma_user

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name') or vals['name'] == 'Borrador':
                vals['name'] = self.env['ir.sequence'].next_by_code('PERO2') or 'PER/BORRADOR'
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