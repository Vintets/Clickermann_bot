#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from telebot import types
from cm_tbot import bot


def send_message(chat_id, text, **kwargs):
    bot.send_message(chat_id, text, **kwargs)
    time.sleep(0.9)


def reply_to(message: types.Message, text, **kwargs):
    bot.reply_to(message, text, **kwargs)
    time.sleep(1)


def indicator_chat_action(message: types.Message):
    """индикатор ввода текста"""

    bot.send_chat_action(message.chat.id, 'typing')


def answer_inline_query(query_id, inline_query_result):
    """Ответы инлайн режима"""

    bot.answer_inline_query(query_id, inline_query_result)
    time.sleep(0.9)
