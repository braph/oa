#!/usr/bin/python
# -*- coding: utf-8 -*-
LABEL = 'www.joz3d.net'
VARIABLES = {'0': {'default': '- Free For All',
       'description': '1- Tournament.',
       'name': '0'},
 '3': {'default': '- Team Deathmatch',
       'description': '4- Capture the Flag.',
       'name': '3'},
 '5': {'default': '- One Flag CTF', 'description': '6- Overload.', 'name': '5'},
 'activeaction': {'default': '',
                  'description': 'Variable holds a command to be executed upon '
                                 'connecting to a server.',
                  'name': 'activeaction'},
 'arch': {'default': 'win98',
          'description': 'Architecture/operating system.',
          'name': 'arch'},
 'bot_aasoptimize': {'default': '0',
                     'description': 'Optimize the .aas file when one is '
                                    'written - MrElusive.',
                     'name': 'bot_aasoptimize'},
 'bot_challenge': {'default': '0',
                   'description': 'Make the bot a bit more challenging - '
                                  'MrElusive.',
                   'name': 'bot_challenge'},
 'bot_debug': {'default': '0',
               'description': 'Toggle debugging tool for bot code.',
               'name': 'bot_debug'},
 'bot_developer': {'default': '0',
                   'description': 'Toggle developer mode for bots.',
                   'name': 'bot_developer'},
 'bot_enable': {'default': '0',
                'description': 'Enable and disable adding of bots to the '
                               'map/game.',
                'name': 'bot_enable'},
 'bot_fastchat': {'default': '0',
                  'description': 'Toggle between frequent and less frequent '
                                 'bot chat strings 1 = more often.',
                  'name': 'bot_fastchat'},
 'bot_forceclustering': {'default': '0',
                         'description': 'Force recalculating the aas clusters '
                                        '- MrElusive.',
                         'name': 'bot_forceclustering'},
 'bot_forcereachability': {'default': '0',
                           'description': 'Force recalculating the aas '
                                          'reachabilities - MrElusive.',
                           'name': 'bot_forcereachability'},
 'bot_forcewrite': {'default': '0',
                    'description': 'Force writing out a new .aas file - '
                                   'MrElusive.',
                    'name': 'bot_forcewrite'},
 'bot_grapple': {'default': '0',
                 'description': 'Toggle determines weather the bots will use '
                                'the grappling hook.',
                 'name': 'bot_grapple'},
 'bot_groundonly': {'default': '1',
                    'description': 'This is a debug cvar to show areas which '
                                   'does not work in the retail version '
                                   'special thanks to - MrElusive.',
                    'name': 'bot_groundonly'},
 'bot_interbreedbots': {'default': '10',
                        'description': 'Number of bots used for goal fuzzy '
                                       'logic interbreeding - MrElusive.',
                        'name': 'bot_interbreedbots'},
 'bot_interbreedchar': {'default': '',
                        'description': 'Bot character to be used with goal '
                                       'fuzzy logic interbreeding - MrElusive.',
                        'name': 'bot_interbreedchar'},
 'bot_interbreedcycle': {'default': '20',
                         'description': 'Number of matches between '
                                        'interbreeding - MrElusive.',
                         'name': 'bot_interbreedcycle'},
 'bot_interbreedwrite': {'default': '',
                         'description': 'File to write interbreeded goal fuzzy '
                                        'logic to - MrElusive.',
                         'name': 'bot_interbreedwrite'},
 'bot_maxdebugpolys': {'default': '128',
                       'description': 'Max number of polygons available for '
                                      'visualizing things when debugging '
                                      'MrElusive.',
                       'name': 'bot_maxdebugpolys'},
 'bot_memorydump': {'default': '0',
                    'description': 'Possibly displays memory allocation/use '
                                   'for bots used for debugging?.',
                    'name': 'bot_memorydump'},
 'bot_minplayers': {'default': '0',
                    'description': 'This is used to ensure a minimum numbers '
                                   'of players are playing on a server bots '
                                   'are added/removed to get the specified '
                                   'number of players in the game special '
                                   'thanks to - MrElusive.',
                    'name': 'bot_minplayers'},
 'bot_nochat': {'default': '0',
                'description': 'Toggle determines weather bots will chat or '
                               'not 0 = bots will chat.',
                'name': 'bot_nochat'},
 'bot_pause': {'default': '0',
               'description': 'Debug command to pause the bots - MrElusive.',
               'name': 'bot_pause'},
 'bot_predictobstacles': {'default': '1',
                          'description': "Possibly tells bot's to predict an "
                                         'obstacle and turn before running '
                                         'into it.',
                          'name': 'bot_predictobstacles'},
 'bot_reachability': {'default': '0',
                      'description': 'This is a debug cvar which does not work '
                                     'in the retail version - MrElusive.',
                      'name': 'bot_reachability'},
 'bot_reloadcharacters': {'default': '0',
                          'description': 'This cvar if set to 1 disabled bot '
                                         'character file caching. used when '
                                         'creating bot characters while '
                                         'keeping Q3A running. kicking and '
                                         're-adding a bot will reload the bot '
                                         'character files - MrElusive.',
                          'name': 'bot_reloadcharacters'},
 'bot_report': {'default': '0',
                'description': 'Debug command to have the bots report what '
                               'they are doing in CTF MrElusive.',
                'name': 'bot_report'},
 'bot_rocketjump': {'default': '1',
                    'description': 'Toggle determines weather the bots will '
                                   'use the rocket jump technique.',
                    'name': 'bot_rocketjump'},
 'bot_saveroutingcache': {'default': '0',
                          'description': 'Possibly allows the BOT AI to save '
                                         'routes for custom maps in memory.',
                          'name': 'bot_saveroutingcache'},
 'bot_testclusters': {'default': '0',
                      'description': 'Possibly a debug variable for testing '
                                     "BOT's on new terrain maps.",
                      'name': 'bot_testclusters'},
 'bot_testichat': {'default': '0',
                   'description': 'Used to test the initial bot chats. set '
                                  'this to 1 and add a bot. the bot will spit '
                                  'out all initial chats. - MrElusive.',
                   'name': 'bot_testichat'},
 'bot_testrchat': {'default': '0',
                   'description': 'Used to test the reply chats. set this to 1 '
                                  'and add one bot. the bot will always reply '
                                  'and dump all possible replies - MrElusive.',
                   'name': 'bot_testrchat'},
 'bot_testsolid': {'default': '0',
                   'description': 'Test for "solid areas" in the .aas file '
                                  '(read the q3r manual) - MrElusive.',
                   'name': 'bot_testsolid'},
 'bot_thinktime': {'default': '100',
                   'description': 'This is the time in milliseconds between '
                                  'two AI frames. - MrElusiveset the amount of '
                                  'time a bot thinks about a move before '
                                  'making it AI...(c:.',
                   'name': 'bot_thinktime'},
 'bot_usehook': {'default': '0',
                 'description': 'Toggle determines weather the bots will use '
                                'the grappling hook.',
                 'name': 'bot_usehook'},
 'bot_visualizejumppads': {'default': '0',
                           'description': 'Visualizes the default arch of a '
                                          'jumppad (read the q3r manual) - '
                                          'MrElusive.',
                           'name': 'bot_visualizejumppads'},
 'capturelimit': {'default': '8',
                  'description': 'Set # of times a team must grab the others '
                                 'flag before the win is declared.',
                  'name': 'capturelimit'},
 'cg_animspeed': {'default': '1',
                  'description': 'Toggle linear interpolation between '
                                 'successive frames in a player animation. 0 = '
                                 'no interpolation 1 = it does interpolate - '
                                 'Coriolis + WhatEver.',
                  'name': 'cg_animspeed'},
 'cg_autoswitch': {'default': '1',
                   'description': 'Auto-switch weapons (on pick-up).',
                   'name': 'cg_autoswitch'},
 'cg_bobpitch': {'default': '0.002',
                 'description': 'Set amount player view bobs forward/back '
                                'while moving.',
                 'name': 'cg_bobpitch'},
 'cg_bobroll': {'default': '0.002',
                'description': 'Set amount player view rolls side to side '
                               'while moving.',
                'name': 'cg_bobroll'},
 'cg_bobup': {'default': '0.005',
              'description': 'Set amount player view bobs up/down while '
                             'moving.',
              'name': 'cg_bobup'},
 'cg_brassTime': {'default': '1250',
                  'description': 'Set amount of time a shell casing gets '
                                 'displayed if set to 0 the game engine will '
                                 'skip all shell eject code.',
                  'name': 'cg_brassTime'},
 'cg_cameraOrbit': {'default': '0',
                    'description': 'Change the step or increment units of the '
                                   'orbit rotation from one angle how much of '
                                   'a step to next angle.',
                    'name': 'cg_cameraOrbit'},
 'cg_cameraOrbitDelay': {'default': '50',
                         'description': 'Change the rate at wich the camara '
                                        'moves to the next orbit position the '
                                        'higher the number the slower.',
                         'name': 'cg_cameraOrbitDelay'},
 'cg_centertime': {'default': '3',
                   'description': 'Set display time for center screen messages '
                                  '(0 off).',
                   'name': 'cg_centertime'},
 'cg_crosshairHealth': {'default': '1',
                        'description': 'Show health by the cross hairs (only '
                                       'works with #10 now?) - LOKi.',
                        'name': 'cg_crosshairHealth'},
 'cg_crosshairSize': {'default': '24',
                      'description': 'Crosshair size...incase you have '
                                     'crosshair envy (c:.',
                      'name': 'cg_crosshairSize'},
 'cg_crosshairX': {'default': '0',
                   'description': 'Set X coordinates of the crosshair if '
                                  'cg_crosshairSize not 0.',
                   'name': 'cg_crosshairX'},
 'cg_crosshairY': {'default': '0',
                   'description': 'Set Y coordinates of the crosshair if '
                                  'cg_crosshairSize not 0.',
                   'name': 'cg_crosshairY'},
 'cg_debuganim': {'default': '0',
                  'description': 'Toggle model animation debug mode.',
                  'name': 'cg_debuganim'},
 'cg_debugevents': {'default': '0',
                    'description': 'Toggle event debug mode.',
                    'name': 'cg_debugevents'},
 'cg_debugposition': {'default': '0',
                      'description': 'Toggle player position debug mode.',
                      'name': 'cg_debugposition'},
 'cg_deferPlayers': {'default': '1',
                     'description': 'The loading of player models will not '
                                    'take place until the next map, or when '
                                    'you die, or toggle the scoreboard (tab) '
                                    'this prevents the "hitch" effect when a '
                                    'player using a new model or skin joins '
                                    'the game after you. if you join the game '
                                    'after them the models and skins will '
                                    'download as you join?.',
                     'name': 'cg_deferPlayers'},
 'cg_demoLook': {'default': '0',
                 'description': 'Possibly to change the look of a recorded '
                                'demo?.',
                 'name': 'cg_demoLook'},
 'cg_draw2D': {'default': '1',
               'description': 'Toggle the drawing of 2D items or text on the '
                              'status display.',
               'name': 'cg_draw2D'},
 'cg_draw3dIcons': {'default': '1',
                    'description': 'Toggle the drawing of 3D icons on the HUD '
                                   'off and on draw 2D icon for ammo if '
                                   'cg_draw3dicons 0 "John Carmack".',
                    'name': 'cg_draw3dIcons'},
 'cg_drawAmmoWarning': {'default': '1',
                        'description': 'Toggle low-ammo warning display.',
                        'name': 'cg_drawAmmoWarning'},
 'cg_drawAttacker': {'default': '1',
                     'description': 'Toggle the display of last know '
                                    'assailant.',
                     'name': 'cg_drawAttacker'},
 'cg_drawCrosshair': {'default': '1',
                      'description': 'Select crosshair (change to zero if you '
                                     'have really good aim ha! ha!) 10 '
                                     'crosshairs to select from '
                                     '(cg_drawCrosshair 1 - 10) "John '
                                     'Carmack".',
                      'name': 'cg_drawCrosshair'},
 'cg_drawCrosshairNames': {'default': '1',
                           'description': 'Toggle displaying of the name of '
                                          "the player you're aiming at.",
                           'name': 'cg_drawCrosshairNames'},
 'cg_drawFPS': {'default': '0',
                'description': 'Toggle Frames Per Second display (when set to '
                               'one "0" is default).',
                'name': 'cg_drawFPS'},
 'cg_drawFriend': {'default': '1',
                   'description': 'Toggle the display of triangle shaped icon '
                                  'over the heads of your team mates.',
                   'name': 'cg_drawFriend'},
 'cg_drawGun': {'default': '1',
                'description': "Toggle determines if the weapon you're holding "
                               'is visible or not.',
                'name': 'cg_drawGun'},
 'cg_drawIcons': {'default': '1',
                  'description': 'Toggle the drawing of any icons on the HUD '
                                 'and scoreboard.',
                  'name': 'cg_drawIcons'},
 'cg_drawKiller': {'default': '1',
                   'description': "Toggle display of player's name and picture "
                                  'that fragged you last.',
                   'name': 'cg_drawKiller'},
 'cg_drawRewards': {'default': '1',
                    'description': 'Toggle display of award icons above the '
                                   '"you fragged..." message - LOKi.',
                    'name': 'cg_drawRewards'},
 'cg_drawSnapshot': {'default': '0',
                     'description': 'Toggle the display of snapshots counter '
                                    '(# of snaps since game start).',
                     'name': 'cg_drawSnapshot'},
 'cg_drawStatus': {'default': '1',
                   'description': 'Draw the HUD. (toggle weather or not health '
                                  'and score are displayed).',
                   'name': 'cg_drawStatus'},
 'cg_drawTeamOverlay': {'default': '0',
                        'description': 'Set the drawing location of the team '
                                       'status overlay 1=top right 2=bottom '
                                       'right 3=bottom left of the screen it '
                                       'shows team player names, location, '
                                       'ammo (and what type weapon), and frag '
                                       'count for each player - LOKi.',
                        'name': 'cg_drawTeamOverlay'},
 'cg_drawTimer': {'default': '1',
                  'description': 'Show timer on HUD. shows time since map '
                                 'start counts up - LOKi.',
                  'name': 'cg_drawTimer'},
 'cg_errordecay': {'default': '100',
                   'description': 'Helps to smooth animation during player '
                                  'prediction while experiencing packet loss '
                                  'or snapshot errors. "detect prediction '
                                  'errors and allow them to be decayed off '
                                  'over several frames to ease the jerk." from '
                                  'the source code comments cg_predict.c.',
                   'name': 'cg_errordecay'},
 'cg_extrapolate': {'default': '1',
                    'description': 'Toggle blending of animations from one to '
                                   'the next (like a segue) - Andre.',
                    'name': 'cg_extrapolate'},
 'cg_footsteps': {'default': '1',
                  'description': 'Toggle the footstep sounds of all players '
                                 '(cheat protected) - LOKi.',
                  'name': 'cg_footsteps'},
 'cg_forceModel': {'default': '0',
                   'description': 'Force model selection, also forces player '
                                  'sounds "John Carmack".',
                   'name': 'cg_forceModel'},
 'cg_fov': {'default': '90',
            'description': 'Field of view/vision "90" is default higher '
                           'numbers give peripheral vision.',
            'name': 'cg_fov'},
 'cg_gibs': {'default': '1',
             'description': 'Toggle the display of animated gibs (explosions '
                            'flying body parts!).',
             'name': 'cg_gibs'},
 'cg_gun': {'default': '1',
            'description': 'Toggle determines if the weapon your holding is '
                           'visible or not.',
            'name': 'cg_gun'},
 'cg_gunX': {'default': '0',
             'description': 'Set X coordinates of viewable weapon if '
                            'cg_drawGun is set to 1.',
             'name': 'cg_gunX'},
 'cg_gunY': {'default': '0',
             'description': 'Set Y coordinates of viewable weapon if '
                            'cg_drawGun is set to 1.',
             'name': 'cg_gunY'},
 'cg_gunZ': {'default': '0',
             'description': 'Set Z coordinates of viewable weapon if '
                            'cg_drawGun is set to 1 moves the gun model '
                            'forward or backward in relation to the player '
                            'models hold.',
             'name': 'cg_gunZ'},
 'cg_ignore': {'default': '0',
               'description': 'Used for debugging possibly like the notarget '
                              'command.',
               'name': 'cg_ignore'},
 'cg_lagometer': {'default': '1',
                  'description': 'Toggle the display of Lag-O-Meter on the HUD '
                                 '1=netgraph 0=frag counter which changes '
                                 'color to reflect what place your in as well '
                                 'Section 6 of the '
                                 'Q3Test_Instructions_Readme.txt has a more '
                                 'detailed description of this tool. Simply '
                                 'put the top graph (blue/yellow): A vertical '
                                 'line is painted for every rendered frame. if '
                                 'the line is blue and going down from the '
                                 'baseline that indicates a steady transition '
                                 'of frames from one to the next. A yellow '
                                 'line going up from the baseline means the '
                                 'frames are not being fully rendered in time. '
                                 'The bottom graph (green/yellow/red): A '
                                 'vertical line is painted for every received '
                                 'snapshot. If the line is green it indicates '
                                 'properly received snapshots, with the height '
                                 'of the bar proportional to the ping. If the '
                                 'bar is yellow it indicates that the snapshot '
                                 'was held back because it hit the rate limit. '
                                 'If the line is red it means the snapshot was '
                                 'dropped by the network...Lots of thanx goes '
                                 'out to hacker, Erik, TeoH, and Wilka.',
                  'name': 'cg_lagometer'},
 'cg_markoffset': {'default': '1',
                   'description': 'Set marks (decals) offset. some video cards '
                                  'display the marks with the wrong offset, so '
                                  'you will be able to see the square decal '
                                  'that encapsulates the effect because the '
                                  'offset rises above the wall surface. change '
                                  'the offset the square goes away.',
                   'name': 'cg_markoffset'},
 'cg_marks': {'default': '1',
              'description': 'Toggle the marks the projectiles leave on the '
                             'wall (bullet holes, etc).',
              'name': 'cg_marks'},
 'cg_noProjectileTrail': {'default': '0',
                          'description': 'Toggle the display of smoke trail '
                                         'effect behind rockets - Jax_Gator '
                                         'Dekard.',
                          'name': 'cg_noProjectileTrail'},
 'cg_noTaunt': {'default': '0',
                'description': 'Possibly turn off the ability to hear voice '
                               'taunts.',
                'name': 'cg_noTaunt'},
 'cg_noVoiceChats': {'default': '0',
                     'description': 'Possibly turn off the ability to hear '
                                    'voice chats.',
                     'name': 'cg_noVoiceChats'},
 'cg_noVoiceText': {'default': '0',
                    'description': 'Possibly turn off the display of the voice '
                                   'chat text copied to the console.',
                    'name': 'cg_noVoiceText'},
 'cg_noplayeranims': {'default': '0',
                      'description': 'Toggle player model animations. (the '
                                     'animation frame displayed when this is '
                                     'disabled is rather odd, though.).',
                      'name': 'cg_noplayeranims'},
 'cg_nopredict': {'default': '0',
                  'description': 'Toggle client-side player prediction. '
                                 '(disabling causes the client to wait for '
                                 'updates from the server before updating the '
                                 'player location.).',
                  'name': 'cg_nopredict'},
 'cg_oldPlasma': {'default': '1',
                  'description': 'Toggle the use of old or new particle style '
                                 'plasma gun effect - 20 20.',
                  'name': 'cg_oldPlasma'},
 'cg_oldRail': {'default': '0',
                'description': 'Toggle the use of old or new spiral style rail '
                               'trail effect - 20 20.',
                'name': 'cg_oldRail'},
 'cg_oldRocket': {'default': '1',
                  'description': 'Toggle the use of old or new style rocket '
                                 'trail effect - 20 20.',
                  'name': 'cg_oldRocket'},
 'cg_predictItems': {'default': '1',
                     'description': 'Toggle client-side item prediction. 0 '
                                    'option to not do local prediction of item '
                                    'pickup - John Carmack.',
                     'name': 'cg_predictItems'},
 'cg_railTrailTime': {'default': '400',
                      'description': "Set how long the railgun's trails last.",
                      'name': 'cg_railTrailTime'},
 'cg_runpitch': {'default': '0.002',
                 'description': 'Set amount player view bobs up and down while '
                                'running.',
                 'name': 'cg_runpitch'},
 'cg_runroll': {'default': '0.005',
                'description': 'Set amount player view rolls side to side '
                               'while running (in 3rd person only?).',
                'name': 'cg_runroll'},
 'cg_scorePlums': {'default': '1',
                   'description': 'Toggle the display of the floating scoring '
                                  'number balloons when a player scores a '
                                  'point or points (including negative points) '
                                  'in any game type, the awarded point value '
                                  'floats up from the target like a balloon '
                                  'and slowly fades out.',
                   'name': 'cg_scorePlums'},
 'cg_shadows': {'default': '0',
                'description': 'Set shadow detail level (0 = OFF, 1 = basic '
                               'discs, 2 = stencil buffered 3 = simple stencil '
                               'buffered(if r_stencilebits is not=0)) - Andre '
                               'Lucas.',
                'name': 'cg_shadows'},
 'cg_showcrosshair': {'default': '1',
                      'description': 'Appeared in version 1.06 then removed in '
                                     '1.07 now back in 1.08 then removed again '
                                     'in 1.09 hmm (replaced with '
                                     'multi-crosshairs).',
                      'name': 'cg_showcrosshair'},
 'cg_showmiss': {'default': '0',
                 'description': 'Toggle the display of missed packets or '
                                'predictions on the HUD.',
                 'name': 'cg_showmiss'},
 'cg_simpleItems': {'default': '0',
                    'description': 'Toggle the use of 2D sprite objects in '
                                   'place of the 3D animated objects makes '
                                   'some objects more "simple" (faster to '
                                   'render) - hacker.',
                    'name': 'cg_simpleItems'},
 'cg_smoothClients': {'default': '0',
                      'description': 'When g_smoothClients is enabled on the '
                                     'server and you enable cg_smoothClients '
                                     'then players in your view will be '
                                     'predicted and will appear more smooth '
                                     'even if they are on a bad network '
                                     'connection. however small prediction '
                                     'errors might appear.',
                      'name': 'cg_smoothClients'},
 'cg_stats': {'default': '0',
              'description': 'Toggles display of client frames in sequence '
                             'missed frames are not shown.',
              'name': 'cg_stats'},
 'cg_stereoSeparation': {'default': '0.4',
                         'description': 'The amount of stereo separation (for '
                                        '3D glasses!) You ever take off your '
                                        'glasses at a 3D movie, remember how '
                                        'the images were separated into 3 '
                                        "colors? that's what this does.",
                         'name': 'cg_stereoSeparation'},
 'cg_swingSpeed': {'default': '0.3',
                   'description': 'Set speed player model rotates to match '
                                  'position (1 is no delay, 0 will never '
                                  'turn).',
                   'name': 'cg_swingSpeed'},
 'cg_teamChatHeight': {'default': '8',
                       'description': 'Set number of lines or strings of text '
                                      'that remain on screen in team play chat '
                                      'mode (messagemode2) values are 1 - 8 - '
                                      'LOKi.',
                       'name': 'cg_teamChatHeight'},
 'cg_teamChatTime': {'default': '3000',
                     'description': 'Set how long messages from teammates are '
                                    'displayed on the screen.',
                     'name': 'cg_teamChatTime'},
 'cg_teamChatsOnly': {'default': '0',
                      'description': 'When this is set to a one only chats '
                                     'from team mates will be displayed.',
                      'name': 'cg_teamChatsOnly'},
 'cg_thirdPerson': {'default': '0',
                    'description': 'Toggle the use of and third person view.',
                    'name': 'cg_thirdPerson'},
 'cg_thirdPersonAngle': {'default': '0',
                         'description': 'Change the angle of perspective you '
                                        'view your player (180 changes view to '
                                        'the front of the model).',
                         'name': 'cg_thirdPersonAngle'},
 'cg_thirdPersonRange': {'default': '40',
                         'description': 'Change the distance you view your '
                                        'player from when in 3rd person view.',
                         'name': 'cg_thirdPersonRange'},
 'cg_tracerchance': {'default': '0.4',
                     'description': 'Set frequency of tracer bullets (1 is all '
                                    'tracers).',
                     'name': 'cg_tracerchance'},
 'cg_tracerlength': {'default': '100',
                     'description': 'Set length of tracer bullets.',
                     'name': 'cg_tracerlength'},
 'cg_tracerwidth': {'default': '1',
                    'description': 'Set width of tracer bullets.',
                    'name': 'cg_tracerwidth'},
 'cg_trueLightning': {'default': '0',
                      'description': 'Settings of the new shaft style. from '
                                     'the OSP readme...specifies the "lag" '
                                     'imposed on the rendering of the '
                                     'lightning gun shaft. a value of 0.0 is '
                                     'just like the baseq3 version "feel" of '
                                     'the LG. a value of 1.0 imposes no lag at '
                                     'all (shaft is always rendered on the '
                                     'crosshairs). a value of 0.5 is a good '
                                     'mix of the two to reduce the wet-noodle '
                                     'effect, while still maintaining '
                                     'consistency of where the server actually '
                                     'sees the shaft. I would like to thank '
                                     'all the readers who submitted good '
                                     'descriptions of this new variable to me, '
                                     'there were a ton, but the ones who had '
                                     'it correct are listed here.',
                      'name': 'cg_trueLightning'},
 'cg_viewsize': {'default': '100',
                 'description': 'Changes view port size 30 - 100 (you probably '
                                "wouldn't want less than 100).",
                 'name': 'cg_viewsize'},
 'cg_zoomfov': {'default': '22.5',
                'description': 'What the zoomed in field of view will be any '
                               'thing more than 30 would not be sniper '
                               'friendly.',
                'name': 'cg_zoomfov'},
 'cheats': {'default': '0',
            'description': 'Enable cheating commands (give all) (serverside '
                           'only).',
            'name': 'cheats'},
 'cl_allowDownload': {'default': '1',
                      'description': 'Toggle automatic downloading of maps, '
                                     'models, sounds, and textures.',
                      'name': 'cl_allowDownload'},
 'cl_anglespeedkey': {'default': '1.5',
                      'description': 'Set the speed that the direction keys '
                                     '(not mouse) change the view angle.',
                      'name': 'cl_anglespeedkey'},
 'cl_anonymous': {'default': '0',
                  'description': 'Possibly to toggle anonymous connection to a '
                                 'server.',
                  'name': 'cl_anonymous'},
 'cl_avidemo': {'default': '0',
                'description': 'Toggle recording of a slideshow of screenshots '
                               'records into the snapshot folder and appears '
                               'to have overwritten some snapshots I had in '
                               'there )c:.',
                'name': 'cl_avidemo'},
 'cl_cdkey': {'default': '123456789',
              'description': 'Variable to hold the CD key number to prevent '
                             'bootleg/warez.',
              'name': 'cl_cdkey'},
 'cl_conXOffset': {'default': '0',
                   'description': 'Offset the console message display 0 - top '
                                  'left 999 - extreme top right (off the '
                                  'page).',
                   'name': 'cl_conXOffset'},
 'cl_currentServerAddress': {'default': None,
                             'description': 'Variable holds the IP address of '
                                            'the currently connected server.',
                             'name': 'cl_currentServerAddress'},
 'cl_debugMove': {'default': '0',
                  'description': 'Used for debugging cl_debugmove [1/2] from '
                                 "John Carmack's plan file.",
                  'name': 'cl_debugMove'},
 'cl_downloadName': {'default': '',
                     'description': 'Variable holds filename of file currently '
                                    'downloading.',
                     'name': 'cl_downloadName'},
 'cl_freelook': {'default': '1',
                 'description': 'Toggle the use of freelook with the mouse '
                                '(your ability to look up and down).',
                 'name': 'cl_freelook'},
 'cl_freezeDemo': {'default': '0',
                   'description': 'Stops a demo play back and freeze on one '
                                  'frame.',
                   'name': 'cl_freezeDemo'},
 'cl_maxPing': {'default': '800',
                'description': 'Controls which servers are displayed in the '
                               'in-game server browser - ata.',
                'name': 'cl_maxPing'},
 'cl_maxpackets': {'default': '30',
                   'description': 'Set the transmission packet size or how '
                                  'many packets are sent to client.',
                   'name': 'cl_maxpackets'},
 'cl_motd': {'default': '1',
             'description': 'Toggle the display of "Message of the day" When '
                            'Quake 3 Arena starts a map up, it sends the '
                            'GL_RENDERER string to the Message Of The Day '
                            'server at id. This responds back with a message '
                            'of the day to the client. If you wish to switch '
                            'this option off, set CL_MOTD to 0.',
             'name': 'cl_motd'},
 'cl_motdString': {'default': '',
                   'description': "Possibly a MOTD from id's master server it "
                                  'is a read only variable.',
                   'name': 'cl_motdString'},
 'cl_mouseAccel': {'default': '0',
                   'description': 'Toggle the use of mouse acceleration the '
                                  'mouse speeds up or becomes more sensitive '
                                  'as it continues in one direction.',
                   'name': 'cl_mouseAccel'},
 'cl_nodelta': {'default': '0',
                'description': 'Disable delta compression (slows net '
                               'performance, only use if net errors happen '
                               'otherwise not recommended).',
                'name': 'cl_nodelta'},
 'cl_noprint': {'default': '0',
                'description': 'Printout messages to your screen or to the '
                               'console (tired of all the chatter?).',
                'name': 'cl_noprint'},
 'cl_packetdup': {'default': '1',
                  'description': 'Default was 2 but changed to 1 since version '
                                 '1.09.',
                  'name': 'cl_packetdup'},
 'cl_paused': {'default': '0',
               'description': 'Variable holds the status of the paused flag on '
                              'the client side.',
               'name': 'cl_paused'},
 'cl_pitchspeed': {'default': '140',
                   'description': 'Set the pitch rate when +lookup and/or '
                                  '+lookdown are active.',
                   'name': 'cl_pitchspeed'},
 'cl_run': {'default': '1',
            'description': 'Always run...play without it I dare you! (c:.',
            'name': 'cl_run'},
 'cl_running': {'default': '1',
                'description': 'Variable which shows weather or not a client '
                               'game is running or weather we are in '
                               'server/client mode (read only).',
                'name': 'cl_running'},
 'cl_serverStatusResendTime': {'default': '750',
                               'description': 'Possibly allows the admin to '
                                              'change the rate of the '
                                              'heartbeats to the master '
                                              'server(s).',
                               'name': 'cl_serverStatusResendTime'},
 'cl_showSend': {'default': '0',
                 'description': 'Network debugging tool "John Carmack".',
                 'name': 'cl_showSend'},
 'cl_showTimeDelta': {'default': '0',
                      'description': 'Display time delta between server '
                                     'updates.',
                      'name': 'cl_showTimeDelta'},
 'cl_showmouserate': {'default': '0',
                      'description': 'Show the mouse rate of mouse samples per '
                                     'frame (USB 1/per frame).',
                      'name': 'cl_showmouserate'},
 'cl_shownet': {'default': '0',
                'description': 'Display network quality info.',
                'name': 'cl_shownet'},
 'cl_timeNudge': {'default': '0',
                  'description': 'Effectively adds local lag to try to make '
                                 'sure you interpolate instead of extrapolate '
                                 '(try 100 for a really laggy server).',
                  'name': 'cl_timeNudge'},
 'cl_timeout': {'default': '125',
                'description': 'Seconds to wait before you are removed from '
                               'the server when you lag out.',
                'name': 'cl_timeout'},
 'cl_updateInfoString': {'default': '',
                         'description': '"challenge\\14985\\motd\\This is used '
                                        'by id when new versions come out".',
                         'name': 'cl_updateInfoString'},
 'cl_yawspeed': {'default': '140',
                 'description': 'Set the yaw rate when +left and/or +right are '
                                'active.',
                 'name': 'cl_yawspeed'},
 'cm_curveClipHack': {'default': '0',
                      'description': 'Must have been a cheat!!! removed now.',
                      'name': 'cm_curveClipHack'},
 'cm_noAreas': {'default': '0',
                'description': 'Toggle the ability of the player bounding box '
                               'to clip through areas?.',
                'name': 'cm_noAreas'},
 'cm_noCurves': {'default': '0',
                 'description': 'Toggle the ability of the player bounding box '
                                'to clip through curved surfaces.',
                 'name': 'cm_noCurves'},
 'cm_playerCurveClip': {'default': '1',
                        'description': 'Toggles the ability of the player '
                                       'bounding box to respect curved '
                                       'surfaces.',
                        'name': 'cm_playerCurveClip'},
 'color': {'default': '1',
           'description': 'Rail trail color '
                          'blue/green/cyan/red/magenta/yellow/white '
                          'respectively 1/2/3/4/5/6/7.',
           'name': 'color'},
 'color1': {'default': '2',
            'description': 'Spiral rail trail color spiral core - special '
                           'thanks to schiz Jax_Gator Dekard '
                           'blue/green/cyan/red/magenta/yellow/white '
                           'respectively 1/2/3/4/5/6/7.',
            'name': 'color1'},
 'color2': {'default': '5',
            'description': 'Spiral rail trail color spiral ring - special '
                           'thanks to schiz Jax_Gator Dekard '
                           'blue/green/cyan/red/magenta/yellow/white '
                           'respectively 1/2/3/4/5/6/7.',
            'name': 'color2'},
 'com_blood': {'default': '1',
               'description': 'Toggle the blood mist effect in the gib '
                              'animations. 0 option for no gibs and no blood '
                              'on hits "John Carmack".',
               'name': 'com_blood'},
 'com_buildScript': {'default': '0',
                     'description': 'Possibly used for the loading and caching '
                                    'of game data like a list of things to be '
                                    'loaded and caches the data for quicker '
                                    'reloading.',
                     'name': 'com_buildScript'},
 'com_cameraMode': {'default': '0',
                    'description': 'Seems to toggle the view of your player '
                                   'model off and on when in 3D camera view.',
                    'name': 'com_cameraMode'},
 'com_dropsim': {'default': '0',
                 'description': 'For testing simulates packet loss during '
                                'communication drops.',
                 'name': 'com_dropsim'},
 'com_hunkMegs': {'default': '20',
                  'description': 'Set the amount of memory you want quake3.exe '
                                 'to reserve for game play dedicated server '
                                 'memory optimizations. Tips: com_hunkMegs 4 '
                                 'sv_maxclients 3 bot_enable 0 "John Carmack".',
                  'name': 'com_hunkMegs'},
 'com_introplayed': {'default': '1',
                     'description': 'Toggle displaying of intro cinematic once '
                                    'it has been seen this variable keeps it '
                                    'from playing each time, to see it again '
                                    'set this to zero.',
                     'name': 'com_introplayed'},
 'com_maxfps': {'default': '100',
                'description': 'Set max frames per second you receive from '
                               'server (maxfps was removed).',
                'name': 'com_maxfps'},
 'com_showtrace': {'default': '0',
                   'description': 'Toggle display of packet traces. '
                                  '0=disables,1=toggles.',
                   'name': 'com_showtrace'},
 'com_soundMegs': {'default': '8',
                   'description': 'Com_soundmegs and com_zonemegs can be '
                                  'adjusted to provide better performance on '
                                  'systems with more than 64mb of memory. the '
                                  'default configuration is set to allow the '
                                  'game to run on a 64 MB system. on a 128 MB '
                                  'system we would run with the '
                                  'following:com_hunkMegs - 64 com_soundMegs - '
                                  '16 com_zoneMegs - 24.',
                   'name': 'com_soundMegs'},
 'com_speeds': {'default': '0',
                'description': 'Toggle display of frame counter, all, sv, cl, '
                               'gm, rf, and bk whatever they are.',
                'name': 'com_speeds'},
 'com_zoneMegs': {'default': '16',
                  'description': 'Com_soundmegs and com_zonemegs can be '
                                 'adjusted to provide better performance on '
                                 'systems with more than 64mb of memory. the '
                                 'default configuration is set to allow the '
                                 'game to run on a 64 MB system. on a 128 MB '
                                 'system we would run with the '
                                 'following:com_hunkMegs - 64 com_soundMegs - '
                                 '16 com_zoneMegs - 24.',
                  'name': 'com_zoneMegs'},
 'con_notifytime': {'default': '3',
                    'description': 'Defines how long messages (from players or '
                                   'the system) are on the screen.',
                    'name': 'con_notifytime'},
 'conback': {'default': '',
             'description': 'Select console background file '
                            '"gfx/2d/conback.tga".',
             'name': 'conback'},
 'crosshairhealth': {'default': '1',
                     'description': 'Show health by the cross hairs.',
                     'name': 'crosshairhealth'},
 'crosshairsize': {'default': '24',
                   'description': 'Crosshair size...incase you have crosshair '
                                  'envy (c:.',
                   'name': 'crosshairsize'},
 'd_bot': {'default': '',
           'description': 'All d_ commands have been removed to disable bots '
                          'most likely.',
           'name': 'd_bot'},
 'd_botai': {'default': '0',
             'description': 'All d_ commands have been removed to disable bots '
                            'most likely.',
             'name': 'd_botai'},
 'd_botaiming': {'default': '0',
                 'description': 'All d_ commands have been removed to disable '
                                'bots most likely.',
                 'name': 'd_botaiming'},
 'd_botfreeze': {'default': '0',
                 'description': 'All d_ commands have been removed to disable '
                                'bots most likely.',
                 'name': 'd_botfreeze'},
 'd_break': {'default': '0',
             'description': 'All d_ commands have been removed to disable bots '
                            'most likely.',
             'name': 'd_break'},
 'd_noroam': {'default': '0',
              'description': 'All d_ commands have been removed to disable '
                             'bots most likely.',
              'name': 'd_noroam'},
 'dedicated': {'default': '0',
               'description': 'Set console to server only 0 is a listen, 1 is '
                              'lan, and 2 is internet (command line cvar '
                              'causes engine not to load 3D game just a server '
                              'console C:\\Q3TEST\\quake3.exe +set dedicated '
                              '2) - Dekard.',
               'name': 'dedicated'},
 'developer': {'default': '0',
               'description': 'Enable developer mode (more verbose messages).',
               'name': 'developer'},
 'disable.cfg': {'default': None,
                 'description': 'Enable.cfg.',
                 'name': 'disable.cfg'},
 'disable_<item': {'default': 'name>',
                   'description': 'This command allows the administrator of a '
                                  'server to disable a particular item from '
                                  'the map. as an example: "/set '
                                  'disable_weapon_bfg 1" will make it so that '
                                  'the bfg does not show up. changing the '
                                  'value back to 0 and executing a '
                                  '/map_restart command will bring the '
                                  'disabled item back. - K2 disable.cfg '
                                  'enable.cfg configs by zYmO.',
                   'name': 'disable_<item'},
 'dmflags': {'default': '0',
             'description': 'Set deathmatch flags originally I posted the '
                            'values of Quake 2 dmflags but have since tested '
                            "them and most of them don't work.",
             'name': 'dmflags'},
 'fixedtime': {'default': '0',
               'description': 'Toggle the rendering of every frame the game '
                              'will wait until each frame is completely '
                              'rendered before sending the next frame.',
               'name': 'fixedtime'},
 'fov': {'default': '90',
         'description': 'Field of view/vision "90" is default higher numbers '
                        'give peripheral vision.',
         'name': 'fov'},
 'fraglimit': {'default': '20',
               'description': 'Set fraglimit on a server (0 is no limit).',
               'name': 'fraglimit'},
 'freelook': {'default': '1',
              'description': 'Steer aim and control head movement with the '
                             'mouse a must (c:.',
              'name': 'freelook'},
 'fs_basegame': {'default': '',
                 'description': 'Allows people to base mods upon mods syntax '
                                'to follow.',
                 'name': 'fs_basegame'},
 'fs_basepath': {'default': '',
                 'description': 'Set base path root C:\\Program Files\\Quake '
                                'III Arena for files to be downloaded from '
                                "this path may change for TC's and MOD's.",
                 'name': 'fs_basepath'},
 'fs_cdpath': {'default': '',
               'description': 'Possibly a variable to use when the full CD was '
                              'copied to the HDD.',
               'name': 'fs_cdpath'},
 'fs_copyfiles': {'default': '0',
                  'description': 'Toggle if files can be copied from servers '
                                 'or if client will download.',
                  'name': 'fs_copyfiles'},
 'fs_debug': {'default': '0',
              'description': 'Possibly enables file server debug mode for '
                             'download/uploads or something.',
              'name': 'fs_debug'},
 'fs_game': {'default': '',
             'description': 'Set gamedir set the game folder/dir default is '
                            'baseq3 (other for MODS).',
             'name': 'fs_game'},
 'fs_homepath': {'default': None,
                 'description': "Possibly for TC's and MODS the default is the "
                                'path to quake3.exe.',
                 'name': 'fs_homepath'},
 'fs_openedList': {'default': '',
                   'description': 'Variable holds a list of all the pk3 files '
                                  'the client found.',
                   'name': 'fs_openedList'},
 'fs_referencedList': {'default': '',
                       'description': 'Variable holds a list of all the pk3 '
                                      'files the client loaded data from.',
                       'name': 'fs_referencedList'},
 'fs_restrict': {'default': '',
                 'description': 'Demoversion if set to 1 restricts game to 4 '
                                'arenas like the Q3A demo.',
                 'name': 'fs_restrict'},
 'g_aimTest': {'default': '0',
               'description': 'Removed possibly was a cheat (bot like aiming).',
               'name': 'g_aimTest'},
 'g_allowVote': {'default': '1',
                 'description': 'Toggle the use of voting on a server.',
                 'name': 'g_allowVote'},
 'g_arenaName': {'default': '0',
                 'description': 'Possibly toggles the display of the name of '
                                'the current arena?.',
                 'name': 'g_arenaName'},
 'g_arenaRank': {'default': '',
                 'description': 'Possibly a variable to hold the value for '
                                'your rank in the current series.',
                 'name': 'g_arenaRank'},
 'g_arenaScores': {'default': '',
                   'description': 'Possibly a variable to hold the value of '
                                  'previous arena series scores.',
                   'name': 'g_arenaScores'},
 'g_arenasFile': {'default': '',
                  'description': 'Sets the file name to use for map rotation '
                                 'and bot names and game type for each arena '
                                 'default scripts/arenas.txt within the PK3 '
                                 'file.',
                  'name': 'g_arenasFile'},
 'g_banIPs': {'default': '',
              'description': 'Ban specified TCP/IP address from connecting to '
                             'your server.',
              'name': 'g_banIPs'},
 'g_blueTeam': {'default': '',
                'description': 'Set the icon for the blue team (example '
                               'Pagans).',
                'name': 'g_blueTeam'},
 'g_botsFile': {'default': '',
                'description': 'Sets the file name to use for setting up the '
                               'bots configuration and characters for each bot '
                               'default scripts/bots.txt within the PK3 file.',
                'name': 'g_botsFile'},
 'g_debugAlloc': {'default': '0',
                  'description': 'Possibly debugging tool for memory '
                                 'allocation?.',
                  'name': 'g_debugAlloc'},
 'g_debugDamage': {'default': '0',
                   'description': 'Debugging tool for damage effects?.',
                   'name': 'g_debugDamage'},
 'g_debugMove': {'default': '0',
                 'description': 'Debugging tool for brush/entity movements?.',
                 'name': 'g_debugMove'},
 'g_doWarmup': {'default': '0',
                'description': 'Toggle the use of a warmup period before a '
                               'match game.',
                'name': 'g_doWarmup'},
 'g_enableBreath': {'default': '0',
                    'description': 'Enable breath in cold maps you can see the '
                                   'players breath - Dekard.',
                    'name': 'g_enableBreath'},
 'g_enableDust': {'default': '0',
                  'description': 'Enable dust to be kicked up from feet in '
                                 'areas that have that map entity - Dekard.',
                  'name': 'g_enableDust'},
 'g_filterBan': {'default': '1',
                 'description': 'Toggle the banning of players that match a '
                                'certain criteria/filter?.',
                 'name': 'g_filterBan'},
 'g_forcerespawn': {'default': '10',
                    'description': "Set the respawn time in seconds, 0 = don't "
                                   'force respawn.',
                    'name': 'g_forcerespawn'},
 'g_friendlyFire': {'default': '0',
                    'description': 'Toggle damage caused by friendly fire 1 = '
                                   'can kill or injure teammate.',
                    'name': 'g_friendlyFire'},
 'g_gametype': {'default': '0',
                'description': '0- Free For All 1 - Tournament 2 - Single '
                               'Player 3 - Team Deathmatch 4 - Capture the '
                               'Flag to start a dedicated server in tournament '
                               'mode, you would use: quake3.exe +set dedicated '
                               '2 +set sv_zone tournaments +set g_gametype 1 '
                               '+map q3tourney2, "Graeme Devine" thanks also '
                               'to TheKiller 5 - One Flag CTF 6 - Overload 7 - '
                               'Harvester (Team Arena only).',
                'name': 'g_gametype'},
 'g_gravity': {'default': '800',
               'description': 'Set the gravity level. (this is normally set by '
                              'a property of the map loaded).',
               'name': 'g_gravity'},
 'g_inactivity': {'default': '0',
                  'description': 'Set the amount of time a player can remain '
                                 'inactive before kicked.',
                  'name': 'g_inactivity'},
 'g_knockback': {'default': '1000',
                 'description': 'The knockback from a weapon, higher number = '
                                'greater knockback.',
                 'name': 'g_knockback'},
 'g_listEntity': {'default': '0',
                  'description': 'Toggles the display of map entities shows '
                                 'them by number.',
                  'name': 'g_listEntity'},
 'g_log': {'default': '1',
           'description': 'Toggles logging of game data or statistics John '
                          'Carmack made g_log a filename instead of a 0/1 in '
                          'this version.',
           'name': 'g_log'},
 'g_logSync': {'default': '0',
               'description': 'Toggle the logging to append to the existing '
                              'file and not overwrite.',
               'name': 'g_logSync'},
 'g_maxGameClients': {'default': '0',
                      'description': 'Set maximum # of players who may join '
                                     'the game the remainder of clients are '
                                     'forced to spectate - Holesinswiss.',
                      'name': 'g_maxGameClients'},
 'g_motd': {'default': '',
            'description': 'Set message of the day to "X" (see "cl_motd" to '
                           'display it).',
            'name': 'g_motd'},
 'g_needpass': {'default': '0',
                'description': 'Variable alerts the client that a password is '
                               'needed to join your server.',
                'name': 'g_needpass'},
 'g_password': {'default': '',
                'description': 'Set the serverside password players use to get '
                               'on the server.',
                'name': 'g_password'},
 'g_podiumDist': {'default': '80',
                  'description': 'Sets the draw distance of the podium object '
                                 'player models stand on after a single player '
                                 'bot match - LOKi.',
                  'name': 'g_podiumDist'},
 'g_podiumDrop': {'default': '70',
                  'description': 'Sets the height of the podium object player '
                                 'models stand on after a single player bot '
                                 'match - LOKi.',
                  'name': 'g_podiumDrop'},
 'g_quadfactor': {'default': '3',
                  'description': 'Allows the admin to set the amount of damage '
                                 'the quad damage will do.',
                  'name': 'g_quadfactor'},
 'g_redTeam': {'default': '',
               'description': 'Set the team icon for the red team (example '
                              'Stroggs).',
               'name': 'g_redTeam'},
 'g_restarted': {'default': '0',
                 'description': 'Read only variable that is toggled when the '
                                'game has been restarted in match mode this '
                                'sets an event trap for if warmup is needed.',
                 'name': 'g_restarted'},
 'g_singlePlayer': {'default': '0',
                    'description': "Possibly to allow 3rd party's to make TC's "
                                   'for single player style games?.',
                    'name': 'g_singlePlayer'},
 'g_smoothClients': {'default': '1',
                     'description': 'Enable players to use the smooth clients '
                                    'option on the server (cg_smoothClients).',
                     'name': 'g_smoothClients'},
 'g_spAwards': {'default': '',
                'description': 'Variable holds the names of the award icons '
                               'that have been earned in the tier levels in '
                               'single player mode.',
                'name': 'g_spAwards'},
 'g_spScores1': {'default': '',
                 'description': 'Holds your scores on skill level 1 in single '
                                'player games - Dr Qube.',
                 'name': 'g_spScores1'},
 'g_spScores2': {'default': '',
                 'description': 'Holds your scores on skill level 2 in single '
                                'player games - Dr Qube.',
                 'name': 'g_spScores2'},
 'g_spScores3': {'default': '',
                 'description': 'Holds your scores on skill level 3 in single '
                                'player games - Dr Qube.',
                 'name': 'g_spScores3'},
 'g_spScores4': {'default': '',
                 'description': 'Holds your scores on skill level 4 in single '
                                'player games - Dr Qube.',
                 'name': 'g_spScores4'},
 'g_spScores5': {'default': '',
                 'description': 'Holds your scores on skill level 5 in single '
                                'player games - Dr Qube.',
                 'name': 'g_spScores5'},
 'g_spSkill': {'default': '2',
               'description': 'Holds your current skill level for single '
                              'player 1 = I can win 2 = bring it on 3 = hurt '
                              'me plenty 4 = hardcore and 5 = nightmare.',
               'name': 'g_spSkill'},
 'g_spVideos': {'default': '',
                'description': 'Variable holds the names of the cinematic '
                               'videos that are unlocked at the end of each '
                               'tier completion.',
                'name': 'g_spVideos'},
 'g_speed': {'default': '320',
             'description': 'How fast you move in Q3Test. The greater the '
                            'number, the greater the velocity.',
             'name': 'g_speed'},
 'g_syncronousClients': {'default': '0',
                         'description': 'Toggle synching of all client '
                                        'movements (1 required to record '
                                        'server demo) show "snc" on lagometer '
                                        '"John Carmack".',
                         'name': 'g_syncronousClients'},
 'g_teamAutoJoin': {'default': '0',
                    'description': 'Toggle the automatic joining of the '
                                   'smallest or loosing team.',
                    'name': 'g_teamAutoJoin'},
 'g_teamForceBalance': {'default': '0',
                        'description': 'Toggle the forcing of teams to be as '
                                       'even as possible on a server.',
                        'name': 'g_teamForceBalance'},
 'g_warmup': {'default': '',
              'description': 'The warmup time for tournament play is set with '
                             'g_warmup. A tournament game is implicitly a one '
                             'on one match, and further players are '
                             'automatically entered as spectators (note, when '
                             'the game starts, all clients, including the '
                             'spectators respawn). You can follow the players '
                             'by using Steam follow1T, Steam follow2T, and you '
                             'can be a scoreboard by using Steam scoreboardT., '
                             '"Graeme Devine".',
              'name': 'g_warmup'},
 'g_weaponrespawn': {'default': '5',
                     'description': 'Set time before a picked up weapon will '
                                    'respawn again 0 = weapons stay.',
                     'name': 'g_weaponrespawn'},
 'gamedate': {'default': '', 'description': 'Aug 20 2001.', 'name': 'gamedate'},
 'gamename': {'default': 'baseq3',
              'description': "Display the game name for TC's basedir would be "
                             'other than baseq3.',
              'name': 'gamename'},
 'gl_pixelformat': {'default': '',
                    'description': 'Color(16) depth(16) stencil(8) sets up how '
                                   'many bits for each pixel item 8, 16, or 32 '
                                   'bit?.',
                    'name': 'gl_pixelformat'},
 'gl_renderer': {'default': '',
                 'description': 'Variable holds the GL Renderer driver '
                                'information "RIVA 128/RIVA 128 ZX (PCI)".',
                 'name': 'gl_renderer'},
 'gl_vendor': {'default': '',
               'description': 'Variable holds the brand of your chipmaker '
                              '"NVIDIA Corporation".',
               'name': 'gl_vendor'},
 'gl_version': {'default': '',
                'description': 'Variable holds the driver version number '
                               '"1.1.0".',
                'name': 'gl_version'},
 'graphheight': {'default': '32',
                 'description': 'Set height, in pixels?, for graph displays.',
                 'name': 'graphheight'},
 'graphscale': {'default': '1',
                'description': 'Set scale multiplier for graph displays.',
                'name': 'graphscale'},
 'graphshift': {'default': '0',
                'description': 'Set offset for graph displays.',
                'name': 'graphshift'},
 'gun_frame': {'default': '0',
               'description': 'Turns off weapon animation and displays '
                              'specified frame in the weapons animation '
                              'sequence 0=animate 1 and up step through '
                              'frames...(c:.',
               'name': 'gun_frame'},
 'gun_x': {'default': '0',
           'description': 'Set the x location of the gun model (one is up and '
                          'down one is side to side).',
           'name': 'gun_x'},
 'gun_y': {'default': '0',
           'description': 'Set the y location of the gun model (one is up and '
                          'down one is side to side).',
           'name': 'gun_y'},
 'gun_z': {'default': '0',
           'description': 'Set the z location of the gun model (possibly '
                          'angle?).',
           'name': 'gun_z'},
 'handicap': {'default': '100',
              'description': 'Set player handicap (max health), valid values 1 '
                             '- 99.',
              'name': 'handicap'},
 'headmodel': {'default': '',
               'description': 'Changes only the head of the model to another '
                              'model Example: If you are playing as the Grunt '
                              'model, /headmodel "sarge" will stick Sarge\'s '
                              "head on Grunt's body selecting a new model will "
                              'load both the model and its matching head.',
               'name': 'headmodel'},
 'host_speeds': {'default': '0',
                 'description': 'Toggle the display of timing information '
                                'sv=server cl=client gm=gametime rf=render '
                                'time all=total time.',
                 'name': 'host_speeds'},
 'in_debugjoystick': {'default': '0',
                      'description': 'Possibly to set the debug level of '
                                     'direct input.',
                      'name': 'in_debugjoystick'},
 'in_joyBall': {'default': '0',
                'description': 'Possibly to allow support for trackball style '
                               "joy sticks and orb's.",
                'name': 'in_joyBall'},
 'in_joyBallScale': {'default': '0.02',
                     'description': 'Possibly sets the scale of a joyball '
                                    'rotation to player model rotation?.',
                     'name': 'in_joyBallScale'},
 'in_joystick': {'default': '0',
                 'description': 'Toggle the initialization of the joystick '
                                '(command line).',
                 'name': 'in_joystick'},
 'in_midi': {'default': '0',
             'description': 'Toggle the use of a midi port as an input device '
                            'r-d-x.',
             'name': 'in_midi'},
 'in_midichannel': {'default': '1',
                    'description': 'Toggle the use of a midi channel as an '
                                   'input device r-d-x.',
                    'name': 'in_midichannel'},
 'in_mididevice': {'default': '0',
                   'description': 'Toggle the use of a midi device as an input '
                                  'device r-d-x.',
                   'name': 'in_mididevice'},
 'in_midiport': {'default': '1',
                 'description': 'Toggle the use of a midi port as an input '
                                'device r-d-x.',
                 'name': 'in_midiport'},
 'in_mouse': {'default': '1',
              'description': 'Toggle initialization of the mouse as an input '
                             'device (command line).',
              'name': 'in_mouse'},
 'journal': {'default': '0',
             'description': 'Possibly logs console events but is read only and '
                            'can not be toggled.',
             'name': 'journal'},
 'joy_advanced': {'default': '0',
                  'description': 'Applies game controller axis mapping '
                                 'settings < maddog.',
                  'name': 'joy_advanced'},
 'joy_advaxisr': {'default': '0',
                  'description': 'Bind an action to the joystick r axis.',
                  'name': 'joy_advaxisr'},
 'joy_advaxisu': {'default': '0',
                  'description': 'Bind an action to the joystick u axis.',
                  'name': 'joy_advaxisu'},
 'joy_advaxisv': {'default': '0',
                  'description': 'Bind an action to the joystick v axis.',
                  'name': 'joy_advaxisv'},
 'joy_advaxisx': {'default': '0',
                  'description': 'Bind an action to the joystick x axis.',
                  'name': 'joy_advaxisx'},
 'joy_advaxisy': {'default': '0',
                  'description': 'Bind an action to the joystick y axis.',
                  'name': 'joy_advaxisy'},
 'joy_advaxisz': {'default': '0',
                  'description': 'Bind an action to the joystick z axis.',
                  'name': 'joy_advaxisz'},
 'joy_forwardsensitivity': {'default': '-1',
                            'description': 'Set forward/back sensitivity '
                                           '(negative is inverted).',
                            'name': 'joy_forwardsensitivity'},
 'joy_forwardthreshold': {'default': '0.15',
                          'description': 'Set forward/back dead zone.',
                          'name': 'joy_forwardthreshold'},
 'joy_name': {'default': 'joystick',
              'description': 'Set joystick name.',
              'name': 'joy_name'},
 'joy_pitchsensitivity': {'default': '1',
                          'description': 'Set pitch sensitivity (negative is '
                                         'inverted).',
                          'name': 'joy_pitchsensitivity'},
 'joy_pitchthreshold': {'default': '0.15',
                        'description': 'Set pitch dead zone.',
                        'name': 'joy_pitchthreshold'},
 'joy_sidesensitivity': {'default': '-1',
                         'description': 'Set side sensitivity (negative is '
                                        'inverted).',
                         'name': 'joy_sidesensitivity'},
 'joy_sidethreshold': {'default': '0.15',
                       'description': 'Set side dead zone.',
                       'name': 'joy_sidethreshold'},
 'joy_threshold': {'default': '0.15',
                   'description': 'Possibly an overall threshold setting all '
                                  'other joy variables removed in 1.08.',
                   'name': 'joy_threshold'},
 'joy_upsensitivity': {'default': '-1',
                       'description': 'Set up/down sensitivity (negative is '
                                      'inverted).',
                       'name': 'joy_upsensitivity'},
 'joy_upthreshold': {'default': '0.15',
                     'description': 'Set up/down dead zone.',
                     'name': 'joy_upthreshold'},
 'joy_yawsensitivity': {'default': '-1',
                        'description': 'Set yaw sensitivity (negative is '
                                       'inverted).',
                        'name': 'joy_yawsensitivity'},
 'joy_yawthreshold': {'default': '0.15',
                      'description': 'Set yaw dead zone.',
                      'name': 'joy_yawthreshold'},
 'logfile': {'default': '0',
             'description': 'Enable console logging 0=no log 1=buffered '
                            '2=continuous 3=append so as not to overwrite old '
                            'logs.',
             'name': 'logfile'},
 'm_filter': {'default': '1',
              'description': 'Toggle use of mouse "smoothing".',
              'name': 'm_filter'},
 'm_forward': {'default': '0.25',
               'description': 'Set the back and forth movement distance of the '
                              'player in relation to how much the mouse moves.',
               'name': 'm_forward'},
 'm_pitch': {'default': '0.022',
             'description': 'Set the up and down movement distance of the '
                            'player in relation to how much the mouse moves.',
             'name': 'm_pitch'},
 'm_side': {'default': '0.25',
            'description': 'Set the strafe movement distance of the player in '
                           'relation to how much the mouse moves.',
            'name': 'm_side'},
 'm_yaw': {'default': '0.022',
           'description': "Set the speed at which the player's screen moves "
                          'left and right while using the mouse.',
           'name': 'm_yaw'},
 'mapname': {'default': '',
             'description': 'Display the name of the current map being used.',
             'name': 'mapname'},
 'maxfps': {'default': '0',
            'description': 'Set the max frames per second the server should '
                           'send you.',
            'name': 'maxfps'},
 'memorydump': {'default': '0',
                'description': 'Possibly used for debugging memory '
                               'allocation/use?.',
                'name': 'memorydump'},
 'model': {'default': 'visor/blue',
           'description': 'Set the model used to represent your player Hey '
                          'John a 3D Keen model would be nice (c:.',
           'name': 'model'},
 'name': {'default': 'Commander Keen',
          'description': 'Pick your own be original (no Player).',
          'name': 'name'},
 'net_ip': {'default': 'localhost',
            'description': 'Variable holds the IP of the local machine (or the '
                           '"hosts" name) passed from the OS environment.',
            'name': 'net_ip'},
 'net_noipx': {'default': '0',
               'description': 'Toggle the use of IPX/SPX network protocol '
                              '(command line only).',
               'name': 'net_noipx'},
 'net_noudp': {'default': '0',
               'description': 'Toggle the use of TCP/IP network protocol '
                              '(command line only).',
               'name': 'net_noudp'},
 'net_port': {'default': '27960',
              'description': 'Set port number server will use if you want to '
                             'run more than one instance of Q3A server on the '
                             'same machine.',
              'name': 'net_port'},
 'net_qport': {'default': '16392',
               'description': 'Set internal network port. this allows more '
                              'than one person to play from behind a NAT '
                              'router by using only one IP address - Questy.',
               'name': 'net_qport'},
 'net_socksEnabled': {'default': '0',
                      'description': 'Toggle the use of network socks 5 '
                                     'protocol enabling firewall access (only '
                                     'settable at init time from the OS '
                                     'command line) - Graeme Devine.',
                      'name': 'net_socksEnabled'},
 'net_socksPassword': {'default': '',
                       'description': 'Variable holds password for socks '
                                      'firewall access supports no '
                                      'authentication and username/password '
                                      'authentication method (RFC-1929); it '
                                      'does NOT support GSS-API method '
                                      '(RFC-1961) authentication (only '
                                      'settable at init time from the OS '
                                      'command line) - Graeme Devine.',
                       'name': 'net_socksPassword'},
 'net_socksPort': {'default': '1080',
                   'description': 'Set proxy and/or firewall port default is '
                                  '1080 (only settable at init time from the '
                                  'OS command line) - Graeme Devine.',
                   'name': 'net_socksPort'},
 'net_socksServer': {'default': '',
                     'description': 'Set the address (name or IP number) of '
                                    'the SOCKS server (firewall machine), NOT '
                                    'a Q3ATEST server. (only settable at init '
                                    'time from the OS command line) - Graeme '
                                    'Devine.',
                     'name': 'net_socksServer'},
 'net_socksUsername': {'default': '',
                       'description': 'Variable holds username for socks '
                                      'firewall supports no authentication and '
                                      'username/password authentication method '
                                      '(RFC-1929); it does NOT support GSS-API '
                                      'method (RFC-1961) authentication (only '
                                      'settable at init time from the OS '
                                      'command line) - Graeme Devine.',
                       'name': 'net_socksUsername'},
 'nextmap': {'default': '',
             'description': 'Variable holds the name of the next map in the '
                            'server rotation myserver.cfg.',
             'name': 'nextmap'},
 'nohealth': {'default': '0',
              'description': 'Toggle the use of health items on next map or do '
                             'it now from the command line.',
              'name': 'nohealth'},
 'password': {'default': '',
              'description': 'Set password for entering a password protected '
                             'server.',
              'name': 'password'},
 'paused': {'default': '0',
            'description': 'Possible to allow the game to pause while in '
                           'single player mode.',
            'name': 'paused'},
 'pmove_fixed': {'default': '0',
                 'description': 'Typically the player physics advances in '
                                'small time steps. when this option is enabled '
                                'all players will use fixed frequency player '
                                'physics, the time between two advances of the '
                                'phsysics will be the same for all players. '
                                'the actual time between two advances of the '
                                'player physics can be set with the pmove_msec '
                                'variable. enabling this option will make the '
                                'player physics the same for all players '
                                'independent from their framerate. should do '
                                'what you want for prediction and should even '
                                'out the machine dependent rates. - Robert '
                                'Duffy.',
                 'name': 'pmove_fixed'},
 'pmove_msec': {'default': '8',
                'description': 'Set the time in milliseconds between two '
                               'advances of the player physics. should do what '
                               'you want for prediction and should even out '
                               'the machine dependent rates. - Robert Duffy.',
                'name': 'pmove_msec'},
 'port': {'default': '27960',
          'description': 'Set port number server will use if you want to run '
                         'more than one instance of Q3A server on the same '
                         'machine.',
          'name': 'port'},
 'protocol': {'default': '66',
              'description': 'Display network protocol version. Useful for '
                             'backward compatibility with servers with '
                             'otherwise incompatible versions < maddog read '
                             'only.',
              'name': 'protocol'},
 'qport': {'default': '59337',
           'description': 'Set internal network port. this allows more than '
                          'one person to play from behind a NAT router by '
                          'using only one IP address - Questy.',
           'name': 'qport'},
 'r_allowExtensions': {'default': '1',
                       'description': 'Use all of the OpenGL extensions your '
                                      'card is capable of.',
                       'name': 'r_allowExtensions'},
 'r_allowSoftwareGL': {'default': '0',
                       'description': 'Toggle the use of the default software '
                                      'OpenGL driver supplied by the Operating '
                                      'System < maddog.',
                       'name': 'r_allowSoftwareGL'},
 'r_ambientScale': {'default': '0.5',
                    'description': 'Set the scale or intensity of ambient '
                                   'light.',
                    'name': 'r_ambientScale'},
 'r_clear': {'default': '0',
             'description': 'Toggle the clearing of the screen between frames.',
             'name': 'r_clear'},
 'r_colorMipLevels': {'default': '0',
                      'description': '"texture visualization tool" John '
                                     'Carmack.',
                      'name': 'r_colorMipLevels'},
 'r_colorbits': {'default': '16',
                 'description': 'Set number of bits used for each color from 0 '
                                'to 32 bit.',
                 'name': 'r_colorbits'},
 'r_customaspect': {'default': '1',
                    'description': 'Toggle the use of custom screen '
                                   'resolution/sizes.',
                    'name': 'r_customaspect'},
 'r_customheight': {'default': '1024',
                    'description': 'Custom resolution (Height).',
                    'name': 'r_customheight'},
 'r_customwidth': {'default': '1600',
                   'description': 'Custom resolution (Width).',
                   'name': 'r_customwidth'},
 'r_debugSort': {'default': '0',
                 'description': 'Possibly toggle debugging of sorting of list '
                                'like scoreboard.',
                 'name': 'r_debugSort'},
 'r_debugSurface': {'default': '0',
                    'description': 'Possibly used for debugging the curve '
                                   'rendering and possibly for map debugging.',
                    'name': 'r_debugSurface'},
 'r_debugSurfaceUpdate': {'default': '1',
                          'description': 'Possibly used for debugging the '
                                         'curve rendering and possibly for map '
                                         'debugging.',
                          'name': 'r_debugSurfaceUpdate'},
 'r_debuglight': {'default': '0',
                  'description': 'Possibly toggle debugging of lighting '
                                 'effects.',
                  'name': 'r_debuglight'},
 'r_depthbits': {'default': '16',
                 'description': 'Set number of bits used for color depth from '
                                '0 to 24 bit.',
                 'name': 'r_depthbits'},
 'r_detailtextures': {'default': '1',
                      'description': 'Toggle the use of detailed textures, '
                                     'when disabled every stage of a shader is '
                                     'rendered except those with the keyword '
                                     '"detail". when enabled detail stages are '
                                     'also rendered. in proper use the detail '
                                     'stages are supposed to enhance the '
                                     "texture's visual quality when viewed "
                                     'close up. more information is available '
                                     'in the shader manual included in the GTK '
                                     'Radiant install. - Rroff.',
                      'name': 'r_detailtextures'},
 'r_directedScale': {'default': '1',
                     'description': 'Set scale/intensity of light shinning '
                                    'directly upon objects.',
                     'name': 'r_directedScale'},
 'r_displayRefresh': {'default': '0',
                      'description': 'Monitor refresh rate in game (will '
                                     'change desktop settings too in Windows '
                                     '98 anyway).',
                      'name': 'r_displayRefresh'},
 'r_dlightBacks': {'default': '1',
                   'description': '"brighter areas are changed more by dlights '
                                  "than dark areas. I don't feel TOO bad about "
                                  'that, because its not like the dlight is '
                                  'much of a proper lighting simulation even '
                                  'in the best case..."John Carmack.',
                   'name': 'r_dlightBacks'},
 'r_drawBuffer': {'default': 'GL_BACK',
                  'description': 'Set which frame buffer to draw into. '
                                 'basically you draw into a "back" buffer '
                                 'while simultaneously showing a "front" '
                                 'buffer. next frame you "swap" these. the '
                                 'benefit is that you won\'t "see" the actual '
                                 'painting of the image take place. - '
                                 'Questy/Carl.',
                  'name': 'r_drawBuffer'},
 'r_drawSun': {'default': '1',
               'description': 'Set to zero if you do not want to render '
                              'sunlight into the equation of lighting effects.',
               'name': 'r_drawSun'},
 'r_drawentities': {'default': '1',
                    'description': 'Toggle display of brush entities.',
                    'name': 'r_drawentities'},
 'r_drawstrips': {'default': '1',
                  'description': 'Toggle triangle strips rendering method.',
                  'name': 'r_drawstrips'},
 'r_drawworld': {'default': '1',
                 'description': 'Toggle rendering of map architecture.',
                 'name': 'r_drawworld'},
 'r_dynamiclight': {'default': '0',
                    'description': 'Toggle dynamic lighting (different '
                                   '"dynamic" method of rendering lights).',
                    'name': 'r_dynamiclight'},
 'r_ext_compiled_vertex_array': {'default': '',
                                 'description': 'Toggle hardware compiled '
                                                'vertex array rendering method '
                                                'default is 1.',
                                 'name': 'r_ext_compiled_vertex_array'},
 'r_ext_compress_textures': {'default': '1',
                             'description': 'Toggle compression of textures.',
                             'name': 'r_ext_compress_textures'},
 'r_ext_compressed_textures': {'default': '1',
                               'description': 'Toggle compression of textures '
                                              '(1.27g changed to past tense '
                                              'compressed).',
                               'name': 'r_ext_compressed_textures'},
 'r_ext_gamma_control': {'default': '1',
                         'description': 'Enable external gamma control '
                                        'settings.',
                         'name': 'r_ext_gamma_control'},
 'r_ext_multitexture': {'default': '1',
                        'description': 'Toggle hardware mutitexturing if set '
                                       'to zero is a direct FPS benefit.',
                        'name': 'r_ext_multitexture'},
 'r_ext_swapinterval': {'default': '1',
                        'description': 'Toggle hardware frame swapping.',
                        'name': 'r_ext_swapinterval'},
 'r_ext_texenv_add': {'default': '1',
                      'description': 'Possible duplicate cvar or an extension '
                                     'to the r_ext_texture_add variable.',
                      'name': 'r_ext_texenv_add'},
 'r_ext_texture_env_add': {'default': '1',
                           'description': 'Toggle additive blending in '
                                          'multitexturing. If not present, '
                                          'OpenGL limits you to multiplicative '
                                          'blending only, so additive will '
                                          'require an extra pass. - '
                                          'Questy/Carl.',
                           'name': 'r_ext_texture_env_add'},
 'r_facePlaneCull': {'default': '1',
                     'description': 'Toggle culling of brush faces not in view '
                                    '(0 will slow FPS).',
                     'name': 'r_facePlaneCull'},
 'r_fastsky': {'default': '1',
               'description': 'Toggle fast rendering of sky if set to 1 (0 is '
                              'default and will slow FPS when outdoors 1 will '
                              'disable your ability to see through '
                              'portals)...Thanx hacker.',
               'name': 'r_fastsky'},
 'r_finish': {'default': '1',
              'description': 'Toggle synchronization of rendered frames '
                             '(engine will wait for GL calls to finish).',
              'name': 'r_finish'},
 'r_fixtjunctions': {'default': '1',
                     'description': 'Toggle fixing of a problem with a certain '
                                    'type of vertex in models that can make '
                                    'gaps appear between polygons - Andre '
                                    'Lucas.',
                     'name': 'r_fixtjunctions'},
 'r_flareFade': {'default': '7',
                 'description': 'Set scale of fading of flares in relation to '
                                'distance.',
                 'name': 'r_flareFade'},
 'r_flares': {'default': '0',
              'description': 'Toggle projectile flare and lighting effect. the '
                             'flare effect is a translucent disk that is used '
                             'to alter the colors around lights with a corona '
                             'effect.',
              'name': 'r_flares'},
 'r_flaresSize': {'default': '40',
                  'description': 'Set the size of flares? I wish you could '
                                 'make the big balls smaller now those are '
                                 'flares.',
                  'name': 'r_flaresSize'},
 'r_fullbright': {'default': '0',
                  'description': 'Toggle textures to full brightness level (is '
                                 'set as a cheat code?) boy who turned on the '
                                 'lights (c:.',
                  'name': 'r_fullbright'},
 'r_fullscreen': {'default': '1',
                  'description': 'Toggle full screen or play in a window.',
                  'name': 'r_fullscreen'},
 'r_gamma': {'default': '1',
             'description': 'Gamma correction.',
             'name': 'r_gamma'},
 'r_glDriver': {'default': 'opengl32',
                'description': 'Used "x" OpenGL driver (Standard OpenGL32 or '
                               '3dfxvgl).',
                'name': 'r_glDriver'},
 'r_ignore': {'default': '0',
              'description': 'Possibly ignores hardware driver settings in '
                             'favor of variable settings.',
              'name': 'r_ignore'},
 'r_ignoreFastPath': {'default': '0',
                      'description': 'Possibly to disable the looking outside '
                                     'of the PAK file first feature in case of '
                                     'duplicate file names etc.',
                      'name': 'r_ignoreFastPath'},
 'r_ignoreGLErrors': {'default': '1',
                      'description': 'Ignores OpenGL errors that occur.',
                      'name': 'r_ignoreGLErrors'},
 'r_ignoreOffset': {'default': '0',
                    'description': 'See r_offsetfactor this will just turn the '
                                   'offset off completely.',
                    'name': 'r_ignoreOffset'},
 'r_ignorehwgamma': {'default': '0',
                     'description': 'Possibly to toggle the use of DirectX '
                                    'gamma correction or video driver gamma '
                                    'correction?.',
                     'name': 'r_ignorehwgamma'},
 'r_inGameVideo': {'default': '1',
                   'description': 'Toggle the display of in game animations on '
                                  'bigscreen map objects that display a camera '
                                  'view of the current game.',
                   'name': 'r_inGameVideo'},
 'r_intensity': {'default': '1',
                 'description': 'Increase brightness of texture colors (may be '
                                'like gl_modulate?).',
                 'name': 'r_intensity'},
 'r_lastValidRenderer': {'default': '',
                         'description': 'Last known video driver (RIVA '
                                        '128/RIVA 128 ZX (PCI)).',
                         'name': 'r_lastValidRenderer'},
 'r_lightmap': {'default': '0',
                'description': 'Toggle entire map to full brightness level all '
                               'textures become blurred with light (is set as '
                               'a cheat code?).',
                'name': 'r_lightmap'},
 'r_lightningSegmentLength': {'default': '32',
                              'description': 'Possibly to set the distance '
                                             'between bends in the lightning '
                                             'bolt of the lightning gun (c:.',
                              'name': 'r_lightningSegmentLength'},
 'r_lockpvs': {'default': '0',
               'description': 'Disable update to PVS table as player moves '
                              'through map (new areas not rendered) - Randy.',
               'name': 'r_lockpvs'},
 'r_lockview': {'default': '0',
                'description': 'Possibly was intended to lock a certain Field '
                               'Of View (FOV) is removed now.',
                'name': 'r_lockview'},
 'r_lodCurveError': {'default': '250',
                     'description': 'Another level of detail setting if set to '
                                    '10000 "don\'t drop curve rows for a long '
                                    'time" John Carmack (really mean 3D cards '
                                    'only??).',
                     'name': 'r_lodCurveError'},
 'r_lodbias': {'default': '0',
               'description': 'Change the geometric level of detail (0 - 2).',
               'name': 'r_lodbias'},
 'r_lodscale': {'default': '5',
                'description': 'Set scale for level of detail adjustment.',
                'name': 'r_lodscale'},
 'r_logFile': {'default': '0',
               'description': 'Possibly toggles logging of rendering errors.',
               'name': 'r_logFile'},
 'r_mapOverBrightBits': {'default': '2',
                         'description': 'Set intensity level of lights '
                                        'reflected from textures.',
                         'name': 'r_mapOverBrightBits'},
 'r_maskMinidriver': {'default': '0',
                      'description': 'Treat the current OpenGL32 driver as an '
                                     'ICD, even if it is in fact a MCD '
                                     'Questy/Zoid.',
                      'name': 'r_maskMinidriver'},
 'r_measureOverdraw': {'default': '0',
                       'description': "Overdraw' is when the same pixel is "
                                      'written to more than once when '
                                      'rendering a scene. I guess '
                                      'r_measureOverdraw is used to see how '
                                      'much is going on. used for software '
                                      'rendering.',
                       'name': 'r_measureOverdraw'},
 'r_mode': {'default': '3',
            'description': 'Set video display mode (resolution), use listmodes '
                           'for list of modes (3 is 640X480).',
            'name': 'r_mode'},
 'r_nobind': {'default': '0',
              'description': 'Toggle the binding of textures to triangles.',
              'name': 'r_nobind'},
 'r_nocull': {'default': '0',
              'description': 'Toggle rendering of hidden objects (1=slow '
                             'performance).',
              'name': 'r_nocull'},
 'r_nocurves': {'default': '0',
                'description': 'Map diagnostic command toggle the use of '
                               'curved geometry.',
                'name': 'r_nocurves'},
 'r_nolightcalc': {'default': '0',
                   'description': 'Disable lighting and shadow calculations '
                                  'hmm.',
                   'name': 'r_nolightcalc'},
 'r_noportals': {'default': '0',
                 'description': 'Toggle player view through portals.',
                 'name': 'r_noportals'},
 'r_norefresh': {'default': '0',
                 'description': 'Toggle the refreshing of the rendered '
                                'display.',
                 'name': 'r_norefresh'},
 'r_novis': {'default': '0',
             'description': 'The VIS tables hold information about which areas '
                            'should be displayed from other areas.',
             'name': 'r_novis'},
 'r_offsetfactor': {'default': '-1',
                    'description': 'Control the OpenGL Polygon Offset, If you '
                                   'see lines appearing in decals, or they '
                                   'seem to flick on and off, these variables '
                                   'may help out. - Questy/Andre.',
                    'name': 'r_offsetfactor'},
 'r_offsetunits': {'default': '-2',
                   'description': 'See r_offsetfactor.',
                   'name': 'r_offsetunits'},
 'r_overBrightBits': {'default': '1',
                      'description': 'Possibly similar to r_mapOverBrightBits '
                                     '(no visible effect on mine).',
                      'name': 'r_overBrightBits'},
 'r_picmip': {'default': '1',
              'description': 'Set maximum texture size (0 - 3, 3=fastest '
                             '0=quality).',
              'name': 'r_picmip'},
 'r_portalOnly': {'default': '0',
                  'description': 'When set to "1" turns off stencil buffering '
                                 'for portals, this allows you to see the '
                                 "entire portal before it's clipped, i.e. more "
                                 "of the room, to get a better feel for who's "
                                 'in there before you jump in.',
                  'name': 'r_portalOnly'},
 'r_preloadTextures': {'default': '0',
                       'description': 'Enable video processor to pre-cache '
                                      'textures.',
                       'name': 'r_preloadTextures'},
 'r_primitives': {'default': '0',
                  'description': 'Set the rendering method. -1 = skips drawing '
                                 '0 = uses glDrawElements if compiled vertex '
                                 'arrays are present, or strips of '
                                 'glArrayElement if not present 1 = forces '
                                 'strips 2 = forces drawElements 3 = path for '
                                 'non-vertex array testing "John Carmack".',
                  'name': 'r_primitives'},
 'r_printShaders': {'default': '0',
                    'description': 'Possibly toggle the printing on console of '
                                   'the number of shaders used?.',
                    'name': 'r_printShaders'},
 'r_railCoreWidth': {'default': '16',
                     'description': "Set size of the rail trail's core.",
                     'name': 'r_railCoreWidth'},
 'r_railSegmentLength': {'default': '64',
                         'description': 'Set distance between rail "sun '
                                        'bursts".',
                         'name': 'r_railSegmentLength'},
 'r_railWidth': {'default': '128',
                 'description': 'Set width of the rail trail.',
                 'name': 'r_railWidth'},
 'r_roundImagesDown': {'default': '1',
                       'description': 'Set rounding down amount (larger = '
                                      'faster, lower quality) - Randy.',
                       'name': 'r_roundImagesDown'},
 'r_showImages': {'default': '0',
                  'description': 'Toggle displaying a collage of all image '
                                 'files when set to a one...texture use '
                                 'debugging tool.',
                  'name': 'r_showImages'},
 'r_showSmp': {'default': '0',
               'description': 'Toggle display of multi processor (SMP) info on '
                              'the HUD.',
               'name': 'r_showSmp'},
 'r_showcluster': {'default': '0',
                   'description': 'Toggle the display of clusters by number as '
                                  'the player enters them on the currently '
                                  'loaded map<maddog.',
                   'name': 'r_showcluster'},
 'r_shownormals': {'default': '0',
                   'description': 'Toggle the drawing of short lines '
                                  'indicating brush and entity polygon '
                                  'vertices, useful when debugging model '
                                  'lighting - Andre Lucas < maddog.',
                   'name': 'r_shownormals'},
 'r_showsky': {'default': '0',
               'description': 'Enable rendering sky in front of other objects.',
               'name': 'r_showsky'},
 'r_showtris': {'default': '0',
                'description': 'Map diagnostic command show triangles, pretty '
                               'cool looking.',
                'name': 'r_showtris'},
 'r_simpleMipMaps': {'default': '1',
                     'description': 'Toggle the use of "simple" mip mapping. '
                                    'used to "dumb-down" resoluiton displays '
                                    'for slower machines - Questy.',
                     'name': 'r_simpleMipMaps'},
 'r_singleShader': {'default': '0',
                    'description': 'Possibly toggles use of 1 shader for '
                                   'objects that have multiple shaders.',
                    'name': 'r_singleShader'},
 'r_skipBackEnd': {'default': '0',
                   'description': 'Possibly to toggle the skipping of the '
                                  'backend video buffer.',
                   'name': 'r_skipBackEnd'},
 'r_smp': {'default': '0',
           'description': 'Toggle the use of multi processor acceleration '
                          'code.',
           'name': 'r_smp'},
 'r_speeds': {'default': '0',
              'description': 'Show the rendering info e.g. how many triangles '
                             'are drawn added r_speeds timing info to '
                             'cinematic texture uploads "John Carmack".',
              'name': 'r_speeds'},
 'r_stencilbits': {'default': '8',
                   'description': 'Stencil buffer size (0, 8bit, and 16bit).',
                   'name': 'r_stencilbits'},
 'r_stereo': {'default': '0',
              'description': 'Toggle the use of stereo separation for 3D '
                             'glasses.',
              'name': 'r_stereo'},
 'r_subdivisions': {'default': '4',
                    'description': 'Set maximum level of detail. (an example '
                                   'would be the complexity of curves. '
                                   '1=highest detail).',
                    'name': 'r_subdivisions'},
 'r_swapInterval': {'default': '0',
                    'description': 'Toggle frame swapping.',
                    'name': 'r_swapInterval'},
 'r_textureMode': {'default': '',
                   'description': 'Select texture mode. '
                                  '"GL_LINEAR_MIPMAP_NEAREST" (nearest or '
                                  'linear).',
                   'name': 'r_textureMode'},
 'r_texturebits': {'default': '0',
                   'description': 'Set number of bits used for each texture '
                                  'from 0 to 32 bit.',
                   'name': 'r_texturebits'},
 'r_verbose': {'default': '0',
               'description': 'Toggle display of rendering commands as they '
                              'happen on the console.',
               'name': 'r_verbose'},
 'r_vertexLight': {'default': '1',
                   'description': 'Enable vertex lighting (faster, lower '
                                  'quality than lightmap) removes lightmaps, '
                                  'forces every shader to only use a single '
                                  'rendering pass, no layered transparancy, '
                                  'environment mapping, world lighting is '
                                  'completely static, and there is no dynamic '
                                  'lighting when in vertex lighting mode. '
                                  '(recommend dynamiclight 0 and this 1) '
                                  'direct FPS benefit "John Carmack".',
                   'name': 'r_vertexLight'},
 'r_znear': {'default': '4',
             'description': 'Set how close objects can be to the player before '
                            "they're clipped out of the scene - Questy/Andre.",
             'name': 'r_znear'},
 'rate': {'default': '',
          'description': 'Modem speed/rate of data transfer "4500" (take a '
                         'zero off the end of your connection speed?).',
          'name': 'rate'},
 'rconAddress': {'default': '',
                 'description': 'Variable holds IP address of the server for '
                                'rcon.',
                 'name': 'rconAddress'},
 'rconPassword': {'default': '',
                  'description': 'Set password for remote console control of '
                                 'the server.',
                  'name': 'rconPassword'},
 'rcon_password': {'default': '',
                   'description': 'Set password for remote console control of '
                                  'the server removed cause dupe.',
                   'name': 'rcon_password'},
 's_2dvolume': {'default': '0.7',
                'description': 'Vortex of sound - has a good description of '
                               'this A3D variable.',
                'name': 's_2dvolume'},
 's_bloat': {'default': '2.0',
             'description': 'Vortex of sound - has a good description of this '
                            'A3D variable.',
             'name': 's_bloat'},
 's_compression': {'default': '1',
                   'description': 'Toggle the use of sound compression.',
                   'name': 's_compression'},
 's_distance': {'default': '100.0',
                'description': 'Vortex of sound - has a good description of '
                               'this A3D variable.',
                'name': 's_distance'},
 's_doppler': {'default': '1.0',
               'description': 'Vortex of sound - has a good description of '
                              'this A3D variable.',
               'name': 's_doppler'},
 's_fogeq': {'default': '0.8',
             'description': 'Vortex of sound - has a good description of this '
                            'A3D variable.',
             'name': 's_fogeq'},
 's_geometry': {'default': '1',
                'description': 'Vortex of sound - has a good description of '
                               'this A3D variable.',
                'name': 's_geometry'},
 's_initsound': {'default': '1',
                 'description': 'Toggle weather sound is initialized or not '
                                '(on next game).',
                 'name': 's_initsound'},
 's_khz': {'default': '11',
           'description': 'Set the sampling frequency of sounds '
                          'lower=performance higher=quality.',
           'name': 's_khz'},
 's_loadas8bit': {'default': '1',
                  'description': 'Load sounds in 8bit mode.',
                  'name': 's_loadas8bit'},
 's_max_distance': {'default': '1000.0',
                    'description': 'Vortex of sound - has a good description '
                                   'of this A3D variable.',
                    'name': 's_max_distance'},
 's_min_distance': {'default': '3.0',
                    'description': 'Vortex of sound - has a good description '
                                   'of this A3D variable.',
                    'name': 's_min_distance'},
 's_mixPreStep': {'default': '0.05',
                  'description': 'Possibly to set the prefetching of sound on '
                                 'sound cards that have that power.',
                  'name': 's_mixPreStep'},
 's_mixahead': {'default': '0.2',
                'description': 'Set delay before mixing sound samples.',
                'name': 's_mixahead'},
 's_musicvolume': {'default': '1',
                   'description': 'Music volume level 0=off.',
                   'name': 's_musicvolume'},
 's_numpolys': {'default': '400',
                'description': 'Vortex of sound - has a good description of '
                               'this A3D variable.',
                'name': 's_numpolys'},
 's_occ_eq': {'default': '0.75',
              'description': 'Vortex of sound - has a good description of this '
                             'A3D variable.',
              'name': 's_occ_eq'},
 's_occfactor': {'default': '0.5',
                 'description': 'Vortex of sound - has a good description of '
                                'this A3D variable.',
                 'name': 's_occfactor'},
 's_occlude': {'default': '0',
               'description': 'Vortex of sound - has a good description of '
                              'this A3D variable.',
               'name': 's_occlude'},
 's_refdelay': {'default': '2.0',
                'description': 'Vortex of sound - has a good description of '
                               'this A3D variable.',
                'name': 's_refdelay'},
 's_refgain': {'default': '0.45',
               'description': 'Vortex of sound - has a good description of '
                              'this A3D variable.',
               'name': 's_refgain'},
 's_reflect': {'default': '1',
               'description': 'Vortex of sound - has a good description of '
                              'this A3D variable.',
               'name': 's_reflect'},
 's_rolloff': {'default': '1.0',
               'description': 'Vortex of sound - has a good description of '
                              'this A3D variable.',
               'name': 's_rolloff'},
 's_separation': {'default': '0.5',
                  'description': 'Set separation between left and right sound '
                                 'channels (this one is it).',
                  'name': 's_separation'},
 's_show': {'default': '0',
            'description': 'Toggle display of paths and filenames of all sound '
                           'files as they are played.',
            'name': 's_show'},
 's_testsound': {'default': '0',
                 'description': 'Toggle a test tone to test sound system. '
                                '0=disables,1=toggles.',
                 'name': 's_testsound'},
 's_usingA3D': {'default': '0',
                'description': 'Vortex of sound - has a good description of '
                               'this A3D variable.',
                'name': 's_usingA3D'},
 's_volume': {'default': '0.7',
              'description': 'Sound FX Volume.',
              'name': 's_volume'},
 's_watereq': {'default': '0.2',
               'description': 'Vortex of sound - has a good description of '
                              'this A3D variable.',
               'name': 's_watereq'},
 'scr_conspeed': {'default': '3',
                  'description': 'Set how fast the console goes up and down.',
                  'name': 'scr_conspeed'},
 'sensitivity': {'default': '9',
                 'description': 'Set how far your mouse moves in relation to '
                                'travel on the mouse pad.',
                 'name': 'sensitivity'},
 'server1': {'default': '',
             'description': 'Holds IP/URL of a servers from the favorite '
                            'servers list - Dr Qube.',
             'name': 'server1'},
 'server10': {'default': '',
              'description': 'Holds IP/URL of a servers from the favorite '
                             'servers list - Dr Qube.',
              'name': 'server10'},
 'server11': {'default': '',
              'description': 'Holds IP/URL of a servers from the favorite '
                             'servers list - Dr Qube.',
              'name': 'server11'},
 'server12': {'default': '',
              'description': 'Holds IP/URL of a servers from the favorite '
                             'servers list - Dr Qube.',
              'name': 'server12'},
 'server13': {'default': '',
              'description': 'Holds IP/URL of a servers from the favorite '
                             'servers list - Dr Qube.',
              'name': 'server13'},
 'server14': {'default': '',
              'description': 'Holds IP/URL of a servers from the favorite '
                             'servers list - Dr Qube.',
              'name': 'server14'},
 'server15': {'default': '',
              'description': 'Holds IP/URL of a servers from the favorite '
                             'servers list - Dr Qube.',
              'name': 'server15'},
 'server16': {'default': '',
              'description': 'Holds IP/URL of a servers from the favorite '
                             'servers list - Dr Qube.',
              'name': 'server16'},
 'server2': {'default': '',
             'description': 'Holds IP/URL of a servers from the favorite '
                            'servers list - Dr Qube.',
             'name': 'server2'},
 'server3': {'default': '',
             'description': 'Holds IP/URL of a servers from the favorite '
                            'servers list - Dr Qube.',
             'name': 'server3'},
 'server4': {'default': '',
             'description': 'Holds IP/URL of a servers from the favorite '
                            'servers list - Dr Qube.',
             'name': 'server4'},
 'server5': {'default': '',
             'description': 'Holds IP/URL of a servers from the favorite '
                            'servers list - Dr Qube.',
             'name': 'server5'},
 'server6': {'default': '',
             'description': 'Holds IP/URL of a servers from the favorite '
                            'servers list - Dr Qube.',
             'name': 'server6'},
 'server7': {'default': '',
             'description': 'Holds IP/URL of a servers from the favorite '
                            'servers list - Dr Qube.',
             'name': 'server7'},
 'server8': {'default': '',
             'description': 'Holds IP/URL of a servers from the favorite '
                            'servers list - Dr Qube.',
             'name': 'server8'},
 'server9': {'default': '',
             'description': 'Holds IP/URL of a servers from the favorite '
                            'servers list - Dr Qube.',
             'name': 'server9'},
 'session': {'default': '2',
             'description': 'Possibly holds the value for the active session '
                            'number when running multiple addresses and '
                            'sockets for multiple servers on one machine?.',
             'name': 'session'},
 'session0': {'default': '0 300 1 0 0 0',
              'description': 'Possibly to set up multiple addresses and '
                             'sockets for multiple servers on one machine (can '
                             'you say BFServer with multiple processors?).',
              'name': 'session0'},
 'session1': {'default': '0 300 1 0 0 0',
              'description': 'Possibly to set up multiple addresses and '
                             'sockets for multiple servers on one machine (can '
                             'you say BFServer with multiple processors?).',
              'name': 'session1'},
 'session2': {'default': '0 300 1 0 0 0',
              'description': 'Possibly to set up multiple addresses and '
                             'sockets for multiple servers on one machine (can '
                             'you say BFServer with multiple processors?).',
              'name': 'session2'},
 'session3': {'default': '0 300 1 0 0 0',
              'description': 'Possibly to set up multiple addresses and '
                             'sockets for multiple servers on one machine (can '
                             'you say BFServer with multiple processors?).',
              'name': 'session3'},
 'session4': {'default': '0 300 1 0 0 0',
              'description': 'Possibly to set up multiple addresses and '
                             'sockets for multiple servers on one machine (can '
                             'you say BFServer with multiple processors?).',
              'name': 'session4'},
 'sex': {'default': 'male',
         'description': 'Set gender for model characteristics (sounds, '
                        "obituary's etc.).",
         'name': 'sex'},
 'showdrop': {'default': '0',
              'description': 'Toggle display of dropped packets. '
                             '0=disables,1=toggles.',
              'name': 'showdrop'},
 'showpackets': {'default': '0',
                 'description': 'Toggle display of all packets sent and '
                                'received. 0=disables,1=toggles.',
                 'name': 'showpackets'},
 'showtrace': {'default': '0',
               'description': 'Toggle display of packet traces. '
                              '0=disables,1=toggles.',
               'name': 'showtrace'},
 'snaps': {'default': '20',
           'description': 'Set the number of snapshots sever will send to a '
                          'client (server run at 40Hz, so use 40, 20, or 10) '
                          '-Randy.',
           'name': 'snaps'},
 'snd': {'default': 'visor',
         'description': 'Select which model sounds your player uses (mix it '
                        'up).',
         'name': 'snd'},
 'sv_allowAnonymous': {'default': '0',
                       'description': 'Possibly to toggle the allowing of '
                                      'anonymous clients to connect to your '
                                      'server.',
                       'name': 'sv_allowAnonymous'},
 'sv_allowdownload': {'default': '1',
                      'description': 'Toggle the ability for clients to '
                                     'download files maps etc. from server..',
                      'name': 'sv_allowdownload'},
 'sv_cheats': {'default': '1',
               'description': 'Enable cheating commands (give all) (serverside '
                              'only).',
               'name': 'sv_cheats'},
 'sv_floodProtect': {'default': '1',
                     'description': 'Toggle server flood protection to keep '
                                    'players from bringing the server down.',
                     'name': 'sv_floodProtect'},
 'sv_fps': {'default': '20',
            'description': 'Set the max frames per second the server sends the '
                           'client.',
            'name': 'sv_fps'},
 'sv_hostname': {'default': '',
                 'description': 'Set the name of the server "Shadowlands".',
                 'name': 'sv_hostname'},
 'sv_keywords': {'default': '',
                 'description': 'Variable holds the search string entered in '
                                'the internet connection menu.',
                 'name': 'sv_keywords'},
 'sv_killserver': {'default': '0',
                   'description': 'If set to a one the server goes down '
                                  '(server console only I hope).',
                   'name': 'sv_killserver'},
 'sv_mapChecksum': {'default': '',
                    'description': 'Allows check for client server map to '
                                   'match.',
                    'name': 'sv_mapChecksum'},
 'sv_mapname': {'default': '',
                'description': 'Display the name of the current map being used '
                               'on a server.',
                'name': 'sv_mapname'},
 'sv_master1': {'default': '',
                'description': 'Set URL or address to master server '
                               '"master3.idsoftware.com".',
                'name': 'sv_master1'},
 'sv_master2': {'default': '',
                'description': 'Optional master 2.',
                'name': 'sv_master2'},
 'sv_master3': {'default': '',
                'description': 'Optional master 3.',
                'name': 'sv_master3'},
 'sv_master4': {'default': '',
                'description': 'Optional master 4.',
                'name': 'sv_master4'},
 'sv_master5': {'default': '',
                'description': 'Optional master 5.',
                'name': 'sv_master5'},
 'sv_maxPing': {'default': '0',
                'description': 'Set the maximum ping aloud on the server to '
                               'keep HPB out.',
                'name': 'sv_maxPing'},
 'sv_maxRate': {'default': '',
                'description': 'Option to force all clients to play with a max '
                               'rate. This can be used to limit the advantage '
                               'of LPB, or to cap bandwidth utilization for a '
                               'server. Note that rate is ignored for clients '
                               'that are on the same LAN. Father John stepping '
                               'in, in the name of fairness (c: (ever notice '
                               "when 3 or so LPB's join a server your PING "
                               "takes a dump? It's because your slice of the "
                               'pie got smaller because theirs is so big die '
                               'bandwidth suckers).',
                'name': 'sv_maxRate'},
 'sv_maxclients': {'default': '8',
                   'description': 'Maximum number of people allowed to join '
                                  'the server dedicated server memory '
                                  'optimizations. Tips: com_hunkMegs 4 '
                                  'sv_maxclients 3 bot_enable 0 "John '
                                  'Carmack".',
                   'name': 'sv_maxclients'},
 'sv_minPing': {'default': '0',
                'description': 'Set the minimum ping aloud on the server to '
                               'keep LPB out.',
                'name': 'sv_minPing'},
 'sv_nopredict': {'default': '0',
                  'description': 'Is it possible that the server is handling '
                                 'some prediction of player location?.',
                  'name': 'sv_nopredict'},
 'sv_padPackets': {'default': '0',
                   'description': 'Possibly toggles the padding of network '
                                  'packets on the server PAD - Packet '
                                  'Assembler/Disassembler.',
                   'name': 'sv_padPackets'},
 'sv_pakNames': {'default': 'antilogic',
                 'description': 'Variable holds a list of all the pk3 files '
                                'the server found "antilogic".',
                 'name': 'sv_pakNames'},
 'sv_paks': {'default': '182784856',
             'description': 'Variable holds the checksum of all pk3 files.',
             'name': 'sv_paks'},
 'sv_paused': {'default': '0',
               'description': 'Allow the game to be paused from the server '
                              'console?.',
               'name': 'sv_paused'},
 'sv_privateClients': {'default': '0',
                       'description': 'The number of spots, out of '
                                      'sv_maxclients, reserved for players '
                                      'with the server password '
                                      '(sv_privatePassword) - Holesinswiss.',
                       'name': 'sv_privateClients'},
 'sv_privatePassword': {'default': '',
                        'description': 'Set password for private clients to '
                                       'login with.',
                        'name': 'sv_privatePassword'},
 'sv_pure': {'default': '1',
             'description': 'Disallow native DLL loading if sv_pure, requires '
                            'clients to only get data from pk3 files the '
                            'server is using "John Carmack".',
             'name': 'sv_pure'},
 'sv_reconnectlimit': {'default': '3',
                       'description': 'Number of times a disconnected client '
                                      'can come back and reconnect.',
                       'name': 'sv_reconnectlimit'},
 'sv_referencedPakNames': {'default': '',
                           'description': 'Variable holds a list of all the '
                                          'pk3 files the server loaded data '
                                          'from. these pk3 files will be '
                                          'autodownloaded by a client if the '
                                          'client does not have them. '
                                          '"baseq3/pak2 baseq3/pak0".',
                           'name': 'sv_referencedPakNames'},
 'sv_referencedPaks': {'default': '',
                       'description': 'Variable holds the checksum of the '
                                      'referenced pk3 files.',
                       'name': 'sv_referencedPaks'},
 'sv_running': {'default': '1',
                'description': 'Variable flag tells the console weather or not '
                               'a local server is running.',
                'name': 'sv_running'},
 'sv_serverid': {'default': '',
                 'description': 'Hmm "8021204".',
                 'name': 'sv_serverid'},
 'sv_showloss': {'default': '0',
                 'description': 'Toggle sever packet loss display.',
                 'name': 'sv_showloss'},
 'sv_timeout': {'default': '120',
                'description': 'Sets the amount of time for the server to wait '
                               'for a client packet before assuming a '
                               'disconnected state.',
                'name': 'sv_timeout'},
 'sv_zombietime': {'default': '2',
                   'description': 'The amount of time in minutes before a '
                                  'frozen character is removed from the map.',
                   'name': 'sv_zombietime'},
 'sv_zone': {'default': 'default',
             'description': 'This is the keyword that clients will search for, '
                            "server admin's should set this variable to the "
                            'gametype they have running. free for all, '
                            'tournament, team deathmatch, and CTF I do not '
                            'know if you can deviate from the keywords the way '
                            'Zaphod laid them down in the whatsnew.txt.',
             'name': 'sv_zone'},
 'sys_cpuid': {'default': '33',
               'description': 'More snooping into your CPU.',
               'name': 'sys_cpuid'},
 'sys_cpustring': {'default': '',
                   'description': 'Variable holds a string that identifies '
                                  'your processor.',
                   'name': 'sys_cpustring'},
 'team_headmodel': {'default': '',
                    'description': 'Set head of team_model to a head that will '
                                   'only be used during team game play.',
                    'name': 'team_headmodel'},
 'team_model': {'default': '',
                'description': 'Set player model that will only be used during '
                               'team game play.',
                'name': 'team_model'},
 'teamflags': {'default': '0',
               'description': 'Set flags for team play (probably will be a hex '
                              'value like deathmatch flags).',
               'name': 'teamflags'},
 'teamoverlay': {'default': '0',
                 'description': 'Toggle the drawing of the colored team '
                                'overlay on the HUD.',
                 'name': 'teamoverlay'},
 'teamtask': {'default': '0',
              'description': 'Variable holds the number of the team task you '
                             'are currently asigned 1 - offense 2 - defense 3 '
                             '- point/patroll 4 - following 5 - retrieving 6 - '
                             'escort(gaurding flag carrier) 7 - camping.',
              'name': 'teamtask'},
 'timedemo': {'default': '0',
              'description': 'When set to "1" times a demo and returns frames '
                             'per second like a benchmark.',
              'name': 'timedemo'},
 'timegraph': {'default': '0',
               'description': 'Toggle the display of the timegraph..',
               'name': 'timegraph'},
 'timelimit': {'default': '0',
               'description': 'Amount of time before new map loads or next '
                              'match begins.',
               'name': 'timelimit'},
 'timescale': {'default': '1',
               'description': 'Set the ratio between game time and real time.',
               'name': 'timescale'},
 'to': {'default': 'start a dedicated server in tournament mode, you would '
                   'use: quake3.exe +set dedicated 2 +set sv_zone tournaments '
                   '+set g_gametype 1 +map q3tourney2, "Graeme Devine" thanks '
                   'also to TheKiller 5 - One Flag CTF 6 - Overload 7 - '
                   'Harvester (Team Arena only)',
        'description': '5- One Flag CTF.',
        'name': 'to'},
 'ui_browserGameType': {'default': '0',
                        'description': 'Set server search game type in the '
                                       'browser list (see g_gametype).',
                        'name': 'ui_browserGameType'},
 'ui_browserMaster': {'default': '0',
                      'description': 'Set server search 0=LAN 1=Mplayer '
                                     '2=Internet 3=Favorites - WeeJoker.',
                      'name': 'ui_browserMaster'},
 'ui_browserShowEmpty': {'default': '1',
                         'description': 'Toggle the displaying of empty '
                                        'servers in the browser list.',
                         'name': 'ui_browserShowEmpty'},
 'ui_browserShowFull': {'default': '1',
                        'description': 'Toggle the displaying of full servers '
                                       'in the browser list.',
                        'name': 'ui_browserShowFull'},
 'ui_browserSortKey': {'default': '4',
                       'description': 'Set the field number to sort by in the '
                                      'browser list 0=Server Name 1=Map Name '
                                      '2=Open Player Spots 3=Game Type '
                                      '4=PingTime.',
                       'name': 'ui_browserSortKey'},
 'ui_cdkeychecked': {'default': '1',
                     'description': 'Set to a 1 after the cdkey has been '
                                    "checked so won't ask again.",
                     'name': 'ui_cdkeychecked'},
 'ui_ctf_capturelimit': {'default': '8',
                         'description': 'Set the menu default capture limit '
                                        'for single player bot matches.',
                         'name': 'ui_ctf_capturelimit'},
 'ui_ctf_friendly': {'default': '0',
                     'description': 'Toggle team mate damage in single player '
                                    'CTF bot matches.',
                     'name': 'ui_ctf_friendly'},
 'ui_ctf_timelimit': {'default': '30',
                      'description': 'Set the menu default CTF time limit for '
                                     'single player bot matches.',
                      'name': 'ui_ctf_timelimit'},
 'ui_ffa_fraglimit': {'default': '20',
                      'description': 'Set the menu default frag limit for '
                                     'single player FFA bot matches.',
                      'name': 'ui_ffa_fraglimit'},
 'ui_ffa_timelimit': {'default': '0',
                      'description': 'Set the menu default time limit for '
                                     'single player FFA bot matches.',
                      'name': 'ui_ffa_timelimit'},
 'ui_master': {'default': '0',
               'description': 'Set server search 0=LAN 1=Mplayer 2=Internet '
                              '3=Favorites - WeeJoker.',
               'name': 'ui_master'},
 'ui_spSelection': {'default': '2',
                    'description': 'Set the menu default gametype of single '
                                   'player? 16 = CTF 2 = FFA DM.',
                    'name': 'ui_spSelection'},
 'ui_team_fraglimit': {'default': '0',
                       'description': 'Set the menu default frag limit for '
                                      'single player team bot matches.',
                       'name': 'ui_team_fraglimit'},
 'ui_team_friendly': {'default': '1',
                      'description': 'Toggle default team mate damage in '
                                     'single player team bot matches.',
                      'name': 'ui_team_friendly'},
 'ui_team_timelimit': {'default': '20',
                       'description': 'Set the menu default time limit for '
                                      'single player team bot matches.',
                       'name': 'ui_team_timelimit'},
 'ui_tourney_fraglimit': {'default': '0',
                          'description': 'Set the menu default frag limit for '
                                         'single player tourney bot matches.',
                          'name': 'ui_tourney_fraglimit'},
 'ui_tourney_timelimit': {'default': '15',
                          'description': 'Sets the menu default time limit for '
                                         'single player tourney bot matches.',
                          'name': 'ui_tourney_timelimit'},
 'username': {'default': 'vern',
              'description': 'Variable holds your network login id from '
                             '%username% env variable hmmm? id hackers!.',
              'name': 'username'},
 'version': {'default': '',
             'description': 'Q3 1.30 win-x86 Aug 20 2001.',
             'name': 'version'},
 'versionNumber': {'default': '',
                   'description': '"Q3T 1.08".',
                   'name': 'versionNumber'},
 'vid_xpos': {'default': '30',
              'description': 'Xposition when windowed.',
              'name': 'vid_xpos'},
 'vid_ypos': {'default': '30',
              'description': 'Yposition when windowed.',
              'name': 'vid_ypos'},
 'viewlog': {'default': '0',
             'description': 'Toggle the display of the startup console window '
                            'over the game screen.',
             'name': 'viewlog'},
 'viewsize': {'default': '100',
              'description': 'Changes view port size 0 - 100 (you probably '
                             "wouldn't want less than 100).",
              'name': 'viewsize'},
 'vm_cgame': {'default': '0',
              'description': 'Part of the virtual machine interpreter which '
                             'allows PC MOD makers to not have to know MAC '
                             'code and MAC MOD makers to not have to know PC.',
              'name': 'vm_cgame'},
 'vm_game': {'default': '0',
             'description': 'Toggle the virtual machine interpreter, cgame can '
                            'switch between being loaded as a binary .dll or '
                            'an interpreted .qvm at the change of this cvar.',
             'name': 'vm_game'},
 'vm_ui': {'default': '0',
           'description': 'Part of the virtual machine interpreter which '
                          'allows PC MOD makers to not have to know MAC code '
                          'and MAC MOD makers to not have to know PC.',
           'name': 'vm_ui'},
 'win_hinstance': {'default': '',
                   'description': 'Address of the handle instance of quake3 '
                                  'under windows - LOKi.',
                   'name': 'win_hinstance'},
 'win_wndproc': {'default': '',
                 'description': 'Hmm..."4368704".',
                 'name': 'win_wndproc'},
 'zoomfov': {'default': '22.5',
             'description': 'What the zoomed in field of view will be any '
                            'thing more than 30 would not be sniper friendly.',
             'name': 'zoomfov'}}
