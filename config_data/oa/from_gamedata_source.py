#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys, re, json

'''
Collects variables from OA source, including variable type and default value.

Get the source from https://github.com/OpenArena/gamecode.

Usage:
$ ./parse_source.py ./gamecode/code/**/*.c
'''

LABEL = 'Openarena Source Code'

# typedef struct {
#   vmCvar_t *vmCvar;
#   char     *cvarName;
#   char     *defaultString;
#   int      cvarFlags;
#   ...
# } cvarTable_t;
#
# static cvarTable_t gameCvarTable[] = {
#   {
#    &g_gametype, "g_gametype", "0",
#    CVAR_SERVERINFO | CVAR_USERINFO | CVAR_LATCH, 0, qfalse
#   },
#
# XXX: Maybe we could also take this into account:
# trap_Cvar_SetValue( "g_spSkill", (float)skill );
# trap_Cvar_SetValue( "cg_crosshairColorRed", ((float)s_preferences.crosshairColorRed.curvalue)/255.f );

class StructMember: # 'Enum'
    SOURCE_NAME = 0
    VARNAME     = 1
    DEFAULT     = 2
    FLAGS       = 3
IDENTIFIER  = r'\w[\w\d_]+'
WS          = re.compile(r'\s+')
RE_IGN_WHITESPACES = lambda p: re.compile(WS.sub(r'\\s*', p), re.VERBOSE)

warn         = lambda *a,**kw: print('WARNING', *a,**kw,file=sys.stderr)
debug        = lambda *a,**kw: print('DEBUG',   *a,**kw,file=sys.stderr)
isFloat      = re.compile('\d+\.\d+').fullmatch
typeToString = {int:'int', float:'float', bool:'bool', None:'None'}.get

class VariableDef:
    __slots__ = ('source_name', 'name', 'default', 'cheat', 'type')
    def __init__(self, source_name, name, default, cheat, type):
        self.source_name = source_name
        self.name        = name
        self.default     = default
        self.cheat       = cheat
        self.type        = type

    def __repr__(self):
        return "{'name': %r, 'default': %r, 'cheat': %r, 'type': %s}" % (
            self.name, self.default, self.cheat, typeToString(self.type))

    def toDict(self):
        d = {   'name':     self.name,
                'default':  self.default,
                'cheat':    self.cheat      }
        if self.type:
            d['type'] = typeToString(self.type)
        return d

def parseInitializer(s):
    values = []
    it = iter(s)
    start = False
    for c in it:
        if c == '{':
            start = True
            break

    if not start:
        raise Exception("Could not parse initializer, missing `{`", s)

    val = ''
    quoted = False

    for c in it:
        if quoted:
            if c == '\\':
                val += c
                val += next(it)
            else:
                if c == '"': quoted = False
                val += c
        else:
            if c in ' \t\n':
                pass
            elif c == '"':
                quoted = True
                val += c
            elif c == ',':
                values.append(val)
                val = ''
            elif c == '}':
                values.append(val)
                break
            else:
                val += c

    return values

#p_find_cvarTable = re.compile(r'cvarTable_t .* \{', re.VERBOSE|re.DOTALL)
def get_defined_cvars(iterable_lines):
#    while True:
#        idx = src.find('cvarTable_t')
#        if idx == -1:
#            return

#static cvarTable_t gameCvarTable[] = {
    
    fh = iter(iterable_lines)

    found = False
    for line in fh:
        if 'cvarTable_t' in line:
            found = True
            break

    if not found:
        return
        #raise Exception("cvarTable_t[] not found")

    for line in fh:
        line = line.strip()
        if line == '};':
            break
        if not line.startswith('{'):
            continue

        vals = parseInitializer(line)
        if vals:
            if 'CVAR_ROM' in vals[StructMember.FLAGS]:
                continue

            cheat = 'CVAR_CHEAT' in vals[StructMember.FLAGS]
            yield VariableDef(
                vals[StructMember.SOURCE_NAME].lstrip('&'),
                vals[StructMember.VARNAME].strip('"'),
                vals[StructMember.DEFAULT].strip('"'),
                cheat, None)

