#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Merge command descriptions from multiple sources into one
'''

import sys
from libmk import *
import net.joz3d as joz3d
import oaconfigurator.commands as oaconfigurator

# @EXPORT
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
# @END

COMMANDS = {}

for source in (oaconfigurator, joz3d):
    for source_cmd in source.COMMANDS.values():
        if source_cmd['name'] not in COMMANDS:
            COMMANDS[source_cmd['name']] = CommandDef(
                name        = source_cmd['name'],
                description = '[%s]\n%s' % (source.LABEL, (source_cmd['description'] or '').strip()),
                alias       = source_cmd.get('alias', None),
                usage       = source_cmd.get('usage', None)
            )
        else:
            cmd = COMMANDS[source_cmd['name']]
            if 'alias' in source_cmd: cmd.alias = source_cmd['alias'] # Always overwrite
            if 'usage' in source_cmd: cmd.usage = source_cmd['usage'] # Always overwrite
            if 'description' in source_cmd:
                if not cmd.description:
                    cmd.description = source_cmd['description']
                else:
                    cmd.description += '\n\n[%s]\n%s' % (source.LABEL, source_cmd['description'])

export_begin(sys.argv[0], 'Availabe commands')
export(sys.argv[0])
export_variable('COMMANDS', COMMANDS)
