#!/usr/bin/python -B
# -*- coding: utf-8 -*-

'''
Crawl variable and command descriptions from joz3d.net
'''

import  sys, re, json
import  requests
from    lxml        import html
from    html2text   import html2text

LABEL     = 'www.joz3d.net'
URL       = 'http://www.joz3d.net/html/q3console.html'
VARIABLES = {}
COMMANDS  = {}
DEBUG     = '--debug' in sys.argv

try:    src = open('/tmp/q3console.html', 'r').read(-1)
except: src = requests.get(URL).content

tree = html.fromstring(src)

tables = tree.xpath('//table')

def trim_space(s, p=re.compile('\\s+')):
    return p.sub(' ', s.strip())

def fix_desc(s):
    s = trim_space(s)
    if not s: return s
    return '%s%s.' % (s[0:1].upper(), trim_space(s[1:].strip('.')))

def getRows(table):
    return [row.xpath('.//td') for row in table.xpath('.//tr')]

for table in tables:
    tbl_commands  = table.xpath('.//tr/td/p/*/text() = "Console Commands"')
    tbl_variables = table.xpath('.//tr/td/p/*/text() = "Variables"')
    if not tbl_commands and not tbl_variables:
        continue

    rows = getRows(table)[1:]
    for row in rows:
        key = trim_space(row[0].text_content())
        if not key or key in ('Red Font', 'Green Font'):
            continue

        desc = fix_desc(row[1].text_content())
        if not desc:
            continue

        if tbl_commands:
            COMMANDS[key] = dict(name=key, description=desc)
        elif tbl_variables:
            try: 
                key, default = key.split(' ', 1)
                default = default.strip('" ')
            except:
                key, default = key, None

            VARIABLES[key] = dict(name=key, description=desc, default=default)

if DEBUG:
    for var in VARIABLES.values(): print(var)
    for cmd in COMMANDS.values():  print(cmd)
else:
    json.dump({
        'label':     LABEL,
        'variables': VARIABLES,
        'commands':  COMMANDS
    }, sys.stdout, indent=1)
