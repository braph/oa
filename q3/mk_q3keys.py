#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, sys
sys.path.append('..')
from libmk import *

'''
This file contains some functions for handling Quake3/Qt keys and also
generates the needed mapping-data.
'''

# =============================================================================
# The list of all known Quake3 keys.
# =============================================================================
# To obtain this list run:
# sed -rn 's/.*K_([A-Z0-9_]+).*/"\1",/p' code/client/keycodes.h | grep -vE 'CHAR_FLAG|LAST_KEY'
# =============================================================================

Q3_KEYS = [
    "TAB",
    "ENTER",
    "ESCAPE",
    "SPACE",
    "BACKSPACE",
    "COMMAND", # Missing in Qt?
    "CAPSLOCK",
    "POWER",
    "PAUSE",
    "UPARROW",
    "DOWNARROW",
    "LEFTARROW",
    "RIGHTARROW",
    "ALT",
    "CTRL",
    "SHIFT",
    "INS",
    "DEL",
    "PGDN",
    "PGUP",
    "HOME",
    "END",
    "KP_HOME",
    "KP_UPARROW",
    "KP_PGUP",
    "KP_LEFTARROW",
    "KP_5",
    "KP_RIGHTARROW",
    "KP_END",
    "KP_DOWNARROW",
    "KP_PGDN",
    "KP_ENTER",
    "KP_INS",
    "KP_DEL",
    "KP_SLASH",
    "KP_MINUS",
    "KP_PLUS",
    "KP_NUMLOCK",
    "KP_STAR",
    "KP_EQUALS",
    "MWHEELDOWN",
    "MWHEELUP",
    "SUPER",
    "COMPOSE", # Missing in Qt?
    "MODE",
    "HELP",
    "PRINT",
    "SYSREQ",
    "SCROLLOCK",
    "BREAK",
    "MENU",
    "EURO", # The EURO-sign is actually a composed key, isn't it?!
    "UNDO"
]

def add_keys(prefix, start, end):
    Q3_KEYS.extend([prefix+str(i) for i in range(start, end+1)])

add_keys('WORLD_', 0, 95)
add_keys('JOY',    1, 32)
add_keys('F',      1, 15)
add_keys('AUX',    1, 16)
add_keys('MOUSE',  1, 5 )

# =============================================================================
# This is used by `quake3_key_reformat()`
# =============================================================================

# These words shall be replaced
__WORDS_REPLACE = {
    'DEL':    'Delete',
    'INS':    'Insert',
    'CTRL':   'Control',
    'ARROW':  '',             # UPARROW, DOWNARROW, LEFTARROW, RIGHTARROW
    'SYSREQ': 'SysReq',
    # Mind the trailing space
    'MWHEEL': 'Mouse Wheel ', # MWHEELUP, MWHEELDOWN
    'PG':     'Page ',        # PGUP, PGDOWN
    'MOUSE':  'Mouse ',
    'WORLD':  'World ',
    'JOY':    'Joystick ',
    'AUX':    'Auxiliary '
}
__WORDS_REPLACE_PATTERN = '|'.join([w for w in __WORDS_REPLACE.keys()])

# Everything else shall be title-cased
is_in_words_replace = re.compile('|'.join([
    'F\\d+', __WORDS_REPLACE_PATTERN
])).search
__WORDS_TITLE_PATTERN = '|'.join(set(map(
        lambda k: k.replace('KP_', ''),
        filter(lambda k: not is_in_words_replace(k), Q3_KEYS)
)))

# =============================================================================
# The Qt to Q3 Mapping
# =============================================================================

# These Qt.Key_'s only differ in case
QtSimilarToQ3 = [
    'Tab', 'Enter', 'Escape', 'Space', 'Backspace', 'CapsLock', 'Help',
    'Menu', 'Pause', 'Home', 'End', 'Shift', 'Alt', 'SysReq', 'ScrollLock'
] + ['F%d'%i for i in range(1, 15+1)]

