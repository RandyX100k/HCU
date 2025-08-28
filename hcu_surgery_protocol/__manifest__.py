# -*- coding: utf-8 -*-
{
    "name": "HCU Surgery Protocol (SNS-MSP/HCU-form.017/2021)",
    "summary": "Protocolo quirúrgico con campos basados en el formulario oficial",
    "author": "Randy Ciprian",
    "website": "https://example.com",
    "depends": ["base", "contacts", "mail"],
    "data": [
    "security/ir.model.access.csv",
    "data/sequence.xml",
    "report/hcu_report_templates.xml",
    "report/hcu_report_report.xml",
    "views/surgery_protocol_views.xml",
    ],

    "assets": {},
    "application": True,
    "license": "OPL-1",
}