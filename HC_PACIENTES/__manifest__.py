{
    'name': 'Pacientes',
    'version': '1.0',
    'summary': 'Gestión de pacientes médicos y su información clínica',
    'description': """
Módulo para registrar y gestionar pacientes en el sistema.

Características:
- Registro completo de datos personales del paciente
- Número de historia clínica, contacto, sexo y edad
- Relación con instituciones de salud
- Base para formularios médicos o evaluaciones clínicas
""",
    'category': 'Human Resources',
    'author': 'Randy Ciprian',
    'depends': ['base','mail'],
    'data': [
        'views/form_view.xml',
        'views/tree_view_pacientes.xml',
        'views/action_pacientes.xml',
        'views/menu.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