# These Qt.Key_'s have a different name
QtNonSimilarToQ3 = {
    'Insert':    'INS',
    'Delete':    'DEL',
    'PageDown':  'PGDN',
    'PageUp':    'PGUP',
    'Return':    'ENTER',
    'Control':   'CTRL',
    'Up':        'RIGHTARROW',
    'Down':      'DOWNARROW',
    'Left':      'LEFTARROW',
    'Right':     'RIGHTARROW',
    'PowerDown': 'POWER', # not sure about these
    'PowerOff':  'POWER', # <-'
    'NumLock':   'KP_NUMLOCK'
}

# Qt return's those keys when in Numpad mode
QT_NUMPAD_KEYS_TO_QUAKE3 = {
    '0':        "INS",
    '1':        "END",
    '2':        "DOWNARROW",
    '3':        "PGDN",
    '4':        "LEFTARROW",
    '5':        "5",
    '6':        "RIGHTARROW",
    '7':        "HOME",
    '8':        "UPARROW",
    '9':        "PGUP",
    'Minus':    'MINUS',
    'Plus':     'PLUS',
    'Equal':    'EQUALS',
    'Slash':    'SLASH',
    'Asterisk': 'STAR',
    'Period':   'DEL',
    'Enter':    'ENTER'
}

# =============================================================================
# Build QT_KEYS_TO_QUAKE3, QT_NUMPAD_KEYS_TO_QUAKE3
# =============================================================================

QT_KEYS_TO_QUAKE3 = { }
QT_NUMPAD_KEYS_TO_QUAKE3 = {'Qt.Key_'+k:'KP_'+v for k,v in QT_NUMPAD_KEYS_TO_QUAKE3.items()}

for k in QtSimilarToQ3:
    QT_KEYS_TO_QUAKE3['Qt.Key_'+k] = k.upper()

for qt, q3 in QtNonSimilarToQ3.items():
    QT_KEYS_TO_QUAKE3['Qt.Key_'+qt] = q3.upper()

# =============================================================================
# Actual code of module
# =============================================================================

# @EXPORT
import re
try:    from PyQt5.QtCore import Qt
except: from PyQt4.QtCore import Qt

def qt_key_to_quake3(qKeyEvent):
    '''
    Interprete a Qt.KeyEvent as Quake3 would do.
    Return a Quake3 key as string or `None` on failure.
    '''

    code = qKeyEvent.key()
    mod  = qKeyEvent.modifiers()

    if mod & Qt.AltModifier:     return 'ALT'
    if mod & Qt.ControlModifier: return 'CTRL'
    if mod & Qt.ShiftModifier:   return 'SHIFT'
    if code == Qt.Key_NumLock:   return 'KP_NUMLOCK'

    if mod & Qt.KeypadModifier:
        try:    return QT_NUMPAD_KEYS_TO_QUAKE3[code]
        except: return None

    try:
        return QT_KEYS_TO_QUAKE3[code] # It's a special key
    except:
        try:    return chr(code).lower() # ASCII
        except: return None              # Not an ASCIi

def quake3_key_reformat(key, format='{numpad}{key}', numpad='(Numpad) '):
    ''' Make a Quake3 key more readable. '''

    if len(key) == 1:
        return key.upper()

    if key.startswith('KP_'):
        key = key[3:]
    else:
        numpad = ''

    key = __RE_REPLACE_WORD.sub(lambda m: __WORDS_REPLACE[m[0]], key)
    key = __RE_TITLE_WORD.sub(lambda m: m[0].title(), key)
    return format.format(numpad=numpad, key=key)

# @END

if __name__ == '__main__':
    import sys
    export_begin(sys.argv[0], 'Qt-Keys to Quake3-Names')
    export(sys.argv[0])
    export_variable('QT_KEYS_TO_QUAKE3',        QT_KEYS_TO_QUAKE3)
    export_variable('QT_NUMPAD_KEYS_TO_QUAKE3', QT_NUMPAD_KEYS_TO_QUAKE3)
    export_variable('Q3_KEYS',                  Q3_KEYS)
    export_variable('__WORDS_REPLACE',          __WORDS_REPLACE)
    export_variable('__RE_REPLACE_WORD',        __WORDS_REPLACE_PATTERN,
        format='{name} = re.compile({value})')
    export_variable('__RE_TITLE_WORD',          __WORDS_TITLE_PATTERN,
        format='{name} = re.compile({value})')
