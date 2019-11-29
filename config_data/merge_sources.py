#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Merge variable and command definitions from from multiple sources into one
'''

import sys
from re import compile as RE
from libmk          import *
from values         import *
from config_classes import *

# Sources
merged          = Source('merged', {}, {})
joz3d           = Source.fromJsonFile('net/joz3d.json')
quake3tweaks    = Source.fromJsonFile('net/quake3tweaks.json')
stupidctf       = Source.fromJsonFile('net/stupidctf.json')
cvarlist        = Source.fromJsonFile('oa/cvarlist.json')
source_vars     = Source.fromJsonFile('oa/source_vars.json')
oaconfigurator  = Source.fromJsonFile('oaconfigurator/oaconfigurator.json')
all_sources     = joz3d, quake3tweaks, stupidctf, cvarlist, source_vars, oaconfigurator

# Funcs
count_upper = lambda s,f=RE('[A-Z]').findall: len(f(s))
is_float    = RE(r'\d+\.\d+').fullmatch
is_str      = RE(r'\D').search

# =============================================================================
#                         Find best name for a variable
# =============================================================================

best_names = {}
def find_best_names(source):
    to_drop = []
    for lower, var in source.variables.items():
        if not var.name or len(var.name) < 3:
            warn('Dropping strange variable %r coming from %r' % (var.name, source.label))
            to_drop.append(lower)
            continue

        if lower not in best_names:
            best_names[lower] = var.name
        else:
            count_old = count_upper(best_names[lower])
            count_new = count_upper(var.name)
            if count_old < count_new: # prefer camelCase names
                info('VAR (%s): %r is better name than %r' %(source.label, var.name, best_names[lower]))
                best_names[lower] = var.name
    
    for _ in to_drop: del source.variables[_]

# Find the best variable names
for source in all_sources:
    find_best_names(source)

# Rename all variable names to the best name
for source in all_sources:
    for lower, var in source.variables.items():
        var.name = best_names[lower]

# Start with empty variable definitions
merged.variables = {lower:VariableDefinition(name=name) for lower, name in best_names.items()}
del best_names # no longer needed

# =============================================================================
# DESCRIPTION
# =============================================================================
EMPTY = VariableDefinition(name='')
get_desc            = lambda src, name: src.variables.get(name,EMPTY).description
get_default         = lambda src, name: src.variables.get(name,EMPTY).default
get_cheat           = lambda src, name: src.variables.get(name,EMPTY).cheat
get_type            = lambda src, name: src.variables.get(name,EMPTY).type
get_alias           = lambda src, name: src.variables.get(name,EMPTY).alias
get_representation  = lambda src, name: src.variables.get(name,EMPTY).representation
get_select          = lambda src, name: src.variables.get(name,EMPTY).select

for lower, var in merged.variables.items():
    name = var.name

    # === DESCRIPTION =========================================================
    # Put togehter all descriptions
    descriptions = []
    for source in oaconfigurator, joz3d, quake3tweaks, stupidctf:
        desc = get_desc(source, lower)
        if desc:
            descriptions.append('[%s]\n%s' % (source.label, desc))

    if descriptions:
        var.description = '\n\n'.join(descriptions)
    # =========================================================================

    # === DEFAULT =============================================================
    # Add the default value. Last definition wins.
    last_source = None
    for source in joz3d, quake3tweaks, stupidctf, cvarlist, source_vars, oaconfigurator:
        default = get_default(source, lower)
        if default:
            if not var.default:
                var.default = default
                last_source = source.label
            elif var.default != default:
                warn('%s: %s overwrites %r to %r (last source: %s)' % (name, source.label, var.default, default, last_source))
                var.default = default
                last_source = source.label

    # === CHEAT ===============================================================
    # Add the cheat flag. Last definition wins.
    last_source = None
    for source in joz3d, quake3tweaks, stupidctf, cvarlist, source_vars, oaconfigurator:
        cheat = get_cheat(source, lower)
        if cheat is not None:
            if var.cheat is None:
                var.cheat = cheat 
                last_source = source.label
            elif var.cheat != cheat:
                warn('%s: %s overwrites cheat %r to %r (last source: %s)' % (name, source.label, var.cheat, cheat, last_source))
                var.cheat = cheat
                last_source = source.label

    # === ALIAS, SELECT, REPRESENTATION =======================================
    # These are only set in `oaconfigurator`
    for source in (oaconfigurator,): # TODO
        var.alias           = get_alias(source, lower)
        var.select          = get_select(source, lower)
        var.representation  = get_representation(source, lower)

    # === TYPE ================================================================
    # Only `source_vars` and `oaconfigurator` have `type`, but do not contain all
    # variables.
    # Look at the default value on the variables for determining type.
    last_source = None
    for source in source_vars, oaconfigurator:
        type = get_type(source, lower)
        if type is not None:
            if var.type is None:
                var.type = type
                last_source = source.label
            elif var.type != type:
                warn('%s: %s overwrites type %r to %r (last source: %s)' % (name, source.label, var.type, type, last_source))
                var.type = type
                last_source = source.label

    if var.type is None and var.default is not None:
        if is_float(var.default):
            info('Setting type of %r to float (%r)' % (name, var.default))
            var.type = float
        #elif is_int(var.default):
        #    info('Setting type of %r to int (%r)' % (name, var.default))
        #    var.type = int 


# =============================================================================
# Finally, we check everything in the end again
# =============================================================================
for var in merged.variables.values():
    # Check if type and default match
    if var.type is not None:
        try:
            if var.type == bool:
                if var.default not in ('0', '-1', '1'):
                    raise Exception('%s has non boolean default: %s' % (var.name, var.default))
            else:
                var.type(var.default)
        except:
            warn('%s: Maybe got an invalid type/default: %s:%s' % (var.name, var.type, var.default))

    #if var.representation is None:
    #    var.representation = var.type


# =============================================================================
#                                   COMMANDS                                  #
# =============================================================================

for source in (oaconfigurator, joz3d):
    for source_cmd in source.commands.values():
        if source_cmd.name not in merged.commands:
            merged.commands[source_cmd.name] = CommandDefinition(
                name        = source_cmd.name,
                description = '[%s]\n%s' % (source.label, (source_cmd.description or '').strip()),
                alias       = source_cmd.alias,
                usage       = source_cmd.usage
            )
        else:
            cmd = merged.commands[source_cmd.name]
            cmd.alias = source_cmd.alias # Always overwrite
            cmd.usage = source_cmd.usage # Always overwrite
            if source_cmd.description:
                if not cmd.description:
                    cmd.description = source_cmd.description
                else:
                    cmd.description += '\n\n[%s]\n%s' % (source.label, source_cmd.description)


if __name__ == '__main__':
    export_begin(sys.argv[0], 'This file contains all available variables and commands')
    export(sys.argv[0])
    print('from .config_classes import *')
    export_variable('VARIABLES', merged.variables)
    export_variable('COMMANDS',  merged.commands)
