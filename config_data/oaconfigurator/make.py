#!/usr/bin/python -B
# -*- coding: utf-8 -*-

'''
This file exports hand written definitions of variables and commands.
'''

import sys, json
sys.path.append('..')
from values         import *
from config_classes import *

source = Source('Openarena Configurator', {}, {})

def C(name, *args, **kwargs):
    ''' Adds a new command definition '''
    lower = name.lower()
    if lower in source.commands:
        raise Exception('Duplicate definition of %r' % name)
    source.commands[lower] = CommandDefinition(name, *args, **kwargs)

def V(name, alias=None, desc=None, **kwargs):
    ''' Adds a new variable definiton '''
    lower = name.lower()
    if lower in source.variables:
        raise Exception('Duplicate definition of %r' % name)
    kwargs['description'] = desc
    kwargs['alias']       = alias
    source.variables[lower] = VariableDefinition(name, **kwargs)

# =============================================================================
#                               === Commands ===                              #
# =============================================================================

C('cmdlist',        'List all available commands')
C('cinematic')
C('rehashbans')
C('net_restart',    'Restart network dependent stuff')
C('which',          'Locate the path of a file', '<FILE>')
C('s_info')
C('s_stop')
C('s_list')
C('stopmusic',      'Stop playing music')
C('music')
C('play')
C('gfxinfo')
C('screenshotJPEG', 'Save screenshot as <FILE>.jpg', '<FILE>')
C('screenshot',     'Save screenshot as <FILE>.tga', '<FILE>')
C('modelist',       'List all available screen resolutions')
C('modellist')
C('skinlist')
C('shaderlist')
C('imagelist')
C('minimize')
C('stopvideo')
C('video')
C('model')
C('fs_referencedList')
C('fs_openedList')
C('showip',         'Show IP address')
C('serverstatus')
C('ping')
C('rcon')
C('globalservers')
C('localservers')
C('reconnect')
C('connect')
C('stoprecord')
C('demo')
C('record')
C('disconnect')
C('vid_restart',    'Restart graphics related stuff', alias='restart_video')
C('snd_restart',    'Restart sound related stuff',    alias='restart_sound')
C('clientinfo')
C('configstrings')
C('cmd')
C('-voiprecord')
C('+voiprecord')
C('-mlook')
C('+mlook')
C('-button14')
C('+button14')
C('-button13')
C('+button13')
C('-button12')
C('+button12')
C('-button11')
C('+button11')
C('-button10')
C('+button10')
C('-button9')
C('+button9')
C('-button8')
C('+button8')
C('-button7')
C('+button7')
C('-button6')
C('+button6')
C('-button5')
C('+button5')
C('-button4')
C('+button4')
C('-button3')
C('+button3')
C('-button2')
C('+button2')
C('-button1')
C('+button1')
C('-button0')
C('+button0')
C('-attack')
C('+attack')
C('-speed',         alias='-run')
C('+speed',         alias='+run')
C('-moveright')
C('+moveright')
C('-moveleft')
C('+moveleft')
C('-strafe')
C('+strafe')
C('-lookdown')
C('+lookdown')
C('-lookup')
C('+lookup')
C('-back')
C('+back')
C('-forward')
C('+forward')
C('-right')
C('+right')
C('-left')
C('+left')
C('-movedown',      alias='-crouch')
C('+movedown',      alias='+crouch')
C('-moveup',        alias='-jump')
C('+moveup',        alias='+jump')
C('centerview')
C('condump',        'Dump console contents to <FILE>', '<FILE>')
C('clear',          'Clear console')
C('messagemode4',   'Enter attacker chat mode', alias='messagemode_attacker')
C('messagemode3',   'Enter target chat mode',   alias='messagemode_target')
C('messagemode2',   'Enter team chat mode',     alias='messagemode_team')
C('messagemode',    'Enter global chat mode',   alias='messagemode_say')
C('toggleconsole',  'Show/Hide the Console')
C('flushbans')
C('exceptdel')
C('bandel')
C('exceptaddr')
C('banaddr')
C('listbans')
C('killserver')
C('spdevmap')
C('spmap')
C('devmap')
C('map')
C('sectorlist')
C('map_restart')
C('dumpuser')
C('systeminfo')
C('serverinfo')
C('status')
C('clientkick')
C('kick')
C('heartbeat')
C('vminfo')
C('vmprofile')
C('in_restart',     'Restart input related stuff',  alias='restart_input')
C('meminfo')
C('exec',           'Execute <FILE[.cfg]> inside config directory', '<FILE[.cfg]>')
C('set')
C('seta',           'Set variable <VAR> to <VALUE> and archive it', '<VAR> <VALUE>')
C('setu')
C('sets')
C('bind',           'Bind <KEY> to <COMMAND>',                      '<KEY> <COMMAND>')
C('unbindall',      'Reset all keybindings')
C('game_restart')
C('writeconfig',    'Save the current configuration to disk')
C('changeVectors')
C('quit',           'Quit the game')
C('setenv')
C('touchFile')
C('fdir')
C('dir')
C('path')
C('bindlist')
C('unbind')
C('wait')
C('echo',           'Write <string> to console', '<string>')
C('cvar_restart')
C('cvarlist')
C('unset')
C('reset')
C('toggle',         'Toggle the value of <VAR>', '<VAR> <value1>, [<value2>, <valueN>...]')
C('print',          'Print value of <VAR> to console', '<VAR>')
C('vstr',           'Execute contents of <VAR> as a config script', '<VAR>')

