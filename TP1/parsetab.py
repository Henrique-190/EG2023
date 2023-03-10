
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "MAIS MENOS NUMEROstart : MAIS intervalos\n             | MENOS intervalosintervalos : intervalo\n                  | intervalo intervalosintervalo : '[' NUMERO ',' NUMERO ']' "
    
_lr_action_items = {'MAIS':([0,],[2,]),'MENOS':([0,],[3,]),'$end':([1,4,5,7,8,12,],[0,-1,-3,-2,-4,-5,]),'[':([2,3,5,12,],[6,6,6,-5,]),'NUMERO':([6,10,],[9,11,]),',':([9,],[10,]),']':([11,],[12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'intervalos':([2,3,5,],[4,7,8,]),'intervalo':([2,3,5,],[5,5,5,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> MAIS intervalos','start',2,'p_start','yacc.py',24),
  ('start -> MENOS intervalos','start',2,'p_start','yacc.py',25),
  ('intervalos -> intervalo','intervalos',1,'p_intervalos','yacc.py',33),
  ('intervalos -> intervalo intervalos','intervalos',2,'p_intervalos','yacc.py',34),
  ('intervalo -> [ NUMERO , NUMERO ]','intervalo',5,'p_intervalo','yacc.py',41),
]
