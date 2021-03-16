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
        keywords='#logfile, logfile, лог, вывод лога в файл, лог в файл, logwrite в файл, printв файл',
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
        example='LCLICK($_xmouse, $_ymouse) - клик в текущих координатах\nPRINT($_cursor) - номер текущего вида курсора',
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
        example='PRINT($_date_str, " ", $_time_str) - выводит в лог текущую дату и время',
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
        example='PRINT($_ver_self) - вывести в лог версию программы',
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
                'PRINT($var)'
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
                'PRINT($var)   // 25'
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
                'PRINT($var)\n'
                '$var = ARCSIN($var) // arcsin(0.5) = 30\n'
                'PRINT($var)'
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
                'PRINT($arr[0])\n'
                'PRINT($arr[1])\n'
                'PRINT($arr[2])'
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
                'PRINT(ARRPOP($arr))\n'
                'PRINT(ARRPOP($arr))\n'
                'PRINT(ARRPOP($arr))'
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
                'PRINT(ARRSIZE($arr))\n'
                'PRINT(ARRPOP($arr))\n'
                'PRINT(ARRSIZE($arr))'
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
                '   PRINT($arr[$a])\n'
                'END_CYC\n'
                '\n'
                '// сортировка\n'
                'ARRSORT($arr)\n'
                '\n'
                '// вывод результата\n'
                'PRINT("sort:")\n'
                'FOR($a=0, $a < 10)\n'
                '   PRINT($arr[$a])\n'
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
                'PRINT($var)\n'
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
                'PRINT($var)\n'
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
                'PRINT(STRLEN("lol") )\n'
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
                'PRINT(STRCUT("hello2000", 6, 2 ))\n'
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
                'PRINT(STRCUT2("hello2000", 2, 5 ))\n'
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
                'PRINT(STRFILTER("hello2000", "20", 0 ))\n'
                '// результат "hello"\n'
                'PRINT(STRFILTER("hello2000", "20", 1 ))\n'
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
                'PRINT($r)  // результат 13 (с 13 символа начинается подстрока)\n'
                '\n'
                '$var = "abcabc"\n'
                '$r = STRPOS($var, "a", 3)\n'
                'PRINT($r)  // результат 4, так как смещение на 3 пропускает первый символ "a"'
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
        example=('PRINT(STRCONCAT("hello", "2000", "!!!"))  // результат "hello2000!!!"'),
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
                'PRINT($s)  // результат "Hello, John!!!"'
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
        parameters=('str - строка '),
        example=('PRINT(STRMD5("123"))  // 202CB962AC59075B964B07152D234B70'),
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
                'PRINT($arr[1])  // "two"'
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
        parameters=('code - числовой код символа '),
        example=(
                '// генерация строки из случайных\n'
                '// символов a..z длинной 10\n'
                '$str = ""\n'
                'FOR($i=0, $i < 10)\n'
                '   $chr = CHAR(RND(97, 122))\n'
                '   $str = STRCONCAT($str, $chr)\n'
                'END_CYC\n'
                '\n'
                'PRINT($str)'
                ),
        notes='Обратите внимание, что используются коды из таблицы юникода. Не путать с ASCII. Таблица кодов доступна в интернете. Например, [здесь](http://unicode-table.com/ru/).',
        keywords='char, чар, вернуть символ по коду, узнать символ по коду, есть код нужен символ',
        version_cm_major=4,
        version_cm_minor=13,
        version_cm_build=14,
        version_cm_releaselevel='',
        ),
])

# Файлы
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
                'PRINT($str)\n'
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
        example=('PRINT(TFREAD("input.txt", 5))'),
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
                    'str_n - необязательный параметр; номер строки в файле '
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
                'TFREADARR("C:\out.txt", $arr)\n'
                'PRINT($arr[0])\n'
                'PRINT($arr[1])'
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
                    'delete - необязательный параметр; флаг удаления файла '
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
        example=('PRINT(TFCOUNT("input.txt"))'),
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
        example=('PRINT(STRREADLN("input.txt", 5)) // результат (пятая строка из этого файла)'),
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

