#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, colorsys

from PyQt5.QtGui        import *
from PyQt5.QtCore       import *
from PyQt5.QtWidgets    import *
from q3.q3colors        import *

FONT_SIZES = [7, 8, 9, 10, 11, 12, 13, 14, 18, 24, 36, 48, 64, 72, 96, 144]
COLOR_PALETTE = Q3Colors()
COLOR_PALETTE.addPalette(Q3Colors.QUAKE_PALETTE)
COLOR_PALETTE.addPalette(Q3Colors.FAILMOD_PALETTE)

def color_sort(str):
    r,g,b = int(str[0:1], 16), int(str[2:3], 16), int(str[4:5], 16)
    h,s,v = colorsys.rgb_to_hsv(r,g,b)
    return (s,v,h)

class ColorPaletteGrid(QGridLayout):
    color_selected = pyqtSignal()
    
    def __init__(self):
        super(ColorPaletteGrid, self).__init__()
        self._color = None
        self.useFailmodPalette(True)

    def useFailmodPalette(self, bool):
        while self.count():
            _ = self.takeAt(0)
            if _: _.widget().deleteLater()

        q3colors = Q3Colors()
        q3colors.addPalette(Q3Colors.QUAKE_PALETTE)
        if bool:
            q3colors.addPalette(Q3Colors.FAILMOD_PALETTE)

        p = list(q3colors.getPalette().items())
        p.sort(key=lambda i: color_sort(i[1]))

        for i, caret_color in enumerate(p):
            _ = QPushButton()
            _.setStyleSheet("background-color: #%s" % caret_color[1])
            _.setProperty('_color', caret_color[1])
            _.pressed.connect(self.color_button_press)
            self.addWidget(_, i / 10, i % 10, 1, 1)

    def color_button_press(self):
        self._color = self.sender().property('_color')
        self.color_selected.emit()

    def color(self):
        return self._color


