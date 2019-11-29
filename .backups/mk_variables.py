#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is also a source
LABEL = 'Openarena Configurator'

import sys
from re import compile as RE
from libmk import *
from values import *
import net.joz3d        as joz3d
import net.quake3tweaks as quake3tweaks
import net.stupidctf    as stupidctf
import oa.cvardump      as cvardump
import oa.source_vars   as source_vars

count_upper = lambda s,f=RE('[A-Z]').findall: len(f(s))
is_float = RE(r'\d+\.\d+').fullmatch
is_str   = RE(r'\D').search
VARIABLES = {}

# =============================================================================
# NAMES
# =============================================================================
VARNAMES = {}
def find_best_names(source):
    to_drop = []
    for lower, var in source.VARIABLES.items():
        name = var['name']
        if not name or len(name) < 3:
            warn('Dropping strange variable %r coming from %r' % (name, source.LABEL))
            to_drop.append(lower)
            continue

        old = VARNAMES.get(lower, None)
        if old:
            count_old = count_upper(old)
            count_new = count_upper(name)
            if count_old < count_new: # prefer camelCase names
                info('VAR (%s): %r is better than %r' %(source.LABEL, name, old))
                VARNAMES[lower] = name
        else:
            VARNAMES[lower] = name
    
    for lower in to_drop: source.VARIABLES.pop(lower)


# We use the lower-cased name as key (quake is also case-insensitive)
for src in cvardump, source_vars, joz3d, quake3tweaks, stupidctf:
    src.VARIABLES = { name.lower():var for name,var in src.VARIABLES.items() }

# Find the best variable names
for source in cvardump, source_vars, joz3d, quake3tweaks, stupidctf:
    find_best_names(source)

# Rename all the var['name'] to the best name
for source in cvardump, source_vars, joz3d, quake3tweaks, stupidctf:
    for lower, var in source.VARIABLES.items():
        var['name'] = VARNAMES[lower]

# Start with 'empty' dictionaries (containing only the variable name)
VARIABLES = {lower:{'name':name} for lower, name in VARNAMES.items()}
del VARNAMES # no longer needed

# =============================================================================
# DESCRIPTION
# =============================================================================
get_desc  = lambda src, name: src.VARIABLES.get(name,{}).get('description', None)
get_defl  = lambda src, name: src.VARIABLES.get(name,{}).get('default', None)
get_cheat = lambda src, name: src.VARIABLES.get(name,{}).get('cheat', None)
get_type  = lambda src, name: src.VARIABLES.get(name,{}).get('type', None)

for lower, var in VARIABLES.items():
    name = var['name']

    # === DESCRIPTION =========================================================
    # Put all descriptions found into the description text
    descriptions = []
    for source in joz3d, quake3tweaks, stupidctf:
        desc = get_desc(source, lower)
        if desc:
            descriptions.append('[%s]\n%s' % (source.LABEL, desc))

    if descriptions:
        var['description'] = '\n\n'.join(descriptions)

    # === DEFAULT =============================================================
    # Add the default value. Last definition wins.
    last_source = None
    for source in joz3d, quake3tweaks, stupidctf, cvardump, source_vars:
        defl = get_defl(source, lower)
        if defl:
            old_defl = var.get('default', None)
            if not old_defl:
                var['default'] = defl
                last_source = source.LABEL
            elif old_defl != defl:
                warn('%s: %s overwrites %r to %r (last source: %s)' % (name, source.LABEL, old_defl, defl, last_source))
                var['default'] = defl
                last_source = source.LABEL

    # === CHEAT ===============================================================
    # Add the cheat flag. Last definition wins.
    last_source = None
    for source in joz3d, quake3tweaks, stupidctf, cvardump, source_vars:
        cheat = get_cheat(source, lower)
        if cheat is not None:
            old_cheat = var.get('cheat', None)
            if old_cheat is None:
                var['cheat'] = cheat 
                last_source = source.LABEL
            elif old_cheat != cheat:
                warn('%s: %s overwrites cheat %r to %r (last source: %s)' % (name, source.LABEL, old_cheat, cheat, last_source))
                var['cheat'] = cheat
                last_source = source.LABEL

    # === TYPE ================================================================
    # Only `source_vars` has type, but `source_vars` does not contain all
    # variables. Look at the default value on the other variables 
    # for determining a float value.
    var['type'] = get_type(source_vars, lower)
    if var['type'] is None:
        default = var.get('default', '')
        if is_float(default):
            info('Setting type of %r to float (%r)' % (name, default))
            var['type'] = float
        #elif is_str(default):
        #    info('Setting type of %r to str (%r)' % (name, default))
        #    var['type'] = str


