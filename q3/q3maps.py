#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, zipfile

class Q3Maps:
    '''
    Quake III maps
    '''

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
            return None

