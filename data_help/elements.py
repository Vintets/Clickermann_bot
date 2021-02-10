#!/usr/bin/env python
# -*- coding: utf-8 -*-

DATA_ELEMENTS = (
    dict(name='математические операции',
        parent_id=1,
        description=(
                    '```\n'
                    ' Операция           |Приоритет| Пример\n'
                    '--------------------|---------|-------------\n'
                    'Скобки приоритета ()|  1      | $var=(1+2)*2\n'
                    'Умножение "*"       |  2      | $var=1 * 2\n'
                    'Деление   "/"       |  2      | $var=1 / 2\n'
                    'Сложение  "+"       |  3      | $var=1 + 2\n'
                    'Вычитание "-"       |  3      | $var=1 - 2```'
                    ),
        keywords='математические операции, математика, скобки, умножение, деление, сложение, вычитание, скобка, плюс, минус, умножить, разделить',
        version_cm_major=3,
        version_cm_minor=2,
        version_cm_build=0,
        version_cm_releaselevel='beta',
        ),
    dict(name='операции сравнения',
        parent_id=1,
        description=(
                    '```\n'
                    ' Операция        | Синтаксис\n'
                    '-----------------|----------\n'
                    'Больше           | >\n'
                    'Меньше           | <\n'
                    'Равно            | =; ==\n'
                    'Неравно          | !; !=\n'
                    'Больше или равно | >=\n'
                    'Меньше или равно | <=```'
                    ),
        keywords='условие, условия, сравнения, сравнение, больше, меньше, равно, неравно, больше или равно, меньше или равно',
        version_cm_major=3,
        version_cm_minor=2,
        version_cm_build=0,
        version_cm_releaselevel='RC1',
        ),
    dict(name='логические операции',
        parent_id=1,
        description=(
                    'Операция                    Синтаксис\n'
                    'Логическое И                &; AND\n'
                    'Логическое ИЛИ              |; OR\n'
                    'Логическое исключающее ИЛИ  ^; XOR'
                    ),
        keywords='условия, сравнения, логические операции, И, ИЛИ, исключающее ИЛИ, and, or, xor',
        version_cm_major=4,
        version_cm_minor=7,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='#name',
        parent_id=2,
        description=('Позволяет задать скрипту имя, которое будет отображаться рядом с названием программы.'),
        syntax='#name "ИмяСкрипта"',
        # parameters=,
        example='#name "СуперБот v1.2"',
        # notes=,
        keywords='#name, name, имя, заголовок, название',
        version_cm_major=4,
        version_cm_minor=6,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='#include',
        parent_id=2,
        description=('Вставляет в это место содержимое текстового файла из папки проекта.\nЭто позволяет "прятать" объемный код, повышая читаемость скрипта.'),
        syntax='#include "ИмяСкрипта"',
        # parameters=,
        example='#include "mylib.cms"',
        # notes=,
        keywords='#include, include, инклюд, подключение, подключение скрипта, подключение библиотеки, вынести код',
        version_cm_major=4,
        version_cm_minor=6,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='#logfile',
        parent_id=2,
        description=('Включает ведение лог-файла в папке проекта, куда дублируется весь вывод через logwrite / print'),
        syntax='#logfile "LogName.txt"',
        # parameters=,
        example='#logfile "debug.txt"',
        # notes=,
        keywords='#logfile, logfile, лог, вывод лога в файл, лог в файл, logwrite в файл, printв файл',
        version_cm_major=4,
        version_cm_minor=8,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='#autorun',
        parent_id=2,
        description=('Автостарт. Сценарий начинает выполняться сразу после загрузки'),
        syntax='#autorun',
        # parameters=,
        # example='',
        # notes=,
        keywords='#autorun, autorun, автостарт, автозапуск, запуск после загрузки',
        version_cm_major=4,
        version_cm_minor=8,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='#ps2_keyboard',
        parent_id=2,
        description=('Включает режим PS/2 клавиатуры'),
        syntax='#ps2_keyboard',
        # parameters=,
        # example='',
        notes='механизм альтернативной симуляции управления, через низкоуровневые порты PS/2. Обязательно наличие PS/2 клавиатуры. В большинстве ноутбуков их клавиатуры и тачпады так же являются PS/2 устройствами. Можете воспользоваться переходником USB-to-PS/2. При режиме PS/2 управление происходит так же, как при обычном режиме, то есть без привязки к конкретному окну',
        keywords='#ps2_keyboard, ps2_keyboard, ps2, режим ps2, ps2 клавиатура',
        version_cm_major=4,
        version_cm_minor=8,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='#ps2_mouse',
        parent_id=2,
        description=('Включает режим PS/2 мыши'),
        syntax='#ps2_mouse',
        # parameters=,
        # example='',
        notes='механизм альтернативной симуляции управления, через низкоуровневые порты PS/2. Обязательно наличие PS/2 мыши. В большинстве ноутбуков их клавиатуры и тачпады так же являются PS/2 устройствами. Можете воспользоваться переходником USB-to-PS/2. При режиме PS/2 управление происходит так же, как при обычном режиме, то есть без привязки к конкретному окну',
        keywords='#ps2_mouse, ps2_mouse, ps2, режим ps2, ps2 мышь',
        version_cm_major=4,
        version_cm_minor=8,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='#define',
        parent_id=2,
        description=('Объявляет макрос - заменяет один текст на другой'),
        syntax='#define find:replace',
        parameters='find - искомая строка\nreplace - на что заменяем',
        example=('переименование lclick в clk:\n'
                '#define clk:lclick\n\n'
                'clk(10,10)\n'
                'clk(20,20)'
                ),
        # notes=,
        keywords='#define, define, макрос, замена текста, замена кода',
        version_cm_major=4,
        version_cm_minor=11,
        version_cm_build=0,
        version_cm_releaselevel='alpha',
        ),
    dict(name='шестнадцатиричная запись',
        parent_id=1,
        description=('Помимо обычного способа написания числа, вы можете использовать шестнадцатиричную запись'),
        syntax='0xFF',
        # parameters=,
        example='число 255 в такой записи будет выглядеть как 0xFF\n а 2018 - как 0x07E2',
        notes='префикс "0x" является обязательным и неизменным',
        keywords='шестнадцатиричная запись, шестнадцатиричное число, шестнадцатиричный формат числа, hex, префикс 0x, 0x префикс',
        version_cm_major=4,
        version_cm_minor=7,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='служебные переменные, координаты и мышь',
        parent_id=3,
        description=(
                'Имя переменной - Значение\n'
                '$_xmouse Текущие координаты мыши по оси Х\n'
                '$_ymouse Текущие координаты мыши по оси Y\n'
                '$_xmax Максимально допустимое значение X, вычисляется из конфигурации рабочего стола\n'
                '$_ymax Максимально допустимое значение Y, (..)\n'
                '$_xmin Минимально допустимое значение X, (..)\n'
                '$_ymin Минимально допустимое значение Y, (..)\n'
                '$_return1 Используется для возврата в неё значения определенными инструкциями\n'
                '$_return2 Используется для возврата в неё значения определенными инструкциями\n'
                '$_cursor Текущий вид указателя мыши (стрелка, палец и т.п.)'
                    ),
        # syntax='',
        # parameters='',
        example='LCLICK($_xmouse, $_ymouse) - клик в текущих координатах\nPRINT($_cursor) - номер текущего вида курсора',
        # notes='',
        keywords='служебные переменные, системные переменные, служебные координаты, xmouse, ymouse, xmax, ymax, xmin, ymin, return1, return2',
        version_cm_major=4,
        version_cm_minor=2,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='служебные переменные, время и дата',
        parent_id=3,
        description=(
                'Имя переменной - Значение\n'
                '$_ms Системный таймер Windows, отсчитывающий миллисекунды с момента старта ОС\n'
                '$_time_t Текущее время в формате Unix-систем\n'
                '$_time_h Текущий час\n'
                '$_time_m Текущая минута\n'
                '$_time_s Текущая секунда\n'
                '$_date_y Текущий год\n'
                '$_date_m Текущий месяц\n'
                '$_date_d Текущие число\n'
                '$_time_str Текущие время\n'
                '$_date_str Текущая дата'
                ),
        # syntax='',
        # parameters='',
        example='PRINT($_date_str, " ", $_time_str) - выводит в лог текущую дату и время',
        # notes='',
        keywords='служебные переменные, системные переменные, служебные время и дата, час, минута, секунда, месяц, год, ms, time_t, time_h, time_m, time_s, date_y, date_m, date_d, time_str, date_str',
        version_cm_major=4,
        version_cm_minor=7,
        version_cm_build=0,
        version_cm_releaselevel='SE',
        ),
    dict(name='служебные переменные, разное',
        parent_id=3,
        description=(
                'Имя переменной - Значение\n'
                '$_hwnd Текущий hwnd привязки (если 0, то привязки к окну нет)\n'
                '$_hwnd_self Собственный hwnd кликера\n'
                '$_pdir Текущая рабочая директория\n'
                '$_ver_self Версия программы\n'
                '$_ver_sys Версия системы\n'
                '$_arch_sys Разрядность системы\n'
                '$_param_str Параметры запуска программы, разделенные ";"'
                ),
        # syntax='',
        # parameters='',
        example='PRINT($_ver_self) - вывести в лог версию программы',
        # notes='',
        keywords='служебные переменные, системные переменные, hwnd привязки, hwnd кликера, текущая рабочая директория, текущая директория, версия программы, версия системы, разрядность системы, параметры программы, hwnd, hwnd_self, pdir, ver_self, ver_sys, arch_sys, param_str',
        version_cm_major=4,
        version_cm_minor=13,
        version_cm_build=14,
        version_cm_releaselevel='',
        ),
)


# --------------------------------------------------------------------------------------------------

'''
    dict(name='',
        # name_isupper=1,
        parent_id=,
        description=(''),
        syntax='',
        # parameters='',
        example='',
        # notes='',
        keywords='',
        version_cm_major=3,
        version_cm_minor=2,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
'''

