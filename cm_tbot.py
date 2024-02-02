#!/usr/bin/env python
# -*- coding: utf-8 -*-

from configs.config import CLICKERMANN_HELP_BOT_TOKEN, PARSE_MODE

from telebot import TeleBot


bot = TeleBot(CLICKERMANN_HELP_BOT_TOKEN, parse_mode=PARSE_MODE)  # None, HTML or MARKDOWN / MarkdownV2
