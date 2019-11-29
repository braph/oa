#!/usr/bin/python
# -*- coding: utf-8 -*-

WEAPONS = {
    1:  'Gauntlet',
    2:  'Machine Gun',
    3:  'Shotgun',
    4:  'Grenade Laucher',
    5:  'Rocket Launcher',
    6:  'Lightning Gun',
    7:  'Rail Gun',
    8:  'Plasma Gun',
    9:  'BFG10K',
    10: 'Grappling Hook',
    11: 'Nail Gun',
    12: 'Prox mine Launcher',
    13: 'Chain Gun'
}

def weaponNo2str(n):
    try: n = int(n)
    except: raise Exception('Weapon not a number: %s' % n)
    return WEAPONS.get(n, 'Weapon #%d'%n)

CROSSHAIRS = {
    0: 'No crosshair',
    1: 'Circle and point «(·)»',
    2: 'Circle (filled) and point «(·)»',
    3: 'Cross «+»',
    4: 'Point «·»',
    5: 'Point «·»',
    6: 'Wide cross «-+–»',
    7: 'Wide cross «-+–»',
    8: 'Wide cross with a hole «–+–»',
    9: 'Wide cross with a hole «–+–»'
}

def crosshairNo2str(n):
    try: n = int(n)
    except: raise Exception('Chrosshair not a number: %s' % n)
    return CROSSHAIRS.get(n, 'Crosshair #%d'%n)