# =============================================================================
#                               === Variables ===                             #
# =============================================================================

# =============================================================================
#                                    Player                                   #
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
#                              Favourite Servers                              #
# =============================================================================
for i in range(1, 16+1):
    V('server%d'%i, 'Favourite Server #%02d'%i, 'Set favourite server #%02d'%i)
    # TODO: Make a selection class for `Server`

# =============================================================================
#                                  Crosshairs                                 #
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
    select=Values(CROSSHAIRS)
)

for i in range(1, 13+1):
    V('cg_ch%d'%i,
      'cg_Crosshair Shape (%s)' % weaponNo2str(i),
      'Set the Crosshair Shape for %s' % weaponNo2str(i),
      type=int,
      default=1,
      select=Values(CROSSHAIRS),
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
select = Values({
 0: '(Off) No shadows under yourself, under the other players and the items.',
 1: '(Blob) Simple semi-transparent "disc" shadow under yourself and under the other players; no shadow under items. It is the default value.',
 2: '(Stencil) Semi-transparent grey detailed shadow under the other players and under items (such as weapons, ammo boxes, health, etc.); no shadow under yourself, unless you enable cg_thirdperson. It needs r_stencilbits <> 0 (usually set to 8 -default-, 24 or 32). Disabled in OpenArena 0.8.5+, except when playing in Single Player Deathmatch mode.',
 3: '(Vertex) Non-transparent uniform black detailed shadow under yourself and under the other players; no shadow under items. Disabled in OpenArena 0.8.5+, except when playing in Single Player Deathmatch mode.'
}))

V('cg_drawDamage', 'cg_Draw Shot Damage', 'Draw the damage of a shot')
V('cg_drawGun',    'cg_Draw Gun', 'Where to draw the weapon', default=1, type=int,
    select=Values({
        0: 'Hide',
        1: 'Right',
        2: 'Left',
        3: 'Center'
    })
)
V('cg_drawTeamOverlay', 'cg_Draw Team Overlay', 'Draw the Team Overlay')
V('cg_drawFriend',      'cg_Draw Friend',       'Draw friend')
V('cg_drawSpeed',       'cg_Draw Speed',    'Draw the speed-o-meter', default=False, type=bool)
V('cg_draw2D',          'cg_Draw HUD',      'Draw the HUD', default=True, type=bool)
V('cg_drawStatus',      'cg_Draw Status',   'Draw ammo, health and armor status', type=bool, default=True)
V('cg_drawTimer',       'cg_Draw Timer',    'Draw time elapsed since the beginning of the match', default=False, type=bool)
V('cg_drawFPS',         'cg_Draw FPS',      'Draw FPS', type=bool, default=False)
V('cg_drawSnapshot',    'cg_Draw Snapshot', default=False, type=bool)
V('cg_draw3dIcons',     'cg_Draw 3D icons', type=bool, default=True)
V('cg_drawIcons',       'cg_Draw Icons',    default=True, type=bool)
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
#                                   Network                                   #
# =============================================================================
V('net_socksEnabled',  'net_SOCKS Proxy Enabled', 'Use a SOCKS proxy', default=False, type=bool)
V('net_socksPassword', 'net_SOCKS Password',      'Set password for SOCKS proxy')
V('net_socksUsername', 'net_SOCKS Username',      'Set username for SOCKS proxy')
V('net_socksPort',     'net_SOCKS Port',          'Set the port number for SOCKS proxy', default=1080, type=int)
V('net_socksServer',   'net_SOCKS Host',          'Set the SOCKS proxy host')
V('rate',              'net_Rate (kbit/s)')       # TODO Default? "25000"
#('net_mcast6iface)
#('net_mcast6addr)
#('net_enabled)