# @EXPORT
'''
Variables are registered and exported using this file.
'''

class VariableDef:
    __slots__ = (
        'name', 'alias', 'description', 'type', 'default',
        'select', 'representation', 'cheat',
        'name_lower'
    )

    def __init__(self,
            name=None, alias=None, description=None, type=None, default=None,
            select=None, representation=None, cheat=None):
        self.name = name
        self.name_lower = name.lower()
        self.type = type
        self.cheat = cheat
        self.alias = alias
        self.select = select
        self.default = default
        self.description = description
        self.representation = representation

    def __repr__(self):
        return ('VariableDef(name=%r%s%s%s%s%s%s)' % (self.name,
            ((',alias=%r' % self.alias)             if self.alias else ''),
            ((',description=%r' % self.description) if self.description else ''),
            ((',type=%s' % TYPE2STR[self.type])     if self.type else ''),
            ((',default=%r' % self.default)         if self.default else ''),
            ((',representation=%r' % self.representation) if self.representation else ''),
            ((',cheat=%r' % self.cheat)             if self.cheat is not None else '')
        ))
        #return 'VariableDef(name=%r, alias=%r, description=%r, type=%s, default=%r, select=%r, representation=%s, cheat=%r)' % (
        #    self.name, self.alias, self.description, TYPE2STR[self.type], self.default,
        #    self.select, myRepr(self.representation), self.cheat)

class Values:
    __slots__ = ('values',)
    def __init__(self, values):
        self.values = values
    def __repr__(self):
        return 'Values(%r)' % (self.values,)

class Range:
    __slots__ = ('start', 'stop', 'increment')
    def __init__(self, start, stop, increment=1):
        self.start, self.stop, self.increment = start, stop, increment
    def __repr__(self):
        return 'Range(%r, %r, %r)' % (self.start, self.stop. self.increment)

# @END

# Convert dictionaries to VariableDef type
VARIABLES = { lower: VariableDef(**v) for lower, v in VARIABLES.items() }
MANUAL_DEFINED = set()

def V(name, alias=None, desc=None, type=None, default=None, cheat=False, select=None, representation=None, force=()):
    '''
    Manual define OR extend a variable.
    Variable attributes will be checked against the attributes taken from the
    sources and a warning is omitted if values do not match.

    If you're sure that you're value is right, use `force=(<attribute_name>)`.

    In general it is recommended to let the sources fill the types
    and only do manual corretions using the function parameters.
    '''
    lower = name.lower()

    if lower in MANUAL_DEFINED:
        warn('Overwriting manual definition of %r' % name)
    MANUAL_DEFINED.add(lower)

    # We allow to use all types for `default`, but in the end we want `str`
    if default is not None:
        if default in (True,False): default = int(default)
        default = str(default)

    if lower in VARIABLES: # TODO: lowercase thing
        # Just adding info to a variable already found in source

        var = VARIABLES[lower]
        if type is not None and var.type is not None and type != var.type:
            if 'type' not in force:
                warn("Type mismatch: %s: Sources say %s but you say %s" % (name, var.type, type))
        if default is not None and default != var.default:
            warn("Default mismatch: %s: Sources say %s but you say %s" % (name, var.default, default))
        if cheat != var.cheat:
            warn("Cheat mismatch: %s: Source says %s but you say %s" % (name, var.cheat, cheat))

        if desc is not None:
            if var.description is None:
                var.description = desc
            else:
                var.description += '\n\n[%s]\n%s' % (LABEL, desc)

        var.alias = alias
        var.select = select
        var.representation = representation
    else:
        # Creating a new variable
        VARIABLES[lower] = VariableDef(name=name, alias=alias, description=desc,
            type=type, default=default, select=select, cheat=cheat,
            representation=representation)

