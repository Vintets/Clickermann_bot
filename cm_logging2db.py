#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telebot import types
from cm_database import db
from cm_sender import send_message
from configs.formatting import frm
from configs.config import IDADMIN
from accessory.safe_markdown import safe_markdown_symbol


def logging_user(handler):
    """Логирование запросов пользователей"""

    def wrapper_logging_user(message: types.Message):
        adding_or_updating_user_information_in_db(message)
        user = db.get_user_by_user_id(message.from_user.id)
        # username = str(message.from_user.first_name)
        request_ = dict(
                        user_id=user.id,
                        request=message.text,
                        )
        db.request2log(request_)
        handler(message)
    return wrapper_logging_user


def logging_user_single(message: types.Message, text: str):
    """Логирование нажатий на InlineKeyboard кнопки пользователями"""

    adding_or_updating_user_information_in_db(message)
    user = db.get_user_by_user_id(message.chat.id)  # так надо (chat.id) чтобы логирование по кнопке назад приписывалось юзеру, а не боту
    # username = str(message.from_user.first_name)
    request_ = dict(
                    user_id=user.id,
                    request=text,
                    )
    db.request2log(request_)


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

        # Оповещение Админу
        msg_to_admin = (
                        f'{frm.b}Clickermann_bot оповещение!{frm.b}\n'
                        f'Добавлен новый пользователь:\n' + safe_markdown_symbol(
                                    f"id         = {us['tm_user_id']}\n"
                                    f"username   = {us['username']}\n"
                                    f"first_name = {us['first_name']}\n"
                                    f"last_name  = {us['last_name']}"
                                    )
                        )
        send_message(IDADMIN, msg_to_admin)
    elif (
            user.username != us['username'] or
            user.first_name != us['first_name'] or
            user.last_name != us['last_name']
            ):
        db.update_user(us)
        print('Update user:', user)
        # запишем в лог что данные пользователя изменились
        msg = (
                f"Пользователь {user.tm_user_id} сменил данные на "
                f"username  = {us['username']}, "
                f"first_name= {us['first_name']}, "
                f"last_name = {us['last_name']}"
                )
        request_ = dict(
                        user_id=user.id,
                        request=msg,
                        )
        db.request2log(request_)
        send_message(IDADMIN, f'{frm.b}тестовое _сообщение{frm.b}')

        # Оповещение Админу
        msg_to_admin = (
                        f'{frm.b}Clickermann_bot оповещение!{frm.b}\n'
                        f'Пользователь {user.tm_user_id} сменил данные на\n' + safe_markdown_symbol(
                                    f"username={us['username']}\n"
                                    f"first_name={us['first_name']}\n"
                                    f"last_name={us['last_name']}"
                                    )
                        )
        send_message(IDADMIN, msg_to_admin)
