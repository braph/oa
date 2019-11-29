#!/usr/bin/python -B
# -*- coding: utf-8 -*-

'''
Crawl variable descriptions from quake3tweaks.tripod.com
'''

URL   = 'http://quake3tweaks.tripod.com/commands.html'
LABEL = 'quake3tweaks.tripod.com'

import  sys, re
import  requests
from    lxml        import html
from    html2text   import html2text
try:    from pprint import pprint
except: pprint = print

VARIABLES = {}
DEBUG     = '--debug' in sys.argv

try:    src = open('/tmp/commands.html', 'r').read(-1)
except: src = requests.get(URL).content

tree = html.fromstring(src)

def fix_desc(s):
    ''' Fix planked ( parentheses ) '''
    s = s.replace('\n', ' ')
    s = re.sub(r'\(\s+|\s+\)', lambda m: m[0].strip(), s)
    return s

fonts = tree.xpath('.//font[@class="Arial-13pxFF0000n"]')
last  = []
for font in fonts:
    name = font.text.strip('" ')
    desc = font.getnext().text.strip(' "/-')
    desc = fix_desc(desc)
    last.append(name)

    if desc:
        for name in last:
            VARIABLES[name] = dict(name=name, description=desc)
        last = []

if DEBUG:
    for v in VARIABLES.values(): print(v)
else:
    print('#!/usr/bin/python')
    print('# -*- coding: utf-8 -*-')
    print('LABEL = %r' % LABEL)
    print('VARIABLES =', end=' '); pprint(VARIABLES)
