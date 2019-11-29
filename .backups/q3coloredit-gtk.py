#!/usr/bin/python

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango

class SearchDialog(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Search", parent,
            Gtk.DialogFlags.MODAL, buttons=(
            Gtk.STOCK_FIND, Gtk.ResponseType.OK,
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL))

        box = self.get_content_area()

        label = Gtk.Label("Insert text you want to search for:")
        box.add(label)

        self.entry = Gtk.Entry()
        box.add(self.entry)

        self.show_all()

COLORS = { '0': 0x000000, '1': 0xFF0000, '2': 0x00FF00, '3': 0xFFFF00,
           '4': 0x0000FF, '5': 0x00FFFF, '6': 0xFF00FF, '7': 0xFFFFFF,
           '8': 0xFFA500 }

css = b'''
/*    *           { font: 16px Mono; } */
/*    *            { background-color: #999; color: #000; } */
    ._blackbg    { background-color: #9AF; }
    #connect     { font: 48px Mono; }
'''

css =''

for caret_code, color in COLORS.items():
    css += '#c%s { background-color: #%06x; } ' % (caret_code, color)

print(css)
provider = Gtk.CssProvider()
provider.load_from_data(css.encode('UTF-8'))
Gtk.StyleContext().add_provider_for_screen(Gdk.Screen.get_default(), provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class MyColorChooser(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        for i, caret_color in enumerate(COLORS):
            b = Gtk.Button(label='a', name='c%s' % caret_color[0])
            #map = b.get_color_map()
            #color = map.alloc_color('#%06s' % caret_color[1])
            #style = b.get_style().copy()
            #style.bg[Gtk.StateType.NORMAL] = color
            #b.set_style(style)
            self.attach(b, i % 5, i / 5, 1, 1)

class TextViewWindow(Gtk.Window):
    def __init__(self, text):
        Gtk.Window.__init__(self, title="Color Editor")

        self.set_default_size(-1, 350)

        self.grid = Gtk.Grid()
        self.add(self.grid)

        self.create_textview(text)
        self.create_toolbar()
        self.create_buttons()

        d = MyColorChooser()

        #d = Gtk.ColorChooserWidget()
        #d.set_property('double-buffered', False)
        #d.show_all()
        #def foo(*args):
        #    print(args)
        #    print('dsfsdfsdfsdfaaaaaaaaaaaaaaaaaaaaaaaaaa')
        #d.connect('color-activated', foo)
        #print(d.list_properties())
        #print(d.container)
        self.grid.attach(d, 9, 1, 1, 1)


    def create_toolbar(self):
        toolbar = Gtk.Toolbar()
        self.grid.attach(toolbar, 0, 0, 3, 1)

        button_bold = Gtk.ToolButton()
        button_bold.set_icon_name("format-text-bold-symbolic")
        toolbar.insert(button_bold, 0)

        button_italic = Gtk.ToolButton()
        button_italic.set_icon_name("format-text-italic-symbolic")
        toolbar.insert(button_italic, 1)

        button_underline = Gtk.ToolButton()
        button_underline.set_icon_name("format-text-underline-symbolic")
        toolbar.insert(button_underline, 2)

        button_bold.connect("clicked", self.on_button_clicked, self.tag_bold)
        button_italic.connect("clicked", self.on_button_clicked,
            self.tag_italic)
        button_underline.connect("clicked", self.on_button_clicked,
            self.tag_underline)

        toolbar.insert(Gtk.SeparatorToolItem(), 8)

        button_clear = Gtk.ToolButton()
        button_clear.set_icon_name("edit-clear-symbolic")
        button_clear.connect("clicked", self.on_clear_clicked)
        toolbar.insert(button_clear, 9)

        toolbar.insert(Gtk.SeparatorToolItem(), 10)

        button_search = Gtk.ToolButton()
        button_search.set_icon_name("system-search-symbolic")
        button_search.connect("clicked", self.on_search_clicked)
        toolbar.insert(button_search, 11)

    def create_textview(self, text):
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_hexpand(True)
        scrolledwindow.set_vexpand(True)
        self.grid.attach(scrolledwindow, 0, 1, 3, 1)

        self.textview = Gtk.TextView()
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text(text)
        scrolledwindow.add(self.textview)

        self.tag_bold = self.textbuffer.create_tag("bold",
            weight=Pango.Weight.BOLD)
        self.tag_italic = self.textbuffer.create_tag("italic",
            style=Pango.Style.ITALIC)
        self.tag_underline = self.textbuffer.create_tag("underline",
            underline=Pango.Underline.SINGLE)
        self.tag_found = self.textbuffer.create_tag("found",
            background="yellow")

    def create_buttons(self):
        check_editable = Gtk.CheckButton(label="Editable")
        check_editable.set_active(True)
        check_editable.connect("toggled", self.on_editable_toggled)
        self.grid.attach(check_editable, 0, 2, 1, 1)

        check_cursor = Gtk.CheckButton(label="Cursor Visible")
        check_cursor.set_active(True)
        check_editable.connect("toggled", self.on_cursor_toggled)
        self.grid.attach_next_to(check_cursor, check_editable,
            Gtk.PositionType.RIGHT, 1, 1)

        radio_wrapnone = Gtk.RadioButton.new_with_label_from_widget(None,
            "No Wrapping")
        self.grid.attach(radio_wrapnone, 0, 3, 1, 1)

        radio_wrapchar = Gtk.RadioButton.new_with_label_from_widget(
            radio_wrapnone, "Character Wrapping")
        self.grid.attach_next_to(radio_wrapchar, radio_wrapnone,
            Gtk.PositionType.RIGHT, 1, 1)

        radio_wrapword = Gtk.RadioButton.new_with_label_from_widget(
            radio_wrapnone, "Word Wrapping")
        self.grid.attach_next_to(radio_wrapword, radio_wrapchar,
            Gtk.PositionType.RIGHT, 1, 1)

        radio_wrapnone.connect("toggled", self.on_wrap_toggled,
            Gtk.WrapMode.NONE)
        radio_wrapchar.connect("toggled", self.on_wrap_toggled,
            Gtk.WrapMode.CHAR)
        radio_wrapword.connect("toggled", self.on_wrap_toggled,
            Gtk.WrapMode.WORD)

    def on_button_clicked(self, widget, tag):
        bounds = self.textbuffer.get_selection_bounds()
        if len(bounds) != 0:
            start, end = bounds
            self.textbuffer.apply_tag(tag, start, end)

    def on_clear_clicked(self, widget):
        start = self.textbuffer.get_start_iter()
        end = self.textbuffer.get_end_iter()
        self.textbuffer.remove_all_tags(start, end)

    def on_editable_toggled(self, widget):
        self.textview.set_editable(widget.get_active())

    def on_cursor_toggled(self, widget):
        self.textview.set_cursor_visible(widget.get_active())

    def on_wrap_toggled(self, widget, mode):
        self.textview.set_wrap_mode(mode)

    def on_search_clicked(self, widget):
        dialog = SearchDialog(self)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            cursor_mark = self.textbuffer.get_insert()
            start = self.textbuffer.get_iter_at_mark(cursor_mark)
            if start.get_offset() == self.textbuffer.get_char_count():
                start = self.textbuffer.get_start_iter()

            self.search_and_mark(dialog.entry.get_text(), start)

        dialog.destroy()

    def search_and_mark(self, text, start):
        end = self.textbuffer.get_end_iter()
        match = start.forward_search(text, 0, end)

        if match is not None:
            match_start, match_end = match
            self.textbuffer.apply_tag(self.tag_found, match_start, match_end)
            self.search_and_mark(text, match_end)

win = TextViewWindow('fooo')
win.connect("destroy", Gtk.main_quit)
win.show_all()

Gtk.main()
