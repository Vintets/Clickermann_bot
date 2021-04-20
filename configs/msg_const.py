#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs.formatting import frm


MSG_SERVER_START = f'Server {frm.b}started{frm.b}'

MSG_SERVER_RESTART = f'Server {frm.b}REstart{frm.b}'

MSG_WELCOME = (
            'Привет, сейчас я расскажу тебе про Clickermann.\n'
            f'Для вывода меню разделов используй {frm.b}/cm_help{frm.b}\n'
            f'Просмотреть все возможные команды можно в {frm.b}/help{frm.b}\n'
            f'{frm.b}Бот находится в стадии тестирования.{frm.b}\n'
            f'{frm.b}Возможны проблемы в работе.{frm.b}'
            )

MSG_HELP = (
            'Я могу ответить на следующие команды:\n'
            # f'{frm.b}/cm_help{frm.b} - cправочник по процедурам и функциям Clickermann\n'
            f'{frm.b}/cm_help{frm.b}  - меню разделов справки Clickermann\n'
            f'{frm.b}/code [клавиша]{frm.b}    - получить код клавиши\n'
            f'{frm.b}/f [искомая фраза]{frm.b} - поиск по ключевым словам\n'
            f'{frm.b}/start{frm.b}   - вернуться в главное меню\n'
            f'{frm.b}/help{frm.b}    - помощь по командам\n'
            f'{frm.b}/info{frm.b}     - info'
            )

MSG_INFO = (
            'Бот создан для быстрого доступа к справке Clickermann не выходя из Телеграм.\n'
            'Удобно быстро подсмотреть правильное название команд для общения в группах.\n'
            'И главное - справка! Может хоть так будут к ней обращаться ))\n'
            '\n'
            'Creator - @Vint\_CM\n'
            'Пожелания и комментарии по работе бота отправлять на\n'
            'cm\_bot@vintets.ru'
            )

MSG_NOT_UNDERSTAND = ('Я тебя не понимаю\n'
                f'{frm.i}Я просто напомню,{frm.i} что есть {frm.c}команда{frm.c} /help\n'
                'для вывода списка доступных команд!')

MSG_HELLO = 'Привет {username}, я могу показать краткую справку по Clickermann'

MSG_CM_HELP_MAIN1 = 'Справочник по процедурам и функциям Clickermann'
MSG_CM_HELP_MAIN2 = 'Выберите раздел'

MSG_IN_THE_PIPELINE = 'Этот функционал в разработке'

MSG_CODE_PARAM = 'С этой командой трубуется передать параметр.\nНапример: /code shift'
MSG_FIND_PARAM = ('С этой командой трубуется передать параметр.\n'
                'Например:\n'
                f'/f {frm.i}остановить скрипт{frm.i}')
MSG_NOT_FIND = (f'{frm.b}Ничего не найдено!{frm.b}\n'
                'Попробуйте изменить слова поиска')

MSG_KEYS_NOT_FIND = (f'{frm.b}Код указанной клавиши не найден!{frm.b}\n'
                'Попробуйте изменить название')

