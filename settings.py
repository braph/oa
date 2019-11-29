#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import intern as _

SETTINGS = {
    _('color.special'):        'orange',
    _('color.int'):            'blue',
    _('color.float'):          'blue',
    _('color.bool.true'):      'green',
    _('color.bool.false'):     'red',
    _('color.maybe.int'):      'blue',
    _('color.maybe.float'):    'blue',
    _('background.invalid'):   '#FFBBBB',
    _('prefixes'): [
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
