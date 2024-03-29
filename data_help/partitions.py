#!/usr/bin/env python
# -*- coding: utf-8 -*-

DATA_PARTITIONS = (
    dict(name='Введение',
         # id=1,
         # parent_id=,
         description='Справка актуальна для версии 4.13.014',
         ),
    dict(name='Директивы препроцессора',
         # id=2,
         parent_id=1,
         description='Ряд команд, которые выполняются только в момент загрузки скрипта и в дальнейшем в работе не участвуют',
         ),
    dict(name='Служебные (системные) переменные',
         # id=3,
         parent_id=1,
         description='Имена этих переменных зарезервированы программой, а значения помещаются в них автоматически при обращении к ним. При этом присваивать этим переменным какие либо значения НЕЛЬЗЯ!, используйте их только для получения значений.',
         ),
    dict(name='Работа с числами',
         # id=4,
         # parent_id=,
         description='В этом разделе описаны процедуры и функции работы с числами, переменными и массивами.',
         ),
    dict(name='Строки',
         # id=5,
         # parent_id=,
         description='Строкой считается любой набор печатаемых символов. Строки-константы представляют собой набор символов в кавычках. Например, "это строка". Так же строкой считается результат возвращаемый текстовыми функциями.',
         ),
    dict(name='Текстовые файлы',
         # id=6,
         # parent_id=,
         description='Работа с текстовыми файлами. Запись, чтение, очистка и удаление данных. Работа с ini файлами',
         ),
    dict(name='Файлы и файловая система',
         # id=7,
         # parent_id=,
         description='Инструкции, предназначенные для работы с файлами и файловой системой.',
         ),
    dict(name='Мышь',
         # id=8,
         # parent_id=,
         description=('Процедуры и функции работы с мышью (программным указателем (курсором).\n'
                      'Почти все инструкции включают в себя два параметра - х и у. В них помешается курсор перед тем как совершить действие.)'
                      ),
         ),
    dict(name='Клавиатура',
         # id=9,
         # parent_id=,
         description=(
                      'Все, что вам необходимо знать - это то, что у каждой клавиши на клавиатуре есть свой числовой код. К примеру для пробела это 32. Эти коды перечислены в Приложении 1.\n'
                      'Стоит понимать, что под нажатием в данном случае понимается программное сообщение (виртуальное нажатие), поведение которого иногда может отличаться от реального нажатия клавиши на клавиатуре.'
                      ),
         ),
    dict(name='Условия, циклы, подпрограммы',
         # id=10,
         # parent_id=,
         description='Элементы, делающие программы более "умными", а сценарии более короткими и лаконичными.',
         ),
    dict(name='Анализ экрана',
         # id=11,
         # parent_id=,
         description=(
                    'В левом верхнем углу находится пиксель с координатами 0,0. Соответственно, если у вас разрешение экрана 800х600, то нижний правый пиксель будет иметь координаты 799х599.'
                    'Для гибкости и удобства кликер работает не с живым экраном, а с его снимком, помещенным в буфер анализа.'
                    ),
         ),
    dict(name='Вывод информации',
         # id=12,
         # parent_id=,
         description='Инструкции, предназначенные для сигнализирования пользователю. ',
         ),
    dict(name='Ввод информации',
         # id=13,
         # parent_id=,
         description='Инструкции, предназначенные для ввода данных в кликер или получение данных кликером из других источников.',
         ),
    dict(name='Управление скриптом, плагины',
         # id=14,
         # parent_id=,
         description='Инструкции для управления сценарием, плагинами и пр.',
         ),
    dict(name='Работа с окнами. WinAPI',
         # id=15,
         # parent_id=,
         description='Процедуры и функции, работающие с окнами Windows и их элементами. У каждого элемента есть свой уникальный идентификатор - hwnd, представленный числом. Зная его, можно обратиться к конкретному окну или его элементу.',
         ),
    dict(name='Приложение 1. Коды клавиш',
         # id=16,
         # parent_id=,
         description=(
                    'Bиртуальные коды клавиш стандартной 101-клавишной клавиатуры и их псевдонимы. Для использования в программе можете использовать десятичные значения кода либо псевдоним, заданный через константы.\n'
                    'Альтернативно, в боте, можно получить код клавиши через команду:\n'
                    '/code названиеКлавиши\n'
                    'примеры:\n'
                    '/code 5       - получить код 5\n'
                    '/code w       - получить код W\n'
                    '/code ctrl    - получить код Control\n'
                    '/code shift   - получить код Shift\n'
                    '/code left    - получить код стрелки влево\n'
                    '/code numpad3 - получить код 3 на цифровой клавиатуре\n'
                    ),
         ),
)


# --------------------------------------------------------------------------------------------------

"""
    dict(name='',
        # id=,
        # parent_id=,
        description='',
        ),
"""
