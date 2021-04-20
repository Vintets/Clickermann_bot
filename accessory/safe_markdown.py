#!/usr/bin/env python
# -*- coding: utf-8 -*-

def safe_markdown_symbol(item: str, italic=False) -> str:
    """Экранирование разметочных символов MARKDOWN"""

    if italic and item.find('_') != -1:
        item = item.replace('_', r'_\__')
    elif item.find('_') != -1:
        item = item.replace('_', r'\_')
    if italic and item.find('#') != -1:
        # item = item.replace('#', '_\#_')
        pass
    elif item.find('#') != -1:
        item = item.replace('#', r'\#')
    if item.find('*') != -1:
        item = item.replace('*', r'\*')
    return item
