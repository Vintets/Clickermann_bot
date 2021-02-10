#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from itertools import chain
import telebot
from telebot import types
from configs.config import CLICKERMANN_HELP_BOT_TOKEN
from cm_database import DB
import accessory.colorprint as cp
import accessory.clear_consol as cc
import accessory.authorship as auth_sh
import configs.msg_const as msg_const
from configs.formatting import frm


bot = telebot.TeleBot(CLICKERMANN_HELP_BOT_TOKEN, parse_mode='MARKDOWN')  # None, HTML or MARKDOWN
db = DB()

@bot.message_handler(commands=['start'])
def process_start_command(message: types.Message):
    menu_remove = types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, msg_const.MSG_WELCOME, reply_markup=menu_remove)

@bot.message_handler(commands=['help'])
def process_help_command(message: types.Message):
    bot.send_message(message.from_user.id, msg_const.MSG_HELP)

@bot.message_handler(content_types=['sticker'])
def get_sticker_id(message: types.Message):
    print(message)

@bot.message_handler(commands=['cm_help'])
def process_cm_help_command(message: types.Message):
    cm_help(message)

@bot.message_handler(content_types=['text'])
def get_text_messages(message: types.Message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, msg_const.MSG_HELLO.format(username=str(message.from_user.first_name)))
    text_ok = processing_text_types(message)
    if not text_ok:
        bot.reply_to(message, msg_const.MSG_NOT_UNDERSTAND)

def cm_help_inline(message: types.Message):
    '''Вариант меню с кнопками Inline'''

    # Готовим кнопки
    keyboard_main = types.InlineKeyboardMarkup()
    key_numbers = types.InlineKeyboardButton(text='Работа с числами', callback_data='numbers')
    key_strings = types.InlineKeyboardButton(text='Строки и файлы', callback_data='strings')
    keyboard_main.add(key_numbers, key_strings)

    bot.send_message(message.from_user.id, msg_const.MSG_CM_HELP_MAIN1)
    bot.send_message(message.from_user.id, text=msg_const.MSG_CM_HELP_MAIN2, reply_markup=keyboard_main)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    '''Обработчик нажатий на кнопки'''

    if call.data == 'numbers':
        msg = 'В этом разделе описаны процедуры и функции работы с числами, переменными и массивами'
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'strings':
        msg = 'Работа со строками'
        bot.send_message(call.message.chat.id, msg)

def cm_help(message: types.Message):
    bot.send_message(message.from_user.id, msg_const.MSG_CM_HELP_MAIN1)

    keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
    core_partitions = db.get_subpartitions(parent=0)
    for partition in core_partitions:
        print(partition)
        key = types.KeyboardButton(partition.name)
        keyboard_main.add(key)

    # Показываем все кнопки сразу и пишем сообщение о выборе
    bot.send_message(message.from_user.id, text=msg_const.MSG_CM_HELP_MAIN2, reply_markup=keyboard_main)

def processing_text_types(message: types.Message):
    text_ok = False
    text = message.text.lower()
    if is_partition_processing(message.from_user.id, text):
        text_ok = True
    if not text_ok:
        if is_element_processing(message.from_user.id, text):
            text_ok = True
    return text_ok

def is_partition_processing(chat_id, text):
    happily = False
    find_partitions = db.get_partition_by_name(text.capitalize())
    if find_partitions.count() == 1:
        happily = True
        find_partition = find_partitions[0]
        cp.cprint(f'14find_partition {find_partition}')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)

        # ищем подразделы
        output_childrens = db.get_subpartitions(parent=find_partition.id)
        # ищем все дочерние элементы
        output_childrens_el = db.get_elements_by_parent(parent=find_partition.id)
        for children in chain(output_childrens, output_childrens_el):
            key = types.KeyboardButton(children.name)
            keyboard.add(key)

        # отправляем имя и описание раздела
        bot.send_message(user_id, f'{frm.b}{find_partition.name}{frm.b}\n{find_partition.description}',
                        reply_markup=keyboard)
    return happily

def is_element_processing(chat_id, text):
    happily = False
    find_element = db.get_elements_by_name(text)
    if find_element.count() == 1:
        happily = True
        output = template_engine_element(find_element[0])
        print(output)
        bot.send_message(chat_id, output)
    return happily

def template_engine_element(el):
    name = el.name
    if el.name_isupper:
        name = name.upper()
    text = [f'{frm.b}{name}{frm.b}']
    if el.description:
        text.append(el.description)
        text.append('')
    if el.syntax:
        text.append(f'{frm.b}Синтаксис{frm.b}')
        text.append(f'{frm.c}{el.syntax}{frm.c}')
        text.append('')
    if el.parameters:
        text.append(f'{frm.b}Параметры{frm.b}')
        text.append(f'{frm.c}{el.parameters}{frm.c}')
        text.append('')
    if el.example:
        text.append(f'{frm.b}Пример{frm.b}')
        text.append(f'{frm.c}{el.example}{frm.c}')
        text.append('')
    if el.notes:
        text.append(f'{frm.b}Примечания{frm.b}')
        text.append(f'{frm.i}{el.notes}{frm.i}')
        text.append('')

    text.append(assembly_version(el))
    return '\n'.join(text)

def assembly_version(el):
    version = '{major}.{minor}.{build:0>3}'.format(
                        major=el.version_cm_major,
                        minor=el.version_cm_minor,
                        build=el.version_cm_build
                        )
    if el.version_cm_releaselevel:
        version += f' {el.version_cm_releaselevel}'
    return version

# @bot.message_handler(func=lambda commands: True)
# def unknown_command(message: types.Message):
    # bot.send_message(message.from_user.id, msg_const.MSG_NOT_UNDERSTAND)

@bot.message_handler(func=lambda commands: True)
def unknown_message(message: types.Message):
    bot.reply_to(message, msg_const.MSG_NOT_UNDERSTAND)

def server_started():
    menu_remove = types.ReplyKeyboardRemove()
    bot.send_message('829838425', msg_const.MSG_SERVER, reply_markup=menu_remove)
    cp.cprint('9Clickermann_bot запущен!')


if __name__ == '__main__':
    _width = 100
    _hight = 50
    if sys.platform == 'win32':
        os.system('color 71')
        # os.system('mode con cols=%d lines=%d' % (_width, _hight))
    cur_script = __file__
    PATH_SCRIPT = os.path.abspath(os.path.dirname(cur_script))
    os.chdir(PATH_SCRIPT)
    cc.clearConsol()

    __author__ = 'master by Vint'
    __title__ = '--- Clickermann_bot ---'
    __version__ = '0.1.2'
    __copyright__ = 'Copyright 2020 (c)  bitbucket.org/Vintets'
    auth_sh.authorship(__author__, __title__, __version__, __copyright__, width=_width)

    server_started()
    
    bot.polling(none_stop=True, interval=1)



# --------------------------------------------------------------------------------------------------

# Send Markdown or HTML, if you want Telegram apps to show
# bold, italic, fixed-width text or inline URLs in the media caption


# Убрать клавиатуру принудительно
# menu_remove = types.ReplyKeyboardRemove()
# bot.send_message(message.from_user.id, text='...', reply_markup=menu_remove)