class TextEditColored(QMainWindow):
    def __init__(self, text=''):
        super(TextEditColored, self).__init__()
        font   = QFont('Monospace', 14)
        layout = QVBoxLayout()
        self.css = {}

        self.editor = _ = QTextEdit()
        _.setAutoFormatting(QTextEdit.AutoAll)
        _.selectionChanged.connect(self.update_format)
        _.setFont(font)
        _.setText(text)
        layout.addWidget(_)

        self.colorPaletteGrid = _ = ColorPaletteGrid()
        def on_color_changed():
            tc = self.editor.textCursor()
            cf = tc.charFormat()
            cf.setForeground(QColor('#'+self.colorPaletteGrid.color()))
            tc.mergeCharFormat(cf)

            #self.editor.setTextColor(QColor('#'+self.colorPaletteGrid.color()))
            #text = self.editor.toHtml() TODO
        _.color_selected.connect(on_color_changed)
        layout.addLayout(_)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        edit_toolbar = QToolBar("Edit")
        edit_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Edit")

        _ = QAction(QIcon.fromTheme('edit-undo'), "Undo", self)
        _.setStatusTip("Undo last change")
        _.triggered.connect(self.editor.undo)
        edit_toolbar.addAction(_)
        edit_menu.addAction(_)

        _ = QAction(QIcon.fromTheme('edit-redo'), "Redo", self)
        _.setStatusTip("Redo last change")
        _.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(_)
        edit_menu.addAction(_)

        edit_menu.addSeparator()

        _ = QAction(QIcon.fromTheme('edit-cut'), "Cut", self)
        _.setStatusTip("Cut selected text")
        _.setShortcut(QKeySequence.Cut)
        _.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(_)
        edit_menu.addAction(_)

        _ = QAction(QIcon.fromTheme('edit-copy'), "Copy", self)
        _.setStatusTip("Copy selected text")
        _.setShortcut(QKeySequence.Copy)
        _.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(_)
        edit_menu.addAction(_)

        _ = QAction(QIcon.fromTheme('edit-paste'), "Paste", self)
        _.setStatusTip("Paste from clipboard")
        _.setShortcut(QKeySequence.Paste)
        _.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(_)
        edit_menu.addAction(_)

        _ = QAction(QIcon.fromTheme('edit-select-all'), "Select all", self)
        _.setStatusTip("Select all text")
        _.setShortcut(QKeySequence.SelectAll)
        _.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(_)

        edit_menu.addSeparator()

        _ = QAction(QIcon.fromTheme('draw-text'), "Wrap text to window", self)
        _.setStatusTip("Toggle wrap text to window")
        _.setCheckable(True)
        _.setChecked(True)
        _.triggered.connect(self.edit_toggle_wrap)
        edit_menu.addAction(_)

        format_toolbar = QToolBar("Format")
        format_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(format_toolbar)
        format_menu = self.menuBar().addMenu("&Format")

        # ======================== Font size ==================================
        self.fontsize = QComboBox()
        self.fontsize.addItems([str(s) for s in FONT_SIZES])
        def on_fontsize_change(str_size):
            self.css['font-size'] = str_size + 'pt'
            self.updateStyleSheet()
        self.fontsize.currentIndexChanged[str].connect(on_fontsize_change)
        format_toolbar.addWidget(self.fontsize)
        on_fontsize_change('14')
        self.fontsize.setCurrentText('14')
        # =====================================================================

        # ===================== Background Color ==============================
        background_combo = QComboBox()
        background_combo.setEditable(False)
        bg_colors = [
            ('#CCCCCC', 'Gray'),
            ('#0000A6', 'Blue'),
            ('#A50000', 'Red'),
            ('#000000', 'Black')
        ]
        for color, name in bg_colors:
            _ = QPixmap(32,32)
            _.fill(QColor(color))
            icon = QIcon(_)
            background_combo.addItem(icon, name + ' Background', color)
        def on_background_change(index):
            color = background_combo.itemData(index)
            self.css['background-color'] = color
            self.updateStyleSheet()
        background_combo.currentIndexChanged.connect(on_background_change)
        format_toolbar.addWidget(background_combo)
        on_background_change(0)
        # =====================================================================

        # ===================== Failmod Palette ===============================
        _ = QCheckBox()
        _.setText('Failmod Colors')
        _.setChecked(True)
        _.stateChanged.connect(self.colorPaletteGrid.useFailmodPalette)
        format_toolbar.addWidget(_)
        # =====================================================================

        # ====================== Bold Checkbox ================================
        self.bold_action = _ = QAction(QIcon.fromTheme('format-text-bold'), "Bold", self)
        _.setStatusTip("Bold")
        _.setShortcut(QKeySequence.Bold)
        _.setCheckable(True)
        def on_bold_toggle(bool):
            self.css['font-weight'] = ('bold' if bool else 'normal')
            self.updateStyleSheet()
        _.toggled.connect(on_bold_toggle)
        format_toolbar.addAction(_)
        format_menu.addAction(_)
        on_bold_toggle(True)
        _.setChecked(True)
        # =====================================================================

        format_menu.addSeparator()

        format_group = QActionGroup(self)
        format_group.setExclusive(True)

        format_menu.addSeparator()

        # A list of all format-related widgets/actions, so we can disable/enable signals when updating.
        self._format_actions = [
            self.fontsize,
            self.bold_action,
        ]

        self.update_format()
        self.setWindowTitle("Quake 3 Color Editor")
        self.show()

    def block_signals(self, objects, b):
        for o in objects:
            o.blockSignals(b)

    def update_format(self):
        self.block_signals(self._format_actions, True)
        self.block_signals(self._format_actions, False)

    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode( 1 if self.editor.lineWrapMode() == 0 else 0 )

    def updateStyleSheet(self):
        _ = ';'.join([ '%s: %s' % (k,v) for k,v in self.css.items() ])
        self.editor.setStyleSheet(_)

    def toPlainText2(self):
        text = ''
        doc = self.editor.document()
        block = doc.begin()
        while block.isValid():
            iterator = block.begin()
            while iterator != block.end():
                fragment = iterator.fragment()
                if fragment.isValid():
                    text   = fragment.text()
                    format = fragment.charFormat()
                    color  = format.foreground().color().name(QColor.HexRgb)
                    print(text, 'color', color)
                iterator += 1
            block = block.next()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName("Quake Name Editor")
    window = MainWindow()
    app.exec_()
