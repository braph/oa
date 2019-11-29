#!/usr/bin/python

'''
Openarena Failmod Server Browser
'''

import sys, os, time, re, gi, threading
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, Gdk, GdkPixbuf

from q3.q3path          import *
from q3.q3maps          import *
from q3.q3stat          import *
from q3.q3colors        import *
from q3.q3specialchars  import *

# ______________________________ Configuration ________________________________
SERVERLIST = [
    ('45.76.94.34', 27963), # INSTA
    ('45.76.94.34', 27960), # CTF
    ('45.76.94.34', 27962), # DEATHMATCH
    ('45.76.94.34', 20002), # GENIUS 2
    ('45.76.94.34', 20003), # CTF FOR GENIUSES
]

# _______________________________ Main stuff __________________________________
OPTIONS = { 'binary': '/usr/bin/openarena' }
q3path   = Q3Path()
q3maps   = Q3Maps()
q3colors = Q3Colors()
q3colors.addPalette(Q3Colors.QUAKE_PALETTE)
if os.path.isdir(q3path.getUserConfigDir()):
    for mod_dir in q3path.getModDirectories():
        q3maps.addFromDirectory(mod_dir)
else:
    print('Warning: No openarena user directory present')
if os.path.isdir(q3path.getGameDataDir()):
    q3maps.addFromDirectory(q3path.getGameDataDir())
else:
    print('Warning: No game data directory found')

def markup_fix(s):
    ''' IDK why, but it seems GTK renders the markup only from the second span on.
        This is why we insert a <span> dummy '''
    return '<span color="#000000"> </span>' + s
# _____________________________________________________________________________

def bold(s):      return '<b>' + s + '</b>'
def monospace(s): return '<span font-family="Mono">' + s + '</span>'

class ServerInfoRow():
    def __init__(self, ip, port):
        self.ip, self.port      = ip, port
        self.serverinfo         = Q3ServerInfo(ip, port)
        self.mapimage           = Gtk.Image.new()
        self.mapimageframe      = Gtk.Frame()
        self.mapimageframe.set_border_width(10)
        self.mapimageframe.add(self.mapimage)
        self.mapimagecontainer  = Gtk.Overlay()
        self.mapimagecontainer.add(self.mapimageframe)
        self.mapimageeventbox   = Gtk.EventBox()
        self.mapimageeventbox.add_events(Gdk.EventMask.ALL_EVENTS_MASK)

        self.connect_button = Gtk.Button(label='Connect', name='connect')
        self.connect_button.set_opacity(0.0)
        self.mapimagecontainer.add_overlay(self.connect_button)

        def focus_in(eventbox, event):
            self.connect_button.set_opacity(0.5)
        def focus_out(eventbox, event):
            self.connect_button.set_opacity(0.0)
        def connect(*_):
            os.spawnvp(os.P_NOWAIT, OPTIONS['binary'],
                [ OPTIONS['binary'], '+set', 'fs_game', 'CTF', '+connect', '%s:%s' % (self.ip, self.port)])

        self.connect_button.connect('clicked', connect)
        self.mapimageeventbox.connect('enter-notify-event', focus_in)
        self.mapimageeventbox.connect('leave-notify-event', focus_out)
        self.mapimageeventbox.add(self.mapimagecontainer)

        self.info_tree_view     = Gtk.TreeView()
        self.player_tree_view   = Gtk.TreeView()
        self.info_tree_view.get_selection().set_mode(Gtk.SelectionMode.NONE)
        self.player_tree_view.get_selection().set_mode(Gtk.SelectionMode.NONE)
        self.renderer_text      = Gtk.CellRendererText()
        #self.info_tree_view.set_sensitive(False)
        #self.player_tree_view.set_sensitive(False)

    def update(self):
        info            = self.serverinfo.info
        status          = self.serverinfo.status
        renderer_text   = self.renderer_text

        # ======================= Image =======================================
        self.mapimage.clear()
        mapname = self.serverinfo.status.get('mapname', None)
        if mapname is not None:
            mapimagedata = q3maps.getLevelshot(mapname)
            if mapimagedata is not None: # TODO
                pbloader = GdkPixbuf.PixbufLoader()
                pbloader.set_size(300, 200)
                pbloader.write(mapimagedata)
                pbloader.close()
                pixbuf = pbloader.get_pixbuf()
                #pixbuf.scale_simple(300, 300, Gdk.INTERP_LINEAR)
                self.mapimage.set_from_pixbuf(pixbuf)

        # ====================== Serverdata ===================================
        ## g_locked [01] | g_rockets[01] | g_instantgib [01] | g_humanplayers
        info_list = Gtk.ListStore(str, str)
        hostname = status.get('sv_hostname', '')
        hostname = q3colors.toHtml(hostname)
        hostname = markup_fix(hostname)
        hostname = monospace(bold(hostname))
        info_list.append(['Hostname',       hostname])
        info_list.append(['Game Type',      info.get('game', '')])
        info_list.append(['Map',            info.get('mapname', '')])
        info_list.append(['Fraglimit',      status.get('fraglimit', '')])
        info_list.append(['Timelimit',      status.get('timelimit', '')])
        info_list.append(['Capturelimit',   status.get('capturelimit', '')])
        for c in self.info_tree_view.get_columns():
            self.info_tree_view.remove_column(c)
        col_label    = Gtk.TreeViewColumn("Type",    renderer_text, text=0)
        col_value    = Gtk.TreeViewColumn("Setting", renderer_text, markup=1)
        self.info_tree_view.append_column(col_label)
        self.info_tree_view.append_column(col_value)
        self.info_tree_view.set_model(info_list)

        # ====================== Players ======================================
        player_list = Gtk.ListStore(str, str, str, str)
        for player in self.serverinfo.players:
            name = Q3SpecialChars.toUTF8(player.name)
            name = q3colors.toHtml(name)
            name = markup_fix(name)
            name = monospace(bold(name))
            player_list.append([player.score, player.ping, player.captures, name])
        for col in self.player_tree_view.get_columns():
            self.player_tree_view.remove_column(col)
        blackrenderer = Gtk.CellRendererText()
        blackrenderer.set_property('background', '#AAA')
        blackrenderer.set_property('foreground', '#FFF')
        col_score    = Gtk.TreeViewColumn('Score',  blackrenderer, text=0)
        col_ping     = Gtk.TreeViewColumn('Ping',   blackrenderer, text=1)
        col_captures = Gtk.TreeViewColumn('Capt.',  blackrenderer, text=2)
        col_name     = Gtk.TreeViewColumn('Player',   blackrenderer, markup=3)
        col_name.set_min_width(200)
        self.player_tree_view.append_column(col_name)
        self.player_tree_view.append_column(col_score)
        self.player_tree_view.append_column(col_captures)
        self.player_tree_view.append_column(col_ping)
        self.player_tree_view.set_model(player_list)

class ServerWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Openarena :F Servers')
        self.set_default_size(500, 500)
        self.set_border_width(10)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)

        servers_grid = Gtk.Grid()
        servers_grid.set_row_spacing(10)
        rows = []
        for i, server in enumerate(SERVERLIST, 1):
            sir = ServerInfoRow(server[0], server[1])
            rows.append(sir)
            servers_grid.attach(sir.mapimageeventbox,   1, i, 1, 1)
            servers_grid.attach(sir.info_tree_view,     3, i, 1, 1)
            servers_grid.attach(sir.player_tree_view,   2, i, 1, 1)

        def fetch_data(rows):
            while True:
                threads = []
                for r in rows:
                    thr = threading.Thread(target=r.serverinfo.query)
                    thr.start()
                    threads.append(thr)
                    time.sleep(0.3)
                while threads:
                    threads.pop().join()
                time.sleep(5)

        def update_rows(rows):
            for r in rows: r.update()
            return True

        threading.Thread(target=fetch_data, args=(rows,)).start()
        GLib.timeout_add_seconds(1, update_rows, rows)

        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        scrolled.add(servers_grid)


        # ___________ ACTIONS ________________
        menubar = Gtk.MenuBar()
        button_settings = Gtk.MenuItem(label='Settings')
        button_about    = Gtk.MenuItem(label='About')
        menubar.add(button_settings)
        menubar.add(button_about)
        button_about.connect('button-press-event', lambda *_: AboutWindow().show_all())

        box.pack_start(menubar,     False, False, 0)
        box.pack_start(scrolled,    True, True, 0)
        self.add(box)


class AboutWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="About")
        box0 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        box  = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,   spacing=20)
        box0.pack_start(box, False, False, 10)
        self.add(box0)

        # =====================================================================
        w = Gtk.Label()
        name = markup_fix(q3colors.toHtml('^0I^1m^7Stu^6PID^51^3:('))
        w.set_markup('This program was made by <span background="#AAA"><b> %s </b></span>' % name)
        box.pack_start(w, True, True, 10)
        # =====================================================================

        # =====================================================================
        grayrenderer = Gtk.CellRendererText()
        grayrenderer.set_property('background', '#AAA')
        grayrenderer.set_property('foreground', '#FFF')
        grayrenderer.set_property('font', 'Monospace 20px')

        sponsors = ['Unnamed Player', '^4Player^7, ^2Unnamed']
        sponsors_tree = Gtk.TreeView()
        sponsors_list = Gtk.ListStore(str)
        sponsors_tree.set_model(sponsors_list)
        for sponsor in sponsors:
            sponsor = Q3SpecialChars.toUTF8(sponsor)
            sponsor = q3colors.toHtml(sponsor)
            sponsor = markup_fix(sponsor)
            sponsors_list.append([sponsor])
        sponsors_tree.append_column(Gtk.TreeViewColumn("Sponsors", grayrenderer, markup=0))
        sponsors_tree.get_selection().set_mode(Gtk.SelectionMode.NONE)
        box.pack_start(sponsors_tree, True, True, 0)
        # =====================================================================

        # =====================================================================
        w = Gtk.LinkButton(uri='http://google.de', label='Send a starving programmer some money')
        box.pack_start(w, True, True, 0)
        # =====================================================================

        # =====================================================================
        w = Gtk.Button(label='Close')
        w.connect('clicked', lambda *_: self.close())
        box.pack_start(w, True, True, 10)
        # =====================================================================


# __________________________________ Theme ____________________________________
css = b'''
/*    *           { font: 16px Mono; } */
/*    *            { background-color: #999; color: #000; } */
    ._blackbg    { background-color: #9AF; }
    #connect     { font: 48px Mono; }
'''
provider = Gtk.CssProvider()
provider.load_from_data(css)
Gtk.StyleContext().add_provider_for_screen(Gdk.Screen.get_default(), provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

win = ServerWindow()
#win = AboutWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