def add_cvar_type(cvars, *sources):
    find_var_member = re.compile(r'(\w[\w\d_]+)\.(value|integer)').finditer
    source = ''.join(sources) # act on one big string

    # Find all <var>.integer and <var>.value and count on integer/value
    variables = {}
    for m in find_var_member(source):
        if not m[1] in variables:
            variables[m[1]] = {'value':0, 'integer':0}
        variables[m[1]][m[2]] += 1

    # Find all var.integer in a switch statement
    variables_in_switch = set([
        m[1] for m in RE_IGN_WHITESPACES(
            r'switch \( (\w[\w\d_]+).integer \)'
        ).finditer(source)
    ])

    # Find all var.integer that evaluated as bool
    variables_as_bool = set([
        (m[1] or m[2]) for m in RE_IGN_WHITESPACES(fr'''
            (?:\(|&&|\|\|)   (?### PAREN_OPEN, &&, ||  ###)
               !? ({IDENTIFIER}).integer|({IDENTIFIER}).integer (!=|==) [10]
            (?:\)|&&|\|\|)   (?### PAREN_CLOSE, &&, || ###)
            '''
        ).finditer(source)
    ])

    # Find all comparisions
    variable_comparisions = {}
    p = RE_IGN_WHITESPACES(fr'''
        ({IDENTIFIER}).integer (!=|==|>=|>|<=|<) (\w+)''')
    for m in p.finditer(source):
        if not m[1] in variable_comparisions:
            variable_comparisions[m[1]] = [ (m[2], m[3]) ]
        else:
            variable_comparisions[m[1]].append( (m[2], m[3]) )

    #debug('Found variables', variables)
    #debug('Variables in switch', variables_in_switch)
    #debug('Possible booleans', variables_as_bool)
    #debug('Comparisons', variable_comparisions)

    for cvar in cvars:
        if cvar.name in variables:
            count = variables[cvar.name]

            if count['value'] > 0 and count['integer'] > 0:
                if isFloat(cvar.default):
                    cvar.type = float # The default looks like float.
                else:
                    # Take the type of the most used member, prefer float
                    warn('Unsure about', cvar.name, count)
                    cvar.type = int if count['integer'] > count['value'] else float
            elif count['value'] > 0:
                cvar.type = float
            else:
                cvar.type = int

            if cvar.type is int: # Maybe it's used as a boolean
                if not cvar.name in variables_as_bool:
                    debug(cvar.name, 'non-bool: not used as a bool expression')
                    continue
                if cvar.default != '1' and cvar.default != '0':
                    debug(cvar.name, 'non-bool: default is', cvar.default)
                    continue
                if cvar.name in variables_in_switch:
                    debug(cvar.name, 'non-bool: found in switch')
                    continue

                isbool = True
                for op, value in variable_comparisions.get(cvar.name, []):
                    if op in ('==', '!='):
                        if value not in ('1', '0'):
                            debug(cvar.name, 'non-bool: comparision', op, value)
                            isbool = False
                            break
                    elif op in ('<', '>', '<=', '>='):
                        debug(cvar.name, 'non-bool: comparision', op, value)
                        isbool = False
                        break
                    else:
                        raise Exception('Unproccesed', op, value)

                if not isbool:
                    continue

                debug(cvar.name, 'BOOL')
                cvar.type = bool

# =============================================================================
# Main
# =============================================================================

# Read all input sources.
# Build a dictionary of cvars with tuple (source_name, name) as key.
# Sometimes a variable name is used in multiple source_names:
#     .-- source_name    .-- name
#  { &cg_drawCrosshair, "cg_drawCrosshair", "4", CVAR_ARCHIVE}
#  { &ui_drawCrosshair, "cg_drawCrosshair", "4", CVAR_ARCHIVE}
# Saving both variants gives us the possibility to determine the variable type
# more accurate.
VARIABLES = {}
all_sources = []
for f in sys.argv[1:]:
    with open(f, 'r') as fh:
        source = fh.read()
        all_sources.append(source)

    VARIABLES.update({(v.source_name,v.name):v for v in get_defined_cvars(source.split('\n')) })

# CVars have been collected, now determine type
add_cvar_type(VARIABLES.values(), *all_sources)

# Now reduce the CVars to `name`. The definition which has a `type` set wins.
old_VARIABLES = VARIABLES
VARIABLES = {}
for source_and_var_name, cvar in old_VARIABLES.items():
    source_name, name = source_and_var_name
    if name in VARIABLES:
        if VARIABLES[name].type is None and cvar.type is not None:
            VARIABLES[name] = cvar
    else:
        VARIABLES[name] = cvar

# Print out results
json.dump({
    'label':     LABEL,
    'variables': { k: v.toDict() for k, v in VARIABLES.items() },
    'commands':  {}
}, sys.stdout, indent=1)

