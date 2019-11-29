#!/usr/bin/python
# -*- coding: utf-8 -*-

class CommandDef:
    __slots__ = (
        'name', 'alias', 'description', 'usage'
    )

    def __init__(self, name=None, alias=None, description=None, usage=None):
        self.name = name
        self.alias = alias
        self.usage = usage
        self.description = description

    def __repr__(self):
        return 'CommandDef(name=%r, alias=%r, description=%r, usage=%r)' % (
            self.name, self.alias, self.description, self.usage)

class VariableDef:
    __slots__ = (
        'name', 'alias', 'description', 'type', 'default',
        'select', 'representation', 'cheat',
        'name_lower'
    )

    def __init__(self,
            name=None, alias=None, description=None, type=None, default=None,
            select=None, representation=None, cheat=None):
        self.name = name
        self.name_lower = name.lower()
        self.type = type
        self.cheat = cheat
        self.alias = alias
        self.select = select
        self.default = default
        self.description = description
        self.representation = representation

    def __repr__(self):
        return ('VariableDef(name=%r%s%s%s%s%s%s)' % (self.name,
            ((',alias=%r' % self.alias)             if self.alias else ''),
            ((',description=%r' % self.description) if self.description else ''),
            ((',type=%s' % TYPE2STR[self.type])     if self.type else ''),
            ((',default=%r' % self.default)         if self.default else ''),
            ((',representation=%r' % self.representation) if self.representation else ''),
            ((',cheat=%r' % self.cheat)             if self.cheat is not None else '')
        ))
        #return 'VariableDef(name=%r, alias=%r, description=%r, type=%s, default=%r, select=%r, representation=%s, cheat=%r)' % (
        #    self.name, self.alias, self.description, TYPE2STR[self.type], self.default,
        #    self.select, myRepr(self.representation), self.cheat)

