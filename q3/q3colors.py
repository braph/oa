#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import re

class Q3Colors:
    '''
    Quake III Coloring System
    '''

    QUAKE_PALETTE = {
        '0': '000000',
        '1': 'FF0000',
        '2': '00FF00',
        '3': 'FFFF00',
        '4': '0000FF',
        '5': '00FFFF',
        '6': 'FF00FF',
        '7': 'FFFFFF',
        '8': 'FFA500'
    }

    FAILMOD_PALETTE = {
        'a': 'FFDC00',
        'b': 'FFFF00',
        'c': 'FFFF00',
        'd': 'E8FF00',
        'e': 'C8FF00',
        'f': 'A6FF00',
        'g': '5EFF00',
        'h': '00FF34',
        'i': '00FF5E',
        'j': '00FFA5',
        'k': '00FFE8',
        'l': '00FFFF',
        'm': '00E8FF',
        'n': '00A6FF',
        'o': '005EFF',
        'p': '0034FF',
        'q': '5C02FC',
        'r': '8400FF',
        's': 'A200FC',
        't': 'E800FF',
        'u': 'FF00FF',
        'v': 'FF00E7',
        'w': 'FF00A6',
        'x': 'FF0084',
        'y': 'FF005E',
        'z': 'FFA6A6',
        'A': 'A50000',
        'B': '5E0000',
        'C': 'FFE8A6',
        'D': 'A65E00',
        'E': '5E3400',
        'F': 'FFFFA6',
        'G': 'A6A600',
        'H': 'A6FFA6',
        'I': '00A500',
        'J': '005E00',
        'K': 'A6A6FF',
        'L': '0000A6',
        'M': '00005E',
        'N': 'A4FFFF',
        'O': '00A6A6',
        'P': 'FFA6FF',
        'Q': 'A600A6',
        'R': '5E005E',
        'S': '202020',
        'T': '343434',
        'U': '5E5E5E',
        'V': '848484',
        'W': 'A6A6A6',
        'X': 'C8C8C8',
        'Y': 'E8E8E8',
        'Z': 'FFFFFF',
        '&': 'FFE8E8',
        '*': 'E8FFFF',
        '(': 'E8FFE8',
        ')': 'E8E8FF',
        '+': 'FEE5FE',
        "'": 'FFFFE6'
    }

    __slots__ = ('_palette')
    def __init__(self):
        self._palette = {}

    def addPalette(self, palette):
        self._palette.update({k:v.upper() for k,v in palette.items()})

    def removePalette(self, palette):
        for k in palette.keys():
            try:    del self._palette[k]
            except: pass

    def getPalette(self):
        return self._palette

    def getAvailableCarets(self):
        '''
        Return all available color carets as list
        '''
        return list(self._palette.keys())

    def getHexForCaret(self, caret, prefix='#'):
        '''
        Return hexadecimal color for `caret` prefixed by `prefix`
        '''
        return '%s%s' % (prefix, self._palette[caret])

    def getCaretForHex(self, hex_rgb, prefix='^'):
        '''
        Return caret character for hexadecimal color `hex_rgb` prefixed by `prefix`
        '''
        hex_rgb = hex_rgb.upper().strip('#')
        r, g, b = int(hex_rgb[0:1], 16), int(hex_rgb[2:3], 16), int(hex_rgb[4:5], 16)
        diffs = []
        for k, v in self._palette.items():
            if hex_rgb == v:
                return '%s%s' % (prefix, k)
            r2, g2, b2 = int(v[0:1], 16), int(v[2:3], 16), int(v[4:5], 16)
            diffs.append((k , abs(r-r2) + abs(g-g2) + abs(b-b2)))

        # Return nearest color
        diffs.sort(key=lambda i: i[1])
        return '%s%s' % (prefix, diffs[0][0])

    _CARET_RE = re.compile(r'\^.')
    def toHtml(self, str, include_carets=False):
        '''
        Convert a string colored with carets (^1,^2,...) to HTML.
        If `include_carets` is True, the carets will not be stripped of.
        '''

        def caret2span(match):
            str = match.group(0)
            try:
                return '<span color="%s">' % self.getHexForCaret(str[1])
            except:
                return str[0]

        def caret2span_with_carets(match):
            str = match.group(0)
            try:
                return '<span color="%s">%s' % (self.getHexForCaret(str[1]), str)
            except:
                return str[0]

        str = str.replace('<', '&lt;')
        str = str.replace('>', '&gt;')
        str = str.replace('&', '&amp;')
        str = str.replace('"', '&quot;')
        str = str.replace("'", '&apos;')
        if '^' in str:
            if include_carets:
                str = Q3Colors._CARET_RE.sub(caret2span_with_carets, str)
            else:
                str = Q3Colors._CARET_RE.sub(caret2span, str)
            str += '</span>'*str.count('<span')
        return str


if __name__ == '__main__':
    q3colors = Q3Colors()
    q3colors.addPalette(Q3Colors.QUAKE_PALETTE)
    assert q3colors.getHexForCaret('0', '')      == '000000'
    assert q3colors.getHexForCaret('0')          == '#000000'
    assert q3colors.getCaretForHex('000000', '') == '0'
    assert q3colors.getCaretForHex('000000')     == '^0'
    assert q3colors.getCaretForHex('000001')     == '^0'
    assert q3colors.toHtml('^0Foo')         == '<span color="#000000">Foo</span>'
    assert q3colors.toHtml('^0Foo^7Bar')    == '<span color="#000000">Foo<span color="#FFFFFF">Bar</span></span>'
    assert q3colors.toHtml('^0Foo', True)   == '<span color="#000000">^0Foo</span>'

