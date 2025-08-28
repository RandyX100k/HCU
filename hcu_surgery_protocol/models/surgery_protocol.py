# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class HcuSurgeryProtocol(models.Model):
    _name = "hcu.surgery.protocol"
    _description = "Protocolo Quirúrgico (SNS-MSP/HCU-form.017/2021)"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    # Identificación / Encabezado
    name = fields.Char(string="Número de Protocolo", default=lambda self: self.env["ir.sequence"].next_by_code("hcu.surgery.protocol") or _("Nuevo"), copy=False, tracking=True)
    institution_id = fields.Many2one("res.partner", string="Institución del Sistema", tracking=True)
    health_center_id = fields.Many2one("res.partner", string="Establecimiento de Salud", tracking=True)
    file_number = fields.Char(string="Número de Archivo", tracking=True)
    unique_medical_record = fields.Char(string="Número de Historia Clínica Única", tracking=True)
    unicodigo = fields.Char(string="UNICÓDIGO", tracking=True)

    # Paciente
    patient_id = fields.Many2one("res.partner", string="Paciente", domain=[("is_company","=",False)], tracking=True, required=True)
    age = fields.Integer(string="Edad", tracking=True)
    age_condition = fields.Char(string="Condición Edad (marcar)", help="Campo libre para replicar las casillas del formulario (p.ej. AD, etc.).")
    sex = fields.Selection([("m","Masculino"),("f","Femenino"),("o","Otro/No especifica")], string="Sexo", tracking=True)

    # Fechas y horas
    surgery_date = fields.Date(string="Fecha de Operación", tracking=True)
    datetime_start = fields.Datetime(string="Hora de Inicio", tracking=True)
    datetime_end = fields.Datetime(string="Hora de Terminación", tracking=True)

    # Diagnósticos
    preop_diagnosis = fields.Text(string="Diagnóstico Preoperatorio", tracking=True)
    preop_cie = fields.Char(string="CIE Preop")
    postop_diagnosis = fields.Text(string="Diagnóstico Postoperatorio", tracking=True)
    postop_cie = fields.Char(string="CIE Postop")

    # Procedimiento (Electiva/Emergencia/Urgencia)
    procedure_urgency = fields.Selection([("electiva","Electiva"), ("emergencia","Emergencia"), ("urgencia","Urgencia")], string="C. Procedimiento", tracking=True)
    procedure_projected = fields.Text(string="Procedimiento Proyectado")
    procedure_done = fields.Text(string="Procedimiento Realizado")
    procedure_other = fields.Char(string="Otros (Procedimiento)")

    # Integrantes del equipo quirúrgico
    surgeon1_id = fields.Many2one("res.partner", string="Cirujano 1", domain=[("is_company","=",False)])
    surgeon2_id = fields.Many2one("res.partner", string="Cirujano 2", domain=[("is_company","=",False)])
    first_assistant_id = fields.Many2one("res.partner", string="Primer Ayudante", domain=[("is_company","=",False)])
    second_assistant_id = fields.Many2one("res.partner", string="Segundo Ayudante", domain=[("is_company","=",False)])
    third_assistant_id = fields.Many2one("res.partner", string="Tercer Ayudante", domain=[("is_company","=",False)])
    anesthesiologist_id = fields.Many2one("res.partner", string="Anestesiólogo/a", domain=[("is_company","=",False)])
    anesthesia_assistant_id = fields.Many2one("res.partner", string="Ayudante Anestesia", domain=[("is_company","=",False)])
    instrument_nurse_id = fields.Many2one("res.partner", string="Instrumentista", domain=[("is_company","=",False)])
    circulating_nurse_id = fields.Many2one("res.partner", string="Circulante", domain=[("is_company","=",False)])

    # Tipo de anestesia
    anesthesia_type = fields.Selection([("general","General"), ("regional","Regional")], string="Tipo de Anestesia")
    sedation = fields.Boolean(string="Sedación")
    anesthesia_other = fields.Char(string="Otros (Anestesia)")

    # Tiempos quirúrgicos y descripción
    dieresis = fields.Text(string="F. Tiempos Quirúrgicos - Dieresis")
    exposure_exploration = fields.Text(string="F. Tiempos Quirúrgicos - Exposición y Exploración")
    surgical_procedure_desc = fields.Text(string="Procedimiento Quirúrgico - Descripción")
    surgical_findings = fields.Text(string="Hallazgos Quirúrgicos")

    # Complicaciones y pérdidas
    complications = fields.Text(string="G. Complicaciones del Procedimiento")
    blood_loss_total_ml = fields.Float(string="Pérdida Sanguínea Total (ml)")
    bleeding_approx_ml = fields.Float(string="Sangrado Aproximado (ml)")
    prosthetic_material_used = fields.Boolean(string="Uso de Material Protésico")
    description_pro = fields.Char(string="Descripcion")
    # Exámenes histopatológicos
    frozen_biopsy = fields.Boolean(string="Biopsia por congelación")
    frozen_biopsy_result = fields.Char(string="Resultado (congelación)")
    histopathology = fields.Boolean(string="Histopatológico")
    histopathology_sample = fields.Char(string="Muestra")
    reporting_pathologist_id = fields.Many2one("res.partner", string="Patólogo que reporta", domain=[("is_company","=",False)])

    # Diagrama del procedimiento
    procedure_diagram = fields.Image(string="I. Diagrama del Procedimiento", max_width=1920, max_height=1920)

    # Profesional responsable
    responsible_id = fields.Many2one("res.partner", string="Profesional Responsable", domain=[("is_company","=",False)], tracking=True)
    responsible_specialty = fields.Char(string="Especialidad")
    responsible_doc_number = fields.Char(string="N° Documento Identificación")
    responsible_stamp = fields.Binary(string="Sello/Firma (opcional)")
    team_other = fields.Char(string="Otros (Equipo Quirúrgico)")
    # Auxiliares
    notes = fields.Text(string="Notas")