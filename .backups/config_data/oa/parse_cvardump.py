#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys, re
LABEL       = '/cvarlist'
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
print('#!/usr/bin/python')
print('# -*- coding: utf-8 -*-')
print('LABEL = %r' % LABEL)
print('VARIABLES =', VARIABLES)
