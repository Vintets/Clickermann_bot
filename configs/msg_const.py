#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs.formatting import frm


MSG_SERVER = f'Server {frm.b}started{frm.b}'

MSG_WELCOME = ('Привет, сейчас я расскажу тебе про Clickermann.\n'
            f'Для вывода меню разделов используй {frm.b}/cm_help{frm.b}')

MSG_HELP = ('Я могу ответить на следующие команды:\n'
            f'{frm.b}/cm_help{frm.b} - cправочник по процедурам и функциям Clickermann')

MSG_NOT_UNDERSTAND = ('Я тебя не понимаю\n'
                f'{frm.i}Я просто напомню,{frm.i} что есть {frm.c}команда{frm.c} /help\n'
                'для вывода списка доступных команд!')

MSG_HELLO = 'Привет {username}, я могу показать краткую справку по Clickermann'

MSG_CM_HELP_MAIN1 = 'Справочник по процедурам и функциям Clickermann'
MSG_CM_HELP_MAIN2 = 'Выберите раздел'

MSG_IN_THE_PIPELINE = 'Этот функционал в разработке'

MSG_CODE_PARAM = 'С этой командой трубуется передать параметр.\nНапример: /code shift'
MSG_FIND_PARAM = 'С этой командой трубуется передать параметр.\nНапример: /f остановить скрипт'
MSG_NOT_FIND = 'Ничего не найдено.\nПопробуйте изменить слова поиска'