# =============================================================================
# === Variable Definitions ====================================================
# =============================================================================

# =============================================================================
# Player ======================================================================
# =============================================================================
V('name',       'player_Name',       'Set the Player Name')
V('headmodel',  'player_Model Head', 'Set the head of the player model', default='sarge')
V('model',      'player_Model', 'Set the body of the player model', default='sarge')
V('team_headmodel', 'player_Team Model Head')
V('team_model',     'player_Team Model')
V('sex',        'player_Sex',        'Set the player\'s sex', default='male')
V('handicap',   'player_Handicap',   'Set handicap', default=100, type=int)
V('color1',     'player_Railgun Color 1', 'Set color 1 for railgun beam', type=int)
V('color2',     'player_Railgun Color 2', 'Set color 2 for railgun beam', type=int)

# =============================================================================
# Favourite Servers ===========================================================
# =============================================================================
for i in range(1, 16+1):
    V('server%d'%i, 'Favourite Server #%02d'%i, 'Set favourite server #%02d'%i, select='server')

# =============================================================================
# Crosshairs ==================================================================
# =============================================================================
V('cg_crosshairSize',       'cg_Crosshair Size',
    'Set the size of the crosshair')
V('cg_crosshairHealth',     'cg_Crosshair indicates Health',
    'Color the crosshair based on your health')
V('cg_crosshairPulse',      'cg_Crosshair Pulse',
    'Resize the crosshair when picking up items')
V('cg_crosshairX',          'cg_Crosshair X',
    'Adjust chrosshair X position')
V('cg_crosshairY',          'cg_Crosshair Y',
    'Adjust chrosshair Y position')
V('cg_crosshairColorGreen', 'cg_Crosshair green',
    'Set the amount of green in chrosshair')
V('cg_crosshairColorBlue',  'cg_Crosshair blue',
    'Set the amount of blue in chrosshair')
V('cg_crosshairColorRed',   'cg_Crosshair red',
    'Set the amount of red in chrosshair')
V('cg_differentCrosshairs', 'cg_Weapon based Crosshairs',
    'Use different chrosshairs based on weapon')
V('cg_drawCrosshair',       'cg_Crosshair Shape',
    'Sets the shape of the crosshair',
    select=CROSSHAIRS
)

for i in range(1, 13+1):
    V('cg_ch%d'%i,
      'cg_Crosshair Shape (%s)' % weaponNo2str(i),
      'Set the Crosshair Shape for %s' % weaponNo2str(i),
      type=int,
      default=1,
      select=CROSSHAIRS,
      representation='crosshair'
    )

    V('cg_ch%dsize'%i,
      'cg_Crosshair Size (%s)' % weaponNo2str(i),
      'Set Crosshair Size for %s' % weaponNo2str(i),
      type=float,
      default=24
    )

V('cg_drawCrosshairNames', 'cg_Identify target',
  'Show the name of the player you are aiming at. ("Identify target" from "game options" menu)',
    type=bool, default=True
)

