#!/usr/bin/env python
# -*- coding: utf-8 -*-

DATA_ELEMENTS = (
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
        version_cm_major=3,
        version_cm_minor=2,
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
        version_cm_major=3,
        version_cm_minor=2,
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
        version_cm_major=3,
        version_cm_minor=2,
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
        version_cm_major=3,
        version_cm_minor=2,
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
        version_cm_major=3,
        version_cm_minor=2,
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
        version_cm_major=3,
        version_cm_minor=2,
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
        version_cm_major=3,
        version_cm_minor=2,
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
        version_cm_major=3,
        version_cm_minor=2,
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
        version_cm_major=3,
        version_cm_minor=2,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    dict(name='char',
        name_isupper=1,
        parent_id=5,
        description=('Функция. Возвращает символ по его коду.'),
        syntax='CHAR(code)',
        parameters=('code - числовой код символа '),
        example=(''),
        notes='Обратите внимание, что используются коды из таблицы юникода. Не путать с ASCII. Таблица кодов доступна в интернете. Например, [здесь](http://unicode-table.com/ru/).',
        keywords='',
        version_cm_major=3,
        version_cm_minor=2,
        version_cm_build=0,
        version_cm_releaselevel='',
        ),
    # dict(name='',
        # name_isupper=1,
        # parent_id=5,
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
        # parent_id=5,
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
        # parent_id=5,
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
)


# iniread
# iniwrite
# tfread
# tfwrite
# tfreadarr
# tfwritearr
# tfdelete
# tfclear
# tfcount
# strreadln
# strwriteln

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
