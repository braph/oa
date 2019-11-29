#!/usr/bin/python

import sys, re, os, signal, hashlib

from PyQt5.QtGui            import *
from PyQt5.QtCore           import *
from PyQt5.QtWidgets        import *

from q3.q3path              import *
from q3.q3colors            import *
from q3.q3config            import *
from settings               import *

from config_data.variables  import *
from config_data.commands   import *
from config_data.values     import *

debug = lambda *a,**kw: print(*a, **kw)

FONTS = {}
QT_MAX_INT = ((1<<31)-1)
RE = re.compile
is_int           = RE(r'[+-]?\d+').fullmatch
is_float         = RE(r'[+-]?\d+\.\d+').fullmatch
is_float_list    = RE(r'(:?[+-]?\d+\.\d+(:?\s+|$))+').fullmatch
FMT_COLOR        = '<span style="color:%s">%s</span>'
prefix_dict      = dict(SETTINGS['prefixes'])
prefix_re        = RE('^(%s)' % '|'.join(prefix_dict.keys()))
capitalize_re    = RE(' .|_.')
capitalize = lambda s: capitalize_re.sub(lambda m: ' '+m[0][1].upper(), s)
q3colors         = Q3Colors()
q3colors.addPalette(Q3Colors.QUAKE_PALETTE)
q3colors.addPalette(Q3Colors.FAILMOD_PALETTE)

def varname_reformat(varname):
    ''' Make a variable name more readable '''
    varname = prefix_re.sub(lambda m: '(%s) ' % prefix_dict[m[0]], varname, 1)
    varname = capitalize(varname)
    return varname

def entities(s):
    return s.replace('&','&amp;').replace('"','&quot;').replace('<','&lt;').replace('>','&gt;')

# TODO: Das hat hier nichts zu suchen
def presentWeapon(s):
    return re.sub(r'\d+', lambda m: weaponNo2str(int(m[0])), s)

def presentChrosshair(s):
    try:
        return crosshairNo2str(int(s))
    except ValueError:
        return s

representation = {
    'weapon': presentWeapon,
    'crosshair': presentChrosshair
}
# /TODO

def present(s, vardef, maxlen=30):
    valid   = True
    vartype = vardef.type

    # Check if value corresponds to type
    if vartype is bool:
        valid = s and s in ('0','-1')
    elif vartype is not None:
        try: vartype(s)
        except:
            valid = False
            print(vardef.name, 'invalid value', s)

    if vardef.representation is not None:
        try:    s = representation[vardef.representation](s)
        except: valid = False

    if len(s) > maxlen:
        s = s[:maxlen] + '...'

    if vardef.representation is not None:
        if valid:
            s = FMT_COLOR % (SETTINGS['color.special'], s)
    elif vartype is bool:
        if not s or s in ('0','-1'):
            s = '<span style="color:%s">Off</span> (%s)' % (SETTINGS['color.bool.false'], s)
        else:
            s = '<span style="color:%s">On</span> (%s)' % (SETTINGS['color.bool.true'], s)
    elif vartype is int:
        s = FMT_COLOR % (SETTINGS['color.int'], s)
    elif vartype is float:
        s = FMT_COLOR % (SETTINGS['color.float'], s)
    # --- not type specified, colorize it by guess ---
    elif '^' in s: 
        s = q3colors.toHtml(s)
    elif is_int(s):
        s = FMT_COLOR % (SETTINGS['color.maybe.int'], s)
    elif is_float_list(s):
        s = FMT_COLOR % (SETTINGS['color.maybe.float'], s)

    if not valid:
        return '<span style="background:%s"> %s </span>' % (SETTINGS['background.invalid'], s)

    return s