V('cg_shadows', 'cg_Draw_Shadows',
r'''
Determines how the shadows of the characters are drawn. The standard shadow is a sort of disc under the character, but the
engine is capable to draw more complex shadows (known as "detailed shadows", "stencil shadows" or "volumetric shadows": they reproduce the 3D model and are
projected to the opposite side from the light source), although with some glitches (sometimes you can see such shadows go through the walls). Since OpenArena 0.8.5, the detailed shadows have been disabled almost completely, and they are available in Single Player Deathmatch (g_gametype 2) mode only; still available in all modes in old mods. Moreover, detailed shadows are not shown under character models that contain more than a certain number of polygons.''',
default=1,
type=int,
select = {
 0: '(Off) No shadows under yourself, under the other players and the items.',
 1: '(Blob) Simple semi-transparent "disc" shadow under yourself and under the other players; no shadow under items. It is the default value.',
 2: '(Stencil) Semi-transparent grey detailed shadow under the other players and under items (such as weapons, ammo boxes, health, etc.); no shadow under yourself, unless you enable cg_thirdperson. It needs r_stencilbits <> 0 (usually set to 8 -default-, 24 or 32). Disabled in OpenArena 0.8.5+, except when playing in Single Player Deathmatch mode.',
 3: '(Vertex) Non-transparent uniform black detailed shadow under yourself and under the other players; no shadow under items. Disabled in OpenArena 0.8.5+, except when playing in Single Player Deathmatch mode.'
})

V('cg_drawDamage', 'cg_Draw Shot Damage', 'Draw the damage of a shot')
V('cg_drawGun',    'cg_Draw Gun', 'Where to draw the weapon', default=1, type=int,
    select={
        0: 'Hide',
        1: 'Right',
        2: 'Left',
        3: 'Center'
    }
)
V('cg_drawTeamOverlay', 'cg_Draw Team Overlay', 'Draw the Team Overlay')
V('cg_drawFriend',      'cg_Draw Friend',       'Draw friend')
V('cg_drawSpeed',       'cg_Draw Speed',    'Draw the speed-o-meter', default=False, type=bool)
V('cg_draw2D',          'cg_Draw HUD',      'Draw the HUD', default=True, type=bool)
V('cg_drawStatus',      'cg_Draw Status',   'Draw ammo, health and armor status', type=bool, default=True)
V('cg_drawTimer',       'cg_Draw Timer',    'Draw time elapsed since the beginning of the match', default=False, type=bool)
V('cg_drawFPS',         'cg_Draw FPS',      'Draw FPS', type=bool, default=False)
V('cg_drawSnapshot',    'cg_Draw Snapshot', 'Draw Snapshot TODO', default=False, type=bool)
V('cg_draw3dIcons',     'cg_Draw 3D icons', 'Draw 3D icons TODO', type=bool, default=True)
V('cg_drawIcons',       'cg_Draw Icons',    'Draw icons TODO', default=True, type=bool)
V('cg_weaponBarStyle',  'cg_Weapon Bar Style', 'Style of Weapon Bar')
V('cg_alwaysWeaponBar', 'cg_Always Show Weapon Bar', 'Always Show Weapon Bar')
V('cg_drawAmmoWarning', 'cg_Draw Ammo Warning',
    'Draw the "low ammo warning" and "out of ammo" on-screen messages when you have few or no ammo left.', default=True, type=bool)
V('cg_drawAttacker',    'cg_Draw Attacker\'s Name',
    'Show the head and the name of the last player who hit you near to the upper right corner of the screen. ', type=bool, default=True)
V('cg_drawRewards',     'cg_Draw Reward Medals',
    'Show the "Medals" over the head of the players. (Excellent, Impressive, etc.)', type=bool, default=True)
V('cg_marks',           'cg_Show Marks on walls', 'Show damaged surfaces on walls hit by shots.', default=True, type=bool)
V('cg_brassTime',       'cg_Ejecting Brass Time',
    'How long you will see the cartridge cases ejected by some weapons, before they disappear.', default=2500, type=int)
