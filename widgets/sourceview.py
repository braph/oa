#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import sys, re, os, signal, hashlib

from PyQt5.QtGui            import *
from PyQt5.QtCore           import *
from PyQt5.QtWidgets        import *

from q3.q3path              import *
from q3.q3colors            import *
from q3.q3config            import *
from settings               import *

from config_data.data       import *
from config_data.values     import *

FMT_COLOR  = '<span style="color:%s">%s</span>'
debug      = lambda *a,**kw: print(*a, **kw)

def entities(s):
    return s.replace('&','&amp;').replace('"','&quot;').replace('<','&lt;').replace('>','&gt;')

class SourceView(QWidget):
    def __init__(self, q3config):
        super(SourceView, self).__init__()
        self.q3config  = q3config
        self.edtSource = QTextEdit()
        self.edtSource.setFont(QFont('Monospace', 10))
        l = QVBoxLayout()
        l.addWidget(self.edtSource)
        self.setLayout(l)
        self.onShow()

    def onShow(self, needs_update=True):
        #if not needs_update: return
        cursor = self.edtSource.textCursor()
        colors = ['orange','red','blue','black']
        txt    = ''
        nword  = 0
        for token in self.q3config:
            if isinstance(token, TComment):
                txt += FMT_COLOR % ('gray', str(token))
                nword = 0
            elif isinstance(token, TNewline):
                txt += '<br>'
                nword = 0
            elif isinstance(token, TWhitespace):
                txt += token.s.replace('\t', ' '*8).replace(' ', '&nbsp;')
            else:
                try:    color = colors[nword]
                except: color = colors[-1]
                txt += FMT_COLOR % (color, entities(str(token)))
                nword += 1

        #self.edit.document().findBlockByLineNumber(line))

        self.edtSource.setHtml(txt)
        self.edtSource.setTextCursor(cursor)
        #self.edtSource.scrollToAnchor(an)

    def onHide(self):
        if str(self.q3config) != self.edtSource.toPlainText():
            _ = Q3Config.from_string(self.edtSource.toPlainText())
            self.q3config.token = _.token # TODO
            debug('SourceView changed content')
        else:
            debug('SourceView did not change content')


