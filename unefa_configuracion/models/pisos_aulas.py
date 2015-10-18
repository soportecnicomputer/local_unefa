# -*- coding: utf-8 -*-
import time
from openerp.osv import fields, osv

class pisos(osv.osv):
    _name='unefa.pisos'
    _rec_name='numero'
    
    _columns={
        'numero':fields.char('Numero de Piso',size=80,required=True,help='Aquí se coloca el nombre del nucleo'),
        'cant_banios':fields.integer('Cantidad de Baños'),
        'cant_filtros':fields.integer('Cantidad de Filtros'),
        'aulas_id':fields.one2many('unefa.aulas','piso_id','Aulas'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...'),
    }
    
    _defaults={
        'active':True,
    }



class aulas(osv.osv):
    _name='unefa.aulas'
    _rec_name='numero'
    
    _columns={
        'numero':fields.char('Numero de Aula',size=80,required=True,help='Aquí se coloca el nombre del nucleo'),
        'tipo':fields.selection([('normal','Normal'),('conferencia','Conferencia')],'Tipo de Aula', required=True, help='Normal o de Conferencia'),
        'cant_pupitres':fields.integer('Cantidad de Pupitres', help="Cantidad de Pupitres que posee"),
        'cant_pizarras':fields.integer('Cantidad de Pizarras', help="Cantidad de Pizarras que posee"),
        'piso_id':fields.many2one('unefa.pisos','Piso'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...'),
    }
    
    _defaults={
        'active':True,
    }