#V('cg_predictItems')
#V('cg_stereoSeparation')
#V('cg_enemyAlwaysGreen')
#V('cg_forceSound')
#V('cg_motdTime')
#V('cg_weaponBobbing')
#V('cg_friendSize')
#V('cg_muzzleFlash')
#V('cg_smoothClients')
#V('cg_lagometer_y')
#V('cg_lagometer_x')
#V('cg_nochatbeep')
#V('cg_leiSuperGoreyAwesome')
#V('cg_leiBrassNoise')
#V('cg_leiGoreNoise')
#V('cg_leiEnhancement')
#V('cg_cyclegrapple')
#V('cg_hitsound')
#V('cg_autovertex')
#V('cg_voipTeamOnly')
#V('cg_music')

# =============================================================================
# net_ Network
# =============================================================================
V('net_socksEnabled',  'net_SOCKS Proxy Enabled', 'Use a SOCKS proxy', default=False, type=bool)
V('net_socksPassword', 'net_SOCKS Password',  'Set password for SOCKS proxy')
V('net_socksUsername', 'net_SOCKS Username',  'Set username for SOCKS proxy')
V('net_socksPort',     'net_SOCKS Port',      'Set the port number for SOCKS proxy', default=1080, type=int)
V('net_socksServer',   'net_SOCKS Host',      'Set the SOCKS proxy host')
V('rate',              'net_Rate (kbit/s)')# TODO "25000"
#('net_mcast6iface)
#('net_mcast6addr)
#('net_enabled)

# =============================================================================
# FM
# =============================================================================
V('fm_chatbeep',      'fm_Chat Beep',         'Enable Beep on Chat (FailMod)')
V('fm_teamchatbeep',  'fm_Team Chat Beep',    'Enable Beep on Team Chat (FailMod)')
V('fm_votebeep',      'fm_Vote Beep',         'Enable Beep on Vote (FailMod)')
V('cg_drawReady',     'fm_Draw Ready',
    'If you are bothered with that text occupying the whole screen. -1 disables completely other numbers do something') #TODO


# =============================================================================
# CL
# =============================================================================

# Console options
V('cl_consoleHeight',     'cl_Console Height',      'Set the percentual height of the console', default=0.5, type=float) #TODO def
V('cl_consoleColorAlpha', 'cl_Console color alpha', 'Set the console color alpha', default=0.8, type=float) # TODO def
V('cl_consoleColorBlue',  'cl_Console color blue',  'Set the amount of blue color', default=0, type=float) # TODO def
V('cl_consoleColorGreen', 'cl_Console color green', 'Set the amount of green color', default=0, type=float) #TODO def
V('cl_consoleColorRed',   'cl_Console color red',   'Set the amount of red color', default=1, type=float) # TODO def "1"
V('cl_consoleType',       'cl_Console type',        'Set the console type TODO',   default=0, type=int) #TODO desc,def
V('cl_consoleKeys',       'cl_Console keys',        'Set which keys activate the console', default="~ ` 0x7e 0x60") # TODO def

V('cl_run', 'cl_Always_Run', '"Always Run" Option from Game Menu')
V('cl_allowDownload', 'cl_Automatic Download', 'Automatically download Maps and Mods from the Server')
#V('cl_voip')
#V('cl_voipShowMeter')
#V('cl_voipVADThreshold')
#V('cl_voipUseVAD')
#V('cl_voipCaptureMult')
#V('cl_voipGainDuringCapture')
#V('cl_mumbleScale')
#V('cl_cURLLib')
#V('cl_mouseAccelOffset')
#V('cl_mouseAccelStyle')
#V('cl_freelook')
#V('cl_mouseAccel')
#V('cl_guidServerUniq')
#V('cl_lanForcePackets')
#V('cl_maxPing')
#V('cl_anonymous')
#V('cl_useMumble')
#V('cl_timeNudge')
#V('cl_packetdup')
#V('cl_maxpackets')
#V('cl_aviMotionJpeg')
#V('cl_aviFrameRate')
#V('cl_autoRecordDemo')
#V('cl_timedemoLog')

