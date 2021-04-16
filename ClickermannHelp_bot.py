#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
from itertools import chain
from telebot import TeleBot, types
from configs.config import CLICKERMANN_HELP_BOT_TOKEN
from cm_database import DB
import accessory.colorprint as cp
import accessory.clear_consol as cc
import accessory.authorship as auth_sh
import configs.msg_const as msg_const
from configs.formatting import frm


__version__ = '0.1.13'
bot = TeleBot(CLICKERMANN_HELP_BOT_TOKEN, parse_mode='MARKDOWN')  # None, HTML or MARKDOWN / MarkdownV2
db = DB()

def send_message(chat_id, text, **kwargs):
    bot.send_message(chat_id, text, **kwargs)
    time.sleep(0.9)

def reply_to(message: types.Message, text, **kwargs):
    bot.reply_to(message, text, **kwargs)
    time.sleep(1)

def indicator_chat_action(message: types.Message):
    """индикатор ввода текста"""

    bot.send_chat_action(message.chat.id, 'typing')

def keyboard_main_comands():
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
        main_comands = ('/start', '/help', '/info', '/cm_help')
        for command in main_comands:
            key = types.KeyboardButton(command)
            keyboard.add(key)
        return keyboard

def logger_user_single(message: types.Message, text: str):
    """Логирование нажатий на InlineKeyboard кнопки пользователями"""

    adding_or_updating_user_information_in_db(message)
    user = db.get_user_by_user_id(message.chat.id) # так надо (chat.id) чтобы логирование по кнопке назад приписывалось юзеру, а не боту
    username = str(message.from_user.first_name)
    request_ = dict(
                    user_id=user.id,
                    request=text,
                    )
    db.request2log(request_)

def logger_user(handler):
    """Логирование запросов пользователей"""

    def wrapper_logger_user(message: types.Message):
        adding_or_updating_user_information_in_db(message)
        user = db.get_user_by_user_id(message.from_user.id)
        username = str(message.from_user.first_name)
        request_ = dict(
                        user_id=user.id,
                        request=message.text,
                        )
        db.request2log(request_)
        handler(message)
    return wrapper_logger_user

def safe_underscore(item, italic=False):
    """Экранирование разметочных символов MARKDOWN"""

    if italic and item.find('_') != -1:
        item = item.replace('_', '_\__')
    elif item.find('_') != -1:
        item = item.replace('_', '\_')
    if italic and item.find('#') != -1:
        # item = item.replace('#', '_\#_')
        pass
    elif item.find('#') != -1:
        item = item.replace('#', '\#')
    if item.find('*') != -1:
        item = item.replace('*', '\*')
    return item

@bot.message_handler(commands=['start', 'Start', 'START'])
@logger_user
def process_start_command(message: types.Message):
    menu_remove = types.ReplyKeyboardRemove()
    send_message(message.chat.id, msg_const.MSG_WELCOME, reply_markup=menu_remove)

@bot.message_handler(commands=['help', 'Help', 'HELP'])
@logger_user
def process_help_command(message: types.Message):
    send_message(message.chat.id, msg_const.MSG_HELP)

@bot.message_handler(commands=['code'])
@logger_user
def process_character_code_command(message: types.Message):
    """Get character code.
    example: /code shift"""

    text = message.text[6:]
    menu_remove = types.ReplyKeyboardRemove()
    if text:
        cp.cprint(f"14_{message.chat.id} /code '{text}'")
        # TODO
        ...
    else:
        send_message(message.chat.id, msg_const.MSG_CODE_PARAM, reply_markup=menu_remove)
    reply_to(message, msg_const.MSG_IN_THE_PIPELINE)

@bot.message_handler(commands=['f'])
@logger_user
def process_search_command(message: types.Message):
    """keyword search processing"""

    # send_message(message.chat.id, message.text[3:])
    # reply_to(message, msg_const.MSG_IN_THE_PIPELINE, reply_markup=types.ReplyKeyboardRemove())

    text = message.text[3:]
    menu_remove = types.ReplyKeyboardRemove()
    if text:
        # ищем элементы по ключевым словам, выводим как список
        if not is_search_elements(message.chat.id, text):
            reply_to(message, msg_const.MSG_NOT_FIND, reply_markup=menu_remove)
    else:
        reply_to(message, msg_const.MSG_FIND_PARAM, reply_markup=menu_remove)

@bot.message_handler(content_types=['sticker'])
def get_sticker_id(message: types.Message):
    print(message)

