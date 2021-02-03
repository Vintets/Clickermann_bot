#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def clearConsol():  # очищаем консоль
    if sys.platform == 'win32': os.system('cls')
    else:
        os.system('clear')