# =============================================================================
# CG
# =============================================================================
V('cg_viewsize', desc='Draw the game world in a smaller window. The HUD and chat messages will be drawn outside of that section.') # TODO
V('cg_simpleItems', 'cg_Simple Items',   'Draw 2D items', type=bool, default=False)
V('cg_lagometer',   'cg_Draw Lagometer', 'Draw the lagometer', type=bool)
V('cg_autoswitch',  'cg_Weapon Autoswitch', 'What to do when picking up a weapon', type=int, default=1,
    select={
        0: 'OFF: Disable automatically switching weapons',
        1: 'ALWAYS: Always choose the weapon you just picked up (even if you already had it)',
        2: 'NEW: Automatically selects the weapon you just picked up, but only if you didn\'t have it before.',
        3: 'BETTER: Automatically selects the the weapon you just picked up, but only if it is "better" than the one you are currently using (even if you already had it). The switch is triggered only if both currently used and picked up weapon are listed in the "better weapons" list variable.',
        4: 'NEW&BETTER: Automatically selects the weapon you just picked up, but only if it is "better" than the one you are currently using and (at the same time) you didn\'t have it before. The switch is triggered only if both currently used and picked up weapon are listed in the "better weapons" list variable'
    }
)
V('cg_weaponOrder', 'cg_Weapon Order', 'Set weapon order', representation='weapon')


V('cg_teamChatBeep',  'cg_Team Chat Beep',    'Enable Beep on Team Chat')
V('cg_chatBeep',      'cg_Chat Beep',         'Enable Beep on Chat')
V('cg_teamChatTime',  'cg_Team Chat Time',    'Set the Team Chat Time in Miliseconds')
V('cg_teamChatHeight','cg_Team Chat Height',  'Set the Team Chat Height')
V('cg_teamChatsOnly', 'cg_Team Chats only',   'Only display Team Chats')
V('cg_zoomfov',       'cg_Zoom Field of View', 'Set the Field of View when zooming', default=22.5, type=float)
V('cg_fov',           'cg_Field of View',      'Set the Field of View',              default=90,   type=float, force=('type',))
V('cg_zoomTime',      'cg_Zoom time',          'Set the time for zoom',              default=0, type=int, force=('default',)) # TODO: desc,def,typ

V('cg_footsteps',     'cg_Footsteps',          'Enable footsteps',                   default=True, type=bool)
V('cg_gibs',          'cg_Gibs',
    'Set to 0 if you want to see less gibs than usual when someone will be "gibbed"',  default=True, type=bool)

V('cg_bobup',         'cg_Bob Up')
V('cg_bobpitch',      'cg_Bob Pitch')
V('cg_bobroll',       'cg_Bob Roll')
V('cg_runpitch',      'cg_Run Pitch')
V('cg_runroll',       'cg_Run Roll')


V('cg_oldRail', 'cg_Old Rail',
    'If enabled, external "spiral" trace is omitted from railgun beam. The spiral is nice at look, but may be distractive',
     type=int)
V('cg_oldRocket', 'cg_Old Rocket',
    'Use old rocket style', default=True, type=bool)

V('cg_oldPlasma', 'cg_Old Plasma',
    'If disabled, plasma balls leave additional particle effects behind them (nice at view, but nothing impressive and they could distract from gameplay). At the time of this writing, with OA 0.8.8, if you have cg_leiEnhancement 1, then cg_oldplasma value is ignored, and you see as with cg_oldplasma 1.',
 default=True, type=bool)

