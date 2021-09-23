#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Введение
DATA_ELEMENTS = [
    dict(name='математические операции',
         # name_isupper=1,
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
         # name_isupper=1,
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
         # name_isupper=1,
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
         # name_isupper=1,
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
         # name_isupper=1,
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
         # name_isupper=1,
         parent_id=2,
         description=('Включает ведение лог-файла в папке проекта, куда дублируется весь вывод через logwrite / print'),
         syntax='#logfile "LogName.txt"',
         # parameters=,
         example='#logfile "debug.txt"',
         # notes=,
         keywords='#logfile, logfile, лог, вывод лога в файл, лог в файл, logwrite в файл, print в файл',
         version_cm_major=4,
         version_cm_minor=8,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='#autorun',
         # name_isupper=1,
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
         # name_isupper=1,
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
         # name_isupper=1,
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
         # name_isupper=1,
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
    dict(name='#preprocessor',
         # name_isupper=1,
         parent_id=2,
         description=('Вызывает внешний препроцессор'),
         syntax='#preprocessor "debug.dll"',
         parameters='имя в кавычках - библиотека с препроцессором',
         # example='',
         # notes=,
         keywords='#preprocessor, препроцессор, препроцесор, действия до запуска скрипта, действия до запуска кода скрипта, действия перед запуском кода скрипта, действия перед запуском скрипта',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='alpha',
         ),
    dict(name='шестнадцатиричная запись',
         # name_isupper=1,
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
         # name_isupper=1,
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
         example='LCLICK($_xmouse, $_ymouse) - клик в текущих координатах\nLOGWRITE($_cursor) - номер текущего вида курсора',
         # notes='',
         keywords='служебные переменные, системные переменные, служебные координаты, $_xmouse, $_ymouse, $_xmax, $_ymax, $_xmin, $_ymin, $_return1, $_return2, $_cursor',
         version_cm_major=4,
         version_cm_minor=2,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='служебные переменные, время и дата',
         # name_isupper=1,
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
         example='LOGWRITE($_date_str, " ", $_time_str) - выводит в лог текущую дату и время',
         # notes='',
         keywords='служебные переменные, системные переменные, служебные время и дата, час, минута, секунда, месяц, год, $_ms, $_time_t, $_time_h, $_time_m, $_time_s, $_date_y, $_date_m, $_date_d, $_time_str, $_date_str',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='SE',
         ),
    dict(name='служебные переменные, разное',
         # name_isupper=1,
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
         example='LOGWRITE($_ver_self) - вывести в лог версию программы',
         # notes='',
         keywords='служебные переменные, системные переменные, hwnd привязки, hwnd кликера, текущая рабочая директория, текущая директория, версия программы, версия системы, разрядность системы, параметры программы, $_hwnd, $_hwnd_self, $_pdir, $_ver_self, $_ver_sys, $_arch_sys, $_param_str',
         version_cm_major=4,
         version_cm_minor=13,
         version_cm_build=14,
         version_cm_releaselevel='',
         ),
]

# Числа
DATA_ELEMENTS.extend([
    dict(name='define',
         name_isupper=1,
         parent_id=4,
         description=('Объявляет переменную и присваивает ей значение.'),
         syntax='DEFINE($var, [value])',
         parameters=(
                    '$var - символьное имя переменной\n'
                    'value - необязательный параметр; числовое либо строковое значение'
                    ),
         example=(
                'DEFINE($myvar, 5)\n'
                'DEFINE($myvar, 10)\n'
                'LOGWRITE("Value: ", $myvar)'
                ),
         notes='Инструкция сработает только если переменная не была объявлена раньше. В противном случае инструкция игнорируется. Если параметр value опущен, переменная инициализируется нулем',
         keywords='define, дефине, дефинэ, создать переменную, создание переменной',
         version_cm_major=3,
         version_cm_minor=2,
         version_cm_build=0,
         version_cm_releaselevel='RC1',
         ),
    dict(name='undefine',
         name_isupper=1,
         parent_id=4,
         description=('Удаляет переменную из памяти.'),
         syntax='UNDEFINE($var)',
         parameters=('$var - символьное имя переменной'),
         example=(''),
         notes='Если обратиться к удаленной переменной, ее значение представится как 0.\nТак же эта процедура может использоваться для удаления массива и всех его элементов.',
         keywords='undefine, андефине, андефинэ, удалить переменную, удаление переменной',
         version_cm_major=3,
         version_cm_minor=2,
         version_cm_build=0,
         version_cm_releaselevel='RC1',
         ),
    dict(name='inc',
         name_isupper=1,
         parent_id=4,
         description=('Увеличивает значение переменной.'),
         syntax='INC($var, [value])',
         parameters=(
                    '$var - переменная\n'
                    'value - числовое значение, прибавляемое к переменной; необязательный параметр;'
                    ),
         example=(
                'INC($myvar, 5)  // увеличивает значение переменной на 5\n'
                'INC($myvar, -3) // уменьшает значение переменной на 3'
                ),
         notes='Если параметр value не указан, происходит увеличение на 1',
         keywords='inc, увеличение переменной, увеличить переменную, инкремент, increment',
         version_cm_major=3,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='alpha',
         ),
    dict(name='rnd',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Возвращает целое число, выбранное случайно из заданного интервала.'),
         syntax='RND(from, to)',
         parameters=(
                    'from - нижняя граница интервала\n'
                    'to - верхняя граница интервала'
                    ),
         example=('// клик в случайное место\nLCLICK(RND(0, 100), RND(0, 100))'),
         notes='Числа from, to входят в выдаваемые функцией значения',
         keywords='rnd, рнд, случайное число, случаеное целое, случайное из, рандом, рандомное число, random',
         version_cm_major=4,
         version_cm_minor=0,
         version_cm_build=2,
         version_cm_releaselevel='',
         ),
    dict(name='rndfrom',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Возвращает случайно выбранный элемент из заданного набора аргументов.'),
         syntax='RNDFROM(a, b, ...)',
         parameters=('a, b, ... - набор элементов; число параметров функции неограниченно;'),
         example=(
                '$var = RNDFROM(1, "apple", 5)\n'
                'LOGWRITE($var)'
                ),
         # notes='',
         keywords='rndfrom, рндфром, случайный элемент из набора, случайный элемент из последовательности, случайный элемент из нескольких, случайный из, рандомный из',
         version_cm_major=4,
         version_cm_minor=0,
         version_cm_build=2,
         version_cm_releaselevel='',
         ),
    dict(name='int',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Возвращает целую часть числа без округления. Принудительно возвращает число.'),
         syntax='INT(num)',
         parameters=('num - число'),
         example=(
                '$var = INT(25.73)\n'
                'LOGWRITE($var)   // 25'
                ),
         notes='Функция может использоваться для приведения типов данных. Позволяет представить строку как число.\nЕсли вам нужно округлить число до заданной точности, см. функцию ROUND',
         keywords='int, integer, инт, интегер, целое число, сделать целым типом, привести к целому типу, целый тип',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='dist',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Возвращает расстояние между двумя точками.'),
         syntax='DIST(x1, y1, x2, y2)',
         parameters=(
                    'x1, y1 - координаты одной точки\n'
                    'x2, y2 - координаты второй'
                    ),
         # example=(''),
         notes='Функция возвращает результат в виде числа с плавающей точкой',
         keywords='dist, distance, дист, дистанция, расстояние между точками, расстояние между координатами',
         version_cm_major=4,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='sin',
         name_isupper=1,
         parent_id=4,
         description=('Числовая функция. Тригонометрический синус.'),
         syntax='SIN(arg)',
         parameters=('arg - аргумент функции в градусах'),
         example=(
                '// движение мыши по синусоиде\n'
                'FOR($i=0, $i < 500)\n'
                '    $y1 = SIN($i) * 180 / 3.1415\n'
                '    MOVE($i*2, INT($y1) + 300)\n'
                '    WAITMS(100)\n'
                'END_CYC'
                ),
         # notes='',
         keywords='sin, sinus, тригонометрический синус угла',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='cos',
         name_isupper=1,
         parent_id=4,
         description=('Числовая функция. Тригонометрический косинус'),
         syntax='COS(arg)',
         parameters=('arg - аргумент функции в градусах'),
         # example=(''),
         # notes='',
         keywords='cos, cosine, тригонометрический косинус угла',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='arcsin',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Тригонометрический арксинус.'),
         syntax='ARCSIN(arg)',
         parameters=('arg - аргумент функции'),
         example=(
                '$var = SIN(30)  // sin(30) = 0.5\n'
                'LOGWRITE($var)\n'
                '$var = ARCSIN($var) // arcsin(0.5) = 30\n'
                'LOGWRITE($var)'
                ),
         notes='В тригонометрическом смысле, является обратной синусу функцией. Позволяет по известному значению функции синуса получить ее исходный аргумент.',
         keywords='arcsin, arcsinus, арксинус, обратный синусу',
         version_cm_major=4,
         version_cm_minor=11,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='arccos',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Тригонометрический арккосинус.'),
         syntax='ARCCOS(arg)',
         parameters=('arg - аргумент функции'),
         # example=(''),
         notes='В тригонометрическом смысле, является обратной косинусу функцией. Позволяет по известному значению функции косинуса получить ее исходный аргумент.',
         keywords='arccos, arccosine, арккосинус, обратный косинусу',
         version_cm_major=4,
         version_cm_minor=11,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='sqrt',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Квадратный корень числа.'),
         syntax='SQRT(arg)',
         parameters=('arg - аргумент функции'),
         # example=(''),
         # notes='',
         keywords='sqrt, квадрутный корень числа',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='pow',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Возведение числа в степень.'),
         syntax='POW(arg, power)',
         parameters=(
                    'arg - число\n'
                    'ower - степень'
                    ),
         # example=(''),
         # notes='',
         keywords='pow, power, возведение в степень числа, возведение числа в степень, число в степень',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='SE',
         ),
    dict(name='abs',
         name_isupper=1,
         parent_id=4,
         description=('Числовая функция. Возвращает модуль числа'),
         syntax='ABS(arg)',
         parameters=('arg - число'),
         # example=(''),
         notes='Функция появилась давно, ещё с версии 4.8 но её забыли внести в справку. Добавили только в 4.12.001',
         keywords='abs, absolute, модуль числа, число по модулю',
         version_cm_major=4,
         version_cm_minor=8,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='round',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Округляет число до заданной точности.'),
         syntax='ROUND(arg, prec)',
         parameters=(
                    'arg - число\n'
                    'prec - точность'
                    ),
         example=(
                '$r = ROUND(1236, 1)   // $r = 1240\n'
                '$r = ROUND(1236, 2)   // $r = 1200\n'
                '$r = ROUND(1.236, -2) // $r = 1.24\n'
                '$r = ROUND(1.236, -1) // $r = 1.2\n'
                '$r = ROUND(1.236, 0)  // $r = 1'
                ),
         notes='Округление происходит в сторону от нуля. То есть prec = 2 округлит число до сотен, а prec = -2 до сотых (два знака после точки).\nОкругление происходит по хрен пойми какому правилу, это не математическое по правилу 0.5 и не банковское - до ближайшего чётного. Похоже на обратное банковскому, но с исключениями.',
         keywords='round, округление числа, округлить число',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='arrpush',
         name_isupper=1,
         parent_id=4,
         description=('Добавляет элемент в конец массива.'),
         syntax='ARRPUSH($arr, value)',
         parameters=(
                    '$arr - массив\n'
                    'value - число либо строка'
                    ),
         example=(
                'ARRPUSH($arr, 435)\n'
                'ARRPUSH($arr, 532)\n'
                'ARRPUSH($arr, 943)\n'
                'LOGWRITE($arr[0])\n'
                'LOGWRITE($arr[1])\n'
                'LOGWRITE($arr[2])'
                ),
         # notes='',
         keywords='arrpush, аррпуш, добавить в массив, добавить к массиву, занести в массив, масив, пополнить массив',
         version_cm_major=4,
         version_cm_minor=8,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='arrpop',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Извлекает из массива последний элемент.'),
         syntax='ARRPOP($arr)',
         parameters=('$arr - массив'),
         example=(
                'ARRPUSH($arr, 435)\n'
                'ARRPUSH($arr, 532)\n'
                'ARRPUSH($arr, 943)\n'
                'LOGWRITE(ARRPOP($arr))\n'
                'LOGWRITE(ARRPOP($arr))\n'
                'LOGWRITE(ARRPOP($arr))'
                ),
         notes='Извлечение подразумевает возвращение значения и удаление элемента из массива. Если результат не нужен и хотим просто удалить последний элемент, всё равно обязательно присвоить результат переменной\n$temp = ARRPOP($arr)',
         keywords='arrpop, аррпоп, извлечь из массива, извлечь элемент из массива, получить элемент из массива, получить значение из массива, получить последний элемент массива, масив',
         version_cm_major=4,
         version_cm_minor=8,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='arrsize',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Возвращает количество элементов в массиве.'),
         syntax='ARRSIZE($arr)',
         parameters=('$arr - массив'),
         example=(
                'ARRPUSH($arr, 435)\n'
                'ARRPUSH($arr, 532)\n'
                'ARRPUSH($arr, 943)\n'
                'LOGWRITE(ARRSIZE($arr))\n'
                'LOGWRITE(ARRPOP($arr))\n'
                'LOGWRITE(ARRSIZE($arr))'
                ),
         notes='Не стоит забывать, что индексация массива идет от нуля, поэтому максимально доступный индекс всегда будет ARRSIZE()-1',
         keywords='arrsize, аррсизе, аррсайз, количество элементов в массиве, длина массива, размер массива',
         version_cm_major=4,
         version_cm_minor=8,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='arrsort',
         name_isupper=1,
         parent_id=4,
         description=('Сортирует элементы массива по возрастанию.'),
         syntax='ARRSORT($arr)',
         parameters=('$arr - массив'),
         example=(
                '// генерация массива\n'
                'FOR($a=0, $a < 10)\n'
                '   $arr[$a] = RND(0, 9)\n'
                '   LOGWRITE($arr[$a])\n'
                'END_CYC\n'
                '\n'
                '// сортировка\n'
                'ARRSORT($arr)\n'
                '\n'
                '// вывод результата\n'
                'LOGWRITE("sort:")\n'
                'FOR($a=0, $a < 10)\n'
                '   LOGWRITE($arr[$a])\n'
                'END_CYC\n'
                '\n'
                'HALT'
                ),
         # notes='',
         keywords='arrsort, аррсорт, сортировка массива, сортировать массив, отсортировать массив, сортировать по возрастанию',
         version_cm_major=4,
         version_cm_minor=13,
         version_cm_build=14,
         version_cm_releaselevel='',
         ),
    dict(name='arrconcat',
         name_isupper=1,
         parent_id=4,
         description=('Объединяет несколько массивов, последовательно добавляя элементы в конец.'),
         syntax='ARRCONCAT($arr_in, $arr1, $arr2, ... )',
         parameters=(
                    '$arr_in - принимающий массив\n'
                    '$arr1, $arr2, ... - массивы для добавления'
                    ),
         example=(
                '// генерация двух массивов\n'
                'FOR($a=0, $a < 3)\n'
                '   $var1[$a] = RND(0, 9)\n'
                '   LOGWRITE($var1[$a])\n'
                '\n'
                '   $var2[$a] = RND(0, 9)\n'
                '   LOGWRITE($var2[$a])\n'
                'END_CYC\n'
                '\n'
                'LOGWRITE("")\n'
                'ARRCONCAT($var_in, $var1, $var2)\n'
                '\n'
                '// вывод объединенного массива\n'
                'FOR($a=0, $a < 6)\n'
                '   LOGWRITE($var_in[$a])\n'
                'END_CYC\n'
                '\n'
                'HALT'
                ),
         notes='Данная инструкция не очищает массив $arr_in.',
         keywords='arrconcat, аррконкат, аррконкэт, добавление массива к массиву, добавление к массиву массива, добавить элементы из массива в другой массив, объединить массивы, объединение массивов, слить массивы, слияние массивов',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='setvar',
         name_isupper=1,
         parent_id=4,
         description=('Присваивает значение переменной по ее имени.'),
         syntax='SETVAR($var, value)',
         parameters=(
                    '$var - строка, содержащая имя переменной\n'
                    'value - присваемое значение'
                    ),
         example=(
                '// подпрограмма, умножающая переменную на три\n'
                '// имя переменной принимается в виде строки\n'
                'SUB(triple, $triple_var)\n'
                '   $tmp = GETVAR($triple_var)\n'
                '   SETVAR($triple_var, $tmp * 3)\n'
                'END_SUB\n'
                '\n'
                '// инициализация\n'
                '$var = 10\n'
                '\n'
                '// вызов подпрограммы\n'
                'triple("$var")\n'
                '\n'
                '// вывод обновленной переменной\n'
                'LOGWRITE($var)\n'
                'HALT\n'
                ),
         notes='К моменту вызова переменная с указанным именем должна существовать',
         keywords='setvar, сетвар, присвоить значение переменной по имени, переменная по имени',
         version_cm_major=4,
         version_cm_minor=12,
         version_cm_build=1,
         version_cm_releaselevel='',
         ),
    dict(name='getvar',
         name_isupper=1,
         parent_id=4,
         description=('Функция. Возвращает значение переменной по ее имени.'),
         syntax='GETVAR($var)',
         parameters=('$var - строка, содержащая имя переменной'),
         example=(
                '// подпрограмма, умножающая переменную на три\n'
                '// имя переменной принимается в виде строки\n'
                'SUB(triple, $triple_var)\n'
                '   $tmp = GETVAR($triple_var)\n'
                '   SETVAR($triple_var, $tmp * 3)\n'
                'END_SUB\n'
                '\n'
                '// инициализация\n'
                '$var = 10\n'
                '\n'
                '// вызов подпрограммы\n'
                'triple("$var")\n'
                '\n'
                '// вывод обновленной переменной\n'
                'LOGWRITE($var)\n'
                'HALT\n'
                ),
         notes='К моменту вызова переменная с указанным именем должна существовать',
         keywords='getvar, гетвар, вывести значение переменной по имени, переменная по имени',
         version_cm_major=4,
         version_cm_minor=12,
         version_cm_build=1,
         version_cm_releaselevel='',
         ),
])

# Строки
DATA_ELEMENTS.extend([
    dict(name='strlen',
         name_isupper=1,
         parent_id=5,
         description=('Функция. Возвращает длину входной строки в символах.'),
         syntax='STRLEN(str)',
         parameters=('str - строка; входная строка'),
         example=(
                'LOGWRITE(STRLEN("lol") )\n'
                '// результат "3"'
                ),
         # notes='',
         keywords='strlen, стрлен, длина строки в символах, количество символов в строке',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='strcut',
         name_isupper=1,
         parent_id=5,
         description=('Функция. Возвращает подстроку из входной строки.'),
         syntax='STRCUT(str, begin, size)',
         parameters=(
                    'str - входная строка\n'
                    'begin - позиция начала копирования\n'
                    'size - количество копируемых символов'
                    ),
         example=(
                'LOGWRITE(STRCUT("hello2000", 6, 2 ))\n'
                '// результат "20"'
                ),
         # notes='',
         keywords='strcut, стркат, вырезать подстроку в строке, вернуть подстроку в строке, вырезать подстроку из строки, вернуть подстроку из строки',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='strcut2',
         name_isupper=1,
         parent_id=5,
         description=('Функция. Возвращает подстроку из входной строки.'),
         syntax='STRCUT2(str, begin, end)',
         parameters=(
                    'str - входная строка\n'
                    'begin - позиция начала копирования\n'
                    'end - позиция конца копирования'
                    ),
         example=(
                'LOGWRITE(STRCUT2("hello2000", 2, 5 ))\n'
                '// результат "ello"'
                ),
         # notes='',
         keywords='strcut2, стркат2, вырезать подстроку в строке, вернуть подстроку в строке, вырезать подстроку из строки, вернуть подстроку из строки',
         version_cm_major=4,
         version_cm_minor=6,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='strfilter',
         name_isupper=1,
         parent_id=5,
         description=('Функция. Возвращает строку, из которой удаляются определенные символы.'),
         syntax='STRFILTER(str, set, mode)',
         parameters=(
                    'str - входная строка\n'
                    'set - набор символов маски\n'
                    'mode - режим фильтрации\n\n'
                    'Режим фильтрации\n'
                    'Если режим будет задан как 0, \nто из входной строки будут вырезаны все символы, указанные в маске\n'
                    'Если режим будет задан как 1, \nто из входной строки будут вырезаны все символы, кроме указанных в маске'
                    ),
         example=(
                'LOGWRITE(STRFILTER("hello2000", "20", 0 ))\n'
                '// результат "hello"\n'
                'LOGWRITE(STRFILTER("hello2000", "20", 1 ))\n'
                '// результат "2000"\n'
                ),
         # notes='',
         keywords='strfilter, стрфильтр, стрфилтер, фильтр строки, фильтр символов в строке, удалить символы из строки',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='strpos',
         name_isupper=1,
         parent_id=5,
         description=('Функция. Возвращает позицию начала искомой подстроки во входной строке.'),
         syntax='STRPOS(str, substr, [offset])',
         parameters=(
                    'str - входная строка\n'
                    'substr - искомая подстрока\n'
                    'offset - необязательный параметр; смещение позиции, с которой начинается поиск'
                    ),
         example=(
                '$search = "mind"\n'
                '$r = STRPOS("where is my mind", $search)\n'
                'LOGWRITE($r)  // результат 13 (с 13 символа начинается подстрока)\n'
                '\n'
                '$var = "abcabc"\n'
                '$r = STRPOS($var, "a", 3)\n'
                'LOGWRITE($r)  // результат 4, так как смещение на 3 пропускает первый символ "a"'
                ),
         notes='По умолчанию offset равен 1. Этот параметр не может быть меньше, чем 1.',
         keywords='strpos, стрпос, найти подстроку в строке, поиск подстроки в строке, поиск символов в строке, найти строку, поиск строки',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='strconcat',
         name_isupper=1,
         parent_id=5,
         description=('Функция. Возвращает объединенную строку, состоящую из других строк.'),
         syntax='STRCONCAT(str1, str2, ...)',
         parameters=('str1, str2, ... - входные строки'),
         example=('LOGWRITE(STRCONCAT("hello", "2000", "!!!"))  // результат "hello2000!!!"'),
         # notes='',
         keywords='strconcat, стрконкат, контактация строки, объединить строки, объединение строк',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='strreplace',
         name_isupper=1,
         parent_id=5,
         description=('Функция. Возвращает результирующую строку, в которой искомая подстрока заменяется на другую строку.'),
         syntax='STRREPLACE(str, find, replace)',
         parameters=(
                    'str - входная строка\n'
                    'find - искомая подстрока\n'
                    'replace - заменяющая строка'
                    ),
         example=(
                '$s = STRREPLACE("Hello, %username%!!!", "%username%", "John")\n'
                'LOGWRITE($s)  // результат "Hello, John!!!"'
                ),
         # notes='',
         keywords='strreplace, стрреплэйс, заменить подстроку в строке, заменить подстроку на другую подстроку, заменить часть строки, поменять часть строки',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='strmd5',
         name_isupper=1,
         parent_id=5,
         description=('Функция. Возвращает md5 хеш для входной строки.'),
         syntax='STRMD5(str)',
         parameters=('str - строка'),
         example=('LOGWRITE(STRMD5("123"))  // 202CB962AC59075B964B07152D234B70'),
         # notes='',
         keywords='strmd5, md5 хэш строки, md5 хеш строки',
         version_cm_major=4,
         version_cm_minor=6,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='strseparate',
         name_isupper=1,
         parent_id=5,
         description=('Разбивает строку на подстроки, которые помещаются в массив.'),
         syntax='STRSEPARATE(str, substr, $arr)',
         parameters=(
                    'str - входная строка\n'
                    'substr - строка-разделитель\n'
                    '$arr - выходной массив'
                    ),
         example=(
                '$str = "one,two,three"\n'
                'STRSEPARATE($str, ",", $arr)\n'
                'LOGWRITE($arr[1])  // "two"'
                ),
         # notes='',
         keywords='strseparate, разбить строку по разделителю, разделить строку по разделителю, разбить строку в массив, разделить строку в массив',
         version_cm_major=4,
         version_cm_minor=11,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='char',
         name_isupper=1,
         parent_id=5,
         description=('Функция. Возвращает символ по его коду.'),
         syntax='CHAR(code)',
         parameters=('code - числовой код символа'),
         example=(
                '// генерация строки из случайных\n'
                '// символов a..z длинной 10\n'
                '$str = ""\n'
                'FOR($i=0, $i < 10)\n'
                '   $chr = CHAR(RND(97, 122))\n'
                '   $str = STRCONCAT($str, $chr)\n'
                'END_CYC\n'
                '\n'
                'LOGWRITE($str)'
                ),
         notes='Обратите внимание, что используются коды из таблицы юникода. Не путать с ASCII. Таблица кодов доступна в интернете. Например, [здесь](http://unicode-table.com/ru/).',
         keywords='char, чар, вернуть символ по коду, узнать символ по коду, есть код нужен символ',
         version_cm_major=4,
         version_cm_minor=13,
         version_cm_build=14,
         version_cm_releaselevel='',
         ),
    dict(name='code',
         name_isupper=1,
         parent_id=5,
         description=('Функция. Возвращает код, соответствующий символу.'),
         syntax='CODE(char)',
         parameters=('char - символ'),
         example=(
                '// Латинский символ A\n'
                '$chr = "A"\n'
                'LOGWRITE(CODE($chr))'
                ),
         notes='Символы Юникода поддерживаются.',
         keywords='code, коде, вернуть код по символу, узнать код по символу, есть символ нужен код',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
])

# Текстовые файлы
DATA_ELEMENTS.extend([
    dict(name='iniread',
         name_isupper=1,
         parent_id=6,
         description=('Функция. Считывает параметр из файла конфгурации (*.ini).'),
         syntax='INIREAD(filename, parname, [section])',
         parameters=(
                    'filename - строка; имя ini файла\n'
                    'parname - строка; имя параметра в ini файле\n'
                    'section - строка, необязательный параметр; название секции в ini файле'
                    ),
         example=(
                '$str = INIREAD("config.ini", "var")\n'
                'LOGWRITE($str)'
                ),
         notes='По умолчанию section имеет значение "default"',
         keywords='iniread, иниреад, чтение из ини файла конфгурации, чтение из ini файла конфгурации, чтение параметра из ини файла конфгурации, чтение параметра из ini файла конфгурации, чтение файла конфигурации ini, чтение из файла конфигурации ini',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='iniwrite',
         name_isupper=1,
         parent_id=6,
         description=('Записывает параметр из файла конфгурации (*.ini).'),
         syntax='INIWRITE(filename, parname, value, [section])',
         parameters=(
                    'filename - строка; имя ini файла\n'
                    'parname - строка; имя параметра в ini файле\n'
                    'value - строка; записываемое значение\n'
                    'section - строка, необязательный параметр; название секции в ini файле'
                    ),
         example=('INIWRITE("config.ini", "var", "23")'),
         notes='По умолчанию section имеет значение "default"',
         keywords='iniwrite, иниврайт, запись в ини файл конфгурации, запись в ini файл конфгурации, запись параметра в ини файл конфгурации, запись параметра в ini файл конфгурации, запись файла конфигурации ini, запись в файл конфигурации ini',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='tfread',
         name_isupper=1,
         parent_id=6,
         description=('Функция. Считывает произвольную строку из текстового файла.'),
         syntax='TFREAD(file, str_n)',
         parameters=(
                    'file - имя файла\n'
                    'str_n - номер строки в файле'
                    ),
         example=('LOGWRITE(TFREAD("input.txt", 5))'),
         # notes='',
         keywords='tfread, тфреад, чтение из файла, читать из файла, чтение строки из файла, читать строку из файла, чтение текстового файла, чтение строки из текстового файла, читать из текстового файла',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='SE',
         ),
    dict(name='tfwrite',
         name_isupper=1,
         parent_id=6,
         description=('Записывает строку в текстовый файл. Возможна произвольная вставка.'),
         syntax='TFWRITE(file, str, [str_n])',
         parameters=(
                    'file - имя файла\n'
                    'str - строка\n'
                    'str_n - необязательный параметр; номер строки в файле'
                    ),
         example=('TFWRITE("input.txt", "Hello")'),
         notes='Новая строка записывается в файл на позицию str_n. При этом все строки (включая ту, которая была ранее на этой позиции) сдвигаются вниз. Если параметр str_n не задан, то новая строка добавляется в конец файла.',
         keywords='tfwrite, тфврайт, запись в файл, писать в файл, запись строки в файл, писать строку в файл, запись текстового файла, запись строки в текстовый файл, писать в текстовый файл',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='SE',
         ),
    dict(name='tfreadarr',
         name_isupper=1,
         parent_id=6,
         description=('Считывает текстовый файл в массив, помещая каждую строку в отдельный элемент массива.'),
         syntax='TFREADARR(file, $arr)',
         parameters=(
                    'file - имя файла\n'
                    '$arr - массив'
                    ),
         example=(
                'TFREADARR("C:\\out.txt", $arr)\n'
                'LOGWRITE($arr[0])\n'
                'LOGWRITE($arr[1])'
                ),
         # notes='',
         keywords='tfreadarr, тфреадарр, чтение из файла в массив, читать из файла в массив, чтение текстового файла в массив, читать из текстового файла в массив, загрузить из файла в массив, загрузить строки из файла в массив',
         version_cm_major=4,
         version_cm_minor=11,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='tfwritearr',
         name_isupper=1,
         parent_id=6,
         description=('Записывает массив в файл путем помещения каждого элемента массива в отдельную строку.'),
         syntax='TFWRITEARR(file, $arr)',
         parameters=(
                    'file - имя файла\n'
                    '$arr - массив'
                    ),
         example=(
                '$arr[0] = "one"\n'
                '$arr[1] = "two\n'
                'TFWRITEARR("out.txt", $arr)'
                ),
         notes='',
         keywords='tfwritearr, тфврайтарр, запись из массива в файл, писать из массива в файл, запись массива в текстовый файл, писать массив в текстовый файл, загрузить из массива в файл, загрузить строки из массива в файл, загрузить элементы из массива в файл',
         version_cm_major=4,
         version_cm_minor=11,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='tfdelete',
         name_isupper=1,
         parent_id=6,
         description=('Удаляет строку из текстового файла.'),
         syntax='TFDELETE(file, str_n)',
         parameters=(
                    'file - имя файла\n'
                    'str_n - номер строки в файле'
                    ),
         example=('TFDELETE("input.txt", 2)'),
         notes='При удалении все строки ниже удаляемой сдвигаются вверх.',
         keywords='tfdelete, тфделете, тфделит, удаляет строку из текстового файла, удаляет строку из файла, удалить строку из текстового файла, удалить строку из файла, в файле удалить строку по номеру',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='SE',
         ),
    dict(name='tfclear',
         name_isupper=1,
         parent_id=6,
         description=('Очищает содержимое текстового файла.'),
         syntax='TFCLEAR(file, [delete])',
         parameters=(
                    'file - имя файла\n'
                    'delete - необязательный параметр; флаг удаления файла'
                    ),
         example=('TFCLEAR("input.txt")'),
         notes='Если параметр flag = 1, то файл удаляется с жесткого диска, если 0, то просто очищается. По умолчанию 0',
         keywords='tfclear, тфклеар, тфклир, очищает содержимое текстового файла, очищает содержимое файла, очистить содержимое текстового файла, очистить содержимое файла, очистить текстовый файл, очистить файл',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='SE',
         ),
    dict(name='tfcount',
         name_isupper=1,
         parent_id=6,
         description=('Функция. Возвращает количество строк в текстовом файле.'),
         syntax='TFCOUNT(file)',
         parameters=('file - имя файла'),
         example=('LOGWRITE(TFCOUNT("input.txt"))'),
         # notes='',
         keywords='tfcount, тфкоунт, возвращает количество строк в текстовом файле, возвращает количество строк в файле, вернуть количествово строк в текстовом файле, вернуть количество строк в файле, узнать количествово строк в текстовом файле, узнать количествово строк в файле, сколько строк в текстовом файле, сколько строк в файле',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='SE',
         ),
    dict(name='strreadln',
         name_isupper=1,
         parent_id=6,
         description=('Функция. Считывает произвольную строку из текстового файла.'),
         syntax='STRREADLN(file, str_n)',
         parameters=(
                    'file - имя файла\n'
                    'str_n - номер строки в файле'
                    ),
         example=('LOGWRITE(STRREADLN("input.txt", 5)) // результат (пятая строка из этого файла)'),
         notes='Схожего поведения можно добиться используя более современную функцию TFREAD',
         keywords='strreadln, стрреадлн, чтение из файла, читать из файла, чтение строки из файла, читать строку из файла, чтение текстового файла, чтение строки из текстового файла, читать из текстового файла',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='strwriteln',
         name_isupper=1,
         parent_id=6,
         description=('Функция. Записывает строку в конец файла.'),
         syntax='STRWRITELN(file, str, [rewrite])',
         parameters=(
                    'file - имя файла\n'
                    'str - строка\n'
                    'rewrite - необязательный параметр; флаг перезаписи'
                    ),
         example=(
                '// Этот код записывает в файл "out.txt" строки вида "Random:N",\n'
                '// где N - случайное число от 1 до 9\n'
                'STRWRITELN("out.txt", STRCONCAT("Random:", RND(1,9)))'
                ),
         notes='Если файла с таким именем еще не существует, он будет создан. Если rewrite = 1, то перед записью строки все содержимое файла будет удалено.\nСхожего поведения можно добиться используя более современные TFREAD и TFCLEAR.',
         keywords='strwriteln, стрврайтлн, запись в файл, писать в файл, запись строки в файл, писать строку в файл, запись текстового файла, запись строки в текстовый файл, писать в текстовый файл',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
])

# Текстовые файлы
DATA_ELEMENTS.extend([
    dict(name='fcreate',
         name_isupper=1,
         parent_id=7,
         description=('Создает пустой файл или каталог по указанному пути.'),
         syntax='FCREATE(path, [isfile])',
         parameters=(
                    'path - путь для создаваемого объекта\n'
                    'isfile - необязательный параметр; признак файла'
                    ),
         example=(
                'FCREATE("C:\\mypath")\n'
                'FCREATE("C:\\mypath\\hello.txt", 1)'
                ),
         notes='Если параметр isfile не задан, то инструкция создаст каталог, в противном случае будет создан пустой файл.',
         keywords='fcreate, фкриэйт, фкреатэ, создать каталог по указанному пути, создать папку по указанному пути, создать директорию по указанному пути, создать файл на диске по указанному пути, создать пустой файл на диске по указанному пути',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='fcopy',
         name_isupper=1,
         parent_id=7,
         description=('Копировать файл или каталог по указанному пути.'),
         syntax='FCOPY(path1, path2)',
         parameters=(
                    'path1 - объект для копирования\n'
                    'path2 - новое размещение'
                    ),
         example=(
                '// Копирование каталога\n'
                'FCOPY("C:\\mypath", "C:\\mypath2")\n'
                '\n'
                '// Копирование файла\n'
                'FCOPY("C:\\mypath\\hello.txt", "C:\\mypath2\\hello.txt")\n'
                '\n'
                '// Копирование файла с новым именем\n'
                'FCOPY("C:\\mypath\\hello.txt", "C:\\mypath2\\goodbye.txt")'
                ),
         notes='Каталоги копируются со всем содержимым. В случае совпадения имен файлов, они будут перезаписаны. При копирования объекта ему можно задать другое имя.',
         keywords='fcopy, фкопи, копировать каталог по указанному пути, копировать файл по указанному пути, копировать каталог на диске, копировать файл на диске',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='fdelete',
         name_isupper=1,
         parent_id=7,
         description=('Удаляет файл или каталог по указанному пути.'),
         syntax='FDELETE(path)',
         parameters=('path - объект для удаления'),
         example=(
                '// Удаление каталога\n'
                'FDELETE("C:\\mypath2")'
                ),
         notes='Каталог будет удален вне зависимости от своего содержимого.',
         keywords='fdelete, фделит, фделитэ, удалить каталог по указанному пути, удалить папку по указанному пути, удалить директорию по указанному пути, удалить файл на диске по указанному пути, удалить файл с диска по указанному пути',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='fexists',
         name_isupper=1,
         parent_id=7,
         description=('Функция. Проверяет наличие файла или каталога по указанному пути.'),
         syntax='FEXISTS(path)',
         parameters=('path - путь к объекту'),
         example=(
                '// Проверка наличия каталога\n'
                'IF(FExists("C:\\mypath2"))\n'
                '   LOGWRITE("exists")\n'
                'ELSE\n'
                '   LOGWRITE("nope")\n'
                'END_IF'
                ),
         # notes='',
         keywords='fexists, фэкзист, фэксист, проверить наличие файла по указанному пути, проверить наличие папки по указанному пути, проверить наличие каталога по указанному пути, проверить наличие директории по указанному пути',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='fsize',
         name_isupper=1,
         parent_id=7,
         description=('Функция. Возвращает размер файла.'),
         syntax='FSIZE(path)',
         parameters=('path - путь к файлу'),
         example=(
                '// Получение списка файлов\n'
                'GetFileList($arr, "C:\\*.*")\n'
                '\n'
                '// Вывод файла и его размера\n'
                'FOR($i=0, $i < arrsize($arr))\n'
                '   $fullname = STRCONCAT("C:\\", $arr[$i])\n'
                '   LOGWRITE($arr[$i], " : ", FSIZE($fullname), " bytes")\n'
                'END_CYC'
                ),
         notes='Если доступ к файлу невозможно получить, то функция вернет -1.',
         keywords='fsize, фсайз, фсизэ, получить размер файла на диске, узнать размер файла на диске',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='freaddata',
         name_isupper=1,
         parent_id=7,
         description=('Считывает блок информации из файла в байтовый массив'),
         syntax='FREADDATA(path, $arr, [start], [count])',
         parameters=(
                    'path - путь к объекту\n'
                    '$arr - получаемый массив\n'
                    'start - необязательный параметр; позиция начала считывания\n'
                    'count - необязательный параметр; количество считываемых байт'
                    ),
         example=(
                '$str = ""\n'
                '\n'
                '// Считывание из exe файла 39 байт начиная с 79\n'
                'FREADDATA("C:\\Windows\\notepad.exe", $var, 78, 39)\n'
                '\n'
                '// Перевод массива байт в строку символов\n'
                'FOR($i=0, $i < 39)\n'
                '   $str = STRCONCAT($str, CHAR($var[$i]))\n'
                'END_CYC\n'
                '\n'
                '// "This program cannot be run in DOS mode."\n'
                'LOGWRITE($str)'
                ),
         notes='Считывание начинается с позиции start. Если параметр start не задан, то он равен 0, то есть началу файла. Если параметр count не задан, то он равен 0, что считается размером целого файла. Итоговый размер полученного массива будет соответствовать количеству считанных байт.',
         keywords='freaddata, aреаддата, читать байты из файла в массив, прочитать байты из файла в массив, читать информацию из файла в массив, прочитать информацию из файла в массив, считать информацию из файла в массив, читать из файла в массив, прочитать из файла в массив, считать из файла в массив',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='fwritedata',
         name_isupper=1,
         parent_id=7,
         description=('Записывает блок информации в файл из байтового массива.'),
         syntax='FWRITEDATA(path, $arr, [start], [count])',
         parameters=(
                    'path - путь к объекту\n'
                    '$arr - входной массив\n'
                    'start - необязательный параметр; позиция начала записи\n'
                    'count - необязательный параметр; количество записываемых байт'
                    ),
         example=(
                '// Замена в текстовом файле всех символов A на Z\n'
                'FREADDATA("text.txt", $arr)\n'
                '\n'
                'FOR($i=0, $i < ARRSIZE($arr))\n'
                '   IF(CHAR($arr[$i]) == "A")\n'
                '      $arr[$i] = CODE("Z")\n'
                '   END_IF\n'
                'END_CYC\n'
                '\n'
                'FWRITEDATA("text.txt", $arr)'
                ),
         notes='Запись в файл начинается с позиции start. Если параметр не задан, то он равен 0, то есть началу файла. Если параметр count не задан, то он равен 0, что считается размером массива $arr. В ином случае, в указанную позицию файла побайтово осуществляется запись первых count элементов от начала массива. При этом изначальные байты файла заменяются соответствующими байтами из массива. В случае, если размер перезаписываемого файла меньше размера массива, либо из-за смещения блок данных выходит за границы файла, то файл будет увеличен на соответствующее количество байт.',
         keywords='fwritedata, фврайтдата, записать байтов из массива в файл, запись байты из массива в файл, записать информацию из массива в файл, запись информации из массива в файл, записать из массива в файл, запись из массива в файл',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='getfilelist',
         name_isupper=1,
         parent_id=7,
         description=('Помещает в массив список файлов, найденных согласно маске.'),
         syntax='GETFILELIST($arr, [dir])',
         parameters=(
                    '$arr - принимающий массив\n'
                    'dir - адрес, содержащий маску выборки'
                    ),
         example=(
                '// пример1 вывод всех файлов из C:\n'
                'GETFILELIST($arr, "C:\\*.*")\n'
                'FOR($i=0, $i < ARRSIZE($arr))\n'
                '   LOGWRITE($arr[$i])\n'
                'END_CYC\n'
                '\n'
                'HALT\n'
                '\n'
                '// пример2 вывод файлов sys из C:\n'
                'GETFILELIST($arr, "C:\\*.sys")\n'
                'FOR($i=0, $i < ARRSIZE($arr))\n'
                '   LOGWRITE($arr[$i])\n'
                'END_CYC\n'
                '\n'
                'HALT'
                ),
         notes='Путь должен обязательно содержать маску. По умолчанию путь равен "*".',
         keywords='getfilelist, гетфилелист, получить список файлов в массив, считать список файлов в массив, получить список файлов из папки в массив, считать список файлов из каталога в массив, получить список файлов в папке, получить список файлов в каталоге, получить список файлов в директории',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='getdirlist',
         name_isupper=1,
         parent_id=7,
         description=('Помещает в массив список каталогов, найденных согласно маске.'),
         syntax='GETDIRLIST($arr, [dir])',
         parameters=(
                    '$arr - принимающий массив\n'
                    'dir - необязательный параметр; адрес, содержащий маску выборки'
                    ),
         example=(
                '// вывод всех каталогов на C:\n'
                'GETDIRLIST($arr, "C:\\*")\n'
                '\n'
                'FOR($i=0, $i < ARRSIZE($arr))\n'
                '   LOGWRITE($arr[$i])\n'
                'END_CYC\n'
                '\n'
                'HALT'
                ),
         notes='Путь должен обязательно содержать маску. По умолчанию путь равен "*". ',
         keywords='getdirlist, гетдирлист, получить список каталогов в массив, считать список каталогов в массив, получить список папок в массив, считать список папок в массив, получить список директорий в массив, считать список директорий в массив',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
])

# Мышь
DATA_ELEMENTS.extend([
    dict(name='lclick',
         name_isupper=1,
         parent_id=8,
         description=('Делает клик левой клавишей мышки в указанной точке.'),
         syntax='LCLICK(x, y)',
         parameters=('x, y - координаты точки на экране'),
         example=(
                '// клик в координаты 10:10\n'
                'LCLICK(10, 10)\n'
                '\n'
                '// клик в текущие координаты курсора\n'
                'LCLICK($_xmouse, $_ymouse)'
                ),
         # notes='',
         keywords='lclick, лклик, клик лкм, клик левой клавишей мышки по координатам, клик левой клавишей мыши по координатам, клик мышкой, клик курсором, клик по координатам, левый клик мыши, нажать левой клавишей мышки по координатам, нажать левой клавишей мыши по координатам, нажать мышкой, нажать курсором, нажать по координатам, нажать левую клавишу мышки в указанной точке, нажать левую клавишу мыши в указанной точке',
         version_cm_major=1,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='ldown',
         name_isupper=1,
         parent_id=8,
         description=('Зажимает левую клавишу мышки в указанной точке.'),
         syntax='LDOWN(x, y)',
         parameters=('x, y - координаты точки на экране'),
         example=(
                '// перетаскивание из точки 10:10 в точку 20:20\n'
                'LDOWN(10, 10)\n'
                'WAITMS(300)\n'
                'LUP(20, 20)'
                ),
         # notes='',
         keywords='ldown, лдовн, зажать лкм, нажать левой клавишей мышки по координатам, нажать левой клавишей мыши по координатам, нажать мышкой, нажать курсором, нажать по координатам, нажать левую клавишу мышки в указанной точке, нажать левую клавишу мыши в указанной точке, зажать левой клавишей мышки по координатам, зажать левой клавишей мыши по координатам, зажать мышкой, зажать курсором, зажать по координатам, зажать левую клавишу мышки в указанной точке, зажать левую клавишу мыши в указанной точке, зажать и держать левой клавишей мышки по координатам, зажать и держать левой клавишей мыши по координатам, зажать и держать мышкой, зажать и держать курсором, зажать курсором и держать, зажать по координатам и держать, зажать и держать по координатам, зажать и держать левую клавишу мышки в указанной точке, зажать и держать левую клавишу мыши в указанной точке',
         version_cm_major=1,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='lup',
         name_isupper=1,
         parent_id=8,
         description=('Отпускает левую клавишу мышки в указанной точке.'),
         syntax='LUP(x, y)',
         parameters=('x, y - координаты точки на экране'),
         example=(
                '// перетаскивание из точки 10:10 в точку 20:20\n'
                'LDOWN(10, 10)\n'
                'WAITMS(300)\n'
                'LUP(20, 20)'
                ),
         # notes='',
         keywords='lup, лап, отпустить лкм, отпустить левую клавишу мышки по координатам, отпустить левую клавишу мыши по координатам, отпустить мышкой, отпустить курсором, отпустить по координатам, отпустить левую клавишу мышки в указанной точке, отпустить левую клавишу мыши в указанной точке',
         version_cm_major=1,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='rclick',
         name_isupper=1,
         parent_id=8,
         description=('Делает клик правой клавишей мышки в указанной точке.'),
         syntax='RCLICK(x, y)',
         parameters=('x, y - координаты точки на экране'),
         example=(
                '// клик ПКМ в координаты 10:10\n'
                'RCLICK(10, 10)\n'
                '\n'
                '// клик ПКМ в текущие координаты курсора\n'
                'RCLICK($_xmouse, $_ymouse)'
                ),
         # notes='',
         keywords='rclick, рклик, клик пкм, клик правой клавишей мышки по координатам, клик правой клавишей мыши по координатам, правый клик мыши, нажать правой клавишей мышки по координатам, нажать правой клавишей мыши по координатам, нажать мышкой, нажать курсором, нажать по координатам, нажать правую клавишу мышки в указанной точке, нажать правую клавишу мыши в указанной точке',
         version_cm_major=1,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='rdown',
         name_isupper=1,
         parent_id=8,
         description=('Зажимает правой клавишу мышки в указанной точке.'),
         syntax='RDOWN(x, y)',
         parameters=('x, y - координаты точки на экране'),
         example=(
                '// перетаскивание правой клавишей из точки 10:10 в точку 20:20\n'
                'RDOWN(10, 10)\n'
                'WAITMS(300)\n'
                'RUP(20, 20)'
                ),
         # notes='',
         keywords='rdown, рдовн, зажать пкм, нажать правой клавишей мышки по координатам, нажать правой клавишей мыши по координатам, нажать правой клавишу мышки в указанной точке, нажать правой клавишу мыши в указанной точке, зажать правой клавишей мышки по координатам, зажать правой клавишей мыши по координатам, зажать мышкой, зажать курсором, зажать по координатам, зажать правую клавишу мышки в указанной точке, зажать правую клавишу мыши в указанной точке, зажать и держать правой клавишей мышки по координатам, зажать и держать правой клавишей мыши по координатам, зажать и держать мышкой, зажать и держать курсором, зажать курсором и держать, зажать по координатам и держать, зажать и держать по координатам, зажать и держать правую клавишу мышки в указанной точке, зажать и держать правую клавишу мыши в указанной точке',
         version_cm_major=2,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='rup',
         name_isupper=1,
         parent_id=8,
         description=('Отпускает правую клавишу мышки в указанной точке.'),
         syntax='RUP(x, y)',
         parameters=('x, y - координаты точки на экране'),
         example=(
                '// перетаскивание правой клавишей из точки 10:10 в точку 20:20\n'
                'RDOWN(10, 10)\n'
                'WAITMS(300)\n'
                'RUP(20, 20)'
                ),
         # notes='',
         keywords='rup, рап, отпустить ркм, отпустить правую клавишу мышки по координатам, отпустить правую клавишу мыши по координатам, отпустить мышкой, отпустить курсором, отпустить по координатам, отпустить правую клавишу мышки в указанной точке, отпустить правую клавишу мыши в указанной точке',
         version_cm_major=2,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='mclick',
         name_isupper=1,
         parent_id=8,
         description=('Делает клик средней клавишей мышки в указанной точке.'),
         syntax='MCLICK(x, y)',
         parameters=('x, y - координаты точки на экране'),
         example=(
                '// клик СКМ в координаты 10:10\n'
                'MCLICK(10, 10)\n'
                '\n'
                '// клик СКМ в текущие координаты курсора\n'
                'MCLICK($_xmouse, $_ymouse)'
                ),
         # notes='',
         keywords='mclick, мклик, клик скм, клик средней клавишей мышки по координатам, клик средней клавишей мыши по координатам, клик мышкой, клик курсором, клик по координатам, средний клик мыши, нажать средней клавишей мышки по координатам, нажать средней клавишей мыши по координатам, нажать мышкой, нажать курсором, нажать по координатам, нажать среднюю клавишу мышки в указанной точке, нажать среднюю клавишу мыши в указанной точке',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='mdown',
         name_isupper=1,
         parent_id=8,
         description=('Зажимает среднюю клавишу мышки в указанной точке.'),
         syntax='MDOWN(x, y)',
         parameters=('x, y - координаты точки на экране'),
         example=(
                '// перетаскивание СКМ из точки 10:10 в точку 20:20\n'
                'MDOWN(10, 10)\n'
                'WAITMS(300)\n'
                'MUP(20, 20)'
                ),
         # notes='',
         keywords='mdown, мдовн, зажать скм, нажать средней клавишей мышки по координатам, нажать средней клавишей мыши по координатам, нажать мышкой, нажать курсором, нажать по координатам, нажать среднюю клавишу мышки в указанной точке, нажать среднюю клавишу мыши в указанной точке, зажать средней клавишей мышки по координатам, зажать средней клавишей мыши по координатам, зажать мышкой, зажать курсором, зажать по координатам, зажать среднюю клавишу мышки в указанной точке, зажать среднюю клавишу мыши в указанной точке, зажать и держать средней клавишей мышки по координатам, зажать и держать средней клавишей мыши по координатам, зажать и держать мышкой, зажать и держать курсором, зажать курсором и держать, зажать по координатам и держать, зажать и держать по координатам, зажать и держать среднюю клавишу мышки в указанной точке, зажать и держать среднюю клавишу мыши в указанной точке',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='mup',
         name_isupper=1,
         parent_id=8,
         description=('Отпускает среднюю клавишу мышки в указанной точке.'),
         syntax='MUP(x, y)',
         parameters=('x, y - координаты точки на экране'),
         example=(
                '// перетаскивание СКМ из точки 10:10 в точку 20:20\n'
                'MDOWN(10, 10)\n'
                'WAITMS(300)\n'
                'MUP(20, 20)'
                ),
         # notes='',
         keywords='mup, мап, отпустить скм, отпустить среднюю клавишу мышки по координатам, отпустить среднюю клавишу мыши по координатам, отпустить мышкой, отпустить курсором, отпустить по координатам, отпустить среднюю клавишу мышки в указанной точке, отпустить среднюю клавишу мыши в указанной точке',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='dblclick',
         name_isupper=1,
         parent_id=8,
         description=('Делает двойной клик левой клавишей мышки в указанной точке.'),
         syntax='DBLCLICK(x, y)',
         parameters=('x, y - координаты точки на экране'),
         example=(
                '// двойной клик ЛКМ в координаты 10:10\n'
                'DBLCLICK(10, 10)\n'
                '\n'
                '// двойной клик ЛКМ в текущие координаты курсора\n'
                'DBLCLICK($_xmouse, $_ymouse)'
                ),
         # notes='',
         keywords='dblclick, даблклик, двойной клик лкм, двойной клик левой клавишей мышки по координатам, двойной клик левой клавишей мыши по координатам, двойной клик мышкой, двойной клик курсором, двойной клик по координатам, двойной левый клик мыши',
         version_cm_major=1,
         version_cm_minor=2,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='move',
         name_isupper=1,
         parent_id=8,
         description=('Перемещает указатель мышки в указанную точку.'),
         syntax='MOVE(x, y)',
         parameters=('x, y - координаты точки на экране'),
         example=(
                '// переместить курсор в верхний левый угол экрана\n'
                'MOVE(0, 0)'
                ),
         # notes='',
         keywords='move, мове, переместить указатель мыши в указанную точку, переместить мышь в указанную точку, переместить курсор в указанную точку, передвинуть указатель мыши в указанную точку, передвинуть мышь в указанную точку, передвинуть курсор в указанную точку, переместить указатель мыши в координаты, переместить мышь в координаты, переместить курсор в координаты, передвинуть указатель мыши в координаты, передвинуть мышь в координаты, передвинуть курсор в координаты, переместить указатель мыши по координатам, переместить мышь по координатам, переместить курсор по координатам, передвинуть указатель мыши по координатам, передвинуть мышь по координатам, передвинуть курсор по координатам',
         version_cm_major=1,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='mover',
         name_isupper=1,
         parent_id=8,
         description=('Смещает указатель мышки относительно текущего положения.'),
         syntax='MOVER(rx, ry)',
         parameters=('rx, ry - величины, на которые указатель будет сдвинут по соотв. осям'),
         example=(
                '// переместить курсор правее на 50 и выше на 10 pxl\n'
                'MOVER(50, -10)'
                ),
         notes='Инструкция не работает в оконном режиме!\nНесмотря на схожее поведение с MOVE($_xmouse+1, $_ymouse+1), инструкция MOVER использует другой механизм работы и немного быстрее выполняется.\nВнимание! Как выяснилось позднее, данная процедура работает немного странно и сдвигает курсор не на то количество пикселей, что указано. Нормального поведения можно добиться только опытным путем.',
         keywords='mover, мовер, переместить указатель мыши на количество пикселей, переместить мышь на количество пикселей, переместить курсор на количество пикселей, передвинуть указатель мыши на количество пикселей, передвинуть мышь на количество пикселей, передвинуть курсор на количество пикселей, сместить мышь, сместить указатель мыши, сместить курсор',
         version_cm_major=4,
         version_cm_minor=2,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='wheeldown',
         name_isupper=1,
         parent_id=8,
         description=('Прокручивает колесико мышки вниз (на себя).'),
         syntax='WHEELDOWN([mult])',
         parameters=('mult - необязательный параметр; множитель прокрутки'),
         example=(
                '// покрутить колесо мыши вниз на 2 положения\n'
                'WHEELDOWN(2)'
                ),
         notes='Колесико прокручивается на дефолтное количество позиций, которое задается через панель управления Windows. По умолчанию оно равно 3 строкам текста. Множитель mult позволяет увеличить скорость прокрутки. Параметр mult по умолчанию равен 1.',
         keywords='wheeldown',
         version_cm_major=4,
         version_cm_minor=3,
         version_cm_build=1,
         version_cm_releaselevel='',
         ),
    dict(name='wheelup',
         name_isupper=1,
         parent_id=8,
         description=('Прокручивает колесико мышки вверх (от себя).'),
         syntax='WHEELUP([mult])',
         parameters=('mult - необязательный параметр; множитель прокрутки'),
         example=(
                '// покрутить колесо мыши вверх на 2 положения\n'
                'WHEELUP(2)'
                ),
         notes='Колесико прокручивается на дефолтное количество позиций, которое задается через панель управления Windows. По умолчанию оно равно 3 строкам текста. Множитель mult позволяет увеличить скорость прокрутки. Параметр mult по умолчанию равен 1.',
         keywords='wheelup',
         version_cm_major=4,
         version_cm_minor=3,
         version_cm_build=1,
         version_cm_releaselevel='',
         ),
])

# Клавиатура
DATA_ELEMENTS.extend([
    dict(name='keypress',
         name_isupper=1,
         parent_id=9,
         description=('Нажимает и отпускает клавишу клавиатуры.'),
         syntax='KEYPRESS(keycode)',
         parameters=('keycode - код клавиши'),
         example=(
                '// нажатие пробела\n'
                'KEYPRESS(32)\n'
                '\n'
                '// нажатие с использованием константы\n'
                'KEYPRESS(#space)'
                ),
         notes='Однократно нажимается клавиша клавиатуры с указанным кодом, не символ! Язык clickermann и язык целевого приложения должны совпадать и соответствовать коду указанного символа.',
         keywords='keypress, кейпресс, нажать кнопку клавиатуры, нажать кнопку на клавиатуре, нажать и отпустить кнопку клавиатуры, нажать и отпустить кнопку на клавиатуре',
         version_cm_major=2,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='keydown',
         name_isupper=1,
         parent_id=9,
         description=('Нажимает и удерживает клавишу клавиатуры.'),
         syntax='KEYDOWN(keycode)',
         parameters=('keycode - код клавиши'),
         example=(
                '// нажатие комбинации Ctrl + S\n'
                'KEYDOWN(#CTRL)\n'
                'KEYPRESS(#S)\n'
                'KEYUP(#CTRL)'
                ),
         notes='Зажать с постоянным повторением клавишу по аналогии с реальной клавиатурой таким способом не получится, так как в реальной клавиатуре за эту функцию отвечает контроллер.\nДля срабатывания, язык clickermann и язык целевого приложения должны совпадать и соответствовать коду указанного символа.',
         keywords='keydown, кейдовн, зажать кнопку клавиатуры, зажать кнопку на клавиатуре, нажать и держать кнопку клавиатуры, нажать и держать кнопку на клавиатуре, нажать и удерживать кнопку клавиатуры, нажать и удерживать кнопку на клавиатуре',
         version_cm_major=2,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='keyup',
         name_isupper=1,
         parent_id=9,
         description=('Отжимает ранее зажатую клавишу клавиатуры.'),
         syntax='KEYUP(keycode)',
         parameters=('keycode - код клавиши'),
         example=(
                '// нажатие комбинации Ctrl + S\n'
                'KEYDOWN(#CTRL)\n'
                'KEYPRESS(#S)\n'
                'KEYUP(#CTRL)'
                ),
         notes='Для срабатывания, язык clickermann и язык целевого приложения должны совпадать и соответствовать коду указанного символа.',
         keywords='keyup',
         version_cm_major=2,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='keystring',
         name_isupper=1,
         parent_id=9,
         description=('Нажимает клавиши соответственно символам входной строки.'),
         syntax='KEYSTRING(string, [delay])',
         parameters=(
                'string - входная строка\n'
                'delay - необязательный параметр; задержка в миллисекундах между каждым набором символа'
                    ),
         example=('KEYSTRING("hello world", 20)'),
         notes='Процедура не печатает строку в привычном понимании, а нажимает клавиши соответственно символам входной строки. Инструкция не может использоваться для нажатия несимвольных клавиш. На результат так же влияет текущая раскладка клавиатуры и целевой программы и clickermann.',
         keywords='keystring, кейстринг, нажатие клавиш клавиатуры, нажатие нескольких клавиш клавиатуры, нажать несколько клавиш клавиатуры, нажатие клавиш на клавиатуре, нажатие нескольких клавиш  на клавиатуре, нажать несколько клавиш  на клавиатуре, замена нескольких keypress подряд, заменить несколько keypress подряд, несколько keypress подряд заменить, напечатать строку',
         version_cm_major=3,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='iskeydown',
         name_isupper=1,
         parent_id=9,
         description=('Функция. Проверяет зажата ли указанная клавиша клавиатуры'),
         syntax='ISKEYDOWN(keycode)',
         parameters=('keycode - код клавиши либо 0'),
         example=(
                '// проверка нажатия пробела\n'
                'IF(ISKEYDOWN(#space)=1)\n'
                '   LOGWRITE("space!")\n'
                'END_IF\n'
                '\n'
                '// проверка нажатия пробела и клавиши A\n'
                'IF((ISKEYDOWN(#space)=1) & (ISKEYDOWN(#a)=1))\n'
                '   LOGWRITE("space and a!")\n'
                'END_IF'
                ),
         notes='Возвращает 1 если в момент вызова функции зажата указанная клавиша и 0 - если нет.\nЕсли в качестве keycode указан 0, то функция вернет 1 если зажата любая клавиша либо кнопка мыши.',
         keywords='iskeydown, искейдовн, проверка нажатия клавиши клавиатуры, проверка нажатия клавиши на клавиатуре, проверка зажатия клавиши клавиатуры, проверка зажатия клавиши на клавиатуре, реакция на клавишу, реакция на клавиатуру, нажата ли кнопка клавиатуры, нажата ли кнопка клавиатуры, проверить нажатую клавишу, проверить нажатую кнопку',
         version_cm_major=4,
         version_cm_minor=5,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='getkeysdown',
         name_isupper=1,
         parent_id=9,
         description=('Помещает список зажатых в момент вызова клавиш в массив.'),
         syntax='GETKEYSDOWN($kvar)',
         parameters=(
                    '$kvar - входной массив'
                    ),
         example=(
                'LOGCLEAR\n'
                'GETKEYSDOWN($kvar)\n'
                '\n'
                'FOR($i=0, $i < arrsize($kvar))\n'
                '    PRINT($kvar[$i])\n'
                'END_CYC\n'
                'waitms(100)'
                ),
         # notes='',
         keywords='getkeysdown, геткейсдовн, получить список нажатых клавиш клавиатуры, получить список зажатых клавиш клавиатуры, все зажатые клавиши клавиатуры, все нажатые клавиши клавиатуры',
         version_cm_major=4,
         version_cm_minor=12,
         version_cm_build=1,
         version_cm_releaselevel='',
         ),
    dict(name='getkblayout',
         name_isupper=1,
         parent_id=9,
         description=('Функция. Возвращает идентификатор языка ввода (раскладки) в конкретном окне.'),
         syntax='GETKBLAYOUT(hwnd)',
         parameters=('hwnd - hwnd окна'),
         example=(
                '// получаем hwnd запущеной программы\n'
                '$hwnd = WNDFIND("Блокнот")\n'
                '\n'
                '// выводим раскладку\n'
                'LOGWRITE(GETKBLAYOUT($hwnd))'
                ),
         notes='В современных операционных системах Windows каждое окно хранит свою собственную раскладку.\n1049 - русский, 1033 - английский',
         keywords='getkblayout, геткейбоардлайоут, получить раскладку клавиатуры, получить язык клавиатуры, узнать раскладку клавиатуры, узнать язык клавиатуры, получить раскладку в окне, получить язык в окне, получить язык окна, какой язык клавиатуры',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='SE',
         ),
    dict(name='setkblayout',
         name_isupper=1,
         parent_id=9,
         description=('Устанавливает языка ввода (раскладки) в конкретном окне.'),
         syntax='SETKBLAYOUT(hwnd, lang)',
         parameters=(
                    'hwnd - hwnd окна\n'
                    'lang - идентификатор языка ввода'
                    ),
         example=(
                '// получаем hwnd запущеной программы\n'
                '$hwnd = WNDFIND("Блокнот")\n'
                '\n'
                '// задаём английскую раскладку\n'
                'SETKBLAYOUT($hwnd, 1033)'
                ),
         notes='В современных операционных системах Windows каждое окно хранит свою собственную раскладку.\n1049 - русский, 1033 - английский',
         keywords='setkblayout, сеткейбоардлайоут, задать раскладку клавиатуры, задать язык клавиатуры, установить раскладку клавиатуры, установить язык клавиатуры, задать раскладку в окне, задать язык в окне, задать язык окна, установить язык в окне, установить язык окна',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='SE',
         ),
])

# Условия, циклы, подпрограммы
DATA_ELEMENTS.extend([
    dict(name='if ... end_if',
         name_isupper=1,
         parent_id=10,
         description=('Условная конструкция. Выполняет часть сценария в зависимости от значения параметра условия.'),
         syntax=(
                'IF(expression)\n'
                '   ...\n'
                'END_IF'
                ),
         parameters=('expression - логическое выражение, при истинности которого выполняется тело условия '),
         example=(
                '// Простой пример\n'
                '$var = 5\n'
                'IF($var > 3)\n'
                '   LOGWRITE("true") // сработает если $var больше 3\n'
                'END_IF\n'
                '\n'
                '// Пример с комплексным условием\n'
                '$var = 5\n'
                'IF(($var > 3) & ($var < 10))\n'
                '   LOGWRITE("true") // сработает если $var от 4 до 9\n'
                'END_IF'
                ),
         notes='Инструкции, находящиеся между IF и END_IF выполняются в зависимости от значения параметра expression. Если данный параметр после всех вычислений равен 0, то инструкции в теле условия не выполняются. Во всех остальных случаях оно будет исполнено.\nПараметр expression может быть представлен, как результат арифмитической или логической операции, а так же результатом выполнения функции.',
         keywords='if end_if, иф, эндиф, условие, проверка условия, условная конструкция, что если',
         version_cm_major=3,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='alpha',
         ),
    dict(name='else',
         name_isupper=1,
         parent_id=10,
         description=('Необязательная часть условной конструкции. Выполняет часть сценария в зависимости от результата проверки условия.'),
         syntax=(
                'IF(expression)\n'
                '   ...\n'
                'ELSE\n'
                '   ...\n'
                'END_IF'
                ),
         # parameters=(''),
         example=(
                '// условие без блока "иначе"\n'
                '// в случае неверного выражения 5 > 3 ничего не делает\n'
                'IF(5 < 3)\n'
                '   LOGWRITE("true")\n'
                'END_IF\n'
                '\n'
                '// тоже самое условие с блоком "иначе"\n'
                '// в случае неверного выражения 5 > 3 выдаст сообщение "false"\n'
                'IF(5 < 3)\n'
                '   LOGWRITE("true")\n'
                'ELSE\n'
                '   LOGWRITE("false")\n'
                'END_IF\n'
                ),
         notes='Блок ELSE позволяет объявить блок инструкций, которые выполнятся в том и только в том случае, если условие ложно и основной блок не выполнился (см. IF). Блок ELSE описывается прямо в блоке условия между заголовком и END_IF. Блок ELSE доступен для следующих условных конструкций: IF, IF_PICTURE_IN, IF_PIXEL_IN.',
         keywords='else, элсе, часть условной конструкции, иначе, если нет, если условие не выполняется, если условие неверно',
         version_cm_major=4,
         version_cm_minor=0,
         version_cm_build=2,
         version_cm_releaselevel='',
         ),
    dict(name='switch ... end_switch',
         name_isupper=1,
         parent_id=10,
         description=('Условная конструкция, состоящая из множества условий. Выполняет часть сценария в зависимости от значения параметра переключателя.'),
         syntax=(
                'SWITCH(var)\n'
                'CASE(result1)\n'
                '   ...\n'
                'CASE(result2 )\n'
                '   ...\n'
                '[DEFAULT]\n'
                '   [...]\n'
                'END_SWITCH\n'
                ),
         parameters=('var - параметр переключатель'),
         example=(
                '// генерируем случайное значение\n'
                '$var = rnd(1,5)\n'
                'LOGWRITE("$var = ", $var)\n'
                '\n'
                '// анализируем значение переменной\n'
                '// при этом явно обрабатываем случаи 1,2 и 3 и неявно в блоке по умолчанию\n'
                'SWITCH($var)\n'
                'CASE(1)\n'
                '   LOGWRITE("one")\n'
                'CASE(2)\n'
                '   LOGWRITE("two")\n'
                'CASE(3)\n'
                '   LOGWRITE("three")\n'
                'DEFAULT\n'
                '   LOGWRITE("smth else")\n'
                'END_SWITCH'
                ),
         notes='Так называемый переключатель используется когда нагромождение условий (IF) нецелесообразно и портит читаемость сценария. Переключатель анализирует входное значение var и в зависимости от него выполняет часть сценария, находящегося после блоке case с соответствующим значением. При этом, все параметры указанных инструкций могут быть представлены как числом, так и переменной. Необязательный блок DEFAULT выполняется в случае, когда ни один CASE не подошел под текущее значение переключателя.',
         keywords='switch end_switch, свич, свитч, замена кучи условий, много условий замена, замена кучи if, много if замена, несколько условий подряд',
         version_cm_major=4,
         version_cm_minor=9,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='for ... end_cyc',
         name_isupper=1,
         parent_id=10,
         description=('Цикл в параметром.'),
         syntax=(
                'FOR($var [=value], expression, [step])\n'
                '   ...\n'
                'END_CYC'
                ),
         parameters=(
                '$var - переменная, которая будет наращиваться на значение step после каждой итерации цикла (параметр цикла)\n'
                'value - необязательный параметр; начальное значение значение параметра цикла\n'
                'expression - логическое выражение, при истинности которого выполняется тело цикла\n'
                'step - необязательный параметр; значение шага, на которое каждую итерацию увеличивается переменная'
                    ),
         example=(
                '// простой пример с инициализацией параметра\n'
                'FOR($var=5, $var < 10)\n'
                '   LOGWRITE("var: ", $var)\n'
                'END_CYC\n'
                '\n'
                '// с инициализацией параметра и заданным шагом\n'
                'FOR($var=10, $var < 100, 10)\n'
                '   LOGWRITE("var: ", $var)\n'
                'END_CYC'
                ),
         notes='Тело цикла (инструкции, находящиеся между FOR и END_CYC) выполняется в случае истинности выражения expression, при этом, закончив выполнение тела, управление снова проверяет истинность выражения и если оно по прежнему истинно, тело цикла выполняется снова. Помимо этого, каждый повтор выполнения тела цикла (итерацию) параметр $var увеличивает свое значение на step. Цикл завершится, когда выражение expression будет ложным.\nЕсли переменная $var до выполнения цикла уже была инициализирована (в том числе в этом же цикле на прошлом прогоне скрипта), то цикл начнется с использованием текущего значения переменной. Если это "новая" переменная, она будет инициализирована нулем. Если указано начальное значение value, то переменной присвоится его значение.\nПараметр step по умолчанию равен 1.',
         keywords='for end_cyc, цикл фор, цикл с параметром, цикл сам наращивает переменную, цикл с шагом',
         version_cm_major=3,
         version_cm_minor=2,
         version_cm_build=0,
         version_cm_releaselevel='beta',
         ),
    dict(name='while ... end_cyc',
         name_isupper=1,
         parent_id=10,
         description=('Цикл с предусловием.'),
         syntax=(
                'WHILE(expression)\n'
                '   ...\n'
                'END_CYC'
                ),
         parameters=('expression - логическое выражение, при истинности которого выполняется тело цикла'),
         example=(
                '// пример простого цикла\n'
                '$var = 1\n'
                'WHILE($var < 5)\n'
                '   LOGWRITE("var: ", $var)\n'
                '   INC($var)\n'
                'END_CYC\n'
                '\n'
                '// пример цикла с комплексным условием\n'
                '$x=0\n'
                '$y=0\n'
                'WHILE(($x < 5) & ($y < 5))\n'
                '   LOGWRITE($x, ",", $y)\n'
                '   INC($x, 1)\n'
                '   INC($y, 2)\n'
                'END_CYC\n'
                'LOGWRITE("end: ", $x, ",", $y)'
                ),
         notes='Упрощенная версия цикла FOR, без параметра и шага. Действует аналогично и просто проверяет условие expression. При этом, существует опасность "зацикливания". По этому важно предусмотреть ситуацию, при которой expression станет ложным и цикл завершится.',
         keywords='while end_cyc, цикл вайл, цикл вхиле, цикл простой',
         version_cm_major=3,
         version_cm_minor=2,
         version_cm_build=0,
         version_cm_releaselevel='beta',
         ),
    dict(name='sub ... end_sub',
         name_isupper=1,
         parent_id=10,
         description=('Подпрограмма. Описывает подпрограмму.'),
         syntax=(
                'SUB(sub_name, [$par1, $par2, ...])\n'
                '   ...\n'
                'END_SUB'
                ),
         parameters=(
                    'sub_name - имя подпрограммы\n'
                    '$par1, $par2, ... - необязательные параметры подпрограммы'
                    ),
         example=(
                '// пример 1. описание и вызов подрограммы без параметров\n'
                '// описание подпрограммы без параметров\n'
                'SUB(mysub)\n'
                '   FOR($i=0, $i<3)\n'
                '      LOGWRITE("flood ", $i)\n'
                '   END_CYC\n'
                'END_SUB\n'
                '\n'
                '// вызов подпрограммы\n'
                'mysub()\n'
                '\n'
                '// ------------------------------------\n'
                '// пример 2. подпрограмма умножения двух случайных числел\n'
                'SUB(mult, $par1, $par2)\n'
                '   LOGWRITE("par1: ", $par1)\n'
                '   LOGWRITE("par2: ", $par2)\n'
                '   LOGWRITE("par1 * par2 = ", $par1 * $par2)\n'
                'END_SUB\n'
                '\n'
                '// вызов подпрограммы (три раза)\n'
                'FOR($i=0, $i < 3)\n'
                '   mult(RND(1,5), RND(1,5))\n'
                'END_CYC'
                ),
         notes='Подпрограмма - это последовательность действий, объединенная в блок. Подпрограмма обязательно имеет собственное уникальное имя sub_name и необязательно набор параметров $par1, $par2,.... Тело подпрограммы будет вызвано только в том случае, если в сценарии будет указано ее имя sub_name (см. пример). Подпрограмму можно описать в любом месте сценария. Однако, описание подпрограммы должно быть раньше (выше) любого из ее вызовов. Поэтому рекомендуется описывать подпрограммы сразу в начале сценария. Хорошим тоном считается вынесение тел подпрограмм в отдельный внешний файл, подключаемый затем через директиву #include.\nПараметры, описанные в заголовке подпрограммы после ее имени, доступны в теле подпрограммы как переменные. Для вызова подпрограммы необходимо написать ее имя в сценарии вместе со всеми параметрами. Очень важно чтобы количество параметров в описании и в вызове совпадало. После выполнения подпрограммы, сценарий продолжится с момента вызова подпрограммы. Локальные переменные подпрограммы (параметры) при этом будут уничтожены. Вызов подпрограммы без параметров все равно должен включать в себя пустые скобки ().',
         keywords='sub end_sub, саб, подпрограмма, описание подпрограммы, вызов подпрограммы, функция',
         version_cm_major=4,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='thread ... end_thread',
         name_isupper=1,
         parent_id=10,
         description=('Потоки. Описывает поток.'),
         syntax=(
                'THREAD(thread_name, [init_state])\n'
                '   ...\n'
                'END_THREAD'
                ),
         parameters=(
                'thread_name - имя потока\n'
                'init_state - необязательный параметр; начальное состояние потока (1 - запуск сразу, 0 - на паузе)'
                    ),
         example=(''),
         notes=(
                'Поток представляет собой независимую цепочку действий, выполняющихся одновременно с основным сценарием и другими потоками.\n'
                'Каждый поток имеет следующие особенности:\n'
                'два состояния: приостановленное и рабочее; в рабочем состоянии выполняется тело потока, в приостановленном соответственно нет\n'
                'собственный таймер, обрабатывающий задержки независимо от состояния сценария и других потоков; задержки, вызванные работой команд так же не влияют на основной сценарий и другие потоки\n'
                'собственные подпрограммы; при необходимости использования внутри потока подпрограмму, она описывается и вызывается внутри тела потока; внешний вызов и описание подпрограмм не в рамках одного тела потока не допускается и ведет к ошибкам\n'
                'все потоки и сценарий работают в одной области видимости, то есть им одинакого доступны все переменные и графический буфер\n'
                'существует возможность приостанавливать и возобновлять потоки, используя процедуру SETTHREAD.\n'
                'при запуске ("с формы") основного сценария все потоки находятся в состоянии, определенном при их объявлении; при паузе и останове потоки так же соответственно встают на паузу или останавливаются'
                ),
         keywords='thread end_thread, треад, тхреад, потоки, описание потока, создание потока, описание потоков, создание потоков',
         version_cm_major=4,
         version_cm_minor=11,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='setthread',
         name_isupper=1,
         parent_id=10,
         description=('Меняет состояние потока.'),
         syntax='SETTHREAD(thread_name, state)',
         parameters=(
                    'thread_name - имя потока\n'
                    'state - задаваемое состояние'
                    ),
         example=(
                '//-------------------------------\n'
                '// Описание остановленного потока\n'
                'THREAD(t1, 0)\n'
                '   LOGWRITE("thr #1 tic-tak")\n'
                '   WAIT(5)\n'
                'END_THREAD\n'
                '//-------------------------------\n'
                '\n'
                '// Снятие потока с паузы\n'
                'setthread(t1, 1)\n'
                'wait(10)'
                ),
         notes=(
                'Значения state\n'
                '0 - поток ставится на паузу\n'
                '1 - поток снимается с паузы (продолжает выполнение с места, где был остановлен паузой)\n'
                '2 - поток ставится на паузу, при этом при дальнейшем снятии с паузы о начинает выполняться с начала, независимо от того, на какой инструкции тела он был остановлен'
                ),
         keywords='setthread, сэттреад, сеттреад, управление потоком, поставить поток на паузу, остановить поток, запустить поток, стартовать поток',
         version_cm_major=4,
         version_cm_minor=11,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
])

# Анализ экрана
DATA_ELEMENTS.extend([
    dict(name='getscreen',
         name_isupper=1,
         parent_id=11,
         description=('Делает снимок экрана и помещает его в буфер анализа программы.'),
         syntax='GETSCREEN([x1, y1, x2, y2])',
         parameters=('x1, y1, x2, y2 - параметры, описывающие область экрана; необязательны'),
         # example=(''),
         notes='Данная процедура помещает снимок экрана в буфер программы. Затем, из этого буфера берут данные все графические функции, вызываемые в сценарии. Соответственно, в случае когда необходимо обновить хранящееся в памяти состояние экрана, нужно вызвать getscreen() еще раз.\nВ случае, если указаны параметры, описывающие область, будет обновлена только соответствующая область в графическом буфере. На некоторых системах это позволяет ускорить выполнение данной инструкции.',
         keywords='getscreen, гетскрин, снимок экрана в память, экран в буфер, снимок в буфер экрана, поместить в буфер анализа',
         version_cm_major=3,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='alpha',
         ),
    dict(name='pxl',
         name_isupper=1,
         parent_id=11,
         description=('Функция. Возвращает код цвета для заданного пикселя.'),
         syntax='PXL(x, y)',
         parameters=('x, y - координаты пикселя'),
         example=('$clr = PXL(50,50)'),
         notes='Функция получает данные о цвете из буфера экрана кликера. Буфер обновляется командой GETSCREEN.',
         keywords='pxl. пиксел, получить цвет пикселя, получить цвет пиксела, получить цвет в координатах, получить цвет пикселя в координатах, получить цвет пиксела в координатах, получить цвет по координатам, получить цвет пикселя по координатам, получить цвет пиксела по координатам, цвет в точке на экране, цвет точки на экране',
         version_cm_major=4,
         version_cm_minor=0,
         version_cm_build=2,
         version_cm_releaselevel='',
         ),
    dict(name='pxlcount',
         name_isupper=1,
         parent_id=11,
         description=('Функция. Производит подсчет количества пикселей заданного цвета в прямоугольной области буфера анализа.'),
         syntax='PXLCOUNT(x1, y1, x2, y2, color)',
         parameters=(
                    'x1, y1 - числовые координаты левого верхнего угла области\n'
                    'x2, y2 - числовые координаты правого нижнего угла области\n'
                    'color - код цвета'
                    ),
         example=(
                '// считаем в области количество пикселов с цветом 255 (красный)\n'
                'GETSCREEN\n'
                '$count = PXLCOUNT(10,20, 100, 40, 255)\n'
                'LOGWRITE("pixels: ", $count)'
                ),
         notes='Если ни одного пикселя не будет найдено, функция вернет нолью\nФункция получает данные из буфера экрана кликера. Буфер обновляется командой GETSCREEN.',
         keywords='pxlcount, пикселькаунт, пикселькоунт, пикселкаунт, пикселкоунт, посчитать количество заданного цвета пикселей в прямоугольной области буфера экрана, посчитать количество пикселей в области экрана, посчитать количество пикселей заданного цвета в области экрана, посчитать количество цвета в области экрана',
         version_cm_major=4,
         version_cm_minor=0,
         version_cm_build=2,
         version_cm_releaselevel='',
         ),
    dict(name='pxlxor',
         name_isupper=1,
         parent_id=11,
         description=('Функция. Производит подсчет контрольной суммы пикселей в заданной области, складывая их цвета оператором XOR.'),
         syntax='PXLXOR(x1, y1, x2, y2)',
         parameters=(
                    'x1, y1 - числовые координаты левого верхнего угла области\n'
                    'x2, y2 - числовые координаты правого нижнего угла области'
                    ),
         example=(
                'GETSCREEN\n'
                '$count = PXLXOR(10,20, 100, 40)\n'
                'LOGWRITE("Hash: ", $count)'
                ),
         notes='Необходимо понимать что контрольная сумма используется для характеристики области экрана. То есть если была подсчитана сумма, в области изменился хотя бы один пиксель и если подсчитать сумму снова - она будет отличаться от первой. Такой способ не очень надежен в плане получения уникального хеша для простых изображений, но весьма быстр.\nФункция получает данные из буфера экрана кликера. Буфер обновляется командой GETSCREEN.',
         keywords='pxlxor, пикселхор, пиксельхор, подсчёт контрольной суммы пикселей в заданной области, подсчёт контрольной суммы в заданной области, контрольная сумма пикселей в заданной области, складывание цвета пикселей в области',
         version_cm_major=4,
         version_cm_minor=0,
         version_cm_build=2,
         version_cm_releaselevel='',
         ),
    dict(name='pxlcrc',
         name_isupper=1,
         parent_id=11,
         description=('Функция. Производит подсчет контрольной суммы пикселей в заданной области, используя алгоритм CRC32.'),
         syntax='PXLCRC(x1, y1, x2, y2)',
         parameters=(
                    'x1, y1 - числовые координаты левого верхнего угла области\n'
                    'x2, y2 - числовые координаты правого нижнего угла области'
                    ),
         example=(
                'GETSCREEN\n'
                '$count = PXLCRC(10,20, 100, 40)\n'
                'LOGWRITE("Hash: ", $count)'
                ),
         notes='Более актуальный метод подсчета хеша для области экрана. Лишен недостатков PXLXOR(), хотя работает примерно в два раза медленнее.\nФункция получает данные из буфера экрана кликера. Буфер обновляется командой GETSCREEN.',
         keywords='pxlcrc, пикселкрк, пикселькрк, подсчёт контрольной суммы пикселей в заданной области используя алгоритм CRC32, подсчёт контрольной суммы в заданной области, контрольная сумма пикселей в заданной области, складывание цвета пикселей в области',
         version_cm_major=4,
         version_cm_minor=7,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='pxlreplace',
         name_isupper=1,
         parent_id=11,
         description=('Производит замену в области графического буфера пикселей одного цвета на пиксели другого цвета.'),
         syntax='PXLREPLACE(x1, y1, x2, y2, color, newcolor)',
         parameters=(
                    'x1, y1 - числовые координаты левого верхнего угла области\n'
                    'x2, y2 - числовые координаты правого нижнего угла области\n'
                    'color - заменяемый цвет\n'
                    'newcolor - новый цвет'
                    ),
         example=(
                '// заменяем в области все цвета на цвет 255 (красный)\n'
                'GETSCREEN\n'
                'PXLREPLACE(10,20, 100, 40, -1, 255)\n'
                'SCREENSHOT'
                ),
         notes='Чтобы заменялись пиксели любого цвета, параметр color должен быть равен -1.\nФункция получает данные из буфера экрана кликера. Буфер обновляется командой GETSCREEN.',
         keywords='pxlreplace, пикселреплэйс, пиксельреплэйс, замена цвета пикселей в области, замена пикселей в области, заменить цвет в буфере экрана, замена цвета в буфере экрана, закрасить область в буфере экрана, заменить цвет один на другой в буфере экрана',
         version_cm_major=4,
         version_cm_minor=12,
         version_cm_build=1,
         version_cm_releaselevel='',
         ),
    dict(name='if_pixel_in ... end_if',
         name_isupper=1,
         parent_id=11,
         description=('Производит поиск пикселя заданного цвета в прямоугольной области буфера анализа.'),
         syntax=(
                'IF_PIXEL_IN(x1, y1, x2, y2, color1, ...)\n'
                '   ...\n'
                'END_IF'
                ),
         parameters=(
                    'x1, y1 - числовые координаты левого верхнего угла области поиска\n'
                    'x2, y2 - числовые координаты правого нижнего угла области поиска\n'
                    'color1, ... - цвета, поиск которых будет осуществляться'
                    ),
         example=(
                'GETSCREEN\n'
                '// поиск красного пикселя\n'
                'IF_PIXEL_IN(10,20, 100,40, 255)\n'
                '   LCLICK($_return1, $_return2)\n'
                'END_IF\n'
                '\n'
                '// поиск красного или зеленого пикселя\n'
                'IF_PIXEL_IN(10,20, 100,40, 255, 65280)\n'
                '   LCLICK($_return1, $_return2)\n'
                'END_IF'
                ),
         notes='Как только первый попавшийся пиксель будет найден, инструкция вернет его координаты в переменные $_return1, $_return2 и прекратит анализю\nДобавление каждого цвета увеличивает длительность анализа на 100%',
         keywords='if_pixel_in end_if, ифпикселин, иф_пиксел_ин, поиск пикселя заданного цвета в прямоугольной области буфера экрана, поиск пикселя в прямоугольной области буфера экрана, поиск пикселя в области буфера экрана, поиск пикселя в буфере экрана, поиск цвета в прямоугольной области буфера экрана, поиск цвета в области буфера экрана, поиск цвета в буфере экрана, найти пиксель, найти цвет',
         version_cm_major=3,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='RC1',
         ),
    dict(name='if_picture_in... end_if',
         name_isupper=1,
         parent_id=11,
         description=('Производит поиск изображения в прямоугольной области буфера анализа.'),
         syntax=(
                'IF_PICTURE_IN(x1, y1, x2, y2, file, [bgcolor], [currency])\n'
                '   ...\n'
                'END_IF'
                ),
         parameters=(
                    'x1, y1 - числовые координаты левого верхнего угла области поиска\n'
                    'x2, y2 - числовые координаты правого нижнего угла области поиска\n'
                    'file - bmp файл, поиск которого будет осуществляться\n'
                    'bgcolor - необязательный параметр; игнорируемый цвет фона входного изображения\n'
                    'currency - необязательный параметр; точность поиска в процентах (1..100)'
                    ),
         example=(
                'GETSCREEN\n'
                'IF_PICTURE_IN(10,20, 300,300, "somefile.bmp")\n'
                '   MOVE($_return1, $_return2)\n'
                'END_IF'
                ),
         notes='Работает аналогично IF_PIXEL_IN. Как только первый попавшийся участок будет найден, инструкция вернет его координаты в переменные $_return1, $_return2 (координаты верхнего левого угла) и прекратит анализ.\nДля того что бы участок признался подходящим, необходимо 100% соответствие пикселей bmp-файла и текущего снимка экрана. Так же можно задать цвет фона изображения, который не будет учитываться при поиске на экране. Если цвет фона не задан, изображение ищется с учетом всех пикселей.\nМожно задать не 100% совпадение. Для этого укажите в параметре currency необходимую точность. Этот параметр определяет количество несовпавших пикселей, которые будут проигнорированы при анализе. Чем ниже значение точности, тем дольше идет поиск.\nЕсли параметр currency не задан, по умолчанию он равен 100. Если параметр bgcolor не задан, по умолчанию он равен -1. Если есть необходимость задать точность, не задавая фон, сделайте bgcolor равным -1.\nВходные файлы для анализа должны находиться в директории проекта, быть формта BMP и иметь стандартную разрядность 24 бита. В случае использования цветокоррекции, входной файл должен быть уже откорректирован. Чтобы добиться этого результата, сохраните скриншот формата bmp после вызова colormode(), затем вырежьте нужный участок картинки в графическом редакторе и сохраните как bmp.',
         keywords='if_picture_in end_if, ифпиктуреин, ифпикчуреин, иф_пикчуре_ин, поиск изображения в прямоугольной области буфера экрана, поиск изображения в области буфера экрана, поиск изображения в буфере экрана, поиск картинки в прямоугольной области буфера экрана, поиск картинки в области буфера экрана, поиск картинки в буфере экрана, найти картинку',
         version_cm_major=4,
         version_cm_minor=5,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='scanpicture',
         name_isupper=1,
         parent_id=11,
         description=('Производит поиск изображений в прямоугольной области буфера анализа и выводит координаты найденных экземпляров в массив.'),
         syntax='SCANPICTURE($arr, x1, y1, x2, y2, file, [bgcolor], [currency])',
         parameters=(
                    '$arr - массив\n'
                    'x1, y1 - числовые координаты левого верхнего угла области поиска\n'
                    'x2, y2 - числовые координаты правого нижнего угла области поиска\n'
                    'file - bmp файл, поиск которого будет осуществляться\n'
                    'bgcolor - необязательный параметр; игнорируемый цвет фона входного изображения\n'
                    'currency - необязательный параметр; точность поиска в процентах (1..100)'
                    ),
         example=(
                'GETSCREEN\n'
                '// поиск изображения pict.bmp в области 0,0 - 1250,959\n'
                'SCANPICTURE($arr, 0,0, 1250,959, "pict.bmp")\n'
                '\n'
                '// вывод массива, содержащего результаты поиска\n'
                'WHILE(ARRSIZE($arr) > 0)\n'
                '   $y = ARRPOP($arr)\n'
                '   $x = ARRPOP($arr)\n'
                '   LOGWRITE($x,":", $y)\n'
                'END_CYC'
                ),
         notes='Основные параметры и тонкости работы аналогичны IF_PICTURE_IN.\nРезультатом работы является массив $arr, в который добавляются координаты найденных экземпляров изображения. Таким образом, координаты первого найденного изображения будут лежать в $arr[0] и $arr[1] для X и Y соответственно. Для второго экземпляра $arr[2] и $arr[3] и т.д.\nSCANPICTURE и SCANPXL используют в своей работе массивы.',
         keywords='scanpicture, сканпикчюре, сканпикчурэ, сканпиктурэ, поиск изображений в прямоугольной области буфера, поиск изображений в области буфера, поиск картинок в прямоугольной области буфера, поиск картинок в области буфера, поиск нескольких картинок, поиск нескольких изображений, найти нескольких картинок, найти нескольких изображений',
         version_cm_major=4,
         version_cm_minor=8,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='scanpxl',
         name_isupper=1,
         parent_id=11,
         description=('Производит поиск пикселей заданного цвета в прямоугольной области буфера анализа.'),
         syntax='SCANPXL($arr, x1, y1, x2, y2, color)',
         parameters=(
                    '$arr - принимающий массив\n'
                    'x1, y1 - числовые координаты левого верхнего угла области поиска\n'
                    'x2, y2 - числовые координаты правого нижнего угла области поиска\n'
                    'color - цвет, поиск которого будет осуществляться'
                    ),
         example=(
                'GETSCREEN\n'
                '// поиск всех красный (255) пикселей в области 0,0 - 1250,959\n'
                'SCANPXL($arr, 0,0, 1250,959, 255)\n'
                '\n'
                '// вывод массива, содержащего результаты поиска\n'
                'WHILE(ARRSIZE($arr) > 0)\n'
                '   $y = ARRPOP($arr)\n'
                '   $x = ARRPOP($arr)\n'
                '   LOGWRITE($x, ":", $y)\n'
                'END_CYC'
                ),
         notes='Результатом работы является массив $arr, в который добавляются координаты найденных пикселей заданного цвета. Таким образом, координаты первого найденного пикселя будут лежать в $arr[0] и $arr[1] для X и Y соответственно. Для второго экземпляра $arr[2] и $arr[3] и т.д.',
         keywords='scanpxl, сканпиксель, поиск пикселей заданного цвета в прямоугольной области буфера, поиск пикселей заданного цвета в области буфера, поиск пикселей в прямоугольной области буфера, поиск пикселей в области буфера',
         version_cm_major=4,
         version_cm_minor=8,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='screenshot',
         name_isupper=1,
         parent_id=11,
         description=('Сохраняет графический буфер анализа на диск.'),
         syntax='SCREENSHOT([pref])',
         parameters=('pref - необязательный параметр; префикс для названия файла'),
         example=(
                'GETSCREEN\n'
                '// будут созданы скриншоты error0000.bmp, error0001.bmp, error0002.bmp\n'
                'SCREENSHOT("error")\n'
                'SCREENSHOT("error")\n'
                'SCREENSHOT("error")\n'
                '\n'
                '// будет создан скриншот shot0000.bmp\n'
                'SCREENSHOT'
                ),
         notes='Скриншот экрана помещается в директорию текущено скрипта в каталог screens и ему присваивается имя вида pref0000.bmp. При этом номер 0000 будет наращиваться по мере необходимости.\nЕсли параметр pref опущен, он считается равным "shot". В случае использования оконного режима будет сделан скриншот только рабочей области. ',
         keywords='screenshot, скриншот, сохранить скриншот в файл, скриншот в файл с инкрементом имени, скриншот с инкрементом имени, скриншот с наращиванием имени',
         version_cm_major=3,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='alpha',
         ),
    dict(name='screenshotex',
         name_isupper=1,
         parent_id=11,
         description=('Сохраняет часть графического буфера анализа на диск.'),
         syntax='SCREENSHOTEX(x1, y1, x2, y2, [pref], [format])',
         parameters=(
                    'x1, y1, x2, y2 - четыре координаты, описывающие сохраняемую область буфера\n'
                    'pref - необязательный параметр; префикс названия\n'
                    'format - необязательный параметр; тип файла (сжатие): 0 - bmp; 1 - jpeg'
                    ),
         example=(
                'GETSCREEN\n'
                '// будет создан скриншот небольшого кусочка левого верхнего угла\n'
                'SCREENSHOTEX(10,10, 50,50, "image_", 0)'
                ),
         notes='Скриншот экрана помещается в директорию текущено скрипта в каталог screens и ему присваивается имя вида pref0000.bmp. При этом номер 0000 будет наращиваться по мере необходимости.\nЕсли параметр pref опущен, он считается равным "shot". В случае использования оконного режима скриншот будет вырезан из привязанной рабочей области.',
         keywords='screenshotex, скриншотэкс, сохранить скриншот области, сохранить скриншот в файл, сохранить скриншот в файл с инкрементом имени, сохранить скриншот с инкрементом имени, сохранить скриншот с наращиванием имени, сохранить скриншот области в файл, сохранить скриншот области в файл с инкрементом имени, сохранить скриншот области с инкрементом имени, сохранить скриншот области с наращиванием имени',
         version_cm_major=4,
         version_cm_minor=9,
         version_cm_build=5,
         version_cm_releaselevel='',
         ),
    dict(name='screenshotfix',
         name_isupper=1,
         parent_id=11,
         description=('Сохраняет часть графического буфера анализа на диск в конкретный файл.'),
         syntax='SCREENSHOTFIX(x1, y1, x2, y2, path, [format])',
         parameters=(
                    'x1, y1, x2, y2 - четыре координаты, описывающие сохраняемую область буфера\n'
                    'path - путь, по которому будет сохранен скриншот\n'
                    'format - необязательный параметр; тип файла (сжатие): 0 - bmp; 1 - jpeg'
                    ),
         example=(
                'GETSCREEN\n'
                '// будет создан скриншот небольшого кусочка левого верхнего угла\n'
                'SCREENSHOTFIX(10,10, 50,50, "D:\file.bmp")'
                ),
         notes='В отличие от SCREENSHOTEX, файл сохраняется в конкретное место по относительному или абсолютному пути, каждый раз перезаписываясь. Расширение файла желательно задавать исходя из параметра format (по умолчанию 0).',
         keywords='screenshotfix, скриншотфикс, скриншот, сохранить скриншот области, сохранить скриншот в файл, сохранить скриншот в один файл, сохранить скриншот области в файл, сохранить скриншот области в один файл, сохранить скриншот в один и тот же файл',
         version_cm_major=4,
         version_cm_minor=12,
         version_cm_build=1,
         version_cm_releaselevel='',
         ),
    dict(name='colormode',
         name_isupper=1,
         parent_id=11,
         description=('Применяет цветокоррекцию к текущему снимку экрана.'),
         syntax='COLORMODE(mode, [x1, y1, x2, y2])',
         parameters=(
                    'mode - число, соответствующее режиму коррекции\n'
                    'x1, y1, x2, y2 - область снимка экрана, к которой будет применена коррекция'
                    ),
         example=(
                '// применяем к области режим цветокоррекции 7\n'
                'GETSCREEN\n'
                'COLORMODE(7, 100,100, 200, 200)'
                ),
         notes=(
                'Процедура изменяет текущий снимок экрана, применяя к нему фильтр, снижающий количество цветов в палитре. В основной справке есть статья посвещенная цветокоррекции.\n'
                'Есть возможность указать отдельную область для применения фильтра. Стоит учитывать, что на его применение так же затрачивается время, поэтому если нет необходимости менять весь снимок, указание конкретной области позволит выиграть немного времени в процессе выполнения сценария. Если область не описана, коррекция применяется ко всему экрану.\n'
                'Вызов COLORMODE(0) не имеет смысла. Поддерживается одностороннее увеличение режима (1, 2, 3..) без необходимости повторного вызова GETSCREEN. Обратно увеличить количество цветов невозможно. Новый "чистый" снимок экрана получается новым вызовом GETSCREEN\n'
                '\n'
                'Таблица значений mode\n'
                'mode Макс. цветов\n'
                '0   16 777 216\n'
                '1   2 097 152\n'
                '2   262 144\n'
                '3   32 768\n'
                '4   4 096\n'
                '5   512\n'
                '6   64\n'
                '7   8\n'
                '8   2'
                ),
         keywords='colormode, колормод, колормодэ, колормоде, цветокоррекция буфера экрана, цветокоррекция снимка экрана, цветокоррекция экрана, уменьшение цветов, уменьшение количества цветов, уменьшить количество цветов в буфере экрана, уменьшить количество цветов на экране',
         version_cm_major=4,
         version_cm_minor=2,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='contrast',
         name_isupper=1,
         parent_id=11,
         description=('Применяет цветокоррекцию к текущему снимку экрана.'),
         syntax='CONTRAST(value, [x1, y1, x2, y2])',
         parameters=(
                    'value - число от 1 до 9, соответствующее степени контраста\n'
                    'x1, y1, x2, y2 - область снимка экрана, к которой будет применена коррекция'
                    ),
         example=(
                '// применяем к области режим максимальной цветокоррекции контраста\n'
                'GETSCREEN\n'
                'CONTRAST(9, 100,100, 200, 200)'
                ),
         notes='Процедура изменяет текущий снимок экрана, увеличивая контрастность и уменьшая количество полутонов. В основной справке есть статья посвещенная цветокоррекции.\nЕсть возможность указать область для применения фильтра. Быстродействие обратно пропорционально размеру области. Вызов CONTRAST(0) не имеет смысла, вызов CONTRAST(9) сделает снимок черно-белым. В отличие от COLORMODE для получения корректного результата необходимо применять процедуру только к неизмененным снимкам.',
         keywords='contrast, контраст, цветокоррекция буфера экрана, цветокоррекция снимка экрана, цветокоррекция экрана, уменьшение цветов, уменьшение количества цветов, уменьшить количество цветов в буфере экрана, уменьшить количество цветов на экране, контраст буфера экрана, контраст снимка экрана, контраст экрана, уменьшение цветов контрастом, уменьшение количества цветов контрастом, уменьшить количество цветов контрастом в буфере экрана, уменьшить количество цветов на экране контрастом',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='colorgen',
         name_isupper=1,
         parent_id=11,
         description=('Функция. Генерирует код цвета путем соединения значений красного, зеленого и синего каналов.'),
         syntax='COLORGEN(red, green, blue)',
         parameters=(
                    'red - значение красного канала (0..255)\n'
                    'green - значение зеленого канала (0..255)\n'
                    'blue - значение синего канала (0..255)'
                    ),
         example=(
                '// создаем цвет\n'
                '$c = COLORGEN(234,34,65)\n'
                '\n'
                '// и разбираем его по каналам\n'
                'LOGWRITE("red: ", colorR($c)) // красный\n'
                'LOGWRITE("grn: ", colorG($c)) // зеленый\n'
                'LOGWRITE("blu: ", colorB($c)) // синий'
                ),
         notes='Получаем код цвета в десятичном формате из трёх значений RGB (красного, зелёного и синего)',
         keywords='colorgen, колорген, rgb to dec, rgb2dec, каналы цвета в десятичный формат цвета кликера, узнать десятичный формат цвета кликера, вычислить десятичный формат цвета кликера, высчитать десятичный формат цвета кликера из значений rgb, цвет из значений красного, зелёного и синего, цвет из значений красного, зеленого и синего',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='colorr, colorg, colorb',
         name_isupper=1,
         parent_id=11,
         description=('Функции. Извлекают из цвета значение красного (зеленого) (синего) канала.'),
         syntax=(
                'COLORR(color)\n'
                'COLORG(color)\n'
                'COLORB(color)'
                ),
         parameters=('color - код цвета'),
         example=(
                '// хватаем произвольный пиксель с экрана\n'
                'GETSCREEN\n'
                '$p = PXL(RND(0, 300), RND(0, 300))\n'
                '\n'
                '// и разбираем его по цветам\n'
                'LOGWRITE("R:", COLORR($p))\n'
                'LOGWRITE("G:", COLORG($p))\n'
                'LOGWRITE("B:", COLORB($p))'
                ),
         notes='Код цвета указывается в десятичном формате - формате кликера',
         keywords='colorr, colorg, colorb, получить составляющую цвета, получить красную составляющую цвета, получить синюю составляющую цвета, получить зелёную составляющую цвета, получить зеленую составляющую цвета, получить знаначение канала цвета, получить знаначение красного канала цвета, получить знаначение синего канала цвета, получить знаначение зелёного канала цвета, получить знаначение зеленого канала цвета',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
])

# Вывод информации
DATA_ELEMENTS.extend([
    dict(name='logwrite, print',
         name_isupper=1,
         parent_id=12,
         description=('Выводит сообщение в окно лога программы.'),
         syntax=(
                'LOGWRITE(str, ...)\n'
                '// или\n'
                'PRINT(str, ...)'
                ),
         parameters=('str - строка сообщения'),
         example=(
                '$var = 5\n'
                '// вывод составного сообщения (коментарий и значение переменной)\n'
                'LOGWRITE("Переменная $var = ", $var)'
                ),
         notes='Данная инструкция имеет псевдоним PRINT, синтаксис аналогичен. Число параметров данной инструкции неограниченно. В случае указания директивы #logfile, помимо окна лога, сообщение записывается в файл.',
         keywords='logwrite, print, логврайт, принт, логирование, вывод сообщения в лог, вывод текста в лог, вывести сообщение в лог, вывести текст в лог, печать в лог, вывод сообщения в окно лога, вывод текста в окно лога, вывести сообщение в окно лога, вывести текст в окно лога, печать в окно лога',
         version_cm_major=3,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='alpha',
         ),
    dict(name='logwritec, printc',
         name_isupper=1,
         parent_id=12,
         description=('Выводит цветное сообщение в окно лога программы.'),
         syntax=(
                'LOGWRITEC(str, [color])\n'
                '// или\n'
                'PRINT(str, [color])'
                ),
         parameters=(
                    'str - строка сообщения\n'
                    'color - необязательный параметр; код цвета'
                    ),
         example=(
                '// вывод красного, зеленого или синего сообщения\n'
                'LOGWRITEC("Цветной текст", rndfrom(255, 65280, 16711680))'
                ),
         notes='Данная инструкция имеет псевдоним PRINTС, синтаксис аналогичен. Если параметр color не указан, его значение считается 0, что соответствует черному цвету. В случае указания директивы #logfile, помимо окна лога, сообщение записывается в файл.',
         keywords='logwritec, printc, логврайтц, принтц, логврайтси, принтси, цветное логирование, вывод цветного сообщения в лог, вывод цветного текста в лог, вывести цветное сообщение в лог, вывести цветной текст в лог, печать в лог цветным, вывод цветного сообщения в окно лога, вывод цветного текста в окно лога, вывести цветное сообщение в окно лога, вывести цветной текст в окно лога, печать в окно лога цветным',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='logclear',
         name_isupper=1,
         parent_id=12,
         description=('Очищает окно лога программы.'),
         syntax='LOGCLEAR()',
         # parameters=(''),
         # example=(''),
         notes='Очищается только окно, если лог дублируется в файл, файл не затрагивается',
         keywords='logclear, логклеар, логклэар, логклир, очистить окно лога, очистить лог, удалить лог из программы',
         version_cm_major=3,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='alpha',
         ),
    dict(name='logshow',
         name_isupper=1,
         parent_id=12,
         description=('Отображает либо скрывает окно лога программы.'),
         syntax='LOGSHOW(show, [x, y])',
         parameters=(
                    'show - флаг отображения; если = 1, окно будет отображено, если = 0, то скрыто\n'
                    'x, y - необязательные параметры; позиция окна лога на экране'
                    ),
         example=(
                'LOGSHOW(1, 10, 100])\n'
                'LOGWRITE("Это текст в логе")'
                ),
         # notes='',
         keywords='logshow, логшов, отобразить окно лога в координатах, показать окно лога в координатах, скрыть окно лога, убрать окно лога, спрятать окно лога, задать координаты окну лога, переместить окно лога в координаты, передвинуть окно лога в координаты, задать координаты логу, переместить лог в координаты, передвинуть лог в координаты',
         version_cm_major=3,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='alpha',
         ),
    dict(name='sound',
         name_isupper=1,
         parent_id=12,
         description=('Воспроизводит звуковой *.wav файл.'),
         syntax='SOUND(file)',
         parameters=('file - путь к файлу'),
         example=('SOUND("tadam.wav")'),
         notes='поддерживается только WAV формат. На время проигрывания скрипт приостанавливается.',
         keywords='sound, соунд, проиграть звук, воспроизвести звук, проиграть звуковой файл, воспроизвести звуковой файл, звуковой сигнал',
         version_cm_major=3,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='RC1',
         ),
    dict(name='beep',
         name_isupper=1,
         parent_id=12,
         description=('Воспроизводит звуковой сигнал через системный динамик (спикер).'),
         syntax='BEEP(freq, [time])',
         parameters=(
                'freq - высота воспроизводимого звука\n'
                'time - необязательный параметр; продолжительность воспроизведения звука в миллисекундах'
                    ),
         example=(
                '// Queen - Another One Bites The Dust (lol :D)\n'
                'BEEP(110, 170)\n'
                'WAITMS(10)\n'
                'BEEP(100, 140)\n'
                'waitms(190)\n'
                '\n'
                'FOR($i=0, $i < 2)\n'
                '    BEEP(90, 200)\n'
                '    WAITMS(300)\n'
                '    BEEP(90, 200)\n'
                '    WAITMS(300)\n'
                '    BEEP(90, 200)\n'
                '    WAITMS(500)\n'
                '\n'
                '    BEEP(90, 140)\n'
                '    WAITMS(60)\n'
                '    BEEP(90, 140)\n'
                '    WAITMS(60)\n'
                '    BEEP(95, 120)\n'
                '    WAITMS(75)\n'
                '\n'
                '    BEEP(90, 120)\n'
                '    WAITMS(60)\n'
                '    BEEP(95, 140)\n'
                '    WAITMS(105)\n'
                '\n'
                '    BEEP(90, 170)\n'
                '    WAITMS(10)\n'
                '    BEEP(110, 150)\n'
                '    WAITMS(500)\n'
                'END_CYC'
                ),
         notes='Данная процедура задерживает сценарий на время проигрывания сигнала. По умолчанию time = 333 (треть секунды). Звук будет воспроизводится через спикер материнской платы, если он существует на вашем компьютере!',
         keywords='beep, бип, бипер, спикер, воспроизвести звук спикера, воспроизвести звук через спикер, проиграть звук спикера, проиграть звук через спикер, воспроизвести звук через системный динамик, воспроизвести звук через через системный динамик, проиграть звук через системный динамик, воспроизвести звуковой сигнал, проиграть звуковой сигнал',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='hintpopup',
         name_isupper=1,
         parent_id=12,
         description=('Выводит всплывающее сообщение в системный трей.'),
         syntax='HINTPOPUP(message, [title])',
         parameters=(
                    'message - строка сообщения\n'
                    'title - необязательный параметр; заголовок сообщения'
                    ),
         example=('HINTPOPUP("Внимание!", "Это суперважное сообщение")'),
         notes='В системх по Windows 7 последующее сообщение убирало предыдущее',
         keywords='hintpopup, хинтпопап, выводит всплывающее сообщение в системный трей, выводит всплывающее сообщение в трей, выводит сообщение в системный трей, выводит сообщение в трей, вывести всплывающее сообщение в системный трей, вывести всплывающее сообщение в трей, вывести сообщение в системный трей, вывести сообщение в трей',
         version_cm_major=4,
         version_cm_minor=6,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='fromclip',
         name_isupper=1,
         parent_id=12,
         description=('Функция. Возвращает строку, находящуюся в буфере обмена.'),
         syntax='FROMCLIP()',
         # parameters=(''),
         example=('LOGWRITE(FROMCLIP())'),
         notes='Обратите внимание что пустые скобки все равно ставятся',
         keywords='fromclip, фромклип, прочитать буфер обмена, взять из буфера обмена, вернуть из буфера обмена, получить из буфера обмена, прочитать данные из буфера обмена, взять данные из буфера обмена, вернуть данные из буфера обмена, получить данные из буфера обмена',
         version_cm_major=4,
         version_cm_minor=0,
         version_cm_build=2,
         version_cm_releaselevel='',
         ),
    dict(name='writemem',
         name_isupper=1,
         parent_id=12,
         description=('Помещает целое значение в память процесса.'),
         syntax='WRITEMEM(pid, addr, value, [size])',
         parameters=(
                    'pid - идентификатор процесса\n'
                    'addr - адрес памяти\n'
                    'value - численное значение\n'
                    'size - тип значения (1,2,4,8)'
                    ),
         example=('WRITEMEM(2080, 0x0006F2B7, 5000)'),
         notes='Идентификатор процесса pid можно узнать в диспетчере задач либо в самом кликере: в области "Оконный режим" и через функцию hgetpid().\nАдрес представляет собой обычное целое число в десятичной или шестнадцатеричной записи. Параметр size указывает на размер целого значения: 1, 2, 4 или 8 байт. Если данный параметр опущен, то он принимается за 4',
         keywords='writemem, враитмем, враитмэм, записать в память процесса, помещает целое значение в память процесса, помещает значение в память процесса, записывает значение в память процесса',
         version_cm_major=4,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
])

# Ввод информации
DATA_ELEMENTS.extend([
    dict(name='inputbox',
         name_isupper=1,
         parent_id=13,
         description=('Функция. Выводит диалоговое окно для ввода строки.'),
         syntax='INPUTBOX(message, default, [delay])',
         parameters=(
                    'message - сообщение диалогового окна\n'
                    'default - значение по умолчанию\n'
                    'delay - необязательный параметр; таймаут'
                    ),
         example=(
                '$str = INPUTBOX("text", "hello")\n'
                'LOGWRITE($str)'
                ),
         notes='Диалоговое окно находится на экране delay секунд. Если за это время пользователь не начал ввод или не нажал одну из кнопок, то функция вернет строку по умолчанию - default. Если пользователь нажал отмену, то будет возвращена пустая строка. По умолчанию параметр delay равен 5. Возможно использовать кнопки Enter для ввода и Esc для отмены.',
         keywords='inputbox, инпутбокс, вывести диалоговое окно, выводит диалоговое окно, окно ввода строки, ввести строку в окно',
         version_cm_major=4,
         version_cm_minor=5,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='dialogbox',
         name_isupper=1,
         parent_id=13,
         description=('Функция. Выводит диалоговое окно с кнопками.'),
         syntax='DIALOGBOX(message, buttons, [icon])',
         parameters=(
                    'message - сообщение диалогового окна\n'
                    'buttons - код набора кнопок\n'
                    'icon - код иконки\n'
                    '\n'
                    'Коды наборов кнопок\n'
                    'Код Кнопка\n'
                    '0 OK\n'
                    '1 OK, CANCEL\n'
                    '2 ABORT, RETRY, IGNORE\n'
                    '3 YES, NO, CANCEL\n'
                    '4 YES, NO\n'
                    '5 RETRY, CANCEL\n'
                    '\n'
                    'Коды иконок\n'
                    'Код Кнопка\n'
                    '0 Без иконки\n'
                    '1 Ошибка\n'
                    '2 Вопрос\n'
                    '3 Внимание\n'
                    '4 Информирование\n'
                    '\n'
                    'Возвращаемые коды\n'
                    'Код Кнопка\n'
                    '1 OK\n'
                    '2 CANCEL\n'
                    '3 ABORT\n'
                    '4 RETRY\n'
                    '5 IGNORE\n'
                    '6 YES\n'
                    '7 NO'
                    ),
         example=(
                '// Выводит диалоговое окно с двумя кнопками - Yes, No\n'
                '$mr = DIALOGBOX("Yes or No?", 4)\n'
                '\n'
                'IF($mr = 6)\n'
                '   LOGWRITE("Yes")\n'
                'ELSE\n'
                '   LOGWRITE("No")\n'
                'END_IF'
                ),
         notes='Функция возвращает код той кнопки, которую нажал пользователь. Выполнение скрипта будет остановлено до тех пор, пока какая-либо из кнопок не будет нажата. По умолчанию параметр icon равен 0.',
         keywords='dialogbox, диалогбокс, вывести диалоговое окно с кнопками, выводит диалоговое окно с кнопками, выбор кнопками в окне',
         version_cm_major=4,
         version_cm_minor=8,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='radiobox',
         name_isupper=1,
         parent_id=13,
         description=('Функция. Выводит диалоговое окно с переключателями.'),
         syntax='RADIOBOX(message, radio1, ...)',
         parameters=(
                    'message - сообщение диалогового окна\n'
                    'radio1 - строка, описывающая переключатель'
                    ),
         example=(
                '$res = RADIOBOX("Выберете пункт", "1 Мясо", "2 Птица", "3 Рыба")\n'
                'IF($res > 0)\n'
                '   LOGWRITE("Вы выбрали: ", $res)\n'
                'ELSE\n'
                '   LOGWRITE("Вы ничего не выбрали")\n'
                'END_IF'
                ),
         notes='Число параметров данной инструкции неограниченно. Функция возвращает порядковый номер выбранного элемента. Выполнение скрипта будет остановлено до тех пор, пока не будет нажаты OK или CANCEL. В случае нажатия CANCEL, функция вернет 0.',
         keywords='кнопки radiobox, кнопки радиобокс, вывести диалоговое окно с переключателями, выводит диалоговое окно с переключателями, выбор кнопками в окне, окно выбора одного из вариантов, радио кнопки, радиокнопки',
         version_cm_major=4,
         version_cm_minor=12,
         version_cm_build=1,
         version_cm_releaselevel='',
         ),
    dict(name='toclip',
         name_isupper=1,
         parent_id=13,
         description=('Помещает текст сообщения в буфер обмена.'),
         syntax='TOCLIP(str)',
         parameters=('str - строка'),
         example=(
                'TOCLIP("https://yandex.ru/")\n'
                'WAITMS(150)'
                ),
         notes='Работа с буфером обмена осуществляется Windows не моментально. После команды занесения, если собираетесь сразу использовать значение из буфера, необходимо поставить задержку. Задержка зависит от загруженности системы и других условий работы.',
         keywords='toclip, токлип, туклип, помещает текст сообщения в буфер обмена, помещает текст в буфер обмена, помещает сообщение в буфер обмена, помещает в буфер обмена, поместить текст сообщения в буфер обмена, поместить текст в буфер обмена, поместить сообщение в буфер обмена, поместить в буфер обмена, строку в буфер обмена, значение в буфер обмена',
         version_cm_major=3,
         version_cm_minor=2,
         version_cm_build=0,
         version_cm_releaselevel='beta',
         ),
    dict(name='readmem',
         name_isupper=1,
         parent_id=13,
         description=('Функция. Извлекает целое значение из памяти процесса.'),
         syntax='READMEM(pid, addr, [size])',
         parameters=(
                    'pid - идентификатор процесса\n'
                    'addr - строка, адрес памяти\n'
                    'size - тип значения (1,2,4,8)'
                    ),
         example=(
                '$var = READMEM(2080, 0x0006F2B7)\n'
                'LOGWRITE($var)'
                ),
         notes='Идентификатор процесса pid можно узнать в диспетчере задач либо в самом кликере: в области "Оконный режим" и через функцию hgetpid().\nАдрес представляет собой обычное целое число в десятичной или шестнадцатеричной записи. Параметр size указывает на размер целого значения: 1, 2, 4 или 8 байт. Если данный параметр опущен, то он принимается за 4',
         keywords='readmem, реадмем, реадмэм, извлекает целое значение из памяти процесса, извлекает значение из памяти процесса, извлекает из памяти процесса, читает целое значение из памяти процесса, читает значение из памяти процесса, читает из памяти процесса',
         version_cm_major=4,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='httpget',
         name_isupper=1,
         parent_id=13,
         description=('Функция. Возвращает результат web-запроса.'),
         syntax='HTTPGET(url, [headers, ...])',
         parameters=(
                    'url - запрос\n'
                    'headers - дополнительные заголовки запроса'
                    ),
         example=(
                '// код вернет последную опубликованную версию Clickermann (можете проверить в браузере)\n'
                '$str = HTTPGET("http://crapware.aidf.org/version/clickermann.php")\n'
                '\n'
                '// тот же запрос, но с добавленным заголовком Referrer\n'
                '$str = HTTPGET("http://crapware.aidf.org/version/clickermann.php", "Referrer: http://crapware.aidf.org")\n'
                '\n'
                'LOGWRITE($str)'
                ),
         notes='Функция запрашивает данные по протоколу HTTP. Следовательно пока удаленный сервер не ответит (или не истечет таймаут), функция не завершится.\nТак же функция может использоваться для отправки командных запросов (запросов с параметрами) удаленному серверу (запросы типа http://somegame.ru/index.php?act=go_to_work&player_id=12345). В любом случае, даже если возвращаемая строка не важна, функция должна вызываться как функция (см. пример)',
         keywords='httpget, finngutn, ашттпгэт, возвращает результат web-запроса, вернуть результат web-запроса, сделать web-запрос, гет запрос, гэт запрос, http get запрос, http get-запрос',
         version_cm_major=4,
         version_cm_minor=5,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
])

# Управление скриптом, плагины
DATA_ELEMENTS.extend([
    dict(name='halt',
         name_isupper=1,
         parent_id=14,
         description=('Полностью останавливает выполнение сценария.'),
         syntax='HALT([close])',
         parameters=('close - необязательный параметр; если 1, то clickermann закрывается целиком'),
         example=(
                '// остановить скрипт\n'
                'HALT\n'
                '\n'
                '// остановить скрипт и закрыть кликер\n'
                'HALT(1)'
                ),
         # notes='',
         keywords='halt, халт, стоп скрипт, стоп программа, стоп выполнение скрипта, стоп выполнение программы, остановить скрипт, остановить программу, остановить выполнение скрипта, остановить выполнение программы, остановить и закрыть кликер, остановить и закрыть программу, выйти из программы, выйти из кликера',
         version_cm_major=3,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='alpha',
         ),
    dict(name='wait',
         name_isupper=1,
         parent_id=14,
         description=('Приостанавливает выполнение сценария на несколько секунд.'),
         syntax='WAIT(delay)',
         parameters=('delay - числовое значение, обозначающее длину задержки в секундах'),
         example=(
                '// задержка 25 секунд\n'
                'WAIT(25)\n'
                '// задержка 3 секунды 250 миллисекунд (3 с четвертью секунды)\n'
                'WAIT(3.25)'
                ),
         notes='Во время задержки другие инструкции в этом потоке не выполняются, но могут выполняться в других потоках если они есть и работают.\nЗадержка имеет некоторую неустранимую погрешность, зависящую от некоторых факторов. На практике, погрешность обычно не превышает 5 мс (0,005 сек.).\nДопускается указание дробного аргумента. Так, задержка 1.25 будет означать одну секунду и 250 миллисекунд.',
         keywords='wait, ваит, вэит, вэйт, приостановить выполнение сценария на несколько секунд, пауза в секундах, задержка в секундах, пауза в скрипте в секундах, пауза в программе в секундах, задержка в скрипте в секундах, задержка в программе в секундах, поставить паузу в секундах, поставить задержку в секундах, замедлить выполнение в секундах',
         version_cm_major=1,
         version_cm_minor=1,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='waitms',
         name_isupper=1,
         parent_id=14,
         description=('Приостанавливает выполнение сценария на несколько миллисекунд.'),
         syntax='WAITMS(delay)',
         parameters=('delay - целое числовое значение, обозначающее длину задержки в миллисекундах'),
         example=(
                '// задержка 20 миллисекунд\n'
                'WAITMS(20)\n'
                '// задержка 8500 миллисекунд (8.5 секунд)\n'
                'WAITMS(8500)'
                ),
         notes='В одной секунде 1000 миллисекунд.\nЗначение миллисекунд должно быть только целым числом!\nЗадержка имеет некоторую неустранимую погрешность, зависящую от некоторых факторов. На практике, погрешность обычно не превышает 5 мс (0,005 сек.) ',
         keywords='waitms, ваитмс, вэитмс, вэйтмс, приостановить выполнение сценария на несколько миллисекунд, пауза в миллисекундах, задержка в миллисекундах, пауза в скрипте, пауза в программе, задержка в скрипте, задержка в программе в миллисекундах, поставить паузу в миллисекундах, поставить задержку в миллисекундах, замедлить выполнение в миллисекундах',
         version_cm_major=1,
         version_cm_minor=3,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='goto',
         name_isupper=1,
         parent_id=14,
         description=('Переход выполнения скрипта на строку с меткой.'),
         syntax=(
                'GOTO(label)\n'
                '...\n'
                'label:'
                ),
         parameters=('label - имя метки'),
         example=(
                'GOTO(skip)\n'
                'LOGWRITE("nope") // пропускается\n'
                'skip:\n'
                'LOGWRITE("yea")  // выполнится'
                ),
         notes='Переход на метку допускается в рамках блоков одного уровня вложенности. Категорически не рекомендуется переходить за пределы циклов, подпрограмм, потоков, как и входить в них по GOTO!\nТекстовая метка задается без кавычек, в тексте скрипта после текстовой метки обязательно должно идти двоеточие ":", как в примере. Метка занимает всю строку',
         keywords='goto, гоуту, гото, готу, переход выполнения скрипта на строку с меткой, переход выполнения на строку с меткой, переход скрипта на строку с меткой, переход на строку с меткой, перейти на строку с меткой, перейти по метке, перейти по goto, перейти по гоуту',
         version_cm_major=3,
         version_cm_minor=0,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='execute',
         name_isupper=1,
         parent_id=14,
         description=('Вызывает внешний файл или консолькую команду.'),
         syntax='EXECUTE(filename, [param])',
         parameters=(
                    'filename - имя файла\n'
                    'param - необязательный параметр; строка параметров'
                    ),
         example=(
                '// вызываем батник\n'
                'execute("some.bat")\n'
                '\n'
                '// пингуем яндекс\n'
                'execute("ping", "ya.ru -n 10")\n'
                '\n'
                '// запускаем хром и окрываем форум кликера\n'
                'execute("chrome.exe", "http://crapware.aidf.org/forum/index.php")'
                ),
         notes='Инструкция вызывает произвольный внешний файл. При этом запуск обрабатывается согласно ассоциациям, прописанным в системе. Дает схожий результат с "Пуск" -> "Выполнить" (Win + R). Допускается задание как относительного пути к файлу, так и абсолютного. Инструкция сразу же возвращает управление в программу без ожидания независимо от времени запуска внешнего файла и его обработчика.',
         keywords='execute, экзекуте, экзекутэ, вызвать внешний файл или консолькую команду, вызвать файл, запустить файл, запустить программу, запустить приложение',
         version_cm_major=4,
         version_cm_minor=6,
         version_cm_build=1,
         version_cm_releaselevel='',
         ),
    dict(name='call',
         name_isupper=1,
         parent_id=14,
         description=('Вызывает плагин.'),
         syntax='CALL("filename", par1, ...)',
         parameters=(
                    'filename - имя файла плагина относительно текущей директории\n'
                    'par1, ... - целочисленные параметры'
                    ),
         example=(
                'CALL("plugin_example.dll", 5, 2, 3)\n'
                'LOGWRITE($_return1)'
                ),
         notes='Кликер ждет момента отработки плагина и только потом продолжает работу. Плагин возвращает значение в переменную $_return1.\nРекомендуется ознакомиться с [пояснением](https://clickermann-help.netlify.app/plugin.html)',
         keywords='call, калл, вызвать плагин, вызвать функцию из dll, вызвать функцию из длл, вызвать dll, вызвать длл, запустить плагин, запустить функцию из dll, запустить функцию из длл',
         version_cm_major=4,
         version_cm_minor=0,
         version_cm_build=2,
         version_cm_releaselevel='',
         ),
    dict(name='callarr',
         name_isupper=1,
         parent_id=14,
         description=('Вызывает плагин, передавая параметры массивом.'),
         syntax='CALLARR("filename", $arr)',
         parameters=(
                    'filename - имя вызываемого плагина\n'
                    '$arr - целочисленный массив'
                    ),
         example=(
                '$arr[0] = 5\n'
                '$arr[1] = 6\n'
                'CALLARR("plugin_example.dll", $arr)\n'
                'LOGWRITE($_return1)'
                ),
         notes='Кликер ждет момента отработки плагина и только потом продолжает работу. Плагин возвращает значение в переменную $_return1.\nРекомендуется ознакомиться с [пояснением](https://clickermann-help.netlify.app/plugin.html)',
         keywords='callarr, калларр, каларр, вызвать плагин, вызвать функцию из dll, вызвать функцию из длл, вызвать dll, вызвать длл, запустить плагин, запустить функцию из dll, запустить функцию из длл',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='httpget',
         name_isupper=1,
         parent_id=14,
         description=('Функция. Возвращает результат web-запроса.'),
         syntax='HTTPGET(url, [headers, ...])',
         parameters=(
                    'url - запрос\n'
                    'headers - дополнительные заголовки запроса'
                    ),
         example=(
                '// код вернет последную опубликованную версию Clickermann\n'
                '$str = HTTPGET("http://crapware.aidf.org/version/clickermann.php")\n'
                '\n'
                '// тот же запрос, но с добавленным заголовком Referrer\n'
                '$str = HTTPGET("http://crapware.aidf.org/version/clickermann.php", "Referrer: http://crapware.aidf.org")\n'
                '\n'
                'LOGWRITE($str)'
                ),
         notes='Функция запрашивает данные по протоколу HTTP. Следовательно пока удаленный сервер не ответит (или не истечет таймаут), функция не завершится.\nТак же функция может использоваться для отправки командных запросов (запросов с параметрами) удаленному серверу (запросы типа http://somegame.ru/index.php?act=go_to_work&player_id=12345). В любом случае, даже если возвращаемая строка не важна, функция должна вызываться как функция (см. пример).',
         keywords='httpget, сделать web-запрос к сайту, сделать web запрос к сайту, сделать запрос к сайту, сделать get-запрос к сайту, сделать get запрос к сайту',
         version_cm_major=4,
         version_cm_minor=5,
         version_cm_build=0,
         version_cm_releaselevel='b',
         ),
])

# Работа с окнами. WinAPI
DATA_ELEMENTS.extend([
    dict(name='hget',
         name_isupper=1,
         parent_id=15,
         description=('Функция. Возвращает hwnd для элемента по заданным координатам.'),
         syntax='HGET(x, y)',
         parameters=('x, y - координаты пикселя, принадлежащего элементу'),
         example=(
                '// получение hwnd элемента\n'
                '$h = HGET(44, 1010)\n'
                '\n'
                '// вывод в лог текста на элементе\n'
                'LOGWRITE(HGETTEXT($h))'
                ),
         # notes='',
         keywords='hget, ашгет, получить hwnd элемента по заданным координатам, получить hwnd элемента по координатам, получить hwnd окна по координатам, получить hwnd по координатам, получить хэндл окна по координатам',
         version_cm_major=4,
         version_cm_minor=3,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='hset',
         name_isupper=1,
         parent_id=15,
         description=('Устанавливает новый рабочий элемент для оконного режима кликера.'),
         syntax='HSET(hwnd, state)',
         parameters=(
                    'hwnd - hwnd элемента\n'
                    'state - состояние оконного режима (1 - вкл. 0 - выкл.)'
                    ),
         example=(
                '// получение hwnd элемента\n'
                '$hwnd = HGET(44, 1010)\n'
                '\n'
                '// включение оконного режима, "нацеленного" на этот элемент\n'
                'HSET($hwnd, 1)'
                ),
         notes='Если вы хотите просто сменить рабочий элемент - нет необходимости выключать оконный режим флагом 0. Просто задаете новый первым параметром.',
         keywords='hset, ашсет, установить новый рабочий элемент для оконного режима, привязать окно по hwnd, привязать новое окно по hwnd, привязать другое окно по hwnd, отвязать окно, отключить привязку',
         version_cm_major=4,
         version_cm_minor=3,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='hgetpid',
         name_isupper=1,
         parent_id=15,
         description=('Функция. Возвращает pid идентификатор родительского процесса по hwnd дочернего окна.'),
         syntax='HGETPID(hwnd)',
         parameters=('hwnd - hwnd элемента'),
         example=(
                '// PID кликера\n'
                '$pid_cm = HGETPID($_hwnd_self)\n'
                'LOGWRITE($pid_cm)'
                ),
         notes='pid процесса представляет собой целое число',
         keywords='hgetpid, ашгетпид, получить pid процесса, получить пид процесса, получить pid идентификатор родительского процесса, получить pid родительского процесса, получить ид процесса, получить id процесса',
         version_cm_major=4,
         version_cm_minor=13,
         version_cm_build=14,
         version_cm_releaselevel='',
         ),
    dict(name='hgettext',
         name_isupper=1,
         parent_id=15,
         description=('Функция. Возвращает текст на элементе управления в окнах Windows.'),
         syntax='HGETTEXT(hwnd)',
         parameters=('hwnd - hwnd элемента'),
         example=(
                '// Пример 1\n'
                '$h = HGET(44, 1010)\n'
                'LOGWRITE(HGETTEXT($h))\n'
                '\n'
                '// Пример 2 (через строковую переменную)\n'
                '$h = HGET(44, 1010)\n'
                '$text = HGETTEXT($h)\n'
                'LOGWRITE($text)'
                ),
         # notes='',
         keywords='hgettext, ашгеттекст, получить текст на элементе управления, получить текст на элементе окна, получить текст в окне, получить текст из окна',
         version_cm_major=4,
         version_cm_minor=3,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='hsettext',
         name_isupper=1,
         parent_id=15,
         description=('Устанавливает текст на элементах управления в окнах Windows.'),
         syntax='HSETTEXT(hwnd, text)',
         parameters=(
                    'hwnd - hwnd элемента\n'
                    'text - текст'
                    ),
         example=(
                '// Меняем заголовок окна редактора кликера\n'
                '$hwnd = WNDFIND("Редактор", 1)\n'
                'HSETTEXT($hwnd, "Мегасуперпуперредактор")'
                ),
         # notes='',
         keywords='hsettext, ашсеттекст, ашсэттекст, задать текст на элементе управления, задать текст на элементе окна, задать текст в окне, задать текст на элементе окна, установить текст на элементе управления, установить текст на элементе окна, установить текст в окне, установить текст на элементе окна',
         version_cm_major=4,
         version_cm_minor=3,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='wndfind',
         name_isupper=1,
         parent_id=15,
         description=('Функция. Возвращает HWND окна с заданным заголовком.'),
         syntax='WNDFIND(title, [begin])',
         parameters=(
                    'title - заголовок окна либо его часть\n'
                    'begin - необязательный параметр; флаг сообщает о том, что строка title может находиться ТОЛЬКО в начале заголовка'
                    ),
         example=(
                '// скрипт найдет окно с заголовком, содержащим "Блокнот"\n'
                '// и поместит его в левый верхний угол (с отступом 10 пикселей)\n'
                'WNDPOS(WNDFIND("Блокнот"), 10, 10)\n'
                '\n'
                '// скрипт найдет окно с заголовком, содержащим "Блокнот"\n'
                '// и переименует его в "Калькулятор"\n'
                'HSETTEXT(WNDFIND("Блокнот"), "Калькулятор")'
                ),
         notes='Чем полнее будет указан заголовок, тем меньше шанс что функция "схватит" не то окно. Если функция не найдет окна, удовлетворяющего условиям, она вернет 0. Данная функция не подходит для поиска отдельных элементов окон (кнопки, поля, надписи).',
         keywords='wndfind, вндфинд, поиск hwnd окна с заданным заголовком, найти hwnd окна с заданным заголовком, получить hwnd окна с заданным заголовком, поиск hwnd нужного окна, найти hwnd нужного окна, получить hwnd нужного окна, поиск окна с заданным заголовком, найти окно с заданным заголовком, поиск окна с заголовком, найти окно с заголовком, поиск окна по заголовку, найти окно по заголовку, поиск hwnd окна с указанным заголовком, найти hwnd окна с указанным заголовком, получить hwnd окна с указанным заголовком, поиск hwnd нужного окна, найти hwnd нужного окна, получить hwnd нужного окна, поиск окна с указанным заголовком, найти окно с указанным заголовком, поиск окна с заголовком, найти окно с заголовком',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='wndfindarr',
         name_isupper=1,
         parent_id=15,
         description=('Помещает в массив HWND всех окон с указанным заголовком.'),
         syntax='WNDFINDARR(arr, title)',
         parameters=(
                    'arr - входной массив\n'
                    'title - заголовок окна либо его часть'
                    ),
         example=(
                '// Переименовывание всех блокнотов в калькуляторы\n'
                'WNDFINDARR($arr, "Блокнот")\n'
                '\n'
                'FOR($i=0, $i < ARRSIZE($arr))\n'
                '    HSETTEXT($arr[$i], "Калькулятор")\n'
                'END_CYC'
                ),
         notes='Чем полнее будет указан заголовок, тем меньше шанс что процедура "схватит" не то окно. Данная процедура не подходит для поиска отдельных элементов окон (кнопки, поля, надписи).',
         keywords='wndfindarr, вндфиндарр, поиск hwnd всех окон с заданным заголовком, найти hwnd всех окон с заданным заголовком, получить hwnd всех окон с заданным заголовком, поиск всех окон с заданным заголовком, найти всех окон с заданным заголовком, поиск всех окон с заголовком, найти все окна с заголовком, поиск всех окон по заголовку, найти все окна по заголовку, поиск hwnd всех окон с указанным заголовком, найти hwnd всех окон с указанным заголовком, получить hwnd всех окон с указанным заголовком, поиск всех окон с указанным заголовком, найти все окна с указанным заголовком, поиск всех окон с заголовком, найти все окна с заголовком',
         version_cm_major=4,
         version_cm_minor=14,
         version_cm_build=3,
         version_cm_releaselevel='b',
         ),
    dict(name='wndpos',
         name_isupper=1,
         parent_id=15,
         description=('Помещает окно на экране в указанные координаты.'),
         syntax='WNDPOS(hwnd, x, y)',
         parameters=(
                    'hwnd - HWND окна\n'
                    'x, y - экранные координаты'
                    ),
         example=(
                '// скрипт найдет окно с заголовком, содержащим "Блокнот"\n'
                '// и поместит его в левый верхний угол 10:10\n'
                'WNDPOS(WNDFIND("Блокнот"), 10, 10)'
                ),
         # notes='',
         keywords='wndpos, вндпос, поместить окно на экране в указанные координаты, поместить окно в указанные координаты на экране, передвинуть окно в указанные координаты на экране, поместить окно на экране в координаты, поместить окно в координаты на экране, передвинуть окно в координаты на экране, задать координаты окну, задать позицию окна',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='wndsize',
         name_isupper=1,
         parent_id=15,
         description=('Задает размер окна.'),
         syntax='WNDSIZE(hwnd, w, h)',
         parameters=(
                    'hwnd - HWND окна\n'
                    'w, h - ширина, высота окна'
                    ),
         example=(
                '// скрипт найдет окно с заголовком, содержащим "Блокнот"\n'
                '// и изменит его размер на квадрат 300 на 300\n'
                'WNDSIZE(WNDFIND("Блокнот"), 300, 300)'
                ),
         notes='Уменьшить до одного пикселя окно не получится, так как будут "мешаться" иконки и пара букв из заголовка',
         keywords='wndsize, вндсайз, задать размер окна, задать размеры окна, задать ширину окна, задать высоту окна, установить размер окна, установить размеры окна, установить ширину окна, установить высоту окна.\nДля разворачивания окна на весь экран (maximize) можно использовать команду\nPOSTMESSAGE($hwnd, 0x0112, 0xF030, 0)',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='wndgetinfo',
         name_isupper=1,
         parent_id=15,
         description=('Получает информацию об окне и записывает ее в указанные переменные.'),
         syntax='WNDGETINFO(hwnd, $var1, $var2, $var3, $var4)',
         parameters=(
                    'hwnd - HWND окна\n'
                    '$var1 - X координата окна\n'
                    '$var2 - Y координата окна\n'
                    '$var3 - ширина окна\n'
                    '$var4 - высота окна'
                    ),
         example=(
                '// получаем информацию окна калькулятора\n'
                '$hwnd = WNDFIND("Калькулятор")\n'
                'WNDGETINFO($hwnd, $win_x, $win_y, $win_w, $win_h)\n'
                'LOGWRITE("Окно: ", $win_x, ",", $win_y, "  ", $win_w, "x", $win_h)'
                ),
         # notes='',
         keywords='wndgetinfo, вндгетинфо, вндгэтинфо, получить информацию об окне, получить размеры окна, ролучить высоту окна, получить ширину окна, получить координаты окна, получить позицию окна',
         version_cm_major=4,
         version_cm_minor=11,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='wndsetinfo',
         name_isupper=1,
         parent_id=15,
         description=('Задать параметры окна.'),
         syntax='WNDSETINFO(hwnd, $var1, $var2, $var3, $var4)',
         parameters=(
                    'hwnd - HWND окна\n'
                    '$var1 - X координата окна\n'
                    '$var2 - Y координата окна\n'
                    '$var3 - ширина окна\n'
                    '$var4 - высота окна'
                    ),
         example=(
                '// получаем информацию окна калькулятора\n'
                '$hwnd = WNDFIND("Калькулятор")\n'
                'WNDGETINFO($hwnd, $win_x, $win_y, $win_w, $win_h)\n'
                'LOGWRITE("Окно: ", $win_x, ",", $win_y, "  ", $win_w, "x", $win_h)\n'
                '\n'
                '// перезаписываем размер окна\n'
                '$win_w = 300\n'
                '$win_h = 400\n'
                '\n'
                '// обновляем информацию\n'
                'WNDSETINFO($hwnd, $win_x, $win_y, $win_w, $win_h)'
                ),
         notes='Для разворачивания окна на весь экран (maximize) можно использовать команду\nPOSTMESSAGE($hwnd, 0x0112, 0xF030, 0)',
         keywords='wndsetinfo, вндсетинфо, вндсэтинфо, задать информацию об окне, задать размеры окна, задать высоту окна, задать ширину окна, задать координаты окна, задать позицию окна',
         version_cm_major=4,
         version_cm_minor=11,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='wndstate',
         name_isupper=1,
         parent_id=15,
         description=('Сворачивает (разворачивает) окно.'),
         syntax='WNDSTATE(hwnd, state)',
         parameters=(
                    'hwnd  - HWND окна\n'
                    'state - состояние (0 - свернуто, 1 - развернуто)'
                    ),
         example=(
                '// скрипт найдет окно с заголовком, содержащим "Блокнот", и свернет его\n'
                'WNDSTATE(WNDFIND("Блокнот"), 0)\n'
                'WAIT(1)\n'
                '// ... а потом развернет\n'
                'WNDSTATE(WNDFIND("Блокнот"), 1)\n'
                'WAIT(1)'
                ),
         # notes='',
         keywords='wndstate, вндстейт, вндстате, вндстатэ, свернуть окно, развернуть окно, восстановить окно, свернуть окно на панель задач, развернуть окно с панели задач, восстановить окно с панели задач, развернуть окно из панели задач, восстановить окно из панели задач',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='wndbump',
         name_isupper=1,
         parent_id=15,
         description=('Помещает окно на передний план и делает его активным.'),
         syntax='WNDBUMP(hwnd)',
         parameters=('hwnd - HWND окна'),
         example=('WNDBUMP(WNDFIND("Блокнот"))'),
         notes='Можно воспользоваться альтернативной командой\nPOSTMESSAGE(hwnd, 0x0112, 0xF120, 0)',
         keywords='wndbump, вндбамп, поместить окно на передний план и сделать его активным, сделать окно активным, сделать активным окно, поместить окно поверх других окон, поместить окно поверх всех окон',
         version_cm_major=4,
         version_cm_minor=11,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='sendmessage, postmessage',
         name_isupper=1,
         parent_id=15,
         description=('Посылает окну системное сообщение.'),
         syntax='SENDMESSAGE / POSTMESSAGE(hwnd, message, wParam, lParam)',
         parameters=(
                    'hwnd - HWND окна\n'
                    'message - сообщение окну\n'
                    'wParam, lParam - параметры сообщения'
                    ),
         example=(
                '// выделить всё (EM_SETSEL)\n'
                'POSTMESSAGE(hwnd, 0x00B1, 0, -1)\n'
                '// копировать (WM_COPY)\n'
                'POSTMESSAGE(hwnd, 0x0301, 0, -1)\n'
                '// вставить (WM_PASTE)\n'
                'POSTMESSAGE(hwnd, 0x0302, 0, -1)\n'
                '\n'
                '// закрыть окно (WM_CLOSE)\n'
                'POSTMESSAGE(hwnd ,0x0010, 0, 0)'
                ),
         notes='Данные процедуры являются фактически обертками для одноименных WinAPI функций. Подробности вы можете найти в MSDN или на многочисленных форумах.\nПоскольку у нас нет всех констант "WM_", то параметр message необходимо задавать десятичным числом.',
         keywords='sendmessage, postmessage, послать системное сообщение окну, отправить системное сообщение окну, послать окну системное сообщение, отправить окну системное сообщение, послать сообщение окну, отправить сообщение окну',
         version_cm_major=4,
         version_cm_minor=4,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
    dict(name='getmessage',
         name_isupper=1,
         parent_id=15,
         description=('Принимает системное сообщение 1024 (WM_USER), посланное главному окну кликера.'),
         syntax='GETMESSAGE(wParam, lParam, [isnew])',
         parameters=(
                    'wParam, lParam - переменные под параметры принятого сообщения\n'
                    'isnew - необязательный параметр; переменная под флаг-индикатор нового сообщения'
                    ),
         example=(
                '// поиск главного окна кликера\n'
                '$hwnd = WNDFIND("Clickermann")\n'
                '\n'
                '// отправка сообщения окну кликера\n'
                'POSTMESSAGE($hwnd, 1024, 123, 321)\n'
                '\n'
                '// прием сообщения\n'
                'WHILE($isnew = 0)\n'
                '    GETMESSAGE($wPar, $lPar, $isnew)\n'
                '    LOGWRITE("wParam:", $wPar, "  lParam:", $lPar)\n'
                'END_CYC'
                ),
         notes='Данная процедура позволяет принимать ТОЛЬКО сообщения, в которых параметр message = 1024 (см. sendmessage). Процедура позволяет получить параметры только последнего полученного сообщения. Сообщения принимаются только во время выполнения сценария.\nВ момент получения нового сообщения от сторонней программы флаг isnew становится равен 1. При повторных вызовах процедуры до получения очередного сообщения флаг становится равен 0, однако параметры wParam, lParam сохраняют свои значения.\nИдентификатор отлавливаемого сообщения message можно изменить в config.ini (параметр msg_hook).',
         keywords='getmessage, гетмессэйж, принять системное сообщение посланное окну кликера, принять системное сообщение посланное кликеру, принять сообщение посланное окну кликера, принять сообщение посланное кликеру, принять сообщение от других программ',
         version_cm_major=4,
         version_cm_minor=13,
         version_cm_build=14,
         version_cm_releaselevel='',
         ),
])

# Приложение 1. Коды клавиш
DATA_ELEMENTS.extend([
    dict(name='коды клавиш',
         name_isupper=0,
         visible=0,
         parent_id=16,
         description=(''),
         syntax='',
         parameters=(''),
         example=(''),
         notes='',
         keywords='',
         version_cm_major=3,
         version_cm_minor=2,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
])

# --------------------------------------------------------------------------------------------------

'''
DATA_ELEMENTS.extend([
    dict(name='',
         name_isupper=1,
         parent_id=,
         description=(''),
         syntax='',
         parameters=(''),
         example=(''),
         notes='',
         keywords='',
         version_cm_major=3,
         version_cm_minor=2,
         version_cm_build=0,
         version_cm_releaselevel='',
         ),
])
'''


'''
v1.3 (11.04.2009)
+ Введена возможность "записи" сценария

v2.1 (05.08.2009)
+ Улучшеный редактор и ядро:
    + Кнопки быстрой вставки команды в редакторе
    + Подсветка синтаксиса в редакторе
    + Поддержка коментариев "//" (C++ Style)
    + Добавлено озвучивание событий воспроизведения, записи и остановки
    + Новая модная справка
'''