class VariableWidget(QWidget):
    def lostFocus(self, *_):
        widget = self.stackValue.currentWidget()
        if isinstance(widget, QLineEdit):
            self.q3var.setValue(widget.text())
        elif isinstance(widget, QComboBox):
            self.q3var.setValue(widget.currentData())
        elif isinstance(widget, (QSpinBox,QDoubleSpinBox)):
            self.q3var.setValue(str(widget.value()))
        self.updateValue()
        self.valueChanged()

    def mouseDoubleClickEvent(self, _):
        value   = self.q3var.getValue()
        vartype = self.vardef.type
        if vartype is None: # Guess vartype
            if   is_int(value):   vartype = int
            elif is_float(value): vartype = float

        try:
            if vartype is bool:
                if not hasattr(self, 'cmbValue'):
                    self.cmbValue = QComboBox()
                    self.cmbValue.addItem('On', '1')
                    self.cmbValue.addItem('Off', '0')
                    self.cmbValue.addItem('Off (-1)', '-1')
                    self.cmbValue.currentIndexChanged.connect(self.lostFocus)
                    self.stackValue.addWidget(self.cmbValue)
                widget = self.cmbValue
                widget.setCurrentIndex({'1': 0, '0': 1, '-1': 2}.get(value, 0))
            elif vartype is int:
                if not hasattr(self, 'spnIntValue'):
                    self.spnIntValue = QSpinBox()
                    self.spnIntValue.setMaximum(QT_MAX_INT)
                    self.stackValue.addWidget(self.spnIntValue)
                widget = self.spnIntValue
                widget.setValue(int(value))
            elif vartype is float:
                if not hasattr(self, 'spnFloatValue'):
                    self.spnFloatValue = QDoubleSpinBox()
                    self.spnFloatValue.setMaximum(QT_MAX_INT)
                    self.spnFloatValue.setDecimals(6)
                    self.stackValue.addWidget(self.spnFloatValue)
                widget = self.spnFloatValue
                widget.setValue(float(value))
        except Exception as e:
            print('Falling back on line edit:', e)
            vartype = None

        if vartype is None:
            if not hasattr(self, 'edtValue'):
                self.edtValue = QLineEdit('', self)
                self.edtValue.returnPressed.connect(self.lostFocus)
                self.stackValue.addWidget(self.edtValue)
            widget = self.edtValue
            widget.setText(self.q3var.getValue())

        self.stackValue.setCurrentWidget(widget)
        widget.setFocus()

    def valueChanged(self):
        pass
        #GLOBAL.execute(str(self.q3var))

    def updateValue(self):
        value = self.q3var.getValue()
        self.lblValue.setToolTip(value)
        self.lblValue.setText(present(value, self.vardef, 40)) #TODO: const 40
        self.stackValue.setCurrentWidget(self.lblValue)

    def updateLabel(self):
        if self.displayOriginalName:
            self.lblName.setText(self.q3var.getName())
        else:
            # TODO: choose between name from config or real name
            self.lblName.setText(varname_reformat(self.vardef.alias or self.vardef.name))

    def setDisplayOriginalName(self, displayOriginalName):
        self.displayOriginalName = displayOriginalName
        self.updateLabel()

    def __init__(self, q3var):
        super(QWidget, self).__init__()
        vardef = VARIABLES.get(q3var.getName().lower(), None)
        if vardef is None:
            VARIABLES[q3var.getName().lower()] = vardef = VariableDef(q3var.getName())
        self.vardef      = vardef
        self.q3var       = q3var
        self.stackValue  = stackValue = QStackedWidget()
        self.lblName     = lblName    = QLabel()
        self.lblValue    = lblValue   = QLabel()
        self.displayOriginalName      = False

        lblValue.setAlignment(Qt.AlignRight)

        lblName.setToolTip(vardef.description or '')
        lblName.setToolTipDuration(QT_MAX_INT)
        lblName.setFont(FONTS['monospace'])

        stackValue.addWidget(lblValue)

        l = QHBoxLayout()
        l.addWidget(lblName,    alignment=Qt.AlignLeft)
        l.addWidget(stackValue, alignment=Qt.AlignRight)
        l.setContentsMargins(0,0,0,0)
        self.setLayout(l)

        self.updateValue()
        self.updateLabel()

class VariableList(QListWidget):
    def __init__(self, q3config):
        super().__init__()
        self.q3config = q3config
        self.setStyleSheet("QListWidget {padding: 0;} QListWidget::item { margin: 0 7px; padding: 0; }");
        self.search = self.prefix = ''
        self.currentItemChanged.connect(self.onCurrentItemChanged)
        self.reload()
        self.setUniformItemSizes(True) # XXX

    def reload(self):
        self.clear()
        self.items = []
        for var in self.q3config.yieldVariables():
            widget = VariableWidget(var)
            item = QListWidgetItem()
            self.addItem(item)
            self.setItemWidget(item, widget)
            item.setSizeHint(widget.sizeHint())
            self.items.append(item)
        self.updateView()

    def onCurrentItemChanged(self, new, old):
        if old: self.itemWidget(old).lostFocus()
        #if new: self.itemWidget(new).mouseDoubleClickEvent(None)

    def setDisplayOriginalName(self, boolean):
        for item in self.items:
            self.itemWidget(item).setDisplayOriginalName(not not boolean)

    def setSearch(self, search):
        self.search = search.lower()
        self.updateView()

    def setPrefix(self, prefix):
        self.prefix = prefix
        self.updateView()

    def updateView(self):
        # There's no way to sort the list except using the `data` attribute
        # of QListWidgetItem. Setting `data` however results in displaying
        # the text AND the itemWidget. Solution: setData() temporary for sort
        # and clear it afterwards.
        search = self.search
        prefix = self.prefix
        for item in self.items:
            widget = self.itemWidget(item)
            name   =  widget.vardef.name_lower
            alias  = (widget.vardef.alias or '').lower()
            desc   = (widget.vardef.description or '').lower()
            self.setRowHidden(self.row(item), not ( # Positive match:
                (name.startswith(prefix) or alias.startswith(prefix)) and
                (search in name or search in desc)
            ))
            item.setData(0, alias or name)

        self.sortItems(Qt.AscendingOrder)
        for item in self.items: item.setData(0, '')