@bot.message_handler(commands=['cm_help'])
@logger_user
def process_cm_help_command(message: types.Message):
    cm_help(message)

@bot.message_handler(content_types=['text'])
@logger_user
def get_text_messages(message: types.Message):
    if message.text.lower() in ('привет', 'hello'):
        send_message(message.chat.id, msg_const.MSG_HELLO.format(username=str(message.from_user.first_name)))
    else:
        text_ok = processing_text_types(message)
        if not text_ok:
            reply_to(message, msg_const.MSG_NOT_UNDERSTAND)

def cm_help_inline(message: types.Message):
    '''Вариант меню с кнопками Inline'''

    # Готовим кнопки
    keyboard_main = types.InlineKeyboardMarkup()
    key_numbers = types.InlineKeyboardButton(text='Работа с числами', callback_data='numbers')
    key_strings = types.InlineKeyboardButton(text='Строки и файлы', callback_data='strings')
    keyboard_main.add(key_numbers, key_strings)

    msg = f'{msg_const.MSG_CM_HELP_MAIN1}\n{msg_const.MSG_CM_HELP_MAIN2}'
    send_message(message.chat.id, text=msg, reply_markup=keyboard_main)

def cm_help(message: types.Message):
    """main handler section cm_help"""

    keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=2)
    core_partitions = db.get_subpartitions(parent=0)
    for partition in core_partitions:
        # print(partition)
        key = types.KeyboardButton(partition.name)
        keyboard_main.add(key)

    # Показываем все кнопки сразу и пишем сообщение о выборе
    msg = f'{msg_const.MSG_CM_HELP_MAIN1}\n{msg_const.MSG_CM_HELP_MAIN2}'
    send_message(message.chat.id, text=msg, reply_markup=keyboard_main)

def processing_text_types(message: types.Message):
    """handler text messages"""

    text_ok = False
    text = message.text
    if text.lower() == '<-- вернуться в корень меню':
        cm_help(message)    # в ручную имитируем команду /cm_help и
        return True         # принудительно завершаем эту ветку
    if text[:16].lower() == '<-- вернуться в ':
        text = text[16:]

    # ищем подразделы и подэлементы, выводим как список
    if is_partition_processing(message.chat.id, text):
        text_ok = True

    # если дочерних нет, то выводим как элемент
    if not text_ok:
        if is_element_processing(message.chat.id, text):
            text_ok = True
    return text_ok

def is_partition_processing(chat_id, text):
    """output partition"""

    happily = False
    find_partitions = db.get_partition_by_name(text)
    if find_partitions.count() == 1:
        happily = True
        find_partition = find_partitions[0]
        cp.cprint(f'14_{chat_id} find_partition {find_partition}')
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)

        # ищем подразделы
        output_childrens = db.get_subpartitions(parent=find_partition.id)
        # ищем все дочерние элементы
        output_childrens_el = db.get_elements_by_parent(parent=find_partition.id)
        for children in chain(output_childrens, output_childrens_el):
            # print(children)
            child_name = children.name
            try:
                isupper = getattr(children, 'name_isupper')
            except AttributeError:
                isupper = 0
            if isupper:
                child_name = child_name.upper()
            key = types.KeyboardButton(child_name)
            keyboard.add(key)

        # добавляем пункт/кнопку назад
        if find_partition.id != 0:
            if find_partition.parent_id == 0:
                parent_name = f'корень меню'
            else:
                parent_name = db.get_partition_by_id(id=find_partition.parent_id).name
            # print(f'parent:  id={find_partition.parent_id},  name={parent_name}')
            keyboard.add(f'<-- Вернуться в {parent_name}')

        # отправляем имя и описание раздела
        send_message(chat_id, f'{frm.b}{find_partition.name}{frm.b}\n{find_partition.description}',
                        reply_markup=keyboard)
    return happily

def is_element_processing(chat_id, text):
    """output element"""

    happily = False
    find_element = db.get_elements_by_name(text)
    if find_element.count() == 1:
        happily = True
        current_element = find_element[0]
        output = template_engine_element(current_element)
        # print(output)
        keyboard = types.InlineKeyboardMarkup()
        key_return = types.InlineKeyboardButton(
                                        text='Вернуться назад',
                                        callback_data=f'return_partition:{current_element.parent_id}')
        keyboard.add(key_return)
        send_message(chat_id, output, reply_markup=keyboard)
    return happily

