#!/usr/bin/python

import sys, os, time, re, gi, socket, zipfile, threading
gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, Gdk, GdkPixbuf

# ______________________________ Configuration ________________________________
SERVERLIST = [
    ('45.76.94.34', 27963), # INSTA
    ('45.76.94.34', 27960), # CTF
    ('45.76.94.34', 27962), # DEATHMATCH
    ('45.76.94.34', 20002), # GENIUS 2
    ('45.76.94.34', 20003), # CTF FOR GENIUSES
]

# ______________________________ Coloring stuff _______________________________
COLORS = { '0': 0x000000, '1': 0xFF0000, '2': 0x00FF00, '3': 0xFFFF00,
           '4': 0x0000FF, '5': 0x00FFFF, '6': 0xFF00FF, '7': 0xFFFFFF,
           '8': 0xFFA500 }

def colorize(s):
    def caret2span(m):
        m = m[0]
        return '<span color="#%06x">' % COLORS[m[1]] if m[1] in COLORS else m
    s = GLib.markup_escape_text(s)
    s = re.sub(r'\^.', caret2span, s)
    return s + '</span>'*s.count('<span')

def bold(s):      return '<b>' + s + '</b>'
def monospace(s): return '<span font-family="Mono">' + s + '</span>'

def getOpenarenaConfigDirectory():
    return os.path.join(os.path.expanduser('~'), '.openarena')

def getModDirectories(config_dir):
    for f in os.listdir(config_dir):
        f = os.path.join(config_dir, f)
        if os.path.isdir(f):
            yield f

class LevelShots:
    __slots__ = ('levelshots',)
    def __init__(self):
        self.levelshots = {}

    def addFromDirectory(self, directory):
        for pk3 in self.getPK3sFromDir(directory):
            for mapname, info in self.getMapsInPK3(pk3):
                self.levelshots[mapname] = info

    def getPK3sFromDir(self, directory):
        for f in os.listdir(directory):
            f = os.path.join(directory, f)
            if os.path.isfile(f) and f.lower().endswith('.pk3'):
                yield f

    def getMapsInPK3(self, pk3):
        with zipfile.ZipFile(pk3) as zf:
            for f in zf.filelist:
                filename = f.filename
                lower = filename.lower()
                if os.path.sep in lower and 'levelshots' in lower:
                    basename = os.path.basename(lower)
                    mapname, ext = os.path.splitext(basename)
                    if mapname and 'levelshots' not in mapname:
                        yield (mapname, (pk3, filename))

    def getLevelshot(self, mapname):
        try:
            pk3, filename = self.levelshots[mapname.lower()]
            with zipfile.ZipFile(pk3) as zf:
                return zf.read(filename)
        except:
            print('Levelshot not found:', mapname)
            return None

class PlayerInfo:
    __slots__ = ('score', 'ping', 'captures', 'name')
    def __init__(self, score, ping, captures, name):
        self.score, self.ping, self.captures, self.name = (score, ping, captures, name)

class ServerInfo:
    PREAMBLE  = bytes([0xFF]*4)
    GETINFO   = PREAMBLE + bytes('getinfo\n', 'ASCII')
    GETSTATUS = PREAMBLE + bytes('getstatus\n', 'ASCII')

    __slots__ = ('ip', 'port', 'info', 'status', 'players')
    def __init__(self, ip, port):
        self.ip, self.port = ip, port
        self.info = {}
        self.status = {}
        self.players = []

    def query(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
            s.settimeout(3)
            s.connect((self.ip, self.port))
            s.send(ServerInfo.GETINFO)
            getinfo_response = s.recv(8192)
            s.send(ServerInfo.GETSTATUS)
            getstatus_response = s.recv(8192)
            s.shutdown(socket.SHUT_RDWR)

            self.decodeInfo(getinfo_response)
            self.decodeStatus(getstatus_response)
        except Exception as e:
            print(self.ip, self.port, e)

    def decodeInfo(self, data):
        if data[:4] != ServerInfo.PREAMBLE:
            raise Exception('decodeInfo: Invalid preamble')
        info = data[4:].decode('ASCII')
        info = info.replace('infoResponse\n\\', '')
        info = info.split('\\')
        result = {}
        for i in range(0, len(info), 2):
            result[info[i]] = info[i+1]
        self.info = result

    def decodeStatus(self, data):
        if data[:4] != ServerInfo.PREAMBLE:
            raise Exception('decodeStatus: Invalid preamble')
        status = data[4:].decode('ASCII')
        status = status.replace('statusResponse\n\\', '')
        status, playerstatus = status.split('\n', 1)
        status = status.split('\\')
        result = {}
        for i in range(0, len(status), 2):
            result[status[i]] = status[i+1]

        self.players = []
        for p in playerstatus.split('\n'):
            if p:
                score, ping, captures_and_name = p.split(' ', 2)
                captures_and_name = captures_and_name.strip('"')
                captures, name = captures_and_name.split(' ', 1)
                captures = re.sub(r'\^.', '', captures)
                self.players.append(PlayerInfo(score, ping, captures, name))

        self.status = result

class ServerInfoRow():
    def __init__(self, ip, port):
        self.ip, self.port      = ip, port
        self.serverinfo         = ServerInfo(ip, port)
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
            os.spawnvp(os.P_NOWAIT, '/usr/bin/openarena',
                ['/usr/bin/openarena', '+set', 'fs_game', 'CTF', '+connect', '%s:%s' % (self.ip, self.port)])

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
            mapimagedata = levelshots.getLevelshot(mapname)
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
        info_list.append(['Hostname',       monospace(bold(colorize(status.get('sv_hostname', ''))))])
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
            player_list.append([player.score, player.ping, player.captures, monospace(bold(colorize(player.name)))])
        for col in self.player_tree_view.get_columns():
            self.player_tree_view.remove_column(col)
        blackrenderer = Gtk.CellRendererText()
        blackrenderer.set_property('background', '#AAA')
        blackrenderer.set_property('foreground', '#FFF')
        col_score    = Gtk.TreeViewColumn("Score",  blackrenderer, text=0)
        col_ping     = Gtk.TreeViewColumn("Ping",   blackrenderer, text=1)
        col_captures = Gtk.TreeViewColumn("Capt.",  blackrenderer, text=2)
        col_name     = Gtk.TreeViewColumn("Player",   blackrenderer, markup=3)
        col_name.set_min_width(200)
        self.player_tree_view.append_column(col_name)
        self.player_tree_view.append_column(col_score)
        self.player_tree_view.append_column(col_captures)
        self.player_tree_view.append_column(col_ping)
        self.player_tree_view.set_model(player_list)

class ServerWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Openarena :F Servers")
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
        def show_about(*a):
            print("LOL")
        button_about.connect('button-press-event', show_about)

        box.pack_start(menubar,     False, False, 0)
        box.pack_start(scrolled,    True, True, 0)
        self.add(box)



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

# _______________________________ Config stuff ________________________________
config_dir = getOpenarenaConfigDirectory()
binary     = '/opt/openarena/openarena.x86_64'
if not os.path.isdir(config_dir):
    raise Exception("Could not find openarena configuration directory")
levelshots = LevelShots()
baseoa = os.path.join(os.path.dirname(binary), 'baseoa')
levelshots.addFromDirectory(baseoa)
for mod_dir in getModDirectories(config_dir):
    levelshots.addFromDirectory(mod_dir)


win = ServerWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
