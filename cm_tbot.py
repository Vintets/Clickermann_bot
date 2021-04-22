#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telebot import TeleBot
from configs.config import CLICKERMANN_HELP_BOT_TOKEN, PARSE_MODE


bot = TeleBot(CLICKERMANN_HELP_BOT_TOKEN, parse_mode=PARSE_MODE)  # None, HTML or MARKDOWN / MarkdownV2