def is_search_elements(chat_id, text):
    """search elements by keywords"""

    # test /f остановить скрипт
    happily = False
    found_elements = db.get_elements_by_keywords(keywords=text.lower())
    if found_elements.count() > 0:
        happily = True
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=1)
        for children_el in found_elements:
            cp.cprint(f'14_найдено: {children_el}')
            child_name = children_el.name
            try:
                isupper = getattr(children_el, 'name_isupper')
            except AttributeError:
                isupper = 0
            if isupper:
                child_name = child_name.upper()
            key = types.KeyboardButton(child_name)
            keyboard.add(key)

        # добавляем пункт/кнопку 'в корень меню'
        keyboard.add(f'<-- вернуться в корень меню')

        # отправляем имя и описание раздела
        send_message(chat_id, f"Поиск по ключевой фразе\n'{text}'",
                        reply_markup=keyboard)
    return happily

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    '''InlineKeyboard click handler'''

    if call.data.startswith('return_partition'):
        parent_id = int(call.data[17:])
        parent_name = db.get_partition_by_id(id=parent_id).name
        # print(f'parent:  id = {parent_id},  name={parent_name}')
        logger_user_single(call.message, parent_name)
        is_partition_processing(call.message.chat.id, parent_name)

def template_engine_element(el):
    """template engine for elements"""

    name = el.name
    if el.name_isupper:
        name = name.upper()
        name = safe_underscore(name)
    text = [f'{frm.b}{name}{frm.b}']
    if el.description:
        text.append(safe_underscore(el.description))
        # print(safe_underscore(el.description))
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
        text.append(f'{frm.i}{safe_underscore(el.notes, italic=True)}{frm.i}')
        text.append('')

    text.append(assembly_version(el))
    return '\n'.join(text)

def assembly_version(el):
    """template engine for version Clickermann"""

    version = 'с версии Clickermann {major}.{minor}.{build:0>3}'.format(
                        major=el.version_cm_major,
                        minor=el.version_cm_minor,
                        build=el.version_cm_build
                        )
    if el.version_cm_releaselevel:
        version += f' {el.version_cm_releaselevel}'
    return version

# @bot.message_handler(func=lambda commands: True)
# def unknown_command(message: types.Message):
    # send_message(message.chat.id, msg_const.MSG_NOT_UNDERSTAND)

@bot.message_handler(func=lambda commands: True)
def unknown_message(message: types.Message):
    """If the message is not recognized"""

    reply_to(message, msg_const.MSG_NOT_UNDERSTAND)

def sending_messages_at_server_start():
    """Sending messages at server start"""

    # ToDo sendin messages  <=30 requests per second
    menu_remove = types.ReplyKeyboardRemove()
    bot.send_message('829838425', msg_const.MSG_SERVER, disable_notification=True, reply_markup=menu_remove)
    time.sleep(0.04)
    time.sleep(1)

def adding_or_updating_user_information_in_db(message: types.Message):
    user = db.get_user_by_user_id(message.from_user.id)
    us = dict(
        tm_user_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        )
    if user is None:
        db.add_user(us)
        print(f"Add user: id={us['tm_user_id']}, username={us['username']}, first_name={us['first_name']}")
    elif (
            user.username != us['username'] or
            user.first_name != us['first_name'] or
            user.last_name != us['last_name']
            ):
        db.update_user(us)
        print('Update user:', user)
        # запишем в лог что данные пользователя изменились
        msg = (
                f"Пользователь N сменил данные на "
                f"username={us['username']}, "
                f"first_name={us['first_name']}, "
                f"last_name={us['last_name']}"
                )
        request_ = dict(
                        user_id=user.id,
                        request=msg,
                        )
        db.request2log(request_)

def main():
    sending_messages_at_server_start()
    bot.polling(none_stop=True, interval=2)


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
    __copyright__ = 'Copyright 2020 (c)  bitbucket.org/Vintets'
    auth_sh.authorship(__author__, __title__, __version__, __copyright__, width=_width)

    cp.cprint('9Clickermann_bot запущен!')

    while True:
        try:
            main()
        except KeyboardInterrupt:
            cp.cprint('13Работа бота остановлена')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
        except Exception as ex:
            print(time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())), ex)
            cp.cprint('13Перезапуск бота…')
            raise(ex)
        break



# --------------------------------------------------------------------------------------------------


# Убрать клавиатуру принудительно
# menu_remove = types.ReplyKeyboardRemove()
# bot.send_message(message.chat.id, text='...', reply_markup=menu_remove, disable_notification=True)

# disable_notification=True   # беззвучно