COMMANDS = {'+attack': {'description': 'Start attacking (shooting, punching).',
             'name': '+attack'},
 '+back': {'description': 'Start moving backwards.', 'name': '+back'},
 '+button0': {'description': 'Start firing same as mouse button 1 (fires '
                             'weapon).',
              'name': '+button0'},
 '+button1': {'description': 'Start displaying chat bubble.',
              'name': '+button1'},
 '+button10': {'description': "Start hand signal, player model looks like it's "
                              'motioning to team "come to my right side" (Team '
                              'Arena Models Only).',
               'name': '+button10'},
 '+button2': {'description': 'Start using items (same as enter).',
              'name': '+button2'},
 '+button3': {'description': 'Start player taunt animation.',
              'name': '+button3'},
 '+button4': {'description': 'Fixed +button4 not causing footsteps "John '
                             'Carmack".',
              'name': '+button4'},
 '+button5': {'description': 'Used for MODS also used by Team Arena Mission '
                             'Pack.',
              'name': '+button5'},
 '+button6': {'description': 'Used for MODS also used by Team Arena Mission '
                             'Pack.',
              'name': '+button6'},
 '+button7': {'description': "Start hand signal, player model looks like it's "
                             'motioning to team "move forward" (Team Arena '
                             'Models Only).',
              'name': '+button7'},
 '+button8': {'description': "Start hand signal, player model looks like it's "
                             'motioning to team "come here" (Team Arena Models '
                             'Only).',
              'name': '+button8'},
 '+button9': {'description': "Stop hand signal, player model looks like it's "
                             'motioning to team "come to my left side" (Team '
                             'Arena Models Only).',
              'name': '+button9'},
 '+forward': {'description': 'Start moving forward.', 'name': '+forward'},
 '+info': {'description': 'Start displaying server information (sv_hostname, '
                          'map, rules, g_gametype, fraglimit).',
           'name': '+info'},
 '+left': {'description': 'Start turning left.', 'name': '+left'},
 '+lookdown': {'description': 'Start looking down.', 'name': '+lookdown'},
 '+lookup': {'description': 'Start looking up.', 'name': '+lookup'},
 '+mlook': {'description': 'Start using mouse movements to control head '
                           'movement.',
            'name': '+mlook'},
 '+movedown': {'description': 'Start moving down (crouch, climb down, swim '
                              'down).',
               'name': '+movedown'},
 '+moveleft': {'description': 'Start strafing to the left.',
               'name': '+moveleft'},
 '+moveright': {'description': 'Start strafing to the right.',
                'name': '+moveright'},
 '+moveup': {'description': 'Start moving up (jump, climb up, swim up).',
             'name': '+moveup'},
 '+right': {'description': 'Start turning right.', 'name': '+right'},
 '+scores': {'description': 'Start displaying current scores.',
             'name': '+scores'},
 '+speed': {'description': 'Speed toggle bound to shift key by default toggles '
                           'run/walk.',
            'name': '+speed'},
 '+strafe': {'description': 'Start changing directional movement into strafing '
                            'movement.',
             'name': '+strafe'},
 '+zoom': {'description': 'Zoom in to fov specified by the zoomfov variable.',
           'name': '+zoom'},
 '-attack': {'description': 'Stop attacking (shooting, punching).',
             'name': '-attack'},
 '-back': {'description': 'Stop moving backwards.', 'name': '-back'},
 '-button0': {'description': 'Stop firing same as mouse button 1 (fires '
                             'weapon).',
              'name': '-button0'},
 '-button1': {'description': 'Stop displaying chat bubble.',
              'name': '-button1'},
 '-button10': {'description': "Stop hand signal, player model looks like it's "
                              'motioning to team "come to my right side" (Team '
                              'Arena Models Only).',
               'name': '-button10'},
 '-button2': {'description': 'Stop using items (same as releasing enter).',
              'name': '-button2'},
 '-button3': {'description': 'Stop player taunt animation.',
              'name': '-button3'},
 '-button4': {'description': 'Fixed +button4 not causing footsteps "John '
                             'Carmack".',
              'name': '-button4'},
 '-button5': {'description': 'Used for MODS also used by Team Arena Mission '
                             'Pack.',
              'name': '-button5'},
 '-button6': {'description': 'Used for MODS also used by Team Arena Mission '
                             'Pack.',
              'name': '-button6'},
 '-button7': {'description': "Stop hand signal, player model looks like it's "
                             'motioning to team "move forward" (Team Arena '
                             'Models Only).',
              'name': '-button7'},
 '-button8': {'description': "Stop hand signal, player model looks like it's "
                             'motioning to team "come here" (Team Arena Models '
                             'Only).',
              'name': '-button8'},
 '-button9': {'description': "Start hand signal, player model looks like it's "
                             'motioning to team "come to my left side" (Team '
                             'Arena Models Only).',
              'name': '-button9'},
 '-forward': {'description': 'Stop moving forward.', 'name': '-forward'},
 '-info': {'description': 'Stop displaying server information (sv_hostname, '
                          'map, rules, g_gametype, fraglimit).',
           'name': '-info'},
 '-left': {'description': 'Stop turning left.', 'name': '-left'},
 '-lookdown': {'description': 'Stop looking down.', 'name': '-lookdown'},
 '-lookup': {'description': 'Stop looking up.', 'name': '-lookup'},
 '-mlook': {'description': 'Stop using mouse look.', 'name': '-mlook'},
 '-movedown': {'description': 'Stop moving down (crouch, climb down, swim '
                              'down).',
               'name': '-movedown'},
 '-moveleft': {'description': 'Stop strafing to the left.',
               'name': '-moveleft'},
 '-moveright': {'description': 'Stop strafing to the right.',
                'name': '-moveright'},
 '-moveup': {'description': 'Stop moving up (jump, climb up, swim up).',
             'name': '-moveup'},
 '-right': {'description': 'Stop turning right.', 'name': '-right'},
 '-scores': {'description': 'Stop displaying current scores.',
             'name': '-scores'},
 '-speed': {'description': 'Speed toggle bound to shift key by default toggles '
                           'run/walk.',
            'name': '-speed'},
 '-strafe': {'description': 'Stop changing directional movement into strafing '
                            'movement.',
             'name': '-strafe'},
 '-zoom': {'description': 'Zoom out to fov specified by the fov variable.',
           'name': '-zoom'},
 'Fs_pureList': {'description': 'This command basically displays the contents '
                                'of the sv_referencedPaks variable.',
                 'name': 'Fs_pureList'},
 'Fs_referencedList': {'description': 'This variable basically displays the '
                                      'contents of the sv_referencedPakNames '
                                      'variable.',
                       'name': 'Fs_referencedList'},
 'addbot': {'description': 'Add one bot <botlib> name of the bot library '
                           '<name> name of the bot <skin> skin of the bot '
                           '<charfile> file with the bot character <charname> '
                           'name of the character - "Mr. Elusive" bots can be '
                           'given a fractional skill when adding them from the '
                           'console. for instance use "/addbot grunt 4.6 blue" '
                           'to add a 4.5 skill Grunt to team blue.',
            'name': 'addbot'},
 'arena': {'description': 'Load arena and bots "name" from arena.txt (arena '
                          '<name>).',
           'name': 'arena'},
 'banClient': {'description': 'Ban a client by slot number used in conjunction '
                              'with serverstatus you can ban players by their '
                              'slot number regardless of player name (from '
                              'server console only) part of the client banning '
                              'system which depends on a master banned list on '
                              'the master server at id software.',
               'name': 'banClient'},
 'banUser': {'description': 'Ban a client by their player name. once the name '
                            'is entered the players name, IP, and CD-Key are '
                            'sent to the master server where the player will '
                            'be band for a length of time determined by id '
                            'software. lamers take heed this system will ban '
                            'you from all servers instantly.',
             'name': 'banUser'},
 'bind': {'description': 'Assign a key to command(s). (bind <key> '
                         '"<command>").',
          'name': 'bind'},
 'bindlist': {'description': 'List all currently bound keys and what command '
                             'they are bound to.',
              'name': 'bindlist'},
 'callteamvote': {'description': 'Allows a team to vote for a captain or team '
                                 'leader.',
                  'name': 'callteamvote'},
 'callvote': {'description': 'Callvote <command> vote <y/n> Caller '
                             'automatically votes yes vote has a 30 second '
                             'timeout each client can only call 3 votes a '
                             'level vote is displayed on screen with totals '
                             '"John Carmack" vote commands are: map_restart, '
                             'nextmap, map , g_gametype and kick.',
              'name': 'callvote'},
 'centerview': {'description': 'Quickly move current view to the center of '
                               'screen.',
                'name': 'centerview'},
 'changeVectors': {'description': 'Change to vector defined by '
                                  'FIND_NEW_CHANGE_VECTORS as in vector '
                                  'graphics - with vector graphics it is '
                                  'possible to change any element of the '
                                  'picture at any time since each part is '
                                  'stored as an independent object whereas '
                                  'once something in a bitmap has been '
                                  'overwritten it cannot in general be '
                                  'retrieved. could also be for 3D rendering '
                                  'vectors?.',
                   'name': 'changeVectors'},
 'cinematic': {'description': 'Play the q3a movie RoQ files (cinematic '
                              'intro.RoQ).',
               'name': 'cinematic'},
 'clear': {'description': 'Clear all text from console.', 'name': 'clear'},
 'clientinfo': {'description': 'Display name, rate, number of snaps, player '
                               'model, rail color, and handicap (state '
                               'number?).',
                'name': 'clientinfo'},
 'clientkick': {'description': 'Kick a client by slot number used in '
                               'conjunction with serverstatus you can kick '
                               'players by their slot number regardless of '
                               'player name (from server console only).',
                'name': 'clientkick'},
 'cmd': {'description': 'Send a command to server remote console.',
         'name': 'cmd'},
 'cmdlist': {'description': 'List all available console commands.',
             'name': 'cmdlist'},
 'condump': {'description': 'Condump "x" write the console text to a file '
                            'where "x" is the name of that file.',
             'name': 'condump'},
 'configstrings': {'description': 'List the current config strings in effect.',
                   'name': 'configstrings'},
 'connect': {'description': 'Connect to server (connect 204.52.135.50) or '
                            '(connect serverURL.com).',
             'name': 'connect'},
 'crash': {'description': 'Causes Q3TEST.EXE to perform an illegal operation '
                          'in Windows.',
           'name': 'crash'},
 'cvar_restart': {'description': 'Reset all variables back to factory defaults '
                                 '(could be handy).',
                  'name': 'cvar_restart'},
 'cvarlist': {'description': 'List all available console variables and their '
                             'values.',
              'name': 'cvarlist'},
 'demo': {'description': 'Play demo (demo q3demo001.dm3).', 'name': 'demo'},
 'devmap': {'description': 'Load maps in development mode? (loads map with '
                           'cheats enabled).',
            'name': 'devmap'},
 'dir': {'description': 'Display directory if syntax is correct ex. (dir \\) '
                        'or (dir ..\\) or (dir ..\\baseq3).',
         'name': 'dir'},
 'disconnect': {'description': 'Disconnects you from server (local included).',
                'name': 'disconnect'},
 'dumpuser': {'description': 'Display user info (handicap, model/color, rail '
                             'color, more )(dumpuser "<name>").',
              'name': 'dumpuser'},
 'echo': {'description': 'Echo a string to the message display to your console '
                         'only.',
          'name': 'echo'},
 'error': {'description': 'Execute an error routine to protect the server.',
           'name': 'error'},
 'exec': {'description': 'Execute a config file or script.', 'name': 'exec'},
 'fdir': {'description': 'Allows the user to search his game directory for the '
                         'presence of file types. a common use for this might '
                         'be to search out the file names of maps that are '
                         'often buried inside pak files with different names. '
                         'syntax: fdir <filter>example: fdir *q3dm?.bsp - In '
                         'this example, the user is searching all '
                         'subdirectories (the "*" stands in for the path name) '
                         'for game maps (the .bsp file extension) that have '
                         'the letters "q3dm" in their name AND that are '
                         'followed by a single character (indicated by the '
                         '"?").one or more metacharacters may be used in the '
                         'filter.* match any string of zero or more '
                         'characters? match any single character[abc...] match '
                         'any of the enclosed characters; a hyphen can be used '
                         'to specify a range (e.g. a-z, A-Z, 0-9).',
          'name': 'fdir'},
 'follow': {'description': 'Switch to follow mode (follow "<name>" or follow1 '
                           'for 1ST place follow2 for 2ND etc ).',
            'name': 'follow'},
 'freeze': {'description': 'Freeze game and all animation for specified time '
                           '(freeze 5) (5 seconds).',
            'name': 'freeze'},
 'fs_openedList': {'description': 'Display the file name of open pak files '
                                  '(pk3).',
                   'name': 'fs_openedList'},
 'gfxinfo': {'description': 'Returns extensive information about video '
                            'settings.',
             'name': 'gfxinfo'},
 'give': {'description': 'Cheat - give player item (give railgun).',
          'name': 'give'},
 'globalservers': {'description': 'List public servers on the internet.',
                   'name': 'globalservers'},
 'god': {'description': 'Cheat - give player invulnerability.', 'name': 'god'},
 'heartbeat': {'description': 'Send a manual heartbeat to the master servers.',
               'name': 'heartbeat'},
 'hunk_stats': {'description': 'Returns value of some registers how many bits '
                               'high/low and total meminfo command replaces '
                               'hunk_stats and z_stats "John Carmack".',
                'name': 'hunk_stats'},
 'imagelist': {'description': 'List currently open images/textures used by the '
                              'current map. also displays the amount of '
                              'texture memory the map is using which is the '
                              'last number displayed - Jax_Gator.',
               'name': 'imagelist'},
 'in_restart': {'description': 'Restarts all the input drivers, dinput, '
                               'joystick, etc.',
                'name': 'in_restart'},
 'joy_advancedupdate': {'description': 'Removed Graeme says joy support still '
                                       'broken.',
                        'name': 'joy_advancedupdate'},
 'kick': {'description': 'Kick the player with the given name off the server. '
                         'if nobody uses the name "all" and "all" is specified '
                         'as player name then everyone is kicked. if there are '
                         'no bots with the name "allbots" and "allbots" is '
                         'specified as player name then all the bots are '
                         'kicked. (from server console only kick "<name>").',
          'name': 'kick'},
 'kill': {'description': 'Kills your player (suicide but can get you unstuck '
                         'some times).',
          'name': 'kill'},
 'killserver': {'description': 'Stops server from running and broadcasting '
                               'heartbeat??.',
                'name': 'killserver'},
 'levelshot': {'description': 'Display the image used at the end of a level.',
               'name': 'levelshot'},
 'loaddefered': {'description': 'Load models and skins that have not yet been '
                                'loaded.',
                 'name': 'loaddefered'},
 'loaddeferred': {'description': 'Load models and skins that have not yet been '
                                 'loaded (corrected spelling).',
                  'name': 'loaddeferred'},
 'localservers': {'description': 'List servers on LAN or local sub net only.',
                  'name': 'localservers'},
 'map': {'description': 'Loads specified map (map q3dm7).', 'name': 'map'},
 'map_restart': {'description': 'Resets the game on the same map (also plays '
                                'fight! sound file and displays FIGHT!).',
                 'name': 'map_restart'},
 'meminfo': {'description': 'Meminfo command replaces hunk_stats and z_stats '
                            '"John Carmack".',
             'name': 'meminfo'},
 'messagemode': {'description': 'Send a message to everyone.',
                 'name': 'messagemode'},
 'messagemode2': {'description': 'Send a message to teammates.',
                  'name': 'messagemode2'},
 'messagemode3': {'description': 'Send a message to tourney opponents?.',
                  'name': 'messagemode3'},
 'messagemode4': {'description': 'Send a message to attacker? (does not work).',
                  'name': 'messagemode4'},
 'midiinfo': {'description': 'Display information about MIDI music system.',
              'name': 'midiinfo'},
 'model': {'description': 'Display the name of current player model if no '
                          'parameters are given (see also model variable).',
           'name': 'model'},
 'modelist': {'description': 'List of accessible screen resolutions.',
              'name': 'modelist'},
 'modellist': {'description': 'List of currently open player models.',
               'name': 'modellist'},
 'music': {'description': 'Plays specified music file (music music.wav).',
           'name': 'music'},
 'net_restart': {'description': 'Reset all the network related variables like '
                                'rate etc.',
                 'name': 'net_restart'},
 'nextframe': {'description': '"nextframe", "prevframe", "nextskin", and '
                              '"prevskin" commands will change the frame or '
                              'skin of the testmodel. These are bound to F5, '
                              'F6, F7, and F8 in q3default.cfg.',
               'name': 'nextframe'},
 'nextskin': {'description': '"nextframe", "prevframe", "nextskin", and '
                             '"prevskin" commands will change the frame or '
                             'skin of the testmodel. These are bound to F5, '
                             'F6, F7, and F8 in q3default.cfg.',
              'name': 'nextskin'},
 'noclip': {'description': 'No clipping objects (nothing will be solid).',
            'name': 'noclip'},
 'notarget': {'description': 'BOTS will not fight/see you (good for getting '
                             'cool screenshots).',
              'name': 'notarget'},
 'path': {'description': 'Display all current game paths.', 'name': 'path'},
 'ping': {'description': 'Manually ping a server (ping "<sv_hostname>" or by '
                         'the IP address).',
          'name': 'ping'},
 'play': {'description': 'Play a sound file (play sound.wav).', 'name': 'play'},
 'prevframe': {'description': '"nextframe", "prevframe", "nextskin", and '
                              '"prevskin" commands will change the frame or '
                              'skin of the testmodel. These are bound to F5, '
                              'F6, F7, and F8 in q3default.cfg.',
               'name': 'prevframe'},
 'prevskin': {'description': '"nextframe", "prevframe", "nextskin", and '
                             '"prevskin" commands will change the frame or '
                             'skin of the testmodel. These are bound to F5, '
                             'F6, F7, and F8 in q3default.cfg.',
              'name': 'prevskin'},
 'quit': {'description': 'Quit arena and quit Quake 3 Arena and return to your '
                         'OS Thanx for flying.',
          'name': 'quit'},
 'rcon': {'description': 'Start a remote console to a server.', 'name': 'rcon'},
 'reconnect': {'description': 'Re-initialize the connection to the last server '
                              'you were connected to.',
               'name': 'reconnect'},
 'record': {'description': 'Records a demo (record mydemo.dm3) '
                           '(g_syncronousClients must be a 1 to start).',
            'name': 'record'},
 'reset': {'description': 'Reset specified variable (reset model) single '
                          'variable as opposed to cvar_restart (c:.',
           'name': 'reset'},
 'restart': {'description': 'Restart the game on the current map (server '
                            'only).',
             'name': 'restart'},
 's_disable_a3d': {'description': 'Disable support for Aureal 3D sound system.',
                   'name': 's_disable_a3d'},
 's_enable_a3d': {'description': 'Enable support for Aureal 3D sound system.',
                  'name': 's_enable_a3d'},
 's_info': {'description': 'Display information about sound system (replaced '
                           'soundinfo command).',
            'name': 's_info'},
 's_list': {'description': 'Display paths and filenames of all sound files as '
                           'they are played. (replaced soundlist command).',
            'name': 's_list'},
 's_stop': {'description': 'Stop whatever sound that is currently playing from '
                           'playing. (Replaced stopsound command).',
            'name': 's_stop'},
 'say': {'description': 'Say something to everyone on the server.',
         'name': 'say'},
 'say_team': {'description': 'Say something to your team only.',
              'name': 'say_team'},
 'scanservers': {'description': 'Scan the local area network for servers (only '
                                'works for same subnet).',
                 'name': 'scanservers'},
 'screenshot': {'description': 'Save current viewport to a TARGA image file '
                               '(usually named sequentially shot0001.tga).',
                'name': 'screenshot'},
 'screenshotJPEG': {'description': 'Save current viewport to a JPEG image file '
                                   '(usually named sequentially shot0001.jpg).',
                    'name': 'screenshotJPEG'},
 'sectorlist': {'description': 'Lists sectors and number of entities in each '
                               'on the currently loaded map.',
                'name': 'sectorlist'},
 'serverinfo': {'description': 'Gives information about local server from the '
                               'console of that server.',
                'name': 'serverinfo'},
 'serverrecord': {'description': 'Records a serverside demo (serverrecord '
                                 'srvrdemo.dm3).',
                  'name': 'serverrecord'},
 'serverstatus': {'description': 'Display the current status of the connected '
                                 'server as well as connected users and their '
                                 'slot number. if you specify an IP address it '
                                 'will display the status of a remote server.',
                  'name': 'serverstatus'},
 'serverstop': {'description': 'Stops the recording of a serverside demo.',
                'name': 'serverstop'},
 'set': {'description': 'Set a variable (set <variable name> '
                        '<commands;separate by;semi;colon>).',
         'name': 'set'},
 'seta': {'description': 'Sets the variable with the archive flag will save '
                         'the last setting to q3config.cfg and reload that '
                         'setting every time you run the game. Any changes to '
                         'variables with an A for the class ID are '
                         'automatically stored in q3config.cfg - LOKi.',
          'name': 'seta'},
 'setenv': {'description': 'Sets environment variables.', 'name': 'setenv'},
 'sets': {'description': 'Sets the variable with the serverinfo flag, so it '
                         'will be transmitted from a server to connecting '
                         'clients - LOKi.',
          'name': 'sets'},
 'setu': {'description': 'Sets the variable with the userinfo flag, so it will '
                         'be transmitted from a client to a server while '
                         'connecting - LOKi.',
          'name': 'setu'},
 'setviewpos': {'description': 'Sets the VR coordinates of the players view '
                               'screen.',
                'name': 'setviewpos'},
 'shaderlist': {'description': 'List of currently open shaders (light '
                               'effects).',
                'name': 'shaderlist'},
 'showip': {'description': 'Display your current TCP/IP address.',
            'name': 'showip'},
 'sizedown': {'description': 'Makes viewport one size smaller.',
              'name': 'sizedown'},
 'sizeup': {'description': 'Makes viewport one size larger.', 'name': 'sizeup'},
 'skinlist': {'description': 'List of currently open skins.',
              'name': 'skinlist'},
 'snd_restart': {'description': 'Reinitialize sound.', 'name': 'snd_restart'},
 'soundinfo': {'description': 'Information about sound system.',
               'name': 'soundinfo'},
 'soundlist': {'description': 'List of currently open sound files.',
               'name': 'soundlist'},
 'spdevmap': {'description': 'Load a devmap with bots spawned in. (cheats '
                             'enabled).',
              'name': 'spdevmap'},
 'spmap': {'description': 'Load a map with bots spawned in. (cheats disabled).',
           'name': 'spmap'},
 'startOrbit': {'description': 'Start the 3rd person display of your player '
                               'model and orbit in a circle around it.',
                'name': 'startOrbit'},
 'status': {'description': 'Status of currently connected server.',
            'name': 'status'},
 'stopdemo': {'description': 'Stop recording demo.', 'name': 'stopdemo'},
 'stoprecord': {'description': 'Stop recording a demo.', 'name': 'stoprecord'},
 'stopsound': {'description': 'Stop whatever sound that is currently playing '
                              'from playing.',
               'name': 'stopsound'},
 'systeminfo': {'description': 'Returns values for: g_syncronousclients, '
                               'sv_serverid, and timescale.',
                'name': 'systeminfo'},
 'tcmd': {'description': 'Display the current target command or displays some '
                         'type of code address.',
          'name': 'tcmd'},
 'team': {'description': 'Set player status. p=player s=spectator red, blue, '
                         'or free (team free joins smallest/loosing team)also '
                         'in tourney play team follow1 2 etc.(follow players '
                         'by lead position) team scoreboard your player '
                         'becomes a scoreboard.',
          'name': 'team'},
 'teamtask': {'description': 'Display the current task you have been assigned '
                             '1 - offense 2 - defense 3 - point/patroll 4 - '
                             'following 5 - retrieving 6 - escort(gaurding '
                             'flag carrier) 7 - camping.',
              'name': 'teamtask'},
 'teamvote': {'description': 'Allows user to cast a vote on a called team vote '
                             'yes or no callteamvote <playername> vote <y/n> '
                             'Caller automatically votes yes vote has a 30 '
                             'second timeout each client can only call 3 votes '
                             'a level vote is displayed on screen with totals.',
              'name': 'teamvote'},
 'tell': {'description': 'Say something to an individual on the server tell '
                         '<playername> "go get the flag".',
          'name': 'tell'},
 'tell_attacker': {'description': 'Possibly to pass a complement to your last '
                                  'known attacker..he he more like insult.',
                   'name': 'tell_attacker'},
 'tell_target': {'description': 'Possibly to pass a complement back ha ha more '
                                'like "Die Llama".',
                 'name': 'tell_target'},
 'testfog': {'description': 'Removed may have been used for development of fog '
                            'emulation.',
             'name': 'testfog'},
 'testgun': {'description': 'Weapon model dissapears cg_gun 1 does not bring '
                            'it back. will cause the model to follow the '
                            'player around and suppress the real view weapon '
                            'model. The default frame 0 of most guns is '
                            'completely off screen, so you will probably have '
                            'to cycle a couple frames to see it. "nextframe", '
                            '"prevframe", "nextskin", and "prevskin" commands '
                            'will change the frame or skin of the testmodel. '
                            'These are bound to F5, F6, F7, and F8 in '
                            'q3default.cfg.',
             'name': 'testgun'},
 'testmodel': {'description': 'Testmodel <path\\model.md3> will create a fake '
                              'entity 100 units in front of the current view '
                              'position, directly facing the viewer. It will '
                              'remain immobile, so you can move around it to '
                              'view it from different angles "nextframe", '
                              '"prevframe", "nextskin", and "prevskin" '
                              'commands will change the frame or skin of the '
                              'testmodel. These are bound to F5, F6, F7, and '
                              'F8 in q3default.cfg. (useful tool for model and '
                              'skin artists).',
               'name': 'testmodel'},
 'testshader': {'description': 'Covers all brushes and entities with the '
                               'selected texture, and lights the map using the '
                               'effect of that texture as well. entering '
                               'testshader without a parameter will restore '
                               'all textures set by the map. -hacker (removed '
                               'possibly because cheat potential).',
                'name': 'testshader'},
 'toggle': {'description': 'Toggle "X", where X is the variable you give, to a '
                           '1 if it is 0 and 0 if it is 1 (toggle '
                           'cg_autoswitch) "The \'toggle\' command can toggle '
                           'write protected cvars." Graeme.',
            'name': 'toggle'},
 'toggleconsole': {'description': 'Usually bound to ~ the tilde key brings the '
                                  'console up and down.',
                   'name': 'toggleconsole'},
 'touchFile': {'description': 'Make the file a zero byte file (not a good idea '
                              'I did not test this one).',
               'name': 'touchFile'},
 'unbind': {'description': 'Unbinds a key.', 'name': 'unbind'},
 'unbindall': {'description': 'Unbinds all keys (be careful).',
               'name': 'unbindall'},
 'userinfo': {'description': 'List user information like (possibly replaced by '
                             'clientinfo).',
              'name': 'userinfo'},
 'vid_restart': {'description': 'Reinitialize video.', 'name': 'vid_restart'},
 'viewpos': {'description': 'Returns player coordinates on the map in x y z '
                            'form.',
             'name': 'viewpos'},
 'vminfo': {'description': 'Display information about virtual machine '
                           'interpreter on the local machine.',
            'name': 'vminfo'},
 'vmprofile': {'description': "Possibly more of the virtual machine John's "
                              'talking about, profile hmm?.',
               'name': 'vmprofile'},
 'vmtest': {'description': 'Probably a developer test which returns levels of '
                           'success, returns >display "C: test 1234".',
            'name': 'vmtest'},
 'vosay': {'description': 'Use a predefined voice message and play everyone.',
           'name': 'vosay'},
 'vosay_team': {'description': 'Use a predefined voice message and play to '
                               'your team.',
                'name': 'vosay_team'},
 'vote': {'description': 'Allows user to cast a vote on a called vote usually '
                         'bound to F1 (yes) and F2 (no)...(c: callvote '
                         '<command> vote <y/n> Caller automatically votes yes '
                         'vote has a 30 second timeout each client can only '
                         'call 3 votes a level vote is displayed on screen '
                         'with totals "John Carmack".',
          'name': 'vote'},
 'votell': {'description': 'Use a predefined voice message and play to a '
                           '<playername> you specify.',
            'name': 'votell'},
 'vsay': {'description': 'Use a predefined voice message and play to everyone.',
          'name': 'vsay'},
 'vsay_team': {'description': 'Use a predefined voice message and play to your '
                              'team.',
               'name': 'vsay_team'},
 'vstr': {'description': 'Identifies the attached command as a variable sting '
                         '(bind a vstr "myvariable").',
          'name': 'vstr'},
 'vtaunt': {'description': 'Play a random voice taunt wav file to everyone.',
            'name': 'vtaunt'},
 'vtell': {'description': 'Possibly to play a random voice taunt to a '
                          '<playername> you specify.',
           'name': 'vtell'},
 'vtell_attacker': {'description': 'Possibly to play a random voice taunt to '
                                   'your last known attacker.',
                    'name': 'vtell_attacker'},
 'vtell_target': {'description': 'Possibly to play a random voice taunt at '
                                 'player you last hit.',
                  'name': 'vtell_target'},
 'wait': {'description': 'Stop execution and wait one game tick (no alias '
                         'support will be added in Q3A per J.C.).',
          'name': 'wait'},
 'weapnext': {'description': 'Switch to the next higher numbered weapon.',
              'name': 'weapnext'},
 'weapon': {'description': 'Select a weapon by it\'s number (weapon "5").',
            'name': 'weapon'},
 'weapprev': {'description': 'Switch to the next lower numbered weapon.',
              'name': 'weapprev'},
 'writeconfig': {'description': 'Saves current configuration to a cfg file '
                                'this is cool! (c:.',
                 'name': 'writeconfig'},
 'z_stats': {'description': 'Display the memory statistics for the Z-buffer in '
                            'the game "lists all blocks >= given size" John '
                            'Carmack meminfo command replaces hunk_stats and '
                            'z_stats "John Carmack".',
             'name': 'z_stats'}}
