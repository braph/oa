#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO

from PyQt5.QtGui            import *
from PyQt5.QtCore           import *
from PyQt5.QtWidgets        import *

class BindingsView(QWidget):
    def __init__(self, q3config):
        super().__init__()
        self.q3config = q3config
        l = QHBoxLayout()

        self.e = e = QLineEdit()
        def foo(t):
            self.e.clearFocus()
            pass
        e.textChanged.connect(foo)
        l.addWidget(e)

        e = QLineEdit()
        e.textChanged = lambda e: print(e)
        l.addWidget(e)

        self.setLayout(l)

    def onHide(self):
        pass

    def onShow(self, needs_update):
        pass

