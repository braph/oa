#!/usr/bin/python
# -*- coding: utf-8 -*-

from widgets.texteditcolored import *

app = QApplication(sys.argv)
app.setApplicationName("Quake Name Editor")
QIcon.setThemeName('oxygen')
window = TextEditColored()
app.exec_()