# =============================================================================
#                                   FailMod                                   #
# =============================================================================
V('fm_chatbeep',      'fm_Chat Beep',         'Enable Beep on Chat (FailMod)')
V('fm_teamchatbeep',  'fm_Team Chat Beep',    'Enable Beep on Team Chat (FailMod)')
V('fm_votebeep',      'fm_Vote Beep',         'Enable Beep on Vote (FailMod)')
V('cg_drawReady',     'fm_Draw Ready',
    'If you are bothered with that text occupying the whole screen. -1 disables completely other numbers do something') #TODO


# =============================================================================
#                                    Client                                   #
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
#                                 Client Game                                 #
# =============================================================================
V('cg_viewsize', desc='Draw the game world in a smaller window. The HUD and chat messages will be drawn outside of that section.') # TODO
V('cg_simpleItems', 'cg_Simple Items',   'Draw 2D items', type=bool, default=False)
V('cg_lagometer',   'cg_Draw Lagometer', 'Draw the lagometer', type=bool)
V('cg_autoswitch',  'cg_Weapon Autoswitch', 'What to do when picking up a weapon', type=int, default=1,
    select=Values({
        0: 'OFF: Disable automatically switching weapons',
        1: 'ALWAYS: Always choose the weapon you just picked up (even if you already had it)',
        2: 'NEW: Automatically selects the weapon you just picked up, but only if you didn\'t have it before.',
        3: 'BETTER: Automatically selects the the weapon you just picked up, but only if it is "better" than the one you are currently using (even if you already had it). The switch is triggered only if both currently used and picked up weapon are listed in the "better weapons" list variable.',
        4: 'NEW&BETTER: Automatically selects the weapon you just picked up, but only if it is "better" than the one you are currently using and (at the same time) you didn\'t have it before. The switch is triggered only if both currently used and picked up weapon are listed in the "better weapons" list variable'
    })
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
#                                    Common                                   #
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
#                                    Server                                   #
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
#                                    Sound                                    #
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
#                                    Input                                    #
# =============================================================================
V('sensitivity', 'in_Mouse Sensitivity') # "5"

# =============================================================================
#                                    Render                                   #
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
V('r_textureMode', select=Values({ # TODO: descriptions
    'GL_LINEAR':  'GL_LINEAR',
    'GL_NEAREST': 'GL_NEAREST',
    'GL_LINEAR_MIPMAP_LINEAR':   'GL_LINEAR_MIPMAP_LINEAR',
    'GL_LINEAR_MIPMAP_NEAREST':  'GL_LINEAR_MIPMAP_NEAREST',
    'GL_NEAREST_MIPMAP_LINEAR':  'GL_NEAREST_MIPMAP_LINEAR',
    'GL_NEAREST_MIPMAP_NEAREST': 'GL_NEAREST_MIPMAP_NEAREST'
    }))
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
#                               Virtual Machine                               #
# =============================================================================
V('vm_ui')
V('vm_game')
V('vm_cgame')

# =============================================================================
#                                    Mouse                                    #
# =============================================================================
V('m_filter')
V('m_side')
V('m_forward')
V('m_yaw')
V('m_pitch')

# =============================================================================
#                                     Misc                                    #
# =============================================================================

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

json.dump(source.serialize(), sys.stdout, indent=1)
