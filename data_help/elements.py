#!/usr/bin/env python
# -*- coding: utf-8 -*-

DATA_ELEMENTS = (
    dict(
        header='математические операции',
        parent_id=1,
        description=(
                    'Операция                Приоритет Пример\n'
                    'Скобки приоритета "( )" 1         $var = (1 + 2) * 2\n'
                    'Умножение "*"           2         $var = 1 * 2\n'
                    'Деление "/"             2         $var = 1 / 2\n'
                    'Сложение "+"            3         $var = 1 + 2\n'
                    'Вычитание "-"           3         $var = 1 - 2\n'
                    ),
        keywords='математические операции, математика, скобки, умножение, деление, сложение, вычитание, скобка, плюс, минус, умножить, разделить',
        version_cm_major=3,
        version_cm_minor=2,
        version_cm_build=0,
        version_cm_releaselevel='beta',
    ),
)