#different levels. Highest quality level is associated with \r_picmip 0, lowest detail level is associated with \r_picmip 3 (higher r_picmip value means lower
#    quality). It needs \vid_restart to be effective and default value is 1 (if you have a good machine, it is advisable to set it to 0). You can use console to
#set even lower texture quality levels, specifying higher values for r_picmip, even 8 or 16: this increases framerate more (making very "plain" textures); but,
#when you set a value higher than "3", it tends to automatically return to "3"; this is due a videoflags lock (value 2), which is included with the default
#videoflags value, 7 (7=4+2+1). This because with high r_picmip values the game isn't nice-looking and because using flat textures on walls may give an unfair
#advantage in finding other players. Unless the server administrator disables that videoflags lock, users r_picmip will continue to automatically return to 3,
#if they set it higher.

#V('cg_fragmsgsize')
#V('cg_railTrailTime')
#V('cg_forceModel')
#V('cg_deferPlayers')
#V('cg_noVoiceChats')
#V('cg_noVoiceText')
#V('cg_cameraOrbitDelay')
#V('cg_scorePlums')
#V('cg_noTaunt')
#V('cg_noProjectileTrail')
#V('cg_delag')
#V('cg_cmdTimeNudge')
#V('cg_projectileNudge')
#V('cg_optimizePrediction')
#V('cg_trueLightning')


# =============================================================================
# com_ COM
# =============================================================================
V('com_introplayed')
V('com_busyWait')
V('com_maxfps')
V('com_maxfpsMinimized')
V('com_maxfpsUnfocused')
V('com_ansiColor')
V('com_altivec')
V('com_hunkMegs')
V('com_blood')
V('com_zoneMegs')
V('com_soundMegs')

# =============================================================================
# sv_ SERVER
# =============================================================================
V('sv_banFile')
V('sv_lanForceRate')
V('sv_master5')
V('sv_master4')
V('sv_master3')
V('sv_master2')
V('sv_master1')
V('sv_dlURL')
V('sv_floodProtect')
V('sv_maxPing')
V('sv_minPing')
V('sv_maxRate')
V('sv_minRate')
V('sv_hostname')
V('sv_maxclients')
V('sv_fps')

# =============================================================================
# s_ SOUND
# =============================================================================
V('s_sdlMixSamps')
V('s_sdlDevSamps')
V('s_sdlChannels')
V('s_sdlSpeed')
V('s_sdlBits')
V('s_mixPreStep')
V('s_mixahead')
V('s_khz')
V('s_alCapture')
V('s_ambient')

# =============================================================================
# in_ INPUT
# =============================================================================
V('sensitivity', 'in_Mouse Sensitivity') # "5"

# =============================================================================
# r_ RENDER
# =============================================================================
V('r_detailtextures',       'r_Detailed_Textures') # TODO
V('r_ext_max_anisotropy',   'r_Anisotropy_Max') # TODO 0,2,4,6,8,16
V('r_ext_texture_filter_anisotropic', 'r_Anisotropy_Enabled') # TODO
V('r_texturebits',          'r_Texture_Quality') # TODO: 0, 12, 15, 16, 32
V('r_bloom')
V('r_flares')
V('r_fullscreen')
V('r_drawSun')
V('r_centerWindow')
V('r_allowResize')
V('r_bloom_sky_only')
V('r_bloom_reflection')
V('r_bloom_dry')
V('r_bloom_cascade_dry')
V('r_bloom_cascade_alpha')
V('r_bloom_cascade_intensity')
V('r_bloom_cascade_blur')
V('r_bloom_cascade')
V('r_bloom_fast_sample')
V('r_bloom_sample_size')
V('r_bloom_darken')
V('r_bloom_intensity')
V('r_bloom_diamond_size')
V('r_bloom_alpha')
V('r_lensReflectionBrightness')
V('r_lensReflection2')
V('r_lensReflection1')
V('r_specMode')
V('r_envMode')
V('r_flaresDlight')
V('r_screenshotJpegQuality')
V('r_aviMotionJpegQuality')
V('r_marksOnTriangleMeshes')
V('r_anaglyphMode')
V('r_primitives')
V('r_railSegmentLength')
V('r_railCoreWidth')
V('r_railWidth')
V('r_facePlaneCull')
V('r_gamma')
V('r_swapInterval')
V('r_textureMode')
V('r_finish')
V('r_dlightBacks')
V('r_dynamiclight')
V('r_fastsky')
V('r_ignoreGLErrors')
V('r_stereoSeparation')
V('r_zproj')
V('r_lodbias')
V('r_lodCurveError')
V('r_monolightmaps')
V('r_greyscale')
V('r_ignoreFastPath')
V('r_stereoEnabled')
V('r_smp')
V('r_subdivisions')
V('r_simpleMipMaps')
V('r_customPixelAspect')
V('r_customheight')
V('r_customwidth')
V('r_noborder')
V('r_ignorehwgamma')
V('r_overBrightBits')
V('r_ext_multisample')
V('r_depthbits')
V('r_stencilbits')
V('r_colorbits')
V('r_roundImagesDown')
V('r_ext_vertex_shader')
V('r_postprocess')
V('r_ext_texture_env_add')
V('r_ext_compiled_vertex_array')
V('r_ext_multitexture')
V('r_ext_compressed_textures')
V('r_allowExtensions')
#V('r_picmip', 'Texture PicMip', '<0,1,2,3..N>: Higher r_picmip value means lower quality'
#    'Changing texture detail can heavily affect framerate and overall video quality. You can change "texture detail" from "graphics" menu, selecting from 4
#        default=1, type=int)
#V('r_vertexLight' "0"
#V('r_mode' "-1"
#V('r_inGameVideo' "1"


