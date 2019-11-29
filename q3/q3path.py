#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import os

class Q3Path:
    '''
    Quake III paths and filenames
    '''

    __slots__ = ('_user_config_dir', '_game_data_dir', '_main_config_filename')
    def __init__(self, user_config_dir=None, game_data_dir=None, main_config_filename='q3config.cfg'):
        home = os.path.expanduser('~')

        if user_config_dir is None:
            user_config_dir = os.path.join(home, '.openarena')

        if game_data_dir is None:
            dirs = [
                '/opt/openarena',
                '/usr/share/openarena',
                '/usr/share/games/openarena',
                os.path.join(home, 'openarena')
            ]
            for dir in dirs:
                baseoa_dir = os.path.join(dir, 'baseoa')
                if os.path.isdir(baseoa_dir):
                    game_data_dir = baseoa_dir
                    break

        self._user_config_dir       = user_config_dir
        self._game_data_dir         = game_data_dir
        self._main_config_filename  = main_config_filename

    def getUserConfigDir(self):
        return self._user_config_dir

    def getGameDataDir(self):
        return self._game_data_dir

    def getModNames(self):
        ''' Return the names of available mods '''
        return [
            f for f in os.listdir(self._user_config_dir) if os.path.isdir(os.path.join(self._user_config_dir, f))
        ]

    def getModDirectories(self):
        ''' Return a list of mod directories '''
        for f in os.listdir(self._user_config_dir):
            f = os.path.join(self._user_config_dir, f)
            if os.path.isdir(f):
                yield f

    def getModConfigFile(self, mod, filename=None):
        ''' Return the path of a configuration file inside `mod`.  '''
        return os.path.join(self._user_config_dir, mod, (filename or self._main_config_filename))


if __name__ == '__main__':
    q3path = Q3Path()
    print('User configuration directory is:', q3path.getUserConfigDir())
    print('Game directory is:              ', q3path.getGameDataDir())
    print('Mod configuration files are:')
    for m in q3path.getModNames():
        print('%-20s: %s' % (m, q3path.getModConfigFile(m)))
    print('Mod directories are:')
    for m in q3path.getModDirectories():
        print(m)
