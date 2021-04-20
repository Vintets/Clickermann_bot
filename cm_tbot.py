#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telebot import TeleBot
from configs.config import CLICKERMANN_HELP_BOT_TOKEN


bot = TeleBot(CLICKERMANN_HELP_BOT_TOKEN, parse_mode='MARKDOWN')  # None, HTML or MARKDOWN / MarkdownV2