# =============================================================================
# vm_ VM
# =============================================================================
V('vm_ui')
V('vm_game')
V('vm_cgame')

# =============================================================================
# m_ M
# =============================================================================
V('m_filter')
V('m_side')
V('m_forward')
V('m_yaw')
V('m_pitch')

#V('ui_setupchecked')
#V('ui_browserOnlyHumans')
#V('ui_browserShowEmpty')
#V('ui_browserShowFull')
#V('ui_browserSortKey')
#V('ui_browserGameType')
#V('ui_browserMaster')
#V('dmflags')
#V('fraglimit')
#V('timelimit')
#V('videoflags')
#V('snaps')
#V('capturelimit')
#V('cm_playerCurveClip')
#V('con_notifytime')
#V('ch_recordMessage')
#V('g_blueTeam')
#V('g_redTeam')
#V('g_doWarmup')
#V('g_respawntime')
#V('g_maxVotes')
#V('g_voteNames')
#V('g_voteBan')
#V('g_voteGametypes')
#V('g_voteMaxTimelimit')
#V('g_voteMinTimelimit')
#V('g_voteMaxFraglimit')
#V('g_voteMinFraglimit')
#V('g_truePing')
#V('g_lagLightning')
#V('g_spawnprotect')
#V('g_awardpushing')
#V('g_runes')
#V('g_lms_mode')
#V('g_catchup')
#V('g_autonextmap')
#V('g_delagHitscan')
#V('g_maxGameClients')
#V('g_friendlyFire')
#V('g_teamAutoJoin')
#V('g_teamForceBalance')
#V('g_warmup')
#V('g_log')
#V('g_logSync')
#V('g_banIPs')
#V('g_filterBan')
#V('g_allowVote')
#V('pmove_float')
#V('pmove_msec')
#V('pmove_fixed')

# =============================================================================
# Finally, we check everything in the end again
# =============================================================================
for var in VARIABLES.values():
    # Check if type and default match
    if var.type is not None:
        try:
            if var.type == bool:
                if var.default not in "0-1": raise Exception
            else:
                var.type(var.default)
        except:
            warn('%s: Maybe got an invalid type/default: %s:%s' % (var.name, var.type, var.default))

    #if var.representation is None:
    #    var.representation = var.type

if __name__ == '__main__':
    export_begin(sys.argv[0], 'This file contains all available variables')
    export(sys.argv[0])
    export_variable('VARIABLES', VARIABLES)
