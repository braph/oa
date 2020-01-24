#!/usr/bin/python
# -*- coding: utf-8 -*-

# 138, 139 <<< ????
# TODO: Clean this up. This is test code!

from widgets.texteditcolored import *

app = QApplication(sys.argv)
app.setApplicationName("Quake Name Editor")
QIcon.setThemeName('oxygen')
font_id = QFontDatabase.addApplicationFont('q3/q3font/QuakeIII.ttf')
assert font_id >= 0

qfd = QFontDatabase()
defaultSystemFont  = qfd.font('Missing_Font_Returns_Default_System_Font0', '', 14)
defaultSystemFont1 = qfd.font('Missing_Font_Returns_Default_System_Font1', '', 14)
assert defaultSystemFont == defaultSystemFont1
monospaceFont      = qfd.font('Monospace', '', 14)
assert defaultSystemFont != monospaceFont
quakeFont          = qfd.font('QuakeIII', '', 14)
assert defaultSystemFont != quakeFont

sample = ''
for i in range(0, 255):
    if i % 16 == 0:
        sample += '\n'
    sample += chr(i)
sample = sample.strip('\n')
bunny  = '\x1b\x13\x02\x03bunny\x01\x02\x13\x1b \n'
sample += bunny
window = TextEditColored(text=sample)
app.exec_()
