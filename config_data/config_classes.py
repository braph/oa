#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Classes that are used for describing commands and variables.

All classes must provide a method for serialization to python primitives.
'''

import json

TYPE2STR = {bool:'bool', int:'int', float:'float'}
STR2TYPE = {'bool':bool, 'int':int, 'float':float}

class CommandDefinition:
    __slots__ = 'name', 'description', 'usage', 'alias',

    def __init__(self, name=None, description=None, usage=None, alias=None):
        self.name        = name
        self.description = description
        self.usage       = usage
        self.alias       = alias

    def __repr__(self):
        return 'CommandDefinition(name=%r%s%s%s)' % (self.name,
            ((',description=%r' % self.description) if self.description else ''),
            ((',usage=%r'       % self.usage)       if self.usage       else ''),
            ((',alias=%r'       % self.alias)       if self.alias       else '')
        )

    def serialize(self):
        d = {'name': self.name}
        if self.description:    d['description'] = self.description
        if self.usage:          d['usage']       = self.usage
        if self.alias:          d['alias']       = self.alias
        return d

class VariableDefinition:
    __slots__ = ('name', 'name_lower', 'alias', 'description', 'type', 'default',
                 'select', 'representation', 'cheat', 'force')

    def __init__(self, name=None, alias=None, description=None, type=None,
            default=None, select=None, representation=None, cheat=None, force=()):
        self.name           = name
        self.name_lower     = name.lower()
        self.cheat          = cheat
        self.alias          = alias
        self.select         = select
        self.description    = description
        self.representation = representation
        self.force          = force

        if isinstance(select, dict):
            select_type = select.get('type', None)
            if select['type'] == 'values':
                select = Values(select['values'])
            elif select['type'] == 'range':
                select = Range(select['start'], select['stop'], select['increment'])
            else:
                raise Exception('%r Invalid `type` for select: %r' % (name, select_type))
        self.select = select

        if isinstance(type, str):
            type = STR2TYPE[type]

        # We allow to use all types for `default`, but in the end we cast to `str` (or None)
        if default is not None:
            if default in (True,False):
                default = int(default)
            default = str(default)

        self.default = default
        self.type    = type

    def __repr__(self):
        return ('VariableDefinition(name=%r%s%s%s%s%s%s%s)' % (self.name,
            ((',alias=%r'          % self.alias)          if self.alias             else ''),
            ((',description=%r'    % self.description)    if self.description       else ''),
            ((',type=%s'           % TYPE2STR[self.type]) if self.type              else ''),
            ((',default=%r'        % self.default)        if self.default           else ''),
            ((',representation=%r' % self.representation) if self.representation    else ''),
            ((',cheat=%r'          % self.cheat)          if self.cheat is not None else ''),
            ((',select=%r'         % self.select)         if self.select            else '')
        ))

    def serialize(self):
        d = {'name':self.name}
        if self.alias:              d['alias']          = self.alias
        if self.description:        d['description']    = self.description
        if self.type:               d['type']           = TYPE2STR[self.type]
        if self.default:            d['default']        = self.default
        if self.representation:     d['representation'] = self.representation
        if self.cheat is not None:  d['cheat']          = self.cheat
        if self.select:             d['select']         = self.select.serialize()
        return d

class Values:
    ''' Used in VariableDefinition.select '''

    type      = 'values'
    __slots__ = 'values'

    def __init__(self, values):
        self.values = values

    def __repr__(self):
        return 'Values(%r)' % (self.values,)

    def serialize(self):
        return {
            'type':     'values',
            'values':   self.values
        }

class Range:
    ''' Used in VariableDefinition.select '''

    type      = 'range'
    __slots__ = 'start', 'stop', 'increment'
    def __init__(self, start=None, stop=None, increment=1):
        self.start, self.stop, self.increment = start, stop, increment

    def __repr__(self):
        return 'Range(start=%r, stop=%r, increment=%r)' % (self.start, self.stop. self.increment)

    def serialize(self):
        return {
            'type':      'range',
            'start':     self.start,
            'stop':      self.stop,
            'increment': self.increment
        }

class Source:
    def __init__(self, label, variables, commands):
        self.label     = label
        self.variables = { n.lower(): VariableDefinition(**k) for n,k in variables.items() }
        self.commands  = { n.lower(): CommandDefinition(**k)  for n,k in commands.items() }

    @staticmethod
    def fromJsonFile(file):
        with open(file, 'r') as f:
            d = json.load(f)
        return Source(d['label'], d['variables'], d['commands'])

    def serialize(self):
        return {
            'label': self.label,
            'variables': { n.lower(): v.serialize() for n,v in self.variables.items() },
            'commands':  { n.lower(): c.serialize() for n,c in self.commands.items() }
        }

