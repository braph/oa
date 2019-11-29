#!/usr/bin/python
# -*- coding: utf-8 -*-
LABEL = 'stupidctf.tk'
VARIABLES = {'': {'default': '',
      'description': "Sets color of enemy model's head/torso/leg and team "
                     "model's head/torso/leg respectively.\n"
                     'See detailed help on these cvars!',
      'name': ''},
 'cg_2dShadowAlpha': {'default': '1.00',
                      'description': "The 2d texts' alpha. A float. 0 means no "
                                     'shadow.',
                      'name': 'cg_2dShadowAlpha'},
 'cg_accBoardAlpha': {'default': '0.81',
                      'description': "The accboard's (when you press +acc) "
                                     "background's alpha. 0 means totally "
                                     'transparent, 1 means totally opaque, '
                                     "solid cg_accBoardTint color. It's a "
                                     'float (ie 0.5 means half-transparent).\n'
                                     '\n'
                                     'Note: this settign does not affect the '
                                     'scoreboard accboard. (because with large '
                                     'alpha value and small tint it looked '
                                     'better than the weaponbar:) will add '
                                     'weaponbarstyles with those settings '
                                     'instead!)',
                      'name': 'cg_accBoardAlpha'},
 'cg_accBoardTint': {'default': '0.14',
                     'description': "The little accuracyboard's (when you "
                                    "press +acc) background's tint. ie: how "
                                    'black or how white it should be. 0 is '
                                    'totally black, 1 white. (the text is '
                                    'still white though, careful with '
                                    'whitening)\n'
                                    '\tSee also: cg_accBoardAlpha',
                     'name': 'cg_accBoardTint'},
 'cg_centerPrintFontSizeOffset': {'default': '0',
                                  'description': 'Changes the centerprint '
                                                 "message's font size. "
                                                 'Increase with positive '
                                                 'values. 0 leaves it at '
                                                 'default size.',
                                  'name': 'cg_centerPrintFontSizeOffset'},
 'cg_crossHairColorBlue': {'default': '1',
                           'description': 'The BLUE component of crosshair. '
                                          'See cg_crossHairColorRed for full '
                                          'description!',
                           'name': 'cg_crossHairColorBlue'},
 'cg_crossHairColorGreen': {'default': '1',
                            'description': 'The GREEN component of crosshair. '
                                           'See cg_crossHairColorRed for full '
                                           'description!',
                            'name': 'cg_crossHairColorGreen'},
 'cg_crossHairColorRed': {'default': '1',
                          'description': 'Crosshairs are now colorizable 0.8.8 '
                                         'style.\n'
                                         '    It does not have the UI, only '
                                         'the cvars. Connect to a 0.8.8 server '
                                         'if you prefer UI configuring! Than '
                                         'you must play with the sliders in UI '
                                         'and get the respective values from '
                                         'your resulting q3config.cfg,\n'
                                         "    but sadly you can't do it "
                                         "because you don't know what and "
                                         'where your q3config is. (or just let '
                                         'it autosave if you are luckily in '
                                         'the same mod folder! (CTF))\n'
                                         '    Search for q3config.cfg on your '
                                         'storage!\n'
                                         '    Yet at the same time if you are '
                                         'reading this, there is a really good '
                                         "chance you know exactly what's your "
                                         "q3config is so you don't need the UI "
                                         'to set it anyway!\n'
                                         '    \n'
                                         '    This is the RED component of the '
                                         'crosshair. see also '
                                         'cg_crossHairColorGreen and '
                                         'cg_crossHairColorBlue\n'
                                         '    \n'
                                         '    It accepts a float in range of '
                                         '0-1:\n'
                                         '    For example '
                                         '/cg_crossHairColorRed 0.33 for a '
                                         'third fullness of red; red 1 green '
                                         '0.5 blue 1 results in a pink xhair. '
                                         "You can figure out the others. It's "
                                         'basically RGB with numbers between '
                                         '[0-1]',
                          'name': 'cg_crossHairColorRed'},
 'cg_crossHairHealth': {'default': '0 coming from 081 and below, 1 from 085 '
                                   '(?)',
                        'description': 'With 2, the crosshair matches your HUD '
                                       'health color, otherwise it is white '
                                       'unless you set it with '
                                       'cg_crossHairColorRed and co.',
                        'name': 'cg_crossHairHealth'},
 'cg_crossHairPulse': {'default': '1',
                       'description': 'The crosshair pulses (grows and shrinks '
                                      'back to original value) upon picking up '
                                      'an item.',
                       'name': 'cg_crossHairPulse'},
 'cg_crosshairAspectRatio': {'default': '1',
                             'description': 'Crosshairs are not eggshaped by '
                                            'default anymore when using a '
                                            'weird resolution.\n'
                                            'This cvar helps you if you prefer '
                                            'the good old 081ish eggshaped '
                                            'xhairs (i do!). The value is a '
                                            'float - you can set custom '
                                            'egginess - ie: 1.5 draws an egg. '
                                            '0.5 an egg on its side.',
                             'name': 'cg_crosshairAspectRatio'},
 'cg_damagePlum': {'default': '1',
                   'description': 'The amount of damage you caused with your '
                                  'shot will pop out as respective numbers '
                                  'from the enemy. Useful and cool, leave it '
                                  'at 1!',
                   'name': 'cg_damagePlum'},
 'cg_drawAntiCampPosY': {'default': '0',
                         'description': 'Move the anticamp warning msg you see '
                                        'all the time at insta vertically with '
                                        'this one.',
                         'name': 'cg_drawAntiCampPosY'},
 'cg_drawHolyShit': {'default': '0',
                     'description': 'Draws a little holy shit icon in the '
                                    'middle of your screen when shit happens '
                                    'with you or you cause some shit. '
                                    'Obscuring the view can be annoying, so '
                                    'you can disable it with -1.',
                     'name': 'cg_drawHolyShit'},
 'cg_drawPusher': {'default': '0',
                   'description': 'Displaying the name of pusher can be '
                                  'disabled with this one (-1)',
                   'name': 'cg_drawPusher'},
 'cg_drawReady': {'default': '0',
                  'description': 'The "Majority of players should be ready you '
                                 'can ready blahblah" text when the game is in '
                                 'waiting for /ready state. Remove it '
                                 'completely with -1, 1 is a short version. 0 '
                                 'is mod default: the long\n'
                                 '    annoying verbose format',
                  'name': 'cg_drawReady'},
 'cg_drawTimer': {'default': '1',
                  'description': '/cg_drawTimer 2 enables Big White Clock '
                                 'cvars, see hud_clock cvars!\n'
                                 '\n'
                                 '    Sets the Y position of the timer and '
                                 'makes it bigger. When you pick up items you '
                                 "don't want to look at the top right corner "
                                 'every time! Move it below the top flagstatus '
                                 'icons! (for example /cg_drawTimer 105). Or '
                                 'between the flags: /cg_drawtimer 2. etc\n'
                                 '    -1 to hides the timer.\n'
                                 "    In baseoa it sets the timer's visibility "
                                 '(on/off 1/0).',
                  'name': 'cg_drawTimer'},
 'cg_drawVote': {'default': '20',
                 'description': 'Moves the callvote text on the y axis. 0 = '
                                'top, 480 = bottom. Move it so the '
                                'demorecording text does not overwrite the '
                                'callvote text!\n'
                                ' Alternatively you can use a customized '
                                'client and the annoying RECORDING text will '
                                'not show up. Download it from here!',
                 'name': 'cg_drawVote'},
 'cg_enemyAlwaysGreen': {'default': '0',
                         'description': "You can force the enemy's skin to an "
                                        'easy to see bright green color:\n'
                                        '/cg_enemyAlwaysGreen 1 : enemy green '
                                        '/ own team red or blue, depends on '
                                        'actual team\n'
                                        '/cg_enemyAlwaysGreen 2 : enemy green '
                                        '/ own team white\n'
                                        '/cg_enemyAlwaysGreen 3 : enemy green '
                                        '/ own team pink\n'
                                        '/cg_enemyAlwaysGreen 4 : enemy white, '
                                        "your team's color is your actual "
                                        'teamcolor\n'
                                        '/cg_enemyAlwaysGreen 5 : enemy pink, '
                                        'your team white\n'
                                        '    Note: You have to be in-game, '
                                        'does not work in spec!',
                         'name': 'cg_enemyAlwaysGreen'},
 'cg_enemyHeadColor': {'default': '0x55DD33',
                       'description': "Sets color of enemy model's "
                                      "head/torso/leg and team model's "
                                      'head/torso/leg respectively.\n'
                                      'See detailed help on these cvars!',
                       'name': 'cg_enemyHeadColor'},
 'cg_enemyLegsColor': {'default': '0x88DD00',
                       'description': "Sets color of enemy model's "
                                      "head/torso/leg and team model's "
                                      'head/torso/leg respectively.\n'
                                      'See detailed help on these cvars!',
                       'name': 'cg_enemyLegsColor'},
 'cg_enemyModel': {'default': '',
                   'description': 'Sets enemy model. See detailed help for '
                                  'this cvar!',
                   'name': 'cg_enemyModel'},
 'cg_enemyRail': {'default': '0',
                  'description': 'The color of all enemy rail trails will be '
                                 'forced to the color secified by this cvar. '
                                 'Single digit numbers only force the CORE of '
                                 'the trail! Use double digits to force the '
                                 'swirl/disks (depending on /cg_railstyle) '
                                 'too!\n'
                                 'For example /cg_enemyRail 62 will force the '
                                 'swirl/disk yellow (6) and the core green '
                                 '(2)! (yes yellow and green because of the '
                                 'railcolor palette, see below)\n'
                                 'Use 0 to skip forcing either the swirl or '
                                 'the core! Like this: /cg_enemyRail 40; this '
                                 "will only force the enemy's secondary color "
                                 '(the swirl or the disk).\n'
                                 'See cg_teamRail too!',
                  'name': 'cg_enemyRail'},
 'cg_enemySound': {'default': 'Beret',
                   'description': "Enemy players' sound will be forced to this "
                                  "model's sound. Every 081 oa model's sounds "
                                  'are available. Tip: set male sound for '
                                  'enemy, female for your team to easily '
                                  'distinguish them.\n'
                                  '    Note: You have to be in-game, does not '
                                  'work in spec!',
                   'name': 'cg_enemySound'},
 'cg_enemyTorsoColor': {'default': '0x66FF33',
                        'description': "Sets color of enemy model's "
                                       "head/torso/leg and team model's "
                                       'head/torso/leg respectively.\n'
                                       'See detailed help on these cvars!',
                        'name': 'cg_enemyTorsoColor'},
 'cg_flagDropSound': {'default': '0',
                      'description': 'You can change the sound you hear when '
                                     'your flag carrier goes down (or '
                                     '/dropflags it deliberately or /kills '
                                     'self). The default is pretty good now, '
                                     'leave it at 0. (Thx f:x3r for the 50+ '
                                     'souds)\n'
                                     '    Available sounds are 0-4, -1 '
                                     'disables it (no flagsound at all).',
                      'name': 'cg_flagDropSound'},
 'cg_flagDropSoundEnemy': {'default': '0',
                           'description': 'Same as cg_flagDropSound but '
                                          'changes the sound played when the '
                                          'enemy carrier drops the flag. 0 is '
                                          'a good choice for this one too.',
                           'name': 'cg_flagDropSoundEnemy'},
 'cg_flagStatusStyle': {'default': '0',
                        'description': 'When the flag is taken (not in its '
                                       'place) you can see it displayed on the '
                                       'top of the screen. Right now with this '
                                       'cvar you can set the fontsize of your '
                                       "flag carrier's name health armor and "
                                       'location,\n'
                                       '    later the style will be settable '
                                       'too.',
                        'name': 'cg_flagStatusStyle'},
 'cg_forceEnemyFootSteps': {'default': '0',
                            'description': "Force the enemy's footsteps to "
                                           'either:\n'
                                           '1 Mech. Skelebot, Smarine and '
                                           'maybe someone else uses this one. '
                                           'This is a good choice\n'
                                           '2 Flesh. Gargoyle makes these '
                                           'footstep sounds when walking, a '
                                           'really good choice imo. Somewhat '
                                           'reminds me of Keel.\n'
                                           "3 Energy. Ayumi's energy skates. "
                                           'No\n'
                                           "4 Boots. This one is sarge's - and "
                                           'everyone else who wears boots xd - '
                                           'boots sound. Not a good choice if '
                                           'your own team model wears boots '
                                           'too! Boot this one!\n'
                                           '5 Normal. The normal boots sound?\n'
                                           '\n'
                                           'A really important setting for '
                                           'proper playing, only a few players '
                                           'set it though:/\n'
                                           'Have an edge and set it! They will '
                                           'wonder how could you know it was '
                                           'an enemy behind that corner. And '
                                           'you just say: f*ck you man, '
                                           'l2cfg!\n'
                                           '    Note: You have to be in-game, '
                                           'does not work in spec!',
                            'name': 'cg_forceEnemyFootSteps'},
 'cg_forceSound': {'default': '0',
                   'description': 'Force the sounds the players make depending '
                                  'on their team!\n'
                                  '    This cvar enables forcing, see '
                                  'cg_enemySound cg_teamSound  and cg_mySound '
                                  "for picking a model's sound.\n"
                                  '    Note: You have to be in-game, does not '
                                  'work in spec!',
                   'name': 'cg_forceSound'},
 'cg_friendSize': {'default': '0 (defaults to 14)',
                   'description': 'The size of the friend-triangle. The Mod '
                                  'default is 14 right now. It means if you '
                                  'are using 0 (0 means mod default setting in '
                                  'general in fm) it results in a size of 14. '
                                  'OA default is size 10, and it was like that '
                                  'in fm until now!\n'
                                  'Max allowed size is 30\n'
                                  '\n'
                                  "At genius you can see your mate's position "
                                  'thru the walls for more teamplay, '
                                  'increasing the size might help if your '
                                  'mates are too far away!',
                   'name': 'cg_friendSize'},
 'cg_hitBeepStyle': {'default': '0',
                     'description': '0 is the moddefault multitonal hitbeep, '
                                    'leave it at this value. the damage '
                                    'thresholds are: >=85, >=60, >=35, >=15. '
                                    'You can change the pitch of the hit beep '
                                    'with values 2-6.\n'
                                    '    2 is default 081 baseoa beep, others '
                                    'are diff pitches.',
                     'name': 'cg_hitBeepStyle'},
 'cg_matchEndSound': {'default': '0',
                      'description': 'That 3 bell rings at the end of the '
                                     'game. Can be disabled by a negative '
                                     'number. It can be useful when you are '
                                     'sitting out a map you find boring with '
                                     "reduced volume to notify you it's over.",
                      'name': 'cg_matchEndSound'},
 'cg_motdTime': {'default': '0',
                 'description': 'This many seconds will the MOTD on the right '
                                'side of the screen displayed in spec. 0 means '
                                "the default 90 seconds, can't set values "
                                'lower than 3 (at least just skim through the '
                                'current message of the day, retard! not you, '
                                'who is reading this! they: "what? railjump is '
                                'on??" "wtf no rocketdamage??" "how change '
                                'back old rail?" "font size big how to '
                                'small??" "why someone dark model!??11" "how '
                                'jump bridge?")',
                 'name': 'cg_motdTime'},
 'cg_mySound': {'default': 'Assassin',
                'description': "Forces your sound to this model's sound.",
                'name': 'cg_mySound'},
 'cg_pusherDisplayTime': {'default': '0 (= 5300ms)',
                          'description': 'At the right side of the screen you '
                                         'can see who pushed you with railgun '
                                         '(this one is particularly useful for '
                                         ':F insta players so they know who '
                                         'the  was, but it  useful for real '
                                         'CTF too. It is an information;\n'
                                         '    you know what your mate is up to '
                                         '(he is pushing right now, with '
                                         'railgun). The more info the merrier. '
                                         'The display time in milliseconds is '
                                         'settable with this cvar. 0 is '
                                         'moddefault, means 5300 ms.',
                          'name': 'cg_pusherDisplayTime'},
 'cg_railStyle': {'default': '6',
                  'description': 'The rail trail style is selectable from '
                                 'preconfigured styles. The core in general is '
                                 'fatter now, more easy to see, not that puny '
                                 'anymore.\n'
                                 '\n'
                                 "    1 similar to baseoa's /cg_oldrail 0, but "
                                 'nonmippable and the core is much stronger.\n'
                                 '    2 same as 1, but the swirl is more '
                                 "emphasized. it's a good choice if you don't "
                                 'force swirl color for your team!\n'
                                 '    3 this is almost like baseoa with '
                                 'oldrail at 0. puny core with swirl, '
                                 'picmippable. (the swirl is not!)\n'
                                 '    4 only the core; but the new strong '
                                 'one.\n'
                                 '    5 mippable core only, and the old one '
                                 'from baseoa. exactly like cg_oldrail 1 in '
                                 'baseoa\n'
                                 '    6 the new fat core with raildiscs like '
                                 'in old q3. this too might be a good choice: '
                                 'force only the core \n'
                                 '      for your team or even for enemy! to '
                                 'distinguish between players but still see if '
                                 'the rail is from your team or enemy!\n'
                                 '      play with /r_railWidth to set disk '
                                 'width!\n'
                                 '    7 same as 6 but mipmapable.',
                  'name': 'cg_railStyle'},
 'cg_scoreBoardAcc': {'default': '1',
                      'description': 'By default your individual weapon '
                                     'accuracies are displayed at the bottom '
                                     'of the screen when the scoreboard is '
                                     'visible. It can be disabled with this '
                                     'one.\n'
                                     '\n'
                                     "Note: If you are 'following' someone, "
                                     'the accuracy is not yours but the '
                                     "player's you spectate (as it should be)!",
                      'name': 'cg_scoreBoardAcc'},
 'cg_statusBarStyle': {'default': '0 ( = mod default: 2)',
                       'description': 'The Statusbar (your ammo, hp, armor). 4 '
                                      'is strongly recommended as it removes '
                                      'the unnecessary clutter: the hp bubble, '
                                      'the armor icon and the HEAD. You know '
                                      'the first number is the ammo, second is '
                                      'hp third is armor.\n'
                                      '    And why would anyone want to see '
                                      'their HEAD displayed all the time '
                                      'during the game?!\n'
                                      '    3 only removes the head\n'
                                      '    1 to get back to ugly 081baseoa.\n'
                                      '    Will be more statusbar styles soon.',
                       'name': 'cg_statusBarStyle'},
 'cg_statusTeamBackground': {'default': '0',
                             'description': '0-5 that red or blue rectangle '
                                            'obscuring the statusbar. You dont '
                                            'need it if you remember which '
                                            'team you joined. (or use 2, 3 or '
                                            '4, they are less annoying)\n'
                                            '    1 draws a line above hp and '
                                            "armor with the team's color you "
                                            'are in.\n'
                                            '    2 draws a bar at the bottom '
                                            'of the screen with the repsective '
                                            'teamcolor\n'
                                            '    3 no background\n'
                                            '    4 a baseoaish background, '
                                            'very faint\n'
                                            '    5 a baseoaish background but '
                                            'still not as opaque, more opaque '
                                            'than 4',
                             'name': 'cg_statusTeamBackground'},
 'cg_teamHeadColor': {'default': '0xFFFFFF',
                      'description': "Sets color of enemy model's "
                                     "head/torso/leg and team model's "
                                     'head/torso/leg respectively.\n'
                                     'See detailed help on these cvars!',
                      'name': 'cg_teamHeadColor'},
 'cg_teamLegsColor': {'default': '0xFFFFFF',
                      'description': "Sets color of enemy model's "
                                     "head/torso/leg and team model's "
                                     'head/torso/leg respectively.\n'
                                     'See detailed help on these cvars!',
                      'name': 'cg_teamLegsColor'},
 'cg_teamModel': {'default': 'major/pm',
                  'description': 'Sets own team model. See detailed help for '
                                 'this cvar!',
                  'name': 'cg_teamModel'},
 'cg_teamOverlayFontSizeOffset': {'default': '0',
                                  'description': 'Increases or decreases the '
                                                 'TeamOverlay font size. '
                                                 '(positive value to increase '
                                                 'from default, negative to '
                                                 'decrease).\n'
                                                 '    Unfortunately it '
                                                 'collides with the flagstatus '
                                                 'icons at the top with just a '
                                                 'slight increase and they are '
                                                 'not repositionable yet:/\n'
                                                 '    Move it it with '
                                                 '/cg_drawTeamoverlay <value> '
                                                 'if you want bigger '
                                                 'overlaytext!',
                                  'name': 'cg_teamOverlayFontSizeOffset'},
 'cg_teamOverlayHealthBar': {'default': '1',
                             'description': "Right now it's Whether to draw "
                                            'healthbars on names in '
                                            'teamoverlay or not. Will be more '
                                            'barstyles later.',
                             'name': 'cg_teamOverlayHealthBar'},
 'cg_teamRail': {'default': '0',
                 'description': "Forces everyone's railcolor in your team to "
                                'specified color.\n'
                                'Accepts the same values as cg_enemyRail (see '
                                "there!) but affects your team's (and yours) "
                                'colors\n'
                                '\n'
                                'A good practice for competitiveness could be '
                                "if you force enemy's rail fully, ie: "
                                '/cg_enemyRail 76 (white, yellow core) and '
                                'your \n'
                                "team's /cg_teamRail 50 only partially, so you "
                                'can see immeditaly who is railing there (or '
                                'was a few seconds ago with eg: '
                                '/cg_railTrailTime 3000\n'
                                'You could agree with your team to use '
                                'different /color1 vars, as that setting '
                                'defines the railcore color.\n'
                                '\n'
                                'You can even go as far as forcing enemy '
                                "rail's color partially, (THE CORE) to an easy "
                                'to see color like yellow /cg_enemyRail 6 and '
                                'leave their\n'
                                'swirls or disks unforced! it means their '
                                '/color2 will be used! If they are using '
                                "different /color2's each, you can see "
                                'immediately who fired that shot!\n'
                                "Force your team's railcore to a more faint "
                                'color, like red or blue (1, 4) - more easy to '
                                'distinguish - and leave the swirl to their '
                                '/color2.\n'
                                '\n'
                                "The colorpalette does not match oa's naming "
                                'and console color convention, but its '
                                'railcolor palette. Those you use for your '
                                '/color1 and /color2. weirdly, \n'
                                'they are different:/ and went with those '
                                'colors in the mod to keep it baseoa '
                                'friendly.\n'
                                '\n'
                                '\n'
                                '\n'
                                '\n'
                                '    1:\tblue\t(001)\n'
                                '    2:\tgreen\t(010)\n'
                                '    3:\tcyan\t(011)\n'
                                '    4:\tred\t(100)\n'
                                '    5:\tpurple\t(101)\n'
                                '    6:\tyellow\t(110)\n'
                                '    7:\twhite\t(111)\n'
                                '\n'
                                '\n'
                                'It is actually a 3bit RGB color. The highest '
                                'bit is red, the mid is green, the lowest bit '
                                'is blue\n'
                                'For example you get purple by adding red and '
                                'blue: binay 101 = 5; cyan is green+blue: 011 '
                                '= 3;\n'
                                'Yes, could have gone with full rgb notation '
                                '(ie: #ff7700) but at the end of the day '
                                'people force green or yellow or something '
                                "simple, don't they?",
                 'name': 'cg_teamRail'},
 'cg_teamSound': {'default': 'Major',
                  'description': "Your team's players' sound will be forced to "
                                 "this model's sound. Every 081 oa model's "
                                 'sounds are available. Tip: set male sound '
                                 'for enemy, female for your team to easily '
                                 'distinguish them.\n'
                                 '    Note: You have to be in-game, does not '
                                 'work in spec!',
                  'name': 'cg_teamSound'},
 'cg_teamTorsoColor': {'default': '0xFFE0FF',
                       'description': "Sets color of enemy model's "
                                      "head/torso/leg and team model's "
                                      'head/torso/leg respectively.\n'
                                      'See detailed help on these cvars!',
                       'name': 'cg_teamTorsoColor'},
 'cg_weaponBarOffsetY': {'default': '0',
                         'description': "This one moves the weaponbar's "
                                        'vertical position. Negative numbers '
                                        'move it upwards, positive ones '
                                        'downwards. 0 leaves it at moddefault '
                                        'place. See cg_weaponBarStyle too!',
                         'name': 'cg_weaponBarOffsetY'},
 'cg_weaponBarStyle': {'default': '0',
                       'description': 'Weapon bar style. Default is 0 which '
                                      'means style 6. It is a horizontal '
                                      'weaponbar at the bottom. Change to 5 '
                                      'for slightly bigger numbers if you have '
                                      'small screen! You can move the bar '
                                      'vertically. (see cg_weaponBarOffsetY)!\n'
                                      '    3 is a vertical bar on the left '
                                      'side of the screen, might consider that '
                                      'one too. 1 is pimped 081baseoa (you can '
                                      'see the ammo left). Valid values are '
                                      '0-6. Out of range values hide the bar.',
                       'name': 'cg_weaponBarStyle'},
 'cg_weaponBobbing': {'default': '1',
                      'description': 'If it is set to 1 (the default OA and '
                                     'mod behaviour) your weapons will swing '
                                     'and sway and bob in the bottom of your '
                                     'screen like MUH DICK. Now some people '
                                     "don't like being reminded to muh "
                                     'swinging dick on their screen\n'
                                     '    while playing so they prefer '
                                     'disabling it with 0. (You can completely '
                                     'disable the gun with /cg_drawGun a '
                                     'baseoa setting)\n'
                                     "    (Exuce me, i'm being tired writing "
                                     'all this list for this mod of a dead '
                                     'game no one will read.)',
                      'name': 'cg_weaponBobbing'},
 'cg_zoomTime': {'default': '0, means 100ms',
                 'description': 'The time the animation takes to switch from '
                                'normal fov (cg_fov) to zoomfov (cg_zoomfov) '
                                'in milliseconds when pressing the zoom '
                                '+button\n'
                                '    Old 081 baseoa setting is 150 ms\n'
                                '    Use small values for immediate zoom '
                                'without distracting animation.',
                 'name': 'cg_zoomTime'},
 'fm_chatBeep': {'default': '0',
                 'description': 'Changes the chat notifier sound. 0 is mod '
                                "default, the same sound as baseoa's beep but "
                                'not that loud. The old baseoa beep is 9. I '
                                "recommend 2, because i don't like baseoa "
                                'beep, annoying. 11 is also baseoa but even '
                                'more silent.\n'
                                '    Selectable Values are from 0 to 12. -1 is '
                                'no beep as usual in the mod.',
                 'name': 'fm_chatBeep'},
 'fm_chatFontSize': {'default': '0',
                     'description': 'Change the font size of chat with this '
                                    'setting! If you leave it at 0 it results '
                                    'in about a default font size of 9.',
                     'name': 'fm_chatFontSize'},
 'fm_chatTime': {'default': '0',
                 'description': 'The display time for each chat msgs in '
                                'milliseconds. Mod default is 0, it is a '
                                'special value, means 12000ms. Very Small or '
                                'negative values are hiding the chat!',
                 'name': 'fm_chatTime'},
 'fm_consoleFontSize': {'default': '0',
                        'description': 'Console font size.',
                        'name': 'fm_consoleFontSize'},
 'fm_consoleTime': {'default': '0 = 5000',
                    'description': 'Console msgs are displayed for [value] '
                                   'milliseconds. If you leave it at 0 it will '
                                   'result console msgs shown for 5 seconds. '
                                   'Use negative value to disable the console.',
                    'name': 'fm_consoleTime'},
 'fm_dropTime': {'default': '0 = 1.6sec',
                 'description': 'The display time of that little '
                                'flagdrop-notification text in milliseconds. '
                                "Use a negative value if you don't like it.",
                 'name': 'fm_dropTime'},
 'fm_noAutoJoin': {'default': '0',
                   'description': 'Even if the server has g_teamAutoJoin '
                                  'enabled - it does sometimes at stupid - you '
                                  "won't autojoin upon connecting. You will "
                                  'join spec. but only if you have the mod '
                                  'loaded already (ie: coming from '
                                  'another          \n'
                                  ':F server in same mod folder)',
                   'name': 'fm_noAutoJoin'},
 'fm_teamChatBeep': {'default': '3',
                     'description': 'Changes the teamchat notifier sound. See '
                                    'fm_chatBeep for available sounds.',
                     'name': 'fm_teamChatBeep'},
 'fm_teamChatFontSize': {'default': '0',
                         'description': 'Font size of team chat. see '
                                        'fm_chatFontSize',
                         'name': 'fm_teamChatFontSize'},
 'fm_voteBeep': {'default': '6',
                 'description': 'You hear this sound when someone votes. See '
                                'fm_chatBeep for available sounds. Leave it as '
                                'default, it is a nice little coin sound. '
                                'Baseoa uses the same ones for chat and votes '
                                '- the horrible votespams,\n'
                                '    if you remember. Votespams are a minor '
                                'annoyance with 6.',
                 'name': 'fm_voteBeep'},
 'hud_ammog': {'default': None,
               'description': 'Cvars to customize the statusbar elements. x y '
                              'are coords, w and h are font widths and font '
                              'heights, g is gap between numbers, i refers to '
                              'icon, s stands for size.\n'
                              'The hp, armor, ammo, the flag (in the hud when '
                              'you have it) and the icons can be moved and '
                              'resized with these. Upper left corner is at '
                              'x=0, y=0; Bottom right corner is at x=640, '
                              'y=480 irrespectively of actual screen '
                              "resolution!Don't forget to save the values in "
                              'your autoexec.cfg or use /seta cvarname value '
                              'followed by /writeconfig q3config.cfg!\n'
                              'Tip: start OA from command line, type hud_TAB, '
                              'the autocompleted hud_ cvars will appear in '
                              'your terminal, copypaste the values from there '
                              '(after removing the equal signs and adding '
                              "'set' in front of them ofc)!\n"
                              '\n'
                              "It is advisable to disable your model's head "
                              "with cg_statusBarStyle as you can't move it!\n"
                              '\n'
                              'You can try some preconfigured statusbars:\n'
                              '/exec hud1 - Start from this one if you played '
                              'too much AS!\n'
                              '/exec hud2\n'
                              '/exec hud3\n'
                              '/exec hud4\n'
                              '/exec hud5\n'
                              '/exec hud6 - Start from this if you prefer how '
                              'cute and unobtrusive this one is!\n'
                              '/exec huddefault - To revert back to defaults.\n'
                              '\n'
                              'Tip: You can use one of the preconfigureds as a '
                              "skeleton and modify only the settings you don't "
                              'like!\n'
                              '\n'
                              'Note: Pick a custom value for cg_statusBarStyle '
                              'if you want to configure the statusbar in '
                              'instantgib! Default 0 will draw the default '
                              'insta statusbar!\n'
                              '\n'
                              'Ps: If you managed to set up a cool looking and '
                              'useful statusbar please send me the respective '
                              'cvars to make it available for everyone with a '
                              '/exec yourstatusbarname.cfg in next update! '
                              'Paste the cvars here!',
               'name': 'hud_ammog'},
 'hud_ammoh': {'default': None,
               'description': 'Cvars to customize the statusbar elements. x y '
                              'are coords, w and h are font widths and font '
                              'heights, g is gap between numbers, i refers to '
                              'icon, s stands for size.\n'
                              'The hp, armor, ammo, the flag (in the hud when '
                              'you have it) and the icons can be moved and '
                              'resized with these. Upper left corner is at '
                              'x=0, y=0; Bottom right corner is at x=640, '
                              'y=480 irrespectively of actual screen '
                              "resolution!Don't forget to save the values in "
                              'your autoexec.cfg or use /seta cvarname value '
                              'followed by /writeconfig q3config.cfg!\n'
                              'Tip: start OA from command line, type hud_TAB, '
                              'the autocompleted hud_ cvars will appear in '
                              'your terminal, copypaste the values from there '
                              '(after removing the equal signs and adding '
                              "'set' in front of them ofc)!\n"
                              '\n'
                              "It is advisable to disable your model's head "
                              "with cg_statusBarStyle as you can't move it!\n"
                              '\n'
                              'You can try some preconfigured statusbars:\n'
                              '/exec hud1 - Start from this one if you played '
                              'too much AS!\n'
                              '/exec hud2\n'
                              '/exec hud3\n'
                              '/exec hud4\n'
                              '/exec hud5\n'
                              '/exec hud6 - Start from this if you prefer how '
                              'cute and unobtrusive this one is!\n'
                              '/exec huddefault - To revert back to defaults.\n'
                              '\n'
                              'Tip: You can use one of the preconfigureds as a '
                              "skeleton and modify only the settings you don't "
                              'like!\n'
                              '\n'
                              'Note: Pick a custom value for cg_statusBarStyle '
                              'if you want to configure the statusbar in '
                              'instantgib! Default 0 will draw the default '
                              'insta statusbar!\n'
                              '\n'
                              'Ps: If you managed to set up a cool looking and '
                              'useful statusbar please send me the respective '
                              'cvars to make it available for everyone with a '
                              '/exec yourstatusbarname.cfg in next update! '
                              'Paste the cvars here!',
               'name': 'hud_ammoh'},
 'hud_ammois': {'default': None,
                'description': 'Cvars to customize the statusbar elements. x y '
                               'are coords, w and h are font widths and font '
                               'heights, g is gap between numbers, i refers to '
                               'icon, s stands for size.\n'
                               'The hp, armor, ammo, the flag (in the hud when '
                               'you have it) and the icons can be moved and '
                               'resized with these. Upper left corner is at '
                               'x=0, y=0; Bottom right corner is at x=640, '
                               'y=480 irrespectively of actual screen '
                               "resolution!Don't forget to save the values in "
                               'your autoexec.cfg or use /seta cvarname value '
                               'followed by /writeconfig q3config.cfg!\n'
                               'Tip: start OA from command line, type hud_TAB, '
                               'the autocompleted hud_ cvars will appear in '
                               'your terminal, copypaste the values from there '
                               '(after removing the equal signs and adding '
                               "'set' in front of them ofc)!\n"
                               '\n'
                               "It is advisable to disable your model's head "
                               "with cg_statusBarStyle as you can't move it!\n"
                               '\n'
                               'You can try some preconfigured statusbars:\n'
                               '/exec hud1 - Start from this one if you played '
                               'too much AS!\n'
                               '/exec hud2\n'
                               '/exec hud3\n'
                               '/exec hud4\n'
                               '/exec hud5\n'
                               '/exec hud6 - Start from this if you prefer how '
                               'cute and unobtrusive this one is!\n'
                               '/exec huddefault - To revert back to '
                               'defaults.\n'
                               '\n'
                               'Tip: You can use one of the preconfigureds as '
                               'a skeleton and modify only the settings you '
                               "don't like!\n"
                               '\n'
                               'Note: Pick a custom value for '
                               'cg_statusBarStyle if you want to configure the '
                               'statusbar in instantgib! Default 0 will draw '
                               'the default insta statusbar!\n'
                               '\n'
                               'Ps: If you managed to set up a cool looking '
                               'and useful statusbar please send me the '
                               'respective cvars to make it available for '
                               'everyone with a /exec yourstatusbarname.cfg in '
                               'next update! Paste the cvars here!',
                'name': 'hud_ammois'},
 'hud_ammoix': {'default': None,
                'description': 'Cvars to customize the statusbar elements. x y '
                               'are coords, w and h are font widths and font '
                               'heights, g is gap between numbers, i refers to '
                               'icon, s stands for size.\n'
                               'The hp, armor, ammo, the flag (in the hud when '
                               'you have it) and the icons can be moved and '
                               'resized with these. Upper left corner is at '
                               'x=0, y=0; Bottom right corner is at x=640, '
                               'y=480 irrespectively of actual screen '
                               "resolution!Don't forget to save the values in "
                               'your autoexec.cfg or use /seta cvarname value '
                               'followed by /writeconfig q3config.cfg!\n'
                               'Tip: start OA from command line, type hud_TAB, '
                               'the autocompleted hud_ cvars will appear in '
                               'your terminal, copypaste the values from there '
                               '(after removing the equal signs and adding '
                               "'set' in front of them ofc)!\n"
                               '\n'
                               "It is advisable to disable your model's head "
                               "with cg_statusBarStyle as you can't move it!\n"
                               '\n'
                               'You can try some preconfigured statusbars:\n'
                               '/exec hud1 - Start from this one if you played '
                               'too much AS!\n'
                               '/exec hud2\n'
                               '/exec hud3\n'
                               '/exec hud4\n'
                               '/exec hud5\n'
                               '/exec hud6 - Start from this if you prefer how '
                               'cute and unobtrusive this one is!\n'
                               '/exec huddefault - To revert back to '
                               'defaults.\n'
                               '\n'
                               'Tip: You can use one of the preconfigureds as '
                               'a skeleton and modify only the settings you '
                               "don't like!\n"
                               '\n'
                               'Note: Pick a custom value for '
                               'cg_statusBarStyle if you want to configure the '
                               'statusbar in instantgib! Default 0 will draw '
                               'the default insta statusbar!\n'
                               '\n'
                               'Ps: If you managed to set up a cool looking '
                               'and useful statusbar please send me the '
                               'respective cvars to make it available for '
                               'everyone with a /exec yourstatusbarname.cfg in '
                               'next update! Paste the cvars here!',
                'name': 'hud_ammoix'},
 'hud_ammoiy': {'default': None,
                'description': 'Cvars to customize the statusbar elements. x y '
                               'are coords, w and h are font widths and font '
                               'heights, g is gap between numbers, i refers to '
                               'icon, s stands for size.\n'
                               'The hp, armor, ammo, the flag (in the hud when '
                               'you have it) and the icons can be moved and '
                               'resized with these. Upper left corner is at '
                               'x=0, y=0; Bottom right corner is at x=640, '
                               'y=480 irrespectively of actual screen '
                               "resolution!Don't forget to save the values in "
                               'your autoexec.cfg or use /seta cvarname value '
                               'followed by /writeconfig q3config.cfg!\n'
                               'Tip: start OA from command line, type hud_TAB, '
                               'the autocompleted hud_ cvars will appear in '
                               'your terminal, copypaste the values from there '
                               '(after removing the equal signs and adding '
                               "'set' in front of them ofc)!\n"
                               '\n'
                               "It is advisable to disable your model's head "
                               "with cg_statusBarStyle as you can't move it!\n"
                               '\n'
                               'You can try some preconfigured statusbars:\n'
                               '/exec hud1 - Start from this one if you played '
                               'too much AS!\n'
                               '/exec hud2\n'
                               '/exec hud3\n'
                               '/exec hud4\n'
                               '/exec hud5\n'
                               '/exec hud6 - Start from this if you prefer how '
                               'cute and unobtrusive this one is!\n'
                               '/exec huddefault - To revert back to '
                               'defaults.\n'
                               '\n'
                               'Tip: You can use one of the preconfigureds as '
                               'a skeleton and modify only the settings you '
                               "don't like!\n"
                               '\n'
                               'Note: Pick a custom value for '
                               'cg_statusBarStyle if you want to configure the '
                               'statusbar in instantgib! Default 0 will draw '
                               'the default insta statusbar!\n'
                               '\n'
                               'Ps: If you managed to set up a cool looking '
                               'and useful statusbar please send me the '
                               'respective cvars to make it available for '
                               'everyone with a /exec yourstatusbarname.cfg in '
                               'next update! Paste the cvars here!',
                'name': 'hud_ammoiy'},
 'hud_ammow': {'default': None,
               'description': 'Cvars to customize the statusbar elements. x y '
                              'are coords, w and h are font widths and font '
                              'heights, g is gap between numbers, i refers to '
                              'icon, s stands for size.\n'
                              'The hp, armor, ammo, the flag (in the hud when '
                              'you have it) and the icons can be moved and '
                              'resized with these. Upper left corner is at '
                              'x=0, y=0; Bottom right corner is at x=640, '
                              'y=480 irrespectively of actual screen '
                              "resolution!Don't forget to save the values in "
                              'your autoexec.cfg or use /seta cvarname value '
                              'followed by /writeconfig q3config.cfg!\n'
                              'Tip: start OA from command line, type hud_TAB, '
                              'the autocompleted hud_ cvars will appear in '
                              'your terminal, copypaste the values from there '
                              '(after removing the equal signs and adding '
                              "'set' in front of them ofc)!\n"
                              '\n'
                              "It is advisable to disable your model's head "
                              "with cg_statusBarStyle as you can't move it!\n"
                              '\n'
                              'You can try some preconfigured statusbars:\n'
                              '/exec hud1 - Start from this one if you played '
                              'too much AS!\n'
                              '/exec hud2\n'
                              '/exec hud3\n'
                              '/exec hud4\n'
                              '/exec hud5\n'
                              '/exec hud6 - Start from this if you prefer how '
                              'cute and unobtrusive this one is!\n'
                              '/exec huddefault - To revert back to defaults.\n'
                              '\n'
                              'Tip: You can use one of the preconfigureds as a '
                              "skeleton and modify only the settings you don't "
                              'like!\n'
                              '\n'
                              'Note: Pick a custom value for cg_statusBarStyle '
                              'if you want to configure the statusbar in '
                              'instantgib! Default 0 will draw the default '
                              'insta statusbar!\n'
                              '\n'
                              'Ps: If you managed to set up a cool looking and '
                              'useful statusbar please send me the respective '
                              'cvars to make it available for everyone with a '
                              '/exec yourstatusbarname.cfg in next update! '
                              'Paste the cvars here!',
               'name': 'hud_ammow'},
 'hud_ammowarningy': {'default': '114',
                      'description': 'The place of "LOW AMMO WARNING" and "OUT '
                                     'OF AMMO" text on the oordinate.',
                      'name': 'hud_ammowarningy'},
 'hud_ammox': {'default': 'Start typing the cvarname and press [TAB] to see!',
               'description': 'Cvars to customize the statusbar elements. x y '
                              'are coords, w and h are font widths and font '
                              'heights, g is gap between numbers, i refers to '
                              'icon, s stands for size.\n'
                              'The hp, armor, ammo, the flag (in the hud when '
                              'you have it) and the icons can be moved and '
                              'resized with these. Upper left corner is at '
                              'x=0, y=0; Bottom right corner is at x=640, '
                              'y=480 irrespectively of actual screen '
                              "resolution!Don't forget to save the values in "
                              'your autoexec.cfg or use /seta cvarname value '
                              'followed by /writeconfig q3config.cfg!\n'
                              'Tip: start OA from command line, type hud_TAB, '
                              'the autocompleted hud_ cvars will appear in '
                              'your terminal, copypaste the values from there '
                              '(after removing the equal signs and adding '
                              "'set' in front of them ofc)!\n"
                              '\n'
                              "It is advisable to disable your model's head "
                              "with cg_statusBarStyle as you can't move it!\n"
                              '\n'
                              'You can try some preconfigured statusbars:\n'
                              '/exec hud1 - Start from this one if you played '
                              'too much AS!\n'
                              '/exec hud2\n'
                              '/exec hud3\n'
                              '/exec hud4\n'
                              '/exec hud5\n'
                              '/exec hud6 - Start from this if you prefer how '
                              'cute and unobtrusive this one is!\n'
                              '/exec huddefault - To revert back to defaults.\n'
                              '\n'
                              'Tip: You can use one of the preconfigureds as a '
                              "skeleton and modify only the settings you don't "
                              'like!\n'
                              '\n'
                              'Note: Pick a custom value for cg_statusBarStyle '
                              'if you want to configure the statusbar in '
                              'instantgib! Default 0 will draw the default '
                              'insta statusbar!\n'
                              '\n'
                              'Ps: If you managed to set up a cool looking and '
                              'useful statusbar please send me the respective '
                              'cvars to make it available for everyone with a '
                              '/exec yourstatusbarname.cfg in next update! '
                              'Paste the cvars here!',
               'name': 'hud_ammox'},
 'hud_ammoy': {'default': None,
               'description': 'Cvars to customize the statusbar elements. x y '
                              'are coords, w and h are font widths and font '
                              'heights, g is gap between numbers, i refers to '
                              'icon, s stands for size.\n'
                              'The hp, armor, ammo, the flag (in the hud when '
                              'you have it) and the icons can be moved and '
                              'resized with these. Upper left corner is at '
                              'x=0, y=0; Bottom right corner is at x=640, '
                              'y=480 irrespectively of actual screen '
                              "resolution!Don't forget to save the values in "
                              'your autoexec.cfg or use /seta cvarname value '
                              'followed by /writeconfig q3config.cfg!\n'
                              'Tip: start OA from command line, type hud_TAB, '
                              'the autocompleted hud_ cvars will appear in '
                              'your terminal, copypaste the values from there '
                              '(after removing the equal signs and adding '
                              "'set' in front of them ofc)!\n"
                              '\n'
                              "It is advisable to disable your model's head "
                              "with cg_statusBarStyle as you can't move it!\n"
                              '\n'
                              'You can try some preconfigured statusbars:\n'
                              '/exec hud1 - Start from this one if you played '
                              'too much AS!\n'
                              '/exec hud2\n'
                              '/exec hud3\n'
                              '/exec hud4\n'
                              '/exec hud5\n'
                              '/exec hud6 - Start from this if you prefer how '
                              'cute and unobtrusive this one is!\n'
                              '/exec huddefault - To revert back to defaults.\n'
                              '\n'
                              'Tip: You can use one of the preconfigureds as a '
                              "skeleton and modify only the settings you don't "
                              'like!\n'
                              '\n'
                              'Note: Pick a custom value for cg_statusBarStyle '
                              'if you want to configure the statusbar in '
                              'instantgib! Default 0 will draw the default '
                              'insta statusbar!\n'
                              '\n'
                              'Ps: If you managed to set up a cool looking and '
                              'useful statusbar please send me the respective '
                              'cvars to make it available for everyone with a '
                              '/exec yourstatusbarname.cfg in next update! '
                              'Paste the cvars here!',
               'name': 'hud_ammoy'},
 'hud_armorg': {'default': None,
                'description': 'Cvars to customize the statusbar elements. x y '
                               'are coords, w and h are font widths and font '
                               'heights, g is gap between numbers, i refers to '
                               'icon, s stands for size.\n'
                               'The hp, armor, ammo, the flag (in the hud when '
                               'you have it) and the icons can be moved and '
                               'resized with these. Upper left corner is at '
                               'x=0, y=0; Bottom right corner is at x=640, '
                               'y=480 irrespectively of actual screen '
                               "resolution!Don't forget to save the values in "
                               'your autoexec.cfg or use /seta cvarname value '
                               'followed by /writeconfig q3config.cfg!\n'
                               'Tip: start OA from command line, type hud_TAB, '
                               'the autocompleted hud_ cvars will appear in '
                               'your terminal, copypaste the values from there '
                               '(after removing the equal signs and adding '
                               "'set' in front of them ofc)!\n"
                               '\n'
                               "It is advisable to disable your model's head "
                               "with cg_statusBarStyle as you can't move it!\n"
                               '\n'
                               'You can try some preconfigured statusbars:\n'
                               '/exec hud1 - Start from this one if you played '
                               'too much AS!\n'
                               '/exec hud2\n'
                               '/exec hud3\n'
                               '/exec hud4\n'
                               '/exec hud5\n'
                               '/exec hud6 - Start from this if you prefer how '
                               'cute and unobtrusive this one is!\n'
                               '/exec huddefault - To revert back to '
                               'defaults.\n'
                               '\n'
                               'Tip: You can use one of the preconfigureds as '
                               'a skeleton and modify only the settings you '
                               "don't like!\n"
                               '\n'
                               'Note: Pick a custom value for '
                               'cg_statusBarStyle if you want to configure the '
                               'statusbar in instantgib! Default 0 will draw '
                               'the default insta statusbar!\n'
                               '\n'
                               'Ps: If you managed to set up a cool looking '
                               'and useful statusbar please send me the '
                               'respective cvars to make it available for '
                               'everyone with a /exec yourstatusbarname.cfg in '
                               'next update! Paste the cvars here!',
                'name': 'hud_armorg'},
 'hud_armorh': {'default': None,
                'description': 'Cvars to customize the statusbar elements. x y '
                               'are coords, w and h are font widths and font '
                               'heights, g is gap between numbers, i refers to '
                               'icon, s stands for size.\n'
                               'The hp, armor, ammo, the flag (in the hud when '
                               'you have it) and the icons can be moved and '
                               'resized with these. Upper left corner is at '
                               'x=0, y=0; Bottom right corner is at x=640, '
                               'y=480 irrespectively of actual screen '
                               "resolution!Don't forget to save the values in "
                               'your autoexec.cfg or use /seta cvarname value '
                               'followed by /writeconfig q3config.cfg!\n'
                               'Tip: start OA from command line, type hud_TAB, '
                               'the autocompleted hud_ cvars will appear in '
                               'your terminal, copypaste the values from there '
                               '(after removing the equal signs and adding '
                               "'set' in front of them ofc)!\n"
                               '\n'
                               "It is advisable to disable your model's head "
                               "with cg_statusBarStyle as you can't move it!\n"
                               '\n'
                               'You can try some preconfigured statusbars:\n'
                               '/exec hud1 - Start from this one if you played '
                               'too much AS!\n'
                               '/exec hud2\n'
                               '/exec hud3\n'
                               '/exec hud4\n'
                               '/exec hud5\n'
                               '/exec hud6 - Start from this if you prefer how '
                               'cute and unobtrusive this one is!\n'
                               '/exec huddefault - To revert back to '
                               'defaults.\n'
                               '\n'
                               'Tip: You can use one of the preconfigureds as '
                               'a skeleton and modify only the settings you '
                               "don't like!\n"
                               '\n'
                               'Note: Pick a custom value for '
                               'cg_statusBarStyle if you want to configure the '
                               'statusbar in instantgib! Default 0 will draw '
                               'the default insta statusbar!\n'
                               '\n'
                               'Ps: If you managed to set up a cool looking '
                               'and useful statusbar please send me the '
                               'respective cvars to make it available for '
                               'everyone with a /exec yourstatusbarname.cfg in '
                               'next update! Paste the cvars here!',
                'name': 'hud_armorh'},
 'hud_armoris': {'default': None,
                 'description': 'Cvars to customize the statusbar elements. x '
                                'y are coords, w and h are font widths and '
                                'font heights, g is gap between numbers, i '
                                'refers to icon, s stands for size.\n'
                                'The hp, armor, ammo, the flag (in the hud '
                                'when you have it) and the icons can be moved '
                                'and resized with these. Upper left corner is '
                                'at x=0, y=0; Bottom right corner is at x=640, '
                                'y=480 irrespectively of actual screen '
                                "resolution!Don't forget to save the values in "
                                'your autoexec.cfg or use /seta cvarname value '
                                'followed by /writeconfig q3config.cfg!\n'
                                'Tip: start OA from command line, type '
                                'hud_TAB, the autocompleted hud_ cvars will '
                                'appear in your terminal, copypaste the values '
                                'from there (after removing the equal signs '
                                "and adding 'set' in front of them ofc)!\n"
                                '\n'
                                "It is advisable to disable your model's head "
                                "with cg_statusBarStyle as you can't move it!\n"
                                '\n'
                                'You can try some preconfigured statusbars:\n'
                                '/exec hud1 - Start from this one if you '
                                'played too much AS!\n'
                                '/exec hud2\n'
                                '/exec hud3\n'
                                '/exec hud4\n'
                                '/exec hud5\n'
                                '/exec hud6 - Start from this if you prefer '
                                'how cute and unobtrusive this one is!\n'
                                '/exec huddefault - To revert back to '
                                'defaults.\n'
                                '\n'
                                'Tip: You can use one of the preconfigureds as '
                                'a skeleton and modify only the settings you '
                                "don't like!\n"
                                '\n'
                                'Note: Pick a custom value for '
                                'cg_statusBarStyle if you want to configure '
                                'the statusbar in instantgib! Default 0 will '
                                'draw the default insta statusbar!\n'
                                '\n'
                                'Ps: If you managed to set up a cool looking '
                                'and useful statusbar please send me the '
                                'respective cvars to make it available for '
                                'everyone with a /exec yourstatusbarname.cfg '
                                'in next update! Paste the cvars here!',
                 'name': 'hud_armoris'},
 'hud_armorix': {'default': None,
                 'description': 'Cvars to customize the statusbar elements. x '
                                'y are coords, w and h are font widths and '
                                'font heights, g is gap between numbers, i '
                                'refers to icon, s stands for size.\n'
                                'The hp, armor, ammo, the flag (in the hud '
                                'when you have it) and the icons can be moved '
                                'and resized with these. Upper left corner is '
                                'at x=0, y=0; Bottom right corner is at x=640, '
                                'y=480 irrespectively of actual screen '
                                "resolution!Don't forget to save the values in "
                                'your autoexec.cfg or use /seta cvarname value '
                                'followed by /writeconfig q3config.cfg!\n'
                                'Tip: start OA from command line, type '
                                'hud_TAB, the autocompleted hud_ cvars will '
                                'appear in your terminal, copypaste the values '
                                'from there (after removing the equal signs '
                                "and adding 'set' in front of them ofc)!\n"
                                '\n'
                                "It is advisable to disable your model's head "
                                "with cg_statusBarStyle as you can't move it!\n"
                                '\n'
                                'You can try some preconfigured statusbars:\n'
                                '/exec hud1 - Start from this one if you '
                                'played too much AS!\n'
                                '/exec hud2\n'
                                '/exec hud3\n'
                                '/exec hud4\n'
                                '/exec hud5\n'
                                '/exec hud6 - Start from this if you prefer '
                                'how cute and unobtrusive this one is!\n'
                                '/exec huddefault - To revert back to '
                                'defaults.\n'
                                '\n'
                                'Tip: You can use one of the preconfigureds as '
                                'a skeleton and modify only the settings you '
                                "don't like!\n"
                                '\n'
                                'Note: Pick a custom value for '
                                'cg_statusBarStyle if you want to configure '
                                'the statusbar in instantgib! Default 0 will '
                                'draw the default insta statusbar!\n'
                                '\n'
                                'Ps: If you managed to set up a cool looking '
                                'and useful statusbar please send me the '
                                'respective cvars to make it available for '
                                'everyone with a /exec yourstatusbarname.cfg '
                                'in next update! Paste the cvars here!',
                 'name': 'hud_armorix'},
 'hud_armoriy': {'default': None,
                 'description': 'Cvars to customize the statusbar elements. x '
                                'y are coords, w and h are font widths and '
                                'font heights, g is gap between numbers, i '
                                'refers to icon, s stands for size.\n'
                                'The hp, armor, ammo, the flag (in the hud '
                                'when you have it) and the icons can be moved '
                                'and resized with these. Upper left corner is '
                                'at x=0, y=0; Bottom right corner is at x=640, '
                                'y=480 irrespectively of actual screen '
                                "resolution!Don't forget to save the values in "
                                'your autoexec.cfg or use /seta cvarname value '
                                'followed by /writeconfig q3config.cfg!\n'
                                'Tip: start OA from command line, type '
                                'hud_TAB, the autocompleted hud_ cvars will '
                                'appear in your terminal, copypaste the values '
                                'from there (after removing the equal signs '
                                "and adding 'set' in front of them ofc)!\n"
                                '\n'
                                "It is advisable to disable your model's head "
                                "with cg_statusBarStyle as you can't move it!\n"
                                '\n'
                                'You can try some preconfigured statusbars:\n'
                                '/exec hud1 - Start from this one if you '
                                'played too much AS!\n'
                                '/exec hud2\n'
                                '/exec hud3\n'
                                '/exec hud4\n'
                                '/exec hud5\n'
                                '/exec hud6 - Start from this if you prefer '
                                'how cute and unobtrusive this one is!\n'
                                '/exec huddefault - To revert back to '
                                'defaults.\n'
                                '\n'
                                'Tip: You can use one of the preconfigureds as '
                                'a skeleton and modify only the settings you '
                                "don't like!\n"
                                '\n'
                                'Note: Pick a custom value for '
                                'cg_statusBarStyle if you want to configure '
                                'the statusbar in instantgib! Default 0 will '
                                'draw the default insta statusbar!\n'
                                '\n'
                                'Ps: If you managed to set up a cool looking '
                                'and useful statusbar please send me the '
                                'respective cvars to make it available for '
                                'everyone with a /exec yourstatusbarname.cfg '
                                'in next update! Paste the cvars here!',
                 'name': 'hud_armoriy'},
 'hud_armorw': {'default': None,
                'description': 'Cvars to customize the statusbar elements. x y '
                               'are coords, w and h are font widths and font '
                               'heights, g is gap between numbers, i refers to '
                               'icon, s stands for size.\n'
                               'The hp, armor, ammo, the flag (in the hud when '
                               'you have it) and the icons can be moved and '
                               'resized with these. Upper left corner is at '
                               'x=0, y=0; Bottom right corner is at x=640, '
                               'y=480 irrespectively of actual screen '
                               "resolution!Don't forget to save the values in "
                               'your autoexec.cfg or use /seta cvarname value '
                               'followed by /writeconfig q3config.cfg!\n'
                               'Tip: start OA from command line, type hud_TAB, '
                               'the autocompleted hud_ cvars will appear in '
                               'your terminal, copypaste the values from there '
                               '(after removing the equal signs and adding '
                               "'set' in front of them ofc)!\n"
                               '\n'
                               "It is advisable to disable your model's head "
                               "with cg_statusBarStyle as you can't move it!\n"
                               '\n'
                               'You can try some preconfigured statusbars:\n'
                               '/exec hud1 - Start from this one if you played '
                               'too much AS!\n'
                               '/exec hud2\n'
                               '/exec hud3\n'
                               '/exec hud4\n'
                               '/exec hud5\n'
                               '/exec hud6 - Start from this if you prefer how '
                               'cute and unobtrusive this one is!\n'
                               '/exec huddefault - To revert back to '
                               'defaults.\n'
                               '\n'
                               'Tip: You can use one of the preconfigureds as '
                               'a skeleton and modify only the settings you '
                               "don't like!\n"
                               '\n'
                               'Note: Pick a custom value for '
                               'cg_statusBarStyle if you want to configure the '
                               'statusbar in instantgib! Default 0 will draw '
                               'the default insta statusbar!\n'
                               '\n'
                               'Ps: If you managed to set up a cool looking '
                               'and useful statusbar please send me the '
                               'respective cvars to make it available for '
                               'everyone with a /exec yourstatusbarname.cfg in '
                               'next update! Paste the cvars here!',
                'name': 'hud_armorw'},
 'hud_armorx': {'default': None,
                'description': 'Cvars to customize the statusbar elements. x y '
                               'are coords, w and h are font widths and font '
                               'heights, g is gap between numbers, i refers to '
                               'icon, s stands for size.\n'
                               'The hp, armor, ammo, the flag (in the hud when '
                               'you have it) and the icons can be moved and '
                               'resized with these. Upper left corner is at '
                               'x=0, y=0; Bottom right corner is at x=640, '
                               'y=480 irrespectively of actual screen '
                               "resolution!Don't forget to save the values in "
                               'your autoexec.cfg or use /seta cvarname value '
                               'followed by /writeconfig q3config.cfg!\n'
                               'Tip: start OA from command line, type hud_TAB, '
                               'the autocompleted hud_ cvars will appear in '
                               'your terminal, copypaste the values from there '
                               '(after removing the equal signs and adding '
                               "'set' in front of them ofc)!\n"
                               '\n'
                               "It is advisable to disable your model's head "
                               "with cg_statusBarStyle as you can't move it!\n"
                               '\n'
                               'You can try some preconfigured statusbars:\n'
                               '/exec hud1 - Start from this one if you played '
                               'too much AS!\n'
                               '/exec hud2\n'
                               '/exec hud3\n'
                               '/exec hud4\n'
                               '/exec hud5\n'
                               '/exec hud6 - Start from this if you prefer how '
                               'cute and unobtrusive this one is!\n'
                               '/exec huddefault - To revert back to '
                               'defaults.\n'
                               '\n'
                               'Tip: You can use one of the preconfigureds as '
                               'a skeleton and modify only the settings you '
                               "don't like!\n"
                               '\n'
                               'Note: Pick a custom value for '
                               'cg_statusBarStyle if you want to configure the '
                               'statusbar in instantgib! Default 0 will draw '
                               'the default insta statusbar!\n'
                               '\n'
                               'Ps: If you managed to set up a cool looking '
                               'and useful statusbar please send me the '
                               'respective cvars to make it available for '
                               'everyone with a /exec yourstatusbarname.cfg in '
                               'next update! Paste the cvars here!',
                'name': 'hud_armorx'},
 'hud_armory': {'default': None,
                'description': 'Cvars to customize the statusbar elements. x y '
                               'are coords, w and h are font widths and font '
                               'heights, g is gap between numbers, i refers to '
                               'icon, s stands for size.\n'
                               'The hp, armor, ammo, the flag (in the hud when '
                               'you have it) and the icons can be moved and '
                               'resized with these. Upper left corner is at '
                               'x=0, y=0; Bottom right corner is at x=640, '
                               'y=480 irrespectively of actual screen '
                               "resolution!Don't forget to save the values in "
                               'your autoexec.cfg or use /seta cvarname value '
                               'followed by /writeconfig q3config.cfg!\n'
                               'Tip: start OA from command line, type hud_TAB, '
                               'the autocompleted hud_ cvars will appear in '
                               'your terminal, copypaste the values from there '
                               '(after removing the equal signs and adding '
                               "'set' in front of them ofc)!\n"
                               '\n'
                               "It is advisable to disable your model's head "
                               "with cg_statusBarStyle as you can't move it!\n"
                               '\n'
                               'You can try some preconfigured statusbars:\n'
                               '/exec hud1 - Start from this one if you played '
                               'too much AS!\n'
                               '/exec hud2\n'
                               '/exec hud3\n'
                               '/exec hud4\n'
                               '/exec hud5\n'
                               '/exec hud6 - Start from this if you prefer how '
                               'cute and unobtrusive this one is!\n'
                               '/exec huddefault - To revert back to '
                               'defaults.\n'
                               '\n'
                               'Tip: You can use one of the preconfigureds as '
                               'a skeleton and modify only the settings you '
                               "don't like!\n"
                               '\n'
                               'Note: Pick a custom value for '
                               'cg_statusBarStyle if you want to configure the '
                               'statusbar in instantgib! Default 0 will draw '
                               'the default insta statusbar!\n'
                               '\n'
                               'Ps: If you managed to set up a cool looking '
                               'and useful statusbar please send me the '
                               'respective cvars to make it available for '
                               'everyone with a /exec yourstatusbarname.cfg in '
                               'next update! Paste the cvars here!',
                'name': 'hud_armory'},
 'hud_clockbg': {'default': '0xEEEEEE33',
                 'description': 'Cvars to customize the clock. x y are coords, '
                                'w and h are font width and height, fg is '
                                'foreground color (text color) and bg is '
                                'background color. Format for the latter two '
                                'is 0xRRGGBBAA in hex. AA means alpha, the '
                                'opaqueness of the element (text or '
                                'background).\n'
                                'Note: you have to set /cg_drawTimer 2 to '
                                'enable the Big White Clock cvars!\n'
                                "Don't forget to use /seta and /writeconfig "
                                'q3config.cfg!\n'
                                '\n'
                                'A clock example: \n'
                                '\n'
                                '\n'
                                'Another clock: \n'
                                '\n'
                                '\n'
                                'The respective hud vars:\n'
                                '\n'
                                'set    hud_clockbg  "0x2299ff4b"\n'
                                'set    hud_clockfg  "0xffffffff"\n'
                                'set    hud_clocky   "400"\n'
                                'set    hud_clockx   "270"\n'
                                'set    hud_clockh   "28"\n'
                                'set    hud_clockw   "24"',
                 'name': 'hud_clockbg'},
 'hud_clockfg': {'default': '0xFFFFDDEE',
                 'description': 'Cvars to customize the clock. x y are coords, '
                                'w and h are font width and height, fg is '
                                'foreground color (text color) and bg is '
                                'background color. Format for the latter two '
                                'is 0xRRGGBBAA in hex. AA means alpha, the '
                                'opaqueness of the element (text or '
                                'background).\n'
                                'Note: you have to set /cg_drawTimer 2 to '
                                'enable the Big White Clock cvars!\n'
                                "Don't forget to use /seta and /writeconfig "
                                'q3config.cfg!\n'
                                '\n'
                                'A clock example: \n'
                                '\n'
                                '\n'
                                'Another clock: \n'
                                '\n'
                                '\n'
                                'The respective hud vars:\n'
                                '\n'
                                'set    hud_clockbg  "0x2299ff4b"\n'
                                'set    hud_clockfg  "0xffffffff"\n'
                                'set    hud_clocky   "400"\n'
                                'set    hud_clockx   "270"\n'
                                'set    hud_clockh   "28"\n'
                                'set    hud_clockw   "24"',
                 'name': 'hud_clockfg'},
 'hud_clockh': {'default': '22',
                'description': 'Cvars to customize the clock. x y are coords, '
                               'w and h are font width and height, fg is '
                               'foreground color (text color) and bg is '
                               'background color. Format for the latter two is '
                               '0xRRGGBBAA in hex. AA means alpha, the '
                               'opaqueness of the element (text or '
                               'background).\n'
                               'Note: you have to set /cg_drawTimer 2 to '
                               'enable the Big White Clock cvars!\n'
                               "Don't forget to use /seta and /writeconfig "
                               'q3config.cfg!\n'
                               '\n'
                               'A clock example: \n'
                               '\n'
                               '\n'
                               'Another clock: \n'
                               '\n'
                               '\n'
                               'The respective hud vars:\n'
                               '\n'
                               'set    hud_clockbg  "0x2299ff4b"\n'
                               'set    hud_clockfg  "0xffffffff"\n'
                               'set    hud_clocky   "400"\n'
                               'set    hud_clockx   "270"\n'
                               'set    hud_clockh   "28"\n'
                               'set    hud_clockw   "24"',
                'name': 'hud_clockh'},
 'hud_clockw': {'default': '22',
                'description': 'Cvars to customize the clock. x y are coords, '
                               'w and h are font width and height, fg is '
                               'foreground color (text color) and bg is '
                               'background color. Format for the latter two is '
                               '0xRRGGBBAA in hex. AA means alpha, the '
                               'opaqueness of the element (text or '
                               'background).\n'
                               'Note: you have to set /cg_drawTimer 2 to '
                               'enable the Big White Clock cvars!\n'
                               "Don't forget to use /seta and /writeconfig "
                               'q3config.cfg!\n'
                               '\n'
                               'A clock example: \n'
                               '\n'
                               '\n'
                               'Another clock: \n'
                               '\n'
                               '\n'
                               'The respective hud vars:\n'
                               '\n'
                               'set    hud_clockbg  "0x2299ff4b"\n'
                               'set    hud_clockfg  "0xffffffff"\n'
                               'set    hud_clocky   "400"\n'
                               'set    hud_clockx   "270"\n'
                               'set    hud_clockh   "28"\n'
                               'set    hud_clockw   "24"',
                'name': 'hud_clockw'},
 'hud_clockx': {'default': '273',
                'description': 'Cvars to customize the clock. x y are coords, '
                               'w and h are font width and height, fg is '
                               'foreground color (text color) and bg is '
                               'background color. Format for the latter two is '
                               '0xRRGGBBAA in hex. AA means alpha, the '
                               'opaqueness of the element (text or '
                               'background).\n'
                               'Note: you have to set /cg_drawTimer 2 to '
                               'enable the Big White Clock cvars!\n'
                               "Don't forget to use /seta and /writeconfig "
                               'q3config.cfg!\n'
                               '\n'
                               'A clock example: \n'
                               '\n'
                               '\n'
                               'Another clock: \n'
                               '\n'
                               '\n'
                               'The respective hud vars:\n'
                               '\n'
                               'set    hud_clockbg  "0x2299ff4b"\n'
                               'set    hud_clockfg  "0xffffffff"\n'
                               'set    hud_clocky   "400"\n'
                               'set    hud_clockx   "270"\n'
                               'set    hud_clockh   "28"\n'
                               'set    hud_clockw   "24"',
                'name': 'hud_clockx'},
 'hud_clocky': {'default': '100',
                'description': 'Cvars to customize the clock. x y are coords, '
                               'w and h are font width and height, fg is '
                               'foreground color (text color) and bg is '
                               'background color. Format for the latter two is '
                               '0xRRGGBBAA in hex. AA means alpha, the '
                               'opaqueness of the element (text or '
                               'background).\n'
                               'Note: you have to set /cg_drawTimer 2 to '
                               'enable the Big White Clock cvars!\n'
                               "Don't forget to use /seta and /writeconfig "
                               'q3config.cfg!\n'
                               '\n'
                               'A clock example: \n'
                               '\n'
                               '\n'
                               'Another clock: \n'
                               '\n'
                               '\n'
                               'The respective hud vars:\n'
                               '\n'
                               'set    hud_clockbg  "0x2299ff4b"\n'
                               'set    hud_clockfg  "0xffffffff"\n'
                               'set    hud_clocky   "400"\n'
                               'set    hud_clockx   "270"\n'
                               'set    hud_clockh   "28"\n'
                               'set    hud_clockw   "24"',
                'name': 'hud_clocky'},
 'hud_flagis': {'default': None,
                'description': 'Cvars to customize the statusbar elements. x y '
                               'are coords, w and h are font widths and font '
                               'heights, g is gap between numbers, i refers to '
                               'icon, s stands for size.\n'
                               'The hp, armor, ammo, the flag (in the hud when '
                               'you have it) and the icons can be moved and '
                               'resized with these. Upper left corner is at '
                               'x=0, y=0; Bottom right corner is at x=640, '
                               'y=480 irrespectively of actual screen '
                               "resolution!Don't forget to save the values in "
                               'your autoexec.cfg or use /seta cvarname value '
                               'followed by /writeconfig q3config.cfg!\n'
                               'Tip: start OA from command line, type hud_TAB, '
                               'the autocompleted hud_ cvars will appear in '
                               'your terminal, copypaste the values from there '
                               '(after removing the equal signs and adding '
                               "'set' in front of them ofc)!\n"
                               '\n'
                               "It is advisable to disable your model's head "
                               "with cg_statusBarStyle as you can't move it!\n"
                               '\n'
                               'You can try some preconfigured statusbars:\n'
                               '/exec hud1 - Start from this one if you played '
                               'too much AS!\n'
                               '/exec hud2\n'
                               '/exec hud3\n'
                               '/exec hud4\n'
                               '/exec hud5\n'
                               '/exec hud6 - Start from this if you prefer how '
                               'cute and unobtrusive this one is!\n'
                               '/exec huddefault - To revert back to '
                               'defaults.\n'
                               '\n'
                               'Tip: You can use one of the preconfigureds as '
                               'a skeleton and modify only the settings you '
                               "don't like!\n"
                               '\n'
                               'Note: Pick a custom value for '
                               'cg_statusBarStyle if you want to configure the '
                               'statusbar in instantgib! Default 0 will draw '
                               'the default insta statusbar!\n'
                               '\n'
                               'Ps: If you managed to set up a cool looking '
                               'and useful statusbar please send me the '
                               'respective cvars to make it available for '
                               'everyone with a /exec yourstatusbarname.cfg in '
                               'next update! Paste the cvars here!',
                'name': 'hud_flagis'},
 'hud_flagx': {'default': None,
               'description': 'Cvars to customize the statusbar elements. x y '
                              'are coords, w and h are font widths and font '
                              'heights, g is gap between numbers, i refers to '
                              'icon, s stands for size.\n'
                              'The hp, armor, ammo, the flag (in the hud when '
                              'you have it) and the icons can be moved and '
                              'resized with these. Upper left corner is at '
                              'x=0, y=0; Bottom right corner is at x=640, '
                              'y=480 irrespectively of actual screen '
                              "resolution!Don't forget to save the values in "
                              'your autoexec.cfg or use /seta cvarname value '
                              'followed by /writeconfig q3config.cfg!\n'
                              'Tip: start OA from command line, type hud_TAB, '
                              'the autocompleted hud_ cvars will appear in '
                              'your terminal, copypaste the values from there '
                              '(after removing the equal signs and adding '
                              "'set' in front of them ofc)!\n"
                              '\n'
                              "It is advisable to disable your model's head "
                              "with cg_statusBarStyle as you can't move it!\n"
                              '\n'
                              'You can try some preconfigured statusbars:\n'
                              '/exec hud1 - Start from this one if you played '
                              'too much AS!\n'
                              '/exec hud2\n'
                              '/exec hud3\n'
                              '/exec hud4\n'
                              '/exec hud5\n'
                              '/exec hud6 - Start from this if you prefer how '
                              'cute and unobtrusive this one is!\n'
                              '/exec huddefault - To revert back to defaults.\n'
                              '\n'
                              'Tip: You can use one of the preconfigureds as a '
                              "skeleton and modify only the settings you don't "
                              'like!\n'
                              '\n'
                              'Note: Pick a custom value for cg_statusBarStyle '
                              'if you want to configure the statusbar in '
                              'instantgib! Default 0 will draw the default '
                              'insta statusbar!\n'
                              '\n'
                              'Ps: If you managed to set up a cool looking and '
                              'useful statusbar please send me the respective '
                              'cvars to make it available for everyone with a '
                              '/exec yourstatusbarname.cfg in next update! '
                              'Paste the cvars here!',
               'name': 'hud_flagx'},
 'hud_flagy': {'default': None,
               'description': 'Cvars to customize the statusbar elements. x y '
                              'are coords, w and h are font widths and font '
                              'heights, g is gap between numbers, i refers to '
                              'icon, s stands for size.\n'
                              'The hp, armor, ammo, the flag (in the hud when '
                              'you have it) and the icons can be moved and '
                              'resized with these. Upper left corner is at '
                              'x=0, y=0; Bottom right corner is at x=640, '
                              'y=480 irrespectively of actual screen '
                              "resolution!Don't forget to save the values in "
                              'your autoexec.cfg or use /seta cvarname value '
                              'followed by /writeconfig q3config.cfg!\n'
                              'Tip: start OA from command line, type hud_TAB, '
                              'the autocompleted hud_ cvars will appear in '
                              'your terminal, copypaste the values from there '
                              '(after removing the equal signs and adding '
                              "'set' in front of them ofc)!\n"
                              '\n'
                              "It is advisable to disable your model's head "
                              "with cg_statusBarStyle as you can't move it!\n"
                              '\n'
                              'You can try some preconfigured statusbars:\n'
                              '/exec hud1 - Start from this one if you played '
                              'too much AS!\n'
                              '/exec hud2\n'
                              '/exec hud3\n'
                              '/exec hud4\n'
                              '/exec hud5\n'
                              '/exec hud6 - Start from this if you prefer how '
                              'cute and unobtrusive this one is!\n'
                              '/exec huddefault - To revert back to defaults.\n'
                              '\n'
                              'Tip: You can use one of the preconfigureds as a '
                              "skeleton and modify only the settings you don't "
                              'like!\n'
                              '\n'
                              'Note: Pick a custom value for cg_statusBarStyle '
                              'if you want to configure the statusbar in '
                              'instantgib! Default 0 will draw the default '
                              'insta statusbar!\n'
                              '\n'
                              'Ps: If you managed to set up a cool looking and '
                              'useful statusbar please send me the respective '
                              'cvars to make it available for everyone with a '
                              '/exec yourstatusbarname.cfg in next update! '
                              'Paste the cvars here!',
               'name': 'hud_flagy'},
 'hud_hpg': {'default': None,
             'description': 'Cvars to customize the statusbar elements. x y '
                            'are coords, w and h are font widths and font '
                            'heights, g is gap between numbers, i refers to '
                            'icon, s stands for size.\n'
                            'The hp, armor, ammo, the flag (in the hud when '
                            'you have it) and the icons can be moved and '
                            'resized with these. Upper left corner is at x=0, '
                            'y=0; Bottom right corner is at x=640, y=480 '
                            "irrespectively of actual screen resolution!Don't "
                            'forget to save the values in your autoexec.cfg or '
                            'use /seta cvarname value followed by /writeconfig '
                            'q3config.cfg!\n'
                            'Tip: start OA from command line, type hud_TAB, '
                            'the autocompleted hud_ cvars will appear in your '
                            'terminal, copypaste the values from there (after '
                            "removing the equal signs and adding 'set' in "
                            'front of them ofc)!\n'
                            '\n'
                            "It is advisable to disable your model's head with "
                            "cg_statusBarStyle as you can't move it!\n"
                            '\n'
                            'You can try some preconfigured statusbars:\n'
                            '/exec hud1 - Start from this one if you played '
                            'too much AS!\n'
                            '/exec hud2\n'
                            '/exec hud3\n'
                            '/exec hud4\n'
                            '/exec hud5\n'
                            '/exec hud6 - Start from this if you prefer how '
                            'cute and unobtrusive this one is!\n'
                            '/exec huddefault - To revert back to defaults.\n'
                            '\n'
                            'Tip: You can use one of the preconfigureds as a '
                            "skeleton and modify only the settings you don't "
                            'like!\n'
                            '\n'
                            'Note: Pick a custom value for cg_statusBarStyle '
                            'if you want to configure the statusbar in '
                            'instantgib! Default 0 will draw the default insta '
                            'statusbar!\n'
                            '\n'
                            'Ps: If you managed to set up a cool looking and '
                            'useful statusbar please send me the respective '
                            'cvars to make it available for everyone with a '
                            '/exec yourstatusbarname.cfg in next update! Paste '
                            'the cvars here!',
             'name': 'hud_hpg'},
 'hud_hph': {'default': None,
             'description': 'Cvars to customize the statusbar elements. x y '
                            'are coords, w and h are font widths and font '
                            'heights, g is gap between numbers, i refers to '
                            'icon, s stands for size.\n'
                            'The hp, armor, ammo, the flag (in the hud when '
                            'you have it) and the icons can be moved and '
                            'resized with these. Upper left corner is at x=0, '
                            'y=0; Bottom right corner is at x=640, y=480 '
                            "irrespectively of actual screen resolution!Don't "
                            'forget to save the values in your autoexec.cfg or '
                            'use /seta cvarname value followed by /writeconfig '
                            'q3config.cfg!\n'
                            'Tip: start OA from command line, type hud_TAB, '
                            'the autocompleted hud_ cvars will appear in your '
                            'terminal, copypaste the values from there (after '
                            "removing the equal signs and adding 'set' in "
                            'front of them ofc)!\n'
                            '\n'
                            "It is advisable to disable your model's head with "
                            "cg_statusBarStyle as you can't move it!\n"
                            '\n'
                            'You can try some preconfigured statusbars:\n'
                            '/exec hud1 - Start from this one if you played '
                            'too much AS!\n'
                            '/exec hud2\n'
                            '/exec hud3\n'
                            '/exec hud4\n'
                            '/exec hud5\n'
                            '/exec hud6 - Start from this if you prefer how '
                            'cute and unobtrusive this one is!\n'
                            '/exec huddefault - To revert back to defaults.\n'
                            '\n'
                            'Tip: You can use one of the preconfigureds as a '
                            "skeleton and modify only the settings you don't "
                            'like!\n'
                            '\n'
                            'Note: Pick a custom value for cg_statusBarStyle '
                            'if you want to configure the statusbar in '
                            'instantgib! Default 0 will draw the default insta '
                            'statusbar!\n'
                            '\n'
                            'Ps: If you managed to set up a cool looking and '
                            'useful statusbar please send me the respective '
                            'cvars to make it available for everyone with a '
                            '/exec yourstatusbarname.cfg in next update! Paste '
                            'the cvars here!',
             'name': 'hud_hph'},
 'hud_hpix': {'default': None,
              'description': 'Cvars to customize the statusbar elements. x y '
                             'are coords, w and h are font widths and font '
                             'heights, g is gap between numbers, i refers to '
                             'icon, s stands for size.\n'
                             'The hp, armor, ammo, the flag (in the hud when '
                             'you have it) and the icons can be moved and '
                             'resized with these. Upper left corner is at x=0, '
                             'y=0; Bottom right corner is at x=640, y=480 '
                             "irrespectively of actual screen resolution!Don't "
                             'forget to save the values in your autoexec.cfg '
                             'or use /seta cvarname value followed by '
                             '/writeconfig q3config.cfg!\n'
                             'Tip: start OA from command line, type hud_TAB, '
                             'the autocompleted hud_ cvars will appear in your '
                             'terminal, copypaste the values from there (after '
                             "removing the equal signs and adding 'set' in "
                             'front of them ofc)!\n'
                             '\n'
                             "It is advisable to disable your model's head "
                             "with cg_statusBarStyle as you can't move it!\n"
                             '\n'
                             'You can try some preconfigured statusbars:\n'
                             '/exec hud1 - Start from this one if you played '
                             'too much AS!\n'
                             '/exec hud2\n'
                             '/exec hud3\n'
                             '/exec hud4\n'
                             '/exec hud5\n'
                             '/exec hud6 - Start from this if you prefer how '
                             'cute and unobtrusive this one is!\n'
                             '/exec huddefault - To revert back to defaults.\n'
                             '\n'
                             'Tip: You can use one of the preconfigureds as a '
                             "skeleton and modify only the settings you don't "
                             'like!\n'
                             '\n'
                             'Note: Pick a custom value for cg_statusBarStyle '
                             'if you want to configure the statusbar in '
                             'instantgib! Default 0 will draw the default '
                             'insta statusbar!\n'
                             '\n'
                             'Ps: If you managed to set up a cool looking and '
                             'useful statusbar please send me the respective '
                             'cvars to make it available for everyone with a '
                             '/exec yourstatusbarname.cfg in next update! '
                             'Paste the cvars here!',
              'name': 'hud_hpix'},
 'hud_hpiy': {'default': None,
              'description': 'Cvars to customize the statusbar elements. x y '
                             'are coords, w and h are font widths and font '
                             'heights, g is gap between numbers, i refers to '
                             'icon, s stands for size.\n'
                             'The hp, armor, ammo, the flag (in the hud when '
                             'you have it) and the icons can be moved and '
                             'resized with these. Upper left corner is at x=0, '
                             'y=0; Bottom right corner is at x=640, y=480 '
                             "irrespectively of actual screen resolution!Don't "
                             'forget to save the values in your autoexec.cfg '
                             'or use /seta cvarname value followed by '
                             '/writeconfig q3config.cfg!\n'
                             'Tip: start OA from command line, type hud_TAB, '
                             'the autocompleted hud_ cvars will appear in your '
                             'terminal, copypaste the values from there (after '
                             "removing the equal signs and adding 'set' in "
                             'front of them ofc)!\n'
                             '\n'
                             "It is advisable to disable your model's head "
                             "with cg_statusBarStyle as you can't move it!\n"
                             '\n'
                             'You can try some preconfigured statusbars:\n'
                             '/exec hud1 - Start from this one if you played '
                             'too much AS!\n'
                             '/exec hud2\n'
                             '/exec hud3\n'
                             '/exec hud4\n'
                             '/exec hud5\n'
                             '/exec hud6 - Start from this if you prefer how '
                             'cute and unobtrusive this one is!\n'
                             '/exec huddefault - To revert back to defaults.\n'
                             '\n'
                             'Tip: You can use one of the preconfigureds as a '
                             "skeleton and modify only the settings you don't "
                             'like!\n'
                             '\n'
                             'Note: Pick a custom value for cg_statusBarStyle '
                             'if you want to configure the statusbar in '
                             'instantgib! Default 0 will draw the default '
                             'insta statusbar!\n'
                             '\n'
                             'Ps: If you managed to set up a cool looking and '
                             'useful statusbar please send me the respective '
                             'cvars to make it available for everyone with a '
                             '/exec yourstatusbarname.cfg in next update! '
                             'Paste the cvars here!',
              'name': 'hud_hpiy'},
 'hud_hpw': {'default': None,
             'description': 'Cvars to customize the statusbar elements. x y '
                            'are coords, w and h are font widths and font '
                            'heights, g is gap between numbers, i refers to '
                            'icon, s stands for size.\n'
                            'The hp, armor, ammo, the flag (in the hud when '
                            'you have it) and the icons can be moved and '
                            'resized with these. Upper left corner is at x=0, '
                            'y=0; Bottom right corner is at x=640, y=480 '
                            "irrespectively of actual screen resolution!Don't "
                            'forget to save the values in your autoexec.cfg or '
                            'use /seta cvarname value followed by /writeconfig '
                            'q3config.cfg!\n'
                            'Tip: start OA from command line, type hud_TAB, '
                            'the autocompleted hud_ cvars will appear in your '
                            'terminal, copypaste the values from there (after '
                            "removing the equal signs and adding 'set' in "
                            'front of them ofc)!\n'
                            '\n'
                            "It is advisable to disable your model's head with "
                            "cg_statusBarStyle as you can't move it!\n"
                            '\n'
                            'You can try some preconfigured statusbars:\n'
                            '/exec hud1 - Start from this one if you played '
                            'too much AS!\n'
                            '/exec hud2\n'
                            '/exec hud3\n'
                            '/exec hud4\n'
                            '/exec hud5\n'
                            '/exec hud6 - Start from this if you prefer how '
                            'cute and unobtrusive this one is!\n'
                            '/exec huddefault - To revert back to defaults.\n'
                            '\n'
                            'Tip: You can use one of the preconfigureds as a '
                            "skeleton and modify only the settings you don't "
                            'like!\n'
                            '\n'
                            'Note: Pick a custom value for cg_statusBarStyle '
                            'if you want to configure the statusbar in '
                            'instantgib! Default 0 will draw the default insta '
                            'statusbar!\n'
                            '\n'
                            'Ps: If you managed to set up a cool looking and '
                            'useful statusbar please send me the respective '
                            'cvars to make it available for everyone with a '
                            '/exec yourstatusbarname.cfg in next update! Paste '
                            'the cvars here!',
             'name': 'hud_hpw'},
 'hud_hpx': {'default': None,
             'description': 'Cvars to customize the statusbar elements. x y '
                            'are coords, w and h are font widths and font '
                            'heights, g is gap between numbers, i refers to '
                            'icon, s stands for size.\n'
                            'The hp, armor, ammo, the flag (in the hud when '
                            'you have it) and the icons can be moved and '
                            'resized with these. Upper left corner is at x=0, '
                            'y=0; Bottom right corner is at x=640, y=480 '
                            "irrespectively of actual screen resolution!Don't "
                            'forget to save the values in your autoexec.cfg or '
                            'use /seta cvarname value followed by /writeconfig '
                            'q3config.cfg!\n'
                            'Tip: start OA from command line, type hud_TAB, '
                            'the autocompleted hud_ cvars will appear in your '
                            'terminal, copypaste the values from there (after '
                            "removing the equal signs and adding 'set' in "
                            'front of them ofc)!\n'
                            '\n'
                            "It is advisable to disable your model's head with "
                            "cg_statusBarStyle as you can't move it!\n"
                            '\n'
                            'You can try some preconfigured statusbars:\n'
                            '/exec hud1 - Start from this one if you played '
                            'too much AS!\n'
                            '/exec hud2\n'
                            '/exec hud3\n'
                            '/exec hud4\n'
                            '/exec hud5\n'
                            '/exec hud6 - Start from this if you prefer how '
                            'cute and unobtrusive this one is!\n'
                            '/exec huddefault - To revert back to defaults.\n'
                            '\n'
                            'Tip: You can use one of the preconfigureds as a '
                            "skeleton and modify only the settings you don't "
                            'like!\n'
                            '\n'
                            'Note: Pick a custom value for cg_statusBarStyle '
                            'if you want to configure the statusbar in '
                            'instantgib! Default 0 will draw the default insta '
                            'statusbar!\n'
                            '\n'
                            'Ps: If you managed to set up a cool looking and '
                            'useful statusbar please send me the respective '
                            'cvars to make it available for everyone with a '
                            '/exec yourstatusbarname.cfg in next update! Paste '
                            'the cvars here!',
             'name': 'hud_hpx'},
 'hud_hpy': {'default': None,
             'description': 'Cvars to customize the statusbar elements. x y '
                            'are coords, w and h are font widths and font '
                            'heights, g is gap between numbers, i refers to '
                            'icon, s stands for size.\n'
                            'The hp, armor, ammo, the flag (in the hud when '
                            'you have it) and the icons can be moved and '
                            'resized with these. Upper left corner is at x=0, '
                            'y=0; Bottom right corner is at x=640, y=480 '
                            "irrespectively of actual screen resolution!Don't "
                            'forget to save the values in your autoexec.cfg or '
                            'use /seta cvarname value followed by /writeconfig '
                            'q3config.cfg!\n'
                            'Tip: start OA from command line, type hud_TAB, '
                            'the autocompleted hud_ cvars will appear in your '
                            'terminal, copypaste the values from there (after '
                            "removing the equal signs and adding 'set' in "
                            'front of them ofc)!\n'
                            '\n'
                            "It is advisable to disable your model's head with "
                            "cg_statusBarStyle as you can't move it!\n"
                            '\n'
                            'You can try some preconfigured statusbars:\n'
                            '/exec hud1 - Start from this one if you played '
                            'too much AS!\n'
                            '/exec hud2\n'
                            '/exec hud3\n'
                            '/exec hud4\n'
                            '/exec hud5\n'
                            '/exec hud6 - Start from this if you prefer how '
                            'cute and unobtrusive this one is!\n'
                            '/exec huddefault - To revert back to defaults.\n'
                            '\n'
                            'Tip: You can use one of the preconfigureds as a '
                            "skeleton and modify only the settings you don't "
                            'like!\n'
                            '\n'
                            'Note: Pick a custom value for cg_statusBarStyle '
                            'if you want to configure the statusbar in '
                            'instantgib! Default 0 will draw the default insta '
                            'statusbar!\n'
                            '\n'
                            'Ps: If you managed to set up a cool looking and '
                            'useful statusbar please send me the respective '
                            'cvars to make it available for everyone with a '
                            '/exec yourstatusbarname.cfg in next update! Paste '
                            'the cvars here!',
             'name': 'hud_hpy'},
 's_ambient': {'default': '1',
               'description': 'The washing machine at mkbase, the torches at '
                              'sago, the horses at cp1, and all the annyoing '
                              'looping ambient sounds can be disabled with '
                              'this one.',
               'name': 's_ambient'}}
