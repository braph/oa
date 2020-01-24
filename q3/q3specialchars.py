#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

'''
FUCK THIS SHIT.

The idea was to translate Quake III special characters to Unicode characters,
but Unicode lacks symbols like `Upper one quarter block` (`Lower one quarter block` does exist, though).
'''

# ᑕ Good site of unicode overview: ᑐ
# http://xahlee.info/comp/unicode_braille.html
# TODO:
# - Change raw unicode to \uXXXX
# - Test assert(toUTF(toQ3Ascii(...)) == ...)

class Q3SpecialChars:
    '''
    Conversion of control characters to UTF8 in Quake III strings
    '''

    # 16 columns X 16 rows, like in pak0.pk3:/gfx/2d/bigchars.tga
    CHARACTERS = [
        #0   1   2   3   4   5   6   7   8   9   A   B    C   E   E   F
        '🞍','▟','▀','▙','█',' ','█','▜','█','▛','▁','⬛',' ','▶',' ',' ',
        '[',']','𐑩',' ','𐑪',' ',' ',' ','𐑧','▬','𐑨',' ' ,'𝅍',' ',' ',' ',
        # ASCII 
        ' ','!','"','#','$','%','&',"'",'(',')','*','+',',','-','.','/',
        '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?',
        '@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
        'P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_',
        '`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
        'p','q','r','s','t','u','v','w','x','y','z','{','|','}','"','⇠'
    ]



    CHARACTERS = [
       None,  # 0x00 |
       '▟',   # 0x01 | A | QUADRANT UPPER RIGHT AND LOWER LEFT AND LOWER RIGHT
       '▀',   # 0x02 | B | UPPER HALF BLOCK
       '▙',   # 0x03 | C | QUADRANT UPPER LEFT AND LOWER LEFT AND LOWER RIGHT
       '█',   # 0x04 | D | FULL BLOCK
       ' ',   # 0x05 | E
       '█',   # 0x06 | F | FULL BLOCK
       '▜',   # 0x07 | G | <BS> QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER RIGHT
       '█',   # 0x08 | H | FULL BLOCK
       '▛',   # 0x09 | I | QUADRANT UPPER LEFT AND UPPER RIGHT AND LOWER LEFT
       ' ',   # 0x0a | J |
       '▇',   # 0x0b | K | LOWER SEVEN EIGHTHS BLOCK
       ' ',   # 0x0c | L |
       ' ',   # 0x0d | M |
       '▪',   # 0x0e | N | BLACK SMALL SQUARE
       '▪',   # 0x0f | O | BLACK SMALL SQUARE
       '❲',   # 0x10 | P | LEFT WHITE SQUARE BRACKET
       '❳',   # 0x11 | Q | RIGHT WHITE SQUARE BRACKET
       '╭',   # 0x12 | R | BOX DRAWINGS LIGHT ARC DOWN AND RIGHT
       '━',   # 0x13 | S | 
       '╮',   # 0x14 | T | BOX DRAWINGS LIGHT ARC DOWN AND LEFT
       '▌',   # 0x15 | U | LEFT HALF BLOCK
       ' ',   # 0x16 | V |
       '▐',   # 0x17 | W | RIGHT HALF BLOCK
       '╰',   # 0x18 | X | BOX DRAWINGS LIGHT ARC UP AND RIGHT
       '▁',   # 0x19 | Y | LOWER ONE EIGHTH BLOCK
       '╯',   # 0x1a | Z | BOX DRAWINGS LIGHT ARC UP AND LEFT
       '▔',   # 0x1b |   | UPPER ONE EIGHTH BLOCK
    ]

    CHARACTERS_LEN = len(CHARACTERS)

    CHAR_7F = '⇠'

    @staticmethod
    def toUTF8(str):
        utf8 = ''
        for c in str:
            o = ord(c)
            if o >= 1 and o < Q3SpecialChars.CHARACTERS_LEN and Q3SpecialChars.CHARACTERS[o] is not None:
                utf8 += Q3SpecialChars.CHARACTERS[o]
            elif o == 0x7F:
                utf8 += Q3SpecialChars.CHAR_7F
            else:
                utf8 += c
        return utf8

    @staticmethod
    def toQ3Ascii(str):
        q3ascii = ''
        for c in str:
            if c in Q3SpecialChars.CHARACTERS:
                q3ascii += chr(Q3SpecialChars.CHARACTERS.index(c))
            elif c == Q3SpecialChars.CHAR_7F:
                q3ascii += chr(0x7F)
            else:
                q3ascii += c
        return q3ascii


if __name__ == '__main__':
    s = ''
    for i in range(0, 256):
        s += chr(i)
    assert s == Q3SpecialChars.toQ3Ascii(Q3SpecialChars.toUTF8(s))

    bunny = '\x1b\x13\x02\x03bunny\x01\x02\x13\x1b'
    print(repr(bunny), '->', Q3SpecialChars.toUTF8(bunny))