class C_View(QWidget):
    def __init__(self, q3config):
        super().__init__()
        self.q3config     = q3config
        #self.last_changed = q3config.changed TODO

    def onHide(self):pass
    def onShow(self,_):pass

class VariablesView(QWidget):
    def __init__(self, q3config):
        super().__init__()
        self.q3config     = q3config
        self.edtSearch    = edtSearch   = QLineEdit()
        self.cmbCategory  = cmbCategory = QComboBox()
        self.chkRealname  = chkRealname = QCheckBox('Variables')
        self.variableList = VariableList(q3config)

        edtSearch.setPlaceholderText('Search...')
        edtSearch.setClearButtonEnabled(True)
        edtSearch.textChanged.connect(self.variableList.setSearch)

        chkRealname.stateChanged.connect(self.variableList.setDisplayOriginalName)
        cmbCategory.addItem('All', '')
        for prefix, label in SETTINGS['prefixes']:
            cmbCategory.addItem(label, prefix)
        cmbCategory.currentIndexChanged.connect(
            lambda: self.variableList.setPrefix(self.cmbCategory.currentData()))

        header = QWidget()
        _ = QHBoxLayout()
        _.addWidget(edtSearch)
        _.addWidget(cmbCategory)
        _.addWidget(chkRealname)
        header.setLayout(_)

        _ = QVBoxLayout()
        _.addWidget(header)
        _.addWidget(self.variableList)
        self.setLayout(_)

    def onHide(self): pass

    def onShow(self, needs_update):
        if needs_update:
            debug('Reloading Variable View')
            self.variableList.reload()
        else:
            debug('Wont relaod Variable View')

class SourceView(C_View):
    def __init__(self, q3config):
        super().__init__(q3config)
        self.edtSource = QTextEdit()
        self.edtSource.setFont(FONTS['monospace'])
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


class BindingsView(C_View):
    def __init__(self, q3config):
        super().__init__(q3config)
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


class ConfigFileView(QTabWidget):
    def __init__(self, q3config, filename):
        super().__init__()
        self.q3config   = q3config
        self.filename   = filename
        self.hash       = self.getConfigHash()
        views = [   (VariablesView(q3config), 'Variables'),
                    (SourceView(q3config),   'Source'),
                    (BindingsView(q3config), 'Bindings')    ]
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


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setGeometry(0, 0, 700, 600)
        layout = QVBoxLayout()

        # Q3Variables
        self.config_file_tabs = config_file_tabs = QTabWidget()
        layout.addWidget(config_file_tabs)

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
        _.setStatusTip("Save current page")
        _.triggered.connect(self.file_save)
        file_menu.addAction(_)
        file_toolbar.addAction(_)

        _ = QAction(QIcon.fromTheme('document-save-as') , "Save As...", self)
        _.setStatusTip("Save current page to specified file")
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

    def dialog_critical(self, s):
        _ = QMessageBox(self)
        _.setText(s)
        _.setIcon(QMessageBox.Critical)
        _.show()

    def file_open(self): # TODO: open(rU)
        path, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Config (*.cfg);All files (*)")
        if path:
            try:
                config = Q3Config.from_file(path)
                widget = ConfigFileView(config, path)
                self.tabs.addTab(widget, path)
                self.tabs.setCurrentWidget(widget)
            except Exception as e:
                self.dialog_critical(str(e))

    def file_save(self):
        configView = self.config_file_tabs.currentWidget()
        q3config   = configView.q3config
        filename   = configView.filename
        if filename is None:
            return self.file_saveas()
        try:
            q3config.write(filename)
        except Exception as e:
            self.dialog_critical(str(e))

    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save file", "", "Config (*.cfg);All files (*)")
        configView = self.tabs.currentWidget()
        q3config   = configView.q3config
        if not path:
            return
        try:
            q3config.write(path)
        except Exception as e:
            self.dialog_critical(str(e))

    def update_title(self):
        pass
        #self.setWindowTitle("%s - Openarena Configurator" % (os.path.basename(self.path) if self.path else "Untitled"))

    def addConfigFileView(self, path):
        _ = ConfigFileView(Q3Config.from_file(path), path)
        self.config_file_tabs.addTab(_, path)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Openarena Configurator")

    FONTS['monospace'] = QFont('Monospace', 10)
    # Setup the QTextEdit editor configuration XXX
    #fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
    #fixedfont.setPointSize(12)

    QIcon.setThemeName('oxygen')

    window = MainWindow()
    window.addConfigFileView('/tmp/foo.cfg')
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    app.exec_()