# Мышь
DATA_ELEMENTS.extend([
    dict(name='lclick',
        name_isupper=1,
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=7,
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
        parent_id=8,
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
        parent_id=8,
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
        parent_id=8,
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
        parent_id=8,
        description=('Нажимает клавиши соответственно символам входной строки.'),
        syntax='KEYSTRING(string, [delay])',
        parameters=(
                'string - входная строка\n'
                'delay - необязательный параметр; задержка в милисекундах между каждым набором символа'
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
        parent_id=8,
        description=('Функция. Проверяет зажата ли указанная клавиша клавиатуры'),
        syntax='ISKEYDOWN(keycode)',
        parameters=('keycode - код клавиши'),
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
        notes='Возвращает 1 если в момент вызова функции зажата указанная клавиша и 0 - если нет.',
        keywords='iskeydown, искейдовн, проверка нажатия клавиши клавиатуры, проверка нажатия клавиши на клавиатуре, проверка зажатия клавиши клавиатуры, проверка зажатия клавиши на клавиатуре, реакция на клавишу, реакция на клавиатуру, нажата ли кнопка клавиатуры, нажата ли кнопка клавиатуры, проверить нажатую клавишу, проверить нажатую кнопку',
        version_cm_major=4,
        version_cm_minor=5,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='getkeysdown',
        name_isupper=1,
        parent_id=8,
        description=('Помещает список зажатых в момент вызова клавиш в массив.'),
        syntax='SETKBLAYOUT(hwnd, lang)',
        parameters=(
                    'hwnd - hwnd окна\n'
                    'lang - идентификатор языка ввода'
                    ),
        example=(
                '$hwnd = WNDFIND("Блокнот")\n'
                '// английский\n'
                'SETKBLAYOUT($hwnd, 1033)'
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
        parent_id=8,
        description=('Функция. Возвращает идентификатор языка ввода (раскладки) в конкретном окне.'),
        syntax='GETKBLAYOUT(hwnd)',
        parameters=('hwnd - hwnd окна'),
        example=(
                '// получаем hwnd запущеной программы\n'
                '$hwnd = WNDFIND("Блокнот")\n'
                '\n'
                '// выводим раскладку\n'
                'PRINT(GETKBLAYOUT($hwnd))'
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
        parent_id=8,
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
        parent_id=9,
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
        parent_id=9,
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
        parent_id=9,
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
        example=(''),
        notes='Так называемый переключатель используется когда нагромождение условий (IF) нецелесообразно и портит читаемость сценария. Переключатель анализирует входное значение var и в зависимости от него выполняет часть сценария, находящегося после блоке case с соответствующим значением. При этом, все параметры указанных инструкций могут быть представлены как числом, так и переменной. Необязательный блок DEFAULT выполняется в случае, когда ни один CASE не подошел под текущее значение переключателя.',
        keywords='switch end_switch, свич, свитч, замена кучи условий, много условий замена, замена кучи if, много if замена, несколько условий подряд',
        version_cm_major=4,
        version_cm_minor=9,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='for ... end_cyc',
        name_isupper=1,
        parent_id=9,
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
        parent_id=9,
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
        parent_id=9,
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
                '      PRINT("flood ", $i)\n'
                '   END_CYC\n'
                'END_SUB\n'
                '\n'
                '// вызов подпрограммы\n'
                'mysub()\n'
                '\n'
                '// ------------------------------------\n'
                '// пример 2. подпрограмма умножения двух случайных числел\n'
                'SUB(mult, $par1, $par2)\n'
                '   PRINT("par1: ", $par1)\n'
                '   PRINT("par2: ", $par2)\n'
                '   PRINT("par1 * par2 = ", $par1 * $par2)\n'
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
        parent_id=9,
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
        keywords='thread end_thread? треад, тхреад, потоки, описание потока, создание потока, описание потоков, создание потоков',
        version_cm_major=4,
        version_cm_minor=11,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='setthread',
        name_isupper=1,
        parent_id=9,
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
                '   PRINT("thr #1 tic-tak")\n'
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
                )',
        keywords='setthread, сэттреад, сеттреад, управление потоком, поставить поток на паузу, остановить поток, запустить поток, стартовать поток',
        version_cm_major=4,
        version_cm_minor=11,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
])


# DATA_ELEMENTS.extend([
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=7,
        # description=(''),
        # syntax='',
        # parameters=(''),
        # example=(''),
        # notes='',
        # keywords='',
        # version_cm_major=3,
        # version_cm_minor=2,
        # version_cm_build=0,
        # version_cm_releaselevel='',
        # ),
# ])


# fromclip
# toclip
# httpget


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



# v1.3 (11.04.2009)
# + Введена возможность "записи" сценария

# v2.1 (05.08.2009)
# + Улучшеный редактор и ядро:
  # + Кнопки быстрой вставки команды в редакторе
  # + Подсветка синтаксиса в редакторе
  # + Поддержка коментариев "//" (C++ Style)
  # + Добавлено озвучивание событий воспроизведения, записи и остановки
  # + Новая модная справка



    # DEFINE
    # UNDEFINE
    # INC
    # RND
    # RNDFROM
    # INT
    # DIST
    # SIN
    # COS
# ARCSIN
# ARCCOS
# SQRT
# POW
# ABS
# ROUND
# ARRPUSH
# ARRPOP
# ARRSIZE
# ARRSORT
# SETVAR
# GETVAR
