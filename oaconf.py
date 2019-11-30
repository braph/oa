#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re, os, signal, hashlib

from PyQt5.QtGui            import *
from PyQt5.QtCore           import *
from PyQt5.QtWidgets        import *

from q3.q3path              import *
from q3.q3config            import *

from widgets.sourceview     import *
from widgets.bindingsview   import *
from widgets.variablesview  import *

q3path = Q3Path()

def dialog_critical(widget, title, text):
    QMessageBox.critical(widget, title, text)

class ConfigFileView(QTabWidget):
    def __init__(self, q3config, filename):
        super(ConfigFileView, self).__init__()
        self.q3config   = q3config
        self.filename   = filename
        self.hash       = self.getConfigHash()
        self.hash_start = self.hash
        views           = [
            (VariablesView(q3config), 'Variables'),
            (SourceView(q3config),    'Source'),
            (BindingsView(q3config),  'Bindings')
        ]
        for _ in views: self.addTab(*_)
        self.setCurrentWidget(views[0][0])
        self.lastwidget = views[0][0]
        self.currentChanged.connect(self.on_tab_changed)

    def getConfigHash(self):
        return hashlib.md5(str(self.q3config).encode('UTF-8')).digest()

    def on_tab_changed(self, index):
        self.lastwidget.onHide()
        _ = self.currentWidget()
        hash = self.getConfigHash()
        _.onShow(hash != self.hash)
        self.hash = hash
        self.lastwidget = _

    def modified(self):
        self.currentWidget().onHide() # XXX...
        return self.hash_start != self.getConfigHash()

    def file_save(self):
        if self.filename is None:
            return self.file_saveas()
        try:
            self.q3config.write(self.filename)
            return True
        except Exception as e:
            dialog_critical(self, 'Could not save file', str(e))
        return False

    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", q3path.getUserConfigDir(), "Config (*.cfg);All files (*)")
        if path:
            try:
                self.q3config.write(path)
                return True
            except Exception as e:
                dialog_critical(self, 'Could not save file', str(e))
        return False

class ConfigFileTabs(QTabWidget):
    def __init__(self):
        QTabWidget.__init__(self)
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.on_tab_close)

    def on_tab_close(self, index):
        w = self.widget(index)
        if w.modified():
            r = QMessageBox.question(self, 'Save changes?', 'Save changes to file?',
                                        QMessageBox.Yes|QMessageBox.No|QMessageBox.Cancel)
            if r == QMessageBox.Cancel:
                return
            elif r == QMessageBox.Yes:
                if not w.file_save():
                    return
            elif r == QMessageBox.No:
                pass
        self.removeTab(index)
        w.close()

    def addConfigFileView(self, path):
        _ = ConfigFileView(Q3Config.from_file(path), path)
        self.addTab(_, path)
        self.setCurrentWidget(_)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(0, 0, 700, 600)
        layout = QVBoxLayout()

        self.config_file_tabs =_= ConfigFileTabs()
        _.currentChanged.connect(self.update_title)
        layout.addWidget(self.config_file_tabs)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        file_toolbar = QToolBar("File")
        file_toolbar.setIconSize(QSize(14, 14))
        self.addToolBar(file_toolbar)
        file_menu = self.menuBar().addMenu("&File")

        _ = QAction(QIcon.fromTheme('document-open'), "Open file...", self)
        _.setStatusTip("Open file")
        _.triggered.connect(self.file_open)
        file_menu.addAction(_)
        file_toolbar.addAction(_)

        _ = QAction(QIcon.fromTheme('document-save'), "Save", self)
        _.setStatusTip("Save current config")
        _.triggered.connect(self.file_save)
        file_menu.addAction(_)
        file_toolbar.addAction(_)

        _ = QAction(QIcon.fromTheme('document-save-as') , "Save As...", self)
        _.setStatusTip("Save current config to specified file")
        _.triggered.connect(self.file_saveas)
        file_menu.addAction(_)
        file_toolbar.addAction(_)

        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Edit")

        edit_menu.addSeparator()

        self.update_title()
        self.show()

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open file", q3path.getUserConfigDir(), "Config (*.cfg);All files (*)")
        if path:
            try:
                self.config_file_tabs.addConfigFileView(path)
            except Exception as e:
                dialog_critical(self, 'Could not open file', str(e))

    def update_title(self):
        filename = 'Untitled'
        w = self.config_file_tabs.currentWidget()
        if w and w.filename:
            filename = os.path.basename(w.filename)
        self.setWindowTitle("%s - Openarena Configurator" % (filename,))

    def file_save(self):
        _ = self.config_file_tabs.currentWidget()
        if _: _.file_save()

    def file_saveas(self):
        _ = self.config_file_tabs.currentWidget()
        if _: _.file_saveas()


if __name__ == '__main__':
    #import cProfile
    #pr = cProfile.Profile()
    #pr.enable()

    app = QApplication(sys.argv)
    app.setApplicationName("Openarena Configurator")

    QIcon.setThemeName('oxygen')
    #QIcon.setFallbackThemeName('gnome')
    # Setup the QTextEdit editor configuration XXX
    #fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
    #fixedfont.setPointSize(12)

    window = MainWindow()

    window.config_file_tabs.addConfigFileView('/tmp/foo.cfg')
    #except: pass

    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app.exec_()

    #pr.disable()
    #pr.print_stats()
