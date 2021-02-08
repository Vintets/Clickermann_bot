#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import telebot
from telebot import types
from configs.config import CLICKERMANN_BOT_TOKEN
from cm_database import DB
import accessory.colorprint as cp
import accessory.clear_consol as cc
import accessory.authorship as auth_sh
import configs.msg_const as msg_const


bot = telebot.TeleBot(CLICKERMANN_BOT_TOKEN, parse_mode='HTML')  # None, HTML or MARKDOWN
db = DB()

@bot.message_handler(commands=['start'])
def process_start_command(message: types.Message):
    bot.send_message(message.from_user.id, msg_const.MSG_WELCOME)

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
        bot.reply(message.from_user.id, msg_const.MSG_NOT_UNDERSTAND)

def cm_help_inline(message: types.Message):
    # Готовим кнопки
    keyboard_main = types.InlineKeyboardMarkup()
    key_numbers = types.InlineKeyboardButton(text='Работа с числами', callback_data='numbers')
    key_strings = types.InlineKeyboardButton(text='Строки и файлы', callback_data='strings')
    keyboard_main.add(key_numbers, key_strings)

    bot.send_message(message.from_user.id, msg_const.MSG_CM_HELP_MAIN1)
    bot.send_message(message.from_user.id, text=msg_const.MSG_CM_HELP_MAIN2, reply_markup=keyboard_main)

def cm_help(message: types.Message):
    bot.send_message(message.from_user.id, msg_const.MSG_CM_HELP_MAIN1)

    keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
    for partition in core_partitions:
        key = types.KeyboardButton(partition.name)
        keyboard_main.add(key)

    # Показываем все кнопки сразу и пишем сообщение о выборе
    bot.send_message(message.from_user.id, text=msg_const.MSG_CM_HELP_MAIN2, reply_markup=keyboard_main)

    # Убрать клавиатуру принудительно
    # menu_remove = types.ReplyKeyboardRemove()
    # bot.send_message(message.from_user.id, text='...', reply_markup=menu_remove)
    pass


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'numbers':
        msg = 'В этом разделе описаны процедуры и функции работы с числами, переменными и массивами'
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)
    elif call.data == 'strings':
        msg = 'Работа со строками'
        bot.send_message(call.message.chat.id, msg)


# @bot.message_handler(func=lambda commands: True)
# def unknown_command(message: types.Message):
    # bot.send_message(message.from_user.id, msg_const.MSG_NOT_UNDERSTAND)

@bot.message_handler(func=lambda commands: True)
def unknown_message(message: types.Message):
    bot.reply(message.from_user.id, msg_const.MSG_NOT_UNDERSTAND)

def server_started():
    bot.send_message('829838425', msg_const.MSG_SERVER)
    cp.cprint('9Clickermann_bot запущен!')


if __name__ == '__main__':
    _width = 100
    _hight = 50
    if sys.platform == 'win32':
        os.system('color 71')
        os.system('mode con cols=%d lines=%d' % (_width, _hight))
    cur_script = __file__
    PATH_SCRIPT = os.path.abspath(os.path.dirname(cur_script))
    os.chdir(PATH_SCRIPT)
    cc.clearConsol()

    __author__ = 'master by Vint'
    __title__ = '--- Clickermann_bot ---'
    __version__ = '0.1.0'
    __copyright__ = 'Copyright 2020 (c)  bitbucket.org/Vintets'
    auth_sh.authorship(__author__, __title__, __version__, __copyright__, width=_width)

    server_started()
    
    bot.polling(none_stop=True, interval=1)



# Send Markdown or HTML, if you want Telegram apps to show
# bold, italic, fixed-width text or inline URLs in the media caption

