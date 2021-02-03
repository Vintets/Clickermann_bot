#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from configs.config import DATABASE
from cm_db_models import Base, Partitions, Elements, Users, LogRequests, create_db_tables
from sqlalchemy.exc import IntegrityError
from data_help.partitions import DATA_PARTITIONS
from data_help.elements import DATA_ELEMENTS
import accessory.colorprint as cp
import accessory.clear_consol as cc
import accessory.authorship as auth_sh


class DB():
    engine = create_engine(URL(**DATABASE), echo = True)
    def __init__(self):
        self.session = self.create_session()

    def create_session(self):
        # Создаём фабрику Session для создания экземпляров
        Session = sessionmaker(bind=DB.engine)
        # Создаём объект сессии из вышесозданной фабрики Session
        session = Session()
        return session

    def create_tables(self):
        create_db_tables(DB.engine)

    def filling_db(self):
        for partition in DATA_PARTITIONS:
            new_partition = Partitions(**partition)
            self.session.add(new_partition)

        for element in DATA_ELEMENTS:
            new_element = Elements(**element)
            self.session.add(new_element)

        try:
            self.session.commit()
        except IntegrityError:
            cp.cprint('12Дубль уникальных значений')

    def create_and_filling(self):
        self.create_tables()
        self.filling_db()
        cp.cprint('2Database created Ok')


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
    __title__ = '--- Clickermann_bot database ---'
    __version__ = '0.1.0'
    __copyright__ = 'Copyright 2020 (c)  bitbucket.org/Vintets'
    auth_sh.authorship(__author__, __title__, __version__, __copyright__, width=_width)

    db = DB()
    db.create_and_filling()


# --------------------------------------------------------------------------------------------------

# cp.cprint(f'12Неправильные данные в файле ^15_{filename}')

