#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import sys
import re
PLATFORM = sys.platform
if PLATFORM == 'win32':
    from ctypes import windll
    _stdout_handle = windll.kernel32.GetStdHandle(-11)
    _SetConsoleTextAttribute = windll.kernel32.SetConsoleTextAttribute
else:
    pass


PY34 = sys.version_info >= (3, 4, 0)

def _pr(cstr):
    clst = cstr.split('^')
    color = 0x0001
    for cstr in clst:
        dglen = re.search('\D', cstr).start()
        if dglen:
            color = int(cstr[:dglen])
        text = cstr[dglen:]
        text = text.replace(u'\u0456', u'i')
        if text[:1] == '_': text = text[1:]
        text = _set_color(color) + text
        if (PLATFORM == 'win32') and (not PY34):
            text = text.encode('cp866', 'ignore')
        # sys.stdout.write(text)
        print(text, end='')
        sys.stdout.flush()

def _restore_colors(e=''):
    # sys.stdout.write(_set_color(20) + u'')
    print(_set_color(20) + u'', end=e)
    sys.stdout.flush()

def cprint(cstr):
    _pr(cstr)
    _restore_colors(e=u'\n')
    # print('')

def cprint2(cstr):
    _pr(cstr)
    _restore_colors()
    # print('', end='')

def colors_win():
    return {
            0 : u'чёрный',
            1 : u'синий',
            2 : u'зелёный',
            3 : u'голубой',
            4 : u'красный',
            5 : u'фиолетовый',
            6 : u'жёлтый',
            7 : u'серый',

            8 : u'тёмно-серый',
            9 : u'светло-синий',
            10: u'светло-зелёный',
            11: u'светло-голубой',
            12: u'светло-красный',
            13: u'светло-фиолетовый (пурпурный)',
            14: u'светло-жёлтый',
            15: u'белый',
            }

def colors_win2linux():
    return {
            0 : 30,
            1 : 34,
            2 : 32,
            3 : 36,
            4 : 31,
            5 : 35,
            6 : 33,
            7 : 37,

            8 : 90,
            9 : 94,
            10: 92,
            11: 96,
            12: 91,
            13: 95,
            14: 93,
            15: 97,
            }

def _dafault_color():
    # цвет по умолчанию: 20
    # для windows это 1, для linux - сброс
    def_color = 1
    if PLATFORM == 'win32':
        def_color = 1
    elif 'linux' in PLATFORM:
        def_color = 0
    return def_color

def _set_color(color):
    if color == 20:
        color = _dafault_color()
    prefix_color = u''
    if PLATFORM == 'win32':
        _SetConsoleTextAttribute(_stdout_handle, color | 0x0070) #78
    elif 'linux' in PLATFORM:
        prefix_color = u'\033[%(col_linux)sm' % {'col_linux': colors_win2linux()[color]}
    return prefix_color


# --------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    os.system('color 71')
    for col in range(16):
        color_win = {
                'color': col,
                'name': colors_win()[col]
                }
        cprint(u'%(color)dЦвет %(color)d\t %(name)s' % color_win)

    print(u'\nПримеры')
    cprint(u'20######### Идем к другу ^14_%s ^8_%d/%d ^20_на ^3_%s ^20_#########' % (12345, 5, 3000, 'main'))
    cprint(u'13Завершили обход всех ^12_НОВЫХ ^13_друзей')

    cprint(u'Обрабатываем файл ^5_XXX ^13_YYY')
    cprint2(u'Обрабатываем файл ^5_XXX ^13_YYY ^14_ZZZ')
    cprint(u'4 конец')

    if PY34:
        input(u'\n---------------   END   ---------------')
    else:
        raw_input(u'\n---------------   END   ---------------')

# ==================================================================================================
