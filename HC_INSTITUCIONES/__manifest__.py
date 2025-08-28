{
    'name': 'Instituciones',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Registro de instituciones y empresas vinculadas',
    'description': """
Módulo para registrar instituciones o empresas en las que se realizan evaluaciones médicas u otras actividades laborales.

Permite gestionar:
- Datos generales de la empresa
- Información relevante para formularios médicos
- Relación con pacientes y certificados
""",
    'author': 'Randy Ciprian',
    'depends': ['base'],
    'data': [
        'views/form_view.xml',
        'views/tree_view.xml',
        'views/action_instituciones.xml',
        'views/menu.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
