#!/usr/bin/python -B
# -*- coding: utf-8 -*-

''' Parses variables from stupidctf.tk '''

URL   = 'http://stupidctf.tk/cvars'
LABEL = 'stupidctf.tk'

import  sys
import  requests
from    lxml        import html
from    html2text   import html2text
try:    from pprint import pprint
except: pprint = print

VARIABLES = {}
DEBUG     = '--debug' in sys.argv

try:    src = open('/tmp/cvars', 'r').read(-1)
except: src = requests.get(URL).content

tree = html.fromstring(src)

table = tree.xpath('//table')[0]
rows  = table.xpath('.//tr')[1:]
for row in rows:
    columns = row.xpath('.//td')
    try:
        varnames    = columns[0]
        default     = columns[2]
        description = columns[4].text_content().strip()

        varnames = html2text(html.tostring(varnames).decode('UTF-8'))
        varnames = list(map(str.strip, varnames.replace('**', '').strip().split('\n')))

        defaults = html2text(html.tostring(default).decode('UTF-8'))
        defaults = list(map(str.strip, defaults.replace('**', '').strip().split('\n')))

        for varname in varnames:
            try:    default = defaults.pop(0)
            except: default = None
            VARIABLES[varname] = dict(name=varname, description=description, default=default)
    except Exception as e:
        print(e, file=sys.stderr)

if DEBUG:
    for var in VARIABLES.values(): print(var)
else:
    print('#!/usr/bin/python')
    print('# -*- coding: utf-8 -*-')
    print('LABEL = %r' % LABEL)
    print('VARIABLES =', end=' '); pprint(VARIABLES)
