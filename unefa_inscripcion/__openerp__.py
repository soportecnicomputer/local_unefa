# -*- coding: utf-8 -*-
##############################################################################
#
#    Programa realizado por, Jeison Pernía y Jonathan Reyes en el marco
#    del plan de estudios de la UNEFA, como TRABAJO ESPECIAL DE GRADO,
#    con el fin de optar al título de Ingeniero de Sistemas.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generated by the OpenERP plugin for Dia !
#
{
    'name': 'Inscripción del Semestre',
    'version': '1.0',
    'depends': ['base','unefa_configuracion','unefa_pensum','unefa_usuarios','unefa_planificacion_semestre','unefa_convalidacion'],
    'authors': 'Jeison Pernía y Jonathan Reyes',
    'category': 'Configuración Técnica',
    'description': """
    Este módulo gestiona el proceso de inscripcion, oferta academica y generacion de secciones y horarios.
    """,
    'update_xml': [],
    "data" : [
        'views/inscripcion/unefa_inscripcion_view.xml',
        'views/oferta_academica/unefa_oferta_academica_view.xml',
        'views/horario/unefa_horario_view.xml',
        'security/group_unefa_admin/ir.model.access.csv',
        'security/group_unefa_coor/ir.model.access.csv',
        'security/group_unefa_est/ir.model.access.csv',
        'security/group_unefa_eval/ir.model.access.csv',
        'security/group_unefa_prof/ir.model.access.csv',
        'security/group_unefa_secret/ir.model.access.csv',
        ],
    'installable': True,
    'auto_install': False,
}

