#!/usr/bin/python
# -*- coding: utf-8 -*-
LABEL = 'quake3tweaks.tripod.com'
VARIABLES = {'bot_nochat': {'description': 'Basicaly, this command lets you turn off those '
                               'automated taunts that the bots come out with. '
                               'I presume there will be a minor framerate '
                               'increase but I am not sure. Once you tire of '
                               'the taunts set this to 1. Be aware that this '
                               'setting works only when it has been entered '
                               'manually into your config - you can place it '
                               'anywhere or you can download',
                'name': 'bot_nochat'},
 'cg_bobpitch': {'description': 'These 3 settings are used to create a more '
                                'realistic walk or run for your character. For '
                                'example, when you are slowly walking in a '
                                'crouch position, you will shuffle side to '
                                'side to give your character more realistic '
                                'movement. The default for all settings is '
                                '0.0025 but I prefer to turn these settings to '
                                '0 as its gives a more fluid movement and '
                                'prevents possible motion sickness 8^)',
                 'name': 'cg_bobpitch'},
 'cg_bobroll': {'description': 'These 3 settings are used to create a more '
                               'realistic walk or run for your character. For '
                               'example, when you are slowly walking in a '
                               'crouch position, you will shuffle side to side '
                               'to give your character more realistic '
                               'movement. The default for all settings is '
                               '0.0025 but I prefer to turn these settings to '
                               '0 as its gives a more fluid movement and '
                               'prevents possible motion sickness 8^)',
                'name': 'cg_bobroll'},
 'cg_bobup': {'description': 'These 3 settings are used to create a more '
                             'realistic walk or run for your character. For '
                             'example, when you are slowly walking in a crouch '
                             'position, you will shuffle side to side to give '
                             'your character more realistic movement. The '
                             'default for all settings is 0.0025 but I prefer '
                             'to turn these settings to 0 as its gives a more '
                             'fluid movement and prevents possible motion '
                             'sickness 8^)',
              'name': 'cg_bobup'},
 'cg_brassTime': {'description': 'With this on, when a gun is fired, the '
                                 'shells ejected are thrown and discarded in '
                                 'the air for added realism. However, this '
                                 'will be the last thing you are looking for '
                                 'when you are being slapped up in Quake 3 so '
                                 'leave this setting off. FPS gain with this '
                                 'off is around 1 - 3 FPS.',
                  'name': 'cg_brassTime'},
 'cg_centertime': {'description': 'This command lets you limit how long the '
                                  '"you fragged <playername>" message appears '
                                  'when you frag someone. The default setting '
                                  'is 3, but the recommended setting is 1. '
                                  'Setting this command to 0 means no message '
                                  'is displayed. This command should be '
                                  'entered manually into your autoexec.',
                   'name': 'cg_centertime'},
 'cg_deferPlayers': {'description': 'A nice simple setting. With this set to '
                                    '1, new player skins will only be loaded '
                                    'when you are either fragged or when you '
                                    'look at the scoreboard. With this set to '
                                    '0, new player models are loaded as soon '
                                    'as a new player joins the server. I like '
                                    'this set to 1 as the screen could stutter '
                                    'at a potentialy crucial time meaning '
                                    'frustration.',
                     'name': 'cg_deferPlayers'},
 'cg_draw3dIcons': {'description': 'When turned on, all icons in the HUD will '
                                   'be displayed in 3D. This can get in the '
                                   'way so it is best turned off. FPS gain '
                                   'with this off - 0.5 - 1 FPS.',
                    'name': 'cg_draw3dIcons'},
 'cg_drawAttacker': {'description': "Displays the opponent's name when you "
                                    'face them. Pretty useless, so this is '
                                    'best turned off. FPS gain with this off - '
                                    '0.5 - 1 FPS.',
                     'name': 'cg_drawAttacker'},
 'cg_drawGun': {'description': "This command let's you toggle between "
                               'displaying, or not displaying the gun. Many '
                               'people like to have a gun on screen at all '
                               'times as it helps distinguish which weapon you '
                               'currently have selected. I myself keep this '
                               'setting on 0 as it speeds up play (around 2-3 '
                               'FPS) and gives the advantage of not having a '
                               'gun blocking your view - especialy helpful '
                               'when using the railgun. It takes time to '
                               'adjust but the benefits are there if you want '
                               'them. Remember, when you change a weapon, you '
                               'are notified of what you have selected.',
                'name': 'cg_drawGun'},
 'cg_drawRewards': {'description': 'Displays rewards earned in current battle '
                                   '(excellent, impressive etc...). Again, not '
                                   'too useful so turn it off. FPS gain with '
                                   'this off - 0.5 - 1 FPS.',
                    'name': 'cg_drawRewards'},
 'cg_forceModel': {'description': 'If you want to use only the same model or '
                                  'skin throughout, then set this to 1. Every '
                                  'character (human, or bot) will have the '
                                  'same character model as yourself. However, '
                                  'if you are using a custom model with a '
                                  'large polycount, this can hinder '
                                  'performance slightly. Default is 0.',
                   'name': 'cg_forceModel'},
 'cg_fov': {'description': 'This setting lets you widen or shrink your viewing '
                           'area or field of vision. The default is 90 but '
                           'feel free to increase this slightly for a sly '
                           "advantage (I wouldn't put it over 100 though as "
                           'the image looks trippy). Unfortunately, because of '
                           'the larger viewing area, the CPU is under more '
                           'stress so bear in mind you may get a slightly '
                           'lower framerate.',
            'name': 'cg_fov'},
 'cg_gibs': {'description': 'When activated, characters will "gib" (blow into '
                            'pieces) with a particulaly viscious shot. '
                            '"com_blood" must be activated for this to take '
                            'effect. This looks pretty, and can be satisfying '
                            'but can slow down gameplay in large scale '
                            'deathmatches. When turned off, FPS gain is around '
                            '1 - 5 FPS depending on the amount of action going '
                            'on.',
             'name': 'cg_gibs'},
 'cg_lagometer': {'description': 'This is a very useful utility which lets you '
                                 'monitor your connection on-line. With this '
                                 'enabled while you are playing on-line you '
                                 'will see 2 boucing lines. The first line '
                                 'displays the conjunction between your '
                                 'graphics card updating the frames in sync '
                                 'with the gameworld updates recieved from the '
                                 'server. Idealy, this should be a straight '
                                 'blue line. If it has bouncing yellow spikes '
                                 'then your display will stutter and be more '
                                 'difficult to view. To combat this, first '
                                 'ensure you have followed my tweaking '
                                 'techniques and then change your snaps '
                                 'setting. Usually, this means lowering it by '
                                 '1 or 2 until your screen is stable and you '
                                 'have a nice flowing blue line in your '
                                 'lagometer. The second line shows if packets '
                                 'are being recieved from the server. This '
                                 'should be green. If it is yellow or red, try '
                                 'increasing your rate or try lowering your '
                                 'snaps. If this does not help, you may be on '
                                 'a dodgy server and so try '
                                 'another.Additionaly, ensure the lagometer is '
                                 'turned OFF when you are not on the internet, '
                                 'and/or when you have a stable connection.',
                  'name': 'cg_lagometer'},
 'cg_marks': {'description': 'With this turned on, every time a player shoots '
                             'at the scenary, a mark is left behind. These '
                             'marks will stay for approximataly 20 seconds. '
                             'Because of this, slowdown is created. FPS gain '
                             'with this turned off is around 3 - 10 FPS '
                             'meaning this is best turned off unless your '
                             'average framerate is at least 65 FPS on demo001.',
              'name': 'cg_marks'},
 'cg_predictItems': {'description': 'This setting determines whether the '
                                    'server or the client decides on whether a '
                                    'weapon has being collected. a setting of '
                                    '1 means the client decides and a setting '
                                    'of 0 means the server decides. I would '
                                    'keep this set at 1 to prevent any '
                                    'un-neccessary confusion.',
                     'name': 'cg_predictItems'},
 'cg_shadows': {'description': 'There are 3 shadow modes - 1, 2, and 3. 1 '
                               'creates round, unrealistic shadows under the '
                               'feet of all characters. 2 creates incredibly '
                               'lifelike shadows, but at a huge performance '
                               'hit. My computer slowed to a halt with this on '
                               'resulting in unplayable gameplay. 3 creates '
                               'suitably lifelike shadows but again at the '
                               'cost of some performance. I recommend you just '
                               'leave them off unless you have at least a '
                               'Pentium 3 500 MHZ with 128 MB RAM and a decent '
                               'third generation graphics card. FPS gain with '
                               'this off are: 3 FPS (setting 1), 8 - 30 FPS '
                               '(setting 2) and 8 FPS (setting 3).',
                'name': 'cg_shadows'},
 'cg_simpleItems': {'description': 'With this on, all items will be displayed '
                                   'in 2D rather than spinning in 3D. This is '
                                   'especially helpful for people with slower '
                                   'machines as it can really speed things up. '
                                   'Dont bother if you have a specification '
                                   'above or near to mine. FPS gain with this '
                                   'on: 3 - 10 FPS.',
                    'name': 'cg_simpleItems'},
 'cl_maxPackets': {'description': 'This setting puts a limit on the maximum '
                                  'amount of packets that can be sent to the '
                                  'server via the client. This setting is '
                                  'useful for people with slower modems. The '
                                  'default setting is 30 (comparable to a 56K '
                                  'modem), but lower this if you have a 33.6K '
                                  'modem or less, and higher this setting if '
                                  'you have an ISDN or higher modem.',
                   'name': 'cl_maxPackets'},
 'cl_packetdups': {'description': 'As the name suggests, this setting is used '
                                  'to send multiple packets to compensate for '
                                  'lost packet drops. This setting should be '
                                  'set at 1 unless you have a VERY good '
                                  'connection in which case set this to 0. Use '
                                  'the lagometer to decide on which setting to '
                                  'use.',
                   'name': 'cl_packetdups'},
 'cl_timenudge': {'description': 'This interesting setting is identical to the '
                                 'pushlatency setting in Half-Life. This is '
                                 'very user determined and impossible to judge '
                                 'for every machine and every connection. I '
                                 'find this setting works well if you set the '
                                 'cl_timenudge setting to minus the ping you '
                                 'currently have with the server. For example '
                                 'if your ping is 100 then set your '
                                 'cl_timenudge setting to -100. I have heard '
                                 'people set this to plus what your ping is '
                                 '(say 100) but this reacted badly when I was '
                                 'playing on-line. If you cannot find a decent '
                                 'setting then leave it at default (0). Use '
                                 'this in conjunction with the lagometer for '
                                 'best results. Remember, plus means you will '
                                 'get a slower response and minus means the '
                                 'computer will try to predict what your next '
                                 'move is in an attempt to reduce lag - this '
                                 'can cause anomalities to occur. However, I '
                                 'would not recommend setting either number '
                                 'higher than 100.',
                  'name': 'cl_timenudge'},
 'com_blindlyLoadDLLs': {'description': 'If you use the',
                         'name': 'com_blindlyLoadDLLs'},
 'com_blood': {'description': 'Displays blood when a character is shot with '
                              'this turned on. Additionaly, characters create '
                              'a small gib when hit hard at the cost of no '
                              'performance. Keep this setting on and turn '
                              '"cg_gibs" off. FPS gain with this off: 1 - 3 '
                              'FPS.',
               'name': 'com_blood'},
 'com_hunkmegs': {'description': 'Only of use if you have more than 64 MB RAM. '
                                 'This setting alocates more system memory to '
                                 'Quake 3 for player models. If you have 128 '
                                 'MB RAM, set this to 86; if you have 96 MB '
                                 'RAM, set this to 64; if you have 192 MB RAM '
                                 'set this to 140; and finaly if you have 256 '
                                 'MB RAM, then set this to 200. You could try '
                                 'higher numbers but your system could become '
                                 'unstable.',
                  'name': 'com_hunkmegs'},
 'com_maxFPS': {'description': 'This command limits your maximum FPS. You may '
                               'ask why you would want to do this, and the '
                               'answer is that it will help the server from '
                               'having lag confusion when your frame rate has '
                               'a sudden rise or fall. Run a timedemo, collect '
                               'your average FPS and use that as the limit for '
                               'when you play on-line. While you are playing '
                               'off line, keep this setting at its default '
                               '(85).',
                'name': 'com_maxFPS'},
 'r_colorbits': {'description': 'Choose between 16 BIT colour (default) and 32 '
                                'BIT. Read the special notes on my homepage if '
                                'you own a Voodoo 3 or Voodoo Banshee Graphics '
                                'card. 32 BIT colour looks very nice (after '
                                'all, it can render 16.7 million colours '
                                "compared to 16 BIT's 65,000) but can be a "
                                'large burdon on computer resources. I guess '
                                'it depends on personal preferences and '
                                'computer speeds as to whether you want 32 BIT '
                                'colour, but you may lose valuable FPS.',
                 'name': 'r_colorbits'},
 'r_detailTextures': {'description': 'This is turned on by default and '
                                     'produces (you guessed it) more detailed '
                                     'textures. With this turned off, you get '
                                     'a slight speed boost, but could suffer '
                                     'slight texture inaccuracies. I found no '
                                     'noticable speed boost so keep it on.',
                      'name': 'r_detailTextures'},
 'r_drawsun': {'description': 'This setting creates shadows in relation to '
                              'where thet are towrads the sun. Of course, you '
                              'will need shadows enabled. I do not think there '
                              'is a drop in FPS so if you like shadows on, '
                              'then set this to enabled.',
               'name': 'r_drawsun'},
 'r_dynamicLight': {'description': 'With this on, the flare from a weapon '
                                   'flash will light up the surrounding area '
                                   'creating added realism. Be aware however '
                                   'that this is quite a large burdon on '
                                   'resources and consumes around 6 FPS.',
                    'name': 'r_dynamicLight'},
 'r_finish': {'description': 'This is the "Sync every frame" command in the '
                             'game options. It Improves response between the '
                             'keyboard/mouse and the on - screen action. I '
                             'recommend you set this to 1 to stop occasional '
                             'frustration. However, you may lose around 1 - 2 '
                             'FPS but that is hardly noticable in combat.',
              'name': 'r_finish'},
 'r_flares': {'description': 'I am not sure on this one. I presume it is '
                             'lighting related but I could see no difference '
                             'with this on or off. I set this to 1 as there is '
                             'no frame - rate loss. In fact, when I turned '
                             'this off, I was getting LOWER FPS!!! Contact me '
                             'if anyone knows what this setting does. I think '
                             'it is the bright flash once you get shot.....',
              'name': 'r_flares'},
 'r_gamma': {'description': 'Brightens/Darkens the screen. This setting varys '
                            'according to the brightness on your monitor. '
                            'Default is 1 but this can be set lower to darken '
                            'image (eg: 0.79010) or it can be increased to '
                            'brighten the image (eg: 1.10000). Experiment to '
                            'find the optimal amount.',
             'name': 'r_gamma'},
 'r_ignorehwgamma': {'description': 'This setting is useful for people running '
                                    'in 32 BIT colour on a Voodoo as it helps '
                                    'tidy the gamma to avoid texture smudging. '
                                    'However, when I tried this I found the '
                                    'image looking more like 16 BIT colour so '
                                    'I left this off. People have assured me '
                                    'that setting this to 1 gave a better '
                                    'image quality so play around with it to '
                                    'find your prefered setting. Thanks to',
                     'name': 'r_ignorehwgamma'},
 'r_intensity': {'description': 'As the name suggests this setting intensifies '
                                'the whole image. Default is 1 and this is '
                                'recommended.',
                 'name': 'r_intensity'},
 'r_lodBias': {'description': 'Produces more rounded images in the character '
                              'model, objects, and pickups the lower this '
                              'setting is. Through benchmarking, I have found '
                              'that the default (0) is the best balance '
                              'between framerate and image quality. I could '
                              'see no noticable visual improvement when '
                              'setting this into the low minuses (the valid '
                              'range is -2 to 2) but the framerate was lower. '
                              'Quite a large FPS increase can be had by '
                              'setting this to either 1 or 2 but the visuals '
                              'do suffer slightly. Leave this at 0 for the '
                              'best comprimise.',
               'name': 'r_lodBias'},
 'r_lodCurveError': {'description': 'This setting determines how close you '
                                    'have to be towards a polygon before it '
                                    '"clips" Think of it as similar to Mip - '
                                    'Mapping. I recommend a setting between '
                                    '100 - 300 depending on the power of your '
                                    'machine.',
                     'name': 'r_lodCurveError'},
 'r_mapOverBrightBits': {'description': 'This is a setting which controls how '
                                        'bright the scenary, textures and '
                                        'objects are. Lately, I have found '
                                        'this is the best way to achieve '
                                        'optimal image quality. This setting '
                                        'defaults at 2 but I would recommend '
                                        'setting this to 3. Secondly, lower '
                                        'the r_gamma setting to 0.82000 and '
                                        'start a new game. You should either '
                                        'find it too bright or too dark - '
                                        'adjust the gamma accordingly. I have '
                                        'found that setting this setting to 3 '
                                        'results in far more clarity and '
                                        'detail in the textures - before the '
                                        'image was a tad "smudged" but now the '
                                        'detail the designers put in the game '
                                        'is more apparent than ever!! This '
                                        'setting is useful for experimenting '
                                        "but don't forget to write down your "
                                        'old values first just in case you '
                                        'mess up your image quality.',
                         'name': 'r_mapOverBrightBits'},
 'r_picmip': {'description': 'This accounts for overall texture and image '
                             'quality, with 0 being the best, and higher '
                             'numbers being progressively worse. This setting '
                             'is a major player in having a high and '
                             'consistant frame - rate. A setting of 1 is '
                             'suitable for most computers as it ensures '
                             'excellent image quality with a solid, consistant '
                             'framerate. If you have a slower computer, set '
                             'this to 2 for less of a performance hit. On the '
                             'other hand, if you have a fast, well speced '
                             'computer with at least 96 MB RAM, feel free to '
                             'set this to 0 to have mind blowing graphics, the '
                             'likes of which are unrivaled on ANY format. '
                             'Ensure you have the best drivers for your '
                             'graphics card as well. I recently got a memory '
                             'upgrade and I now play with texture quality on '
                             'full and still get the same framerate as before '
                             '- I certainly recommend you have 128 MB RAM - '
                             'the difference in amazing!',
              'name': 'r_picmip'},
 'r_roundImagesDown': {'description': 'Smoothes and rounds images producing '
                                      "slightly inferior visuals. You don't "
                                      'gain noticable FPS with this set to 1 '
                                      'so keep it turned off. (',
                       'name': 'r_roundImagesDown'},
 'r_smp': {'description': "If you have two CPU's, Windows NT or 2000, and have "
                          'a graphics card AND a driver which supports SMP, '
                          'then you can benefit from a more sustained '
                          'Framerate, which may also be noticeably higher. The '
                          'default of course is 0, but if your system fulfils '
                          'the above requirements then by all means set this '
                          'to 1.',
           'name': 'r_smp'},
 'r_stencilBits': {'description': 'This is a graphical setting which lets you '
                                  'get more realistic cracks and texture in '
                                  'the architexture. I would set this to '
                                  'either 4 or 8. I find it has no effect on '
                                  'my framerate but that may be because I have '
                                  'an 8 BIT stencil buffer on my Voodoo 3 3000 '
                                  'PCI - if you have a different card to mine '
                                  '(TNT2, etc...) then experiment with this '
                                  'setting to get the optimal balance. Be '
                                  'aware that the screen will darken with this '
                                  'enabled - you may have to alter the gamma '
                                  'accordingly.',
                   'name': 'r_stencilBits'},
 'r_subDivisions': {'description': 'This is a texture setting which when set '
                                   'low, produces a better image with less '
                                   'graphical inacuracies. The maximum setting '
                                   'I would recommend is between 100 - 150 '
                                   'depending on the map. I like this set at 4 '
                                   'but feel free to experiment for the best '
                                   'comprimise between image quality and frame '
                                   '- rate.',
                    'name': 'r_subDivisions'},
 'r_swapInterval': {'description': 'This setting eliminates the slight screen '
                                   'ripping that appears when you turn '
                                   'quickly. Bear in mind that although the '
                                   'FPS loss is not large (1-2 FPS) there is a '
                                   'noticable lag between mouse/keyboard to '
                                   'the on screen action. It can affect '
                                   'gameplay so I would recommend leaving this '
                                   'setting to 0. (This setting is otherwise '
                                   'known as V SYNC).',
                    'name': 'r_swapInterval'},
 'r_texturebits': {'description': 'Similar to colourbits. However, if you run '
                                  'at high resolutions (1024x768 or above) '
                                  'this can cause texture corruption in 32 BIT '
                                  'colour mode. You must also have a card that '
                                  'supports 32 BIT colour. For best results, '
                                  'keep this at 16 BIT - the difference is not '
                                  'as instantly noticable as colorbits.',
                   'name': 'r_texturebits'},
 'r_vertexLight': {'description': 'This creates lighting made out of voxels '
                                  'instead of polygons. On a slow machine, '
                                  'this will speed things up considerably but '
                                  "can look quite dull. Don't bother if you "
                                  'have a decent machine.',
                   'name': 'r_vertexLight'},
 'rate': {'description': 'This setting controls packets to ensure a good '
                         'connection. If you have an ISDN modem (128K) then '
                         'this can be set to around 12000. If you have a 56K '
                         'modem then this should be around 4000-5500 depending '
                         'on your connection speed. If you are on a LAN or '
                         'have a ADSL modem (lucky bastard) then this can be '
                         'around 25000 or perhaps even higher. Remember, it is '
                         'best to experiment to find a suitable number but '
                         "don't get too carried away or you may cap "
                         'performance.',
          'name': 'rate'},
 's_loadas8bit': {'description': 'With this set to 1, all the sounds in the '
                                 'game will be forced to be played in 8 BIT '
                                 'meaning much lower sound quality. The FPS '
                                 'gain is around 2-3, so choose what would be '
                                 'the ideal setting for you.',
                  'name': 's_loadas8bit'},
 's_musicVolume': {'description': 'Self explanatary. Bear in mind that turning '
                                  "off the music doesn't result in such a "
                                  'noticably higher frame - rate as in Quake '
                                  '2. Only keep this on if you like musical '
                                  'accompanyment...',
                   'name': 's_musicVolume'},
 'snaps': {'description': 'This is possibly the most important setting for '
                          'getting a good connection. As everyone knows, in '
                          'Quake 2, your gameworld updates depended on your '
                          'current FPS so slower computers were at a '
                          'disadvantage. Now, in Quake 3, your snaps setting '
                          'determines how many updates you recieve from the '
                          'server. 56K modems should have a setting of around '
                          '20 - 30. ISDN modems (128K) should be around\xa0 40 '
                          'as should any other fast connection devices (LAN, '
                          'T1 etc....). Remember to read my cg_lagometer '
                          'section for\xa0 tips on "snaps".',
           'name': 'snaps'},
 'sv_pure': {'description': 'Controls whether the game should be played in '
                            'pure (as the developer intended) or unpure (which '
                            'means that certain mods can be used). I set this '
                            'to 0 as when playing on a pure server, quake 3 '
                            'automaticaly sets this command to 1. Make sure '
                            'you enter this command manualy into your '
                            'autoexec.',
             'name': 'sv_pure'},
 'vm_cgame': {'description': 'These settings MUST be set to 0 for the speed '
                             "dll's to function correctly. If any of these are "
                             'set to 1 in your config, then you are losing '
                             'performance, so change them immediately.',
              'name': 'vm_cgame'},
 'vm_game': {'description': 'These settings MUST be set to 0 for the speed '
                            "dll's to function correctly. If any of these are "
                            'set to 1 in your config, then you are losing '
                            'performance, so change them immediately.',
             'name': 'vm_game'},
 'vm_ui': {'description': "These settings MUST be set to 0 for the speed dll's "
                          'to function correctly. If any of these are set to 1 '
                          'in your config, then you are losing performance, so '
                          'change them immediately.',
           'name': 'vm_ui'}}
