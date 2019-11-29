#!/usr/bin/python
# -*- coding: utf-8 -*-

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

debug = lambda *a,**kw: print(*a, **kw)

RE               = re.compile
QT_MAX_INT       = ((1<<31)-1)
is_int           = RE(r'[+-]?\d+').fullmatch
is_float         = RE(r'[+-]?\d+\.\d+').fullmatch
is_float_list    = RE(r'(:?[+-]?\d+\.\d+(:?\s+|$))+').fullmatch
FMT_COLOR        = '<span style="color:%s">%s</span>'
prefix_dict      = dict(SETTINGS['prefixes'])
prefix_re        = RE('^(%s)' % '|'.join(prefix_dict.keys()))
capitalize_re    = RE(' .|_.')
capitalize       = lambda s: capitalize_re.sub(lambda m: ' '+m[0][1].upper(), s)
q3colors         = Q3Colors()
q3colors.addPalette(Q3Colors.QUAKE_PALETTE)
q3colors.addPalette(Q3Colors.FAILMOD_PALETTE)
monospace = QFont('Monospace', 10)

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
        valid = s in ('-1','0','1')
    elif vartype is not None:
        try: vartype(s)
        except:
            valid = False
            print(vardef.name, 'invalid value', s)

    if vardef.representation is not None:
        try:    s = representation[vardef.representation](s)
        except: valid = False

    if len(s) > maxlen + 3:
        s = s[:maxlen] + '...'

    if vardef.representation is not None:
        if valid:
            s = FMT_COLOR % (SETTINGS['color.special'], s)
    elif vartype is bool:
        if s in ('', '0', '-1'):
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
        select  = self.vardef.select

        if vartype is None: # Guess vartype
            if   is_int(value):   vartype = int
            elif is_float(value): vartype = float

        try:
            if select and select.type == 'values':
                if not hasattr(self, 'cmbValue'):
                    self.cmbValue = QComboBox()
                    self.stackValue.addWidget(self.cmbValue)
                self.cmbValue.clear()
                for value, string in select.values.items():
                    self.cmbValue.addItem(string, str(value))
                widget = self.cmbValue
                # TODO
            elif vartype is bool:
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
        QWidget.__init__(self)
        lower = q3var.getName().lower()
        if lower in VARIABLES:
            vardef = VARIABLES[lower]
        else:
            VARIABLES[lower] = vardef = VariableDefinition(q3var.getName())

        self.q3var       = q3var
        self.vardef      = vardef
        self.displayOriginalName      = False
        self.stackValue  = stackValue = QStackedWidget()
        self.lblName     = lblName    = QLabel()
        self.lblValue    = lblValue   = QLabel()

        #lblValue.setAlignment(Qt.AlignRight) XXX

        lblName.setToolTip(vardef.description or '')
        lblName.setToolTipDuration(QT_MAX_INT)
        lblName.setFont(monospace)

        stackValue.addWidget(lblValue)

        l = QHBoxLayout()
        l.setContentsMargins(0,0,0,0)
        l.addWidget(lblName,    alignment=Qt.AlignLeft)
        l.addWidget(stackValue, alignment=Qt.AlignRight)
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
        self.setUniformItemSizes(True) # XXX
        self.reload()

    def reload(self):
        self.clear()
        self.items = []
        for var in self.q3config.yieldVariables():
            widget = VariableWidget(var)
            item = QListWidgetItem()
            self.addItem(item)
            self.setItemWidget(item, widget)
            #item.setSizeHint(widget.sizeHint()) XXX
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
