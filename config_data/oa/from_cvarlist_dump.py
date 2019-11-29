#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

'''
Parse cvar defaults and flags from /cvarlist command.
'''

import sys, re, json
LABEL       = 'Openarena /cvarlist command'
VARIABLES   = {}

try:    file = sys.argv[1]
except: file = 'cvardump.out'

parse = re.compile(r'([A-Za-z\?\s]*) \s+ ([\w\d_]+) \s+ "([^\n"]*)', re.VERBOSE).match
parse_flags = re.compile(r'\w\?').findall

with open(file, 'r') as fh:
    for l in fh:
        if l.startswith('CVARLIST_BEGIN'):
            break

    for l in fh:
        if 'total cvars' in l: break
        m = parse(l)
        if not m:
            print('Not parsed:', l, end='', file=sys.stderr)
            continue

        flags   = parse_flags(m[1])
        name    = m[2]
        default = m[3]
        VARIABLES[name] = dict(name=name, default=default, cheat=('C' in flags))

#for v in VARIABLES.values(): print(v)

# Print out results
json.dump({
    'label':     LABEL,
    'variables': VARIABLES,
    'commands':  {}
}, sys.stdout, indent=1)

