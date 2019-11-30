#!/usr/bin/python
# -*- coding: utf-8 -*-

try:    from sys import intern
except: pass #Python2

SETTINGS = {
    intern('color.special'):        'orange',
    intern('color.int'):            'blue',
    intern('color.float'):          'blue',
    intern('color.bool.true'):      'green',
    intern('color.bool.false'):     'red',
    intern('color.maybe.int'):      'blue',
    intern('color.maybe.float'):    'blue',
    intern('background.invalid'):   '#FFBBBB',
    intern('prefixes'): [
        # Order as shown in GUI
        ('cl_',          'Client'),
        ('cg_',          'Client Game'),
        ('com_',         'Common'),         # TODO: Not sure about this 
        ('player_',      'Player'),
        ('df_',          'Mod:Defrag'),
        ('fm_',          'Mod:FailMod'),
        ('xp_',          'Mod:Excessive'),
        ('g_',           'Game'),
        ('in_',          'Input'),
        ('r_',           'Render'),
        ('j_',           'Joystick'),
        ('net_',         'Network'),
        ('s_',           'Sound'),
        ('sv_',          'Server'),
        ('elimination_', 'Elimination'),
        ('ui_',          'User Interface'),
        ('cmd_',         'User Command'),   # Internal prefix (not yet used)
        ('m_',           'Mouse'),
        ('vm_',          'VM'),
    ]
}
