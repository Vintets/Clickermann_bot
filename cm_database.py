#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from pathlib import Path
import sys

import accessory.authorship as auth_sh
import accessory.clear_console as cc
import accessory.colorprint as cp
from cm_db_models import CodeKeys, create_db_tables, Elements, LogRequests, Partitions, Users
from configs.config import DATABASE, ECHO_SQL
from data_help.code_keys import DATA_CODE_KEYS
from data_help.elements import DATA_ELEMENTS
from data_help.partitions import DATA_PARTITIONS
from sqlalchemy import and_, create_engine, func
# from sqlalchemy_utils import database_exists
from sqlalchemy.engine.url import URL
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker


class DB():
    engine = create_engine(URL(**DATABASE),
                           connect_args={'check_same_thread': False},
                           pool_recycle=3600, echo=ECHO_SQL)

    def __init__(self):
        self.session = self.create_session()

    def create_session(self):
        # Создаём фабрику _session_fab для создания экземпляров
        _session_fab = sessionmaker(bind=DB.engine)
        # Создаём объект сессии из вышесозданной фабрики _session_fab
        session = _session_fab()
        # session.expire_on_commit = False
        return session

    def close_session(self):
        self.session.close()

    def create_tables(self):
        create_db_tables(DB.engine)

    def filling_db(self):
        self.filling_db_partition()
        self.filling_db_element()
        self.filling_db_code_keys()

    def filling_db_partition(self):
        for partition in DATA_PARTITIONS:
            new_partition = Partitions(**partition)
            has_name = self.session.query(Partitions).filter(Partitions.name == partition['name'])
            if has_name.count() == 0:
                self.session.add(new_partition)
                cp.cprint(f"2Добавляем раздел '{partition['name']}'")

        try:
            self.session.commit()
        except IntegrityError:
            # self.session.rollback()
            cp.cprint('12Дубль уникальных значений разделов')

    def filling_db_element(self):
        for element in DATA_ELEMENTS:
            new_element = Elements(**element)
            has_name = self.session.query(Elements).filter(Elements.name == element['name'])
            if has_name.count() == 0:
                self.session.add(new_element)
                cp.cprint(f"2Добавляем элемент' '{element['name']}'")

        try:
            self.session.commit()
        except IntegrityError:
            # self.session.rollback()
            cp.cprint('12Дубль уникальных значений элементов')

    def filling_db_code_keys(self):
        for code_keys in DATA_CODE_KEYS:
            new_element = CodeKeys(**code_keys)
            has_name = self.session.query(CodeKeys).filter(CodeKeys.name == code_keys['name'])
            if has_name.count() == 0:
                self.session.add(new_element)
                cp.cprint(f"2Добавляем элемент' '{code_keys['name']}'")

        try:
            self.session.commit()
        except IntegrityError:
            # self.session.rollback()
            cp.cprint('12Дубль уникальных значений кодов клавиш')

    def create_and_filling(self):
        self.create_tables()
        self.filling_db()
        cp.cprint('2Database created Ok')

    def get_subpartitions(self, parent=0, visible=1):
        return self.session.query(Partitions).filter(
                            and_(Partitions.parent_id == parent, Partitions.visible == visible))

    def get_partition_by_name(self, name, visible=1):
        return self.session.query(Partitions).filter(
                            and_(func.lower(Partitions.name) == func.lower(name), Partitions.visible == visible))

    def get_elements_by_parent(self, parent=0, visible=1):
        return self.session.query(Elements).filter(
                            and_(Elements.parent_id == parent, Elements.visible == visible))

    def get_elements_by_name(self, name, visible=1):
        return self.session.query(Elements).filter(
                            and_(func.lower(Elements.name) == func.lower(name), Elements.visible == visible))

    def get_elements_by_keywords(self, keywords, visible=1):
        return self.session.query(Elements).filter(
                            and_(Elements.keywords.like(f'%{keywords}%'), Elements.visible == visible))

    def get_partition_by_id(self, id=0, visible=1):  # noqa: A002, VNE003
        return (self.session.query(Partitions).filter(
                            and_(Partitions.id == id, Partitions.visible == visible)))[0]

    def get_code_key_by_alias(self, alias):
        alias = f',{alias.lower()},'
        return self.session.query(CodeKeys).filter(CodeKeys.alias.like(f'%{alias}%'))

    def get_user_by_user_id(self, user_id):
        return self.session.query(Users).filter(Users.tm_user_id == user_id).first()

    def add_user(self, us):
        self.session.add(Users(**us))
        self.session.commit()

    def update_user(self, us):
        self.session.query(Users).filter(Users.tm_user_id == us['tm_user_id']).update(us, synchronize_session='fetch')
        self.session.commit()

    def request2log(self, request_):
        self.session.add(LogRequests(**request_))
        self.session.commit()

    def __del__(self):
        self.session.close()


db = DB()


if __name__ == '__main__':
    _width = 100
    _hight = 50
    if sys.platform == 'win32':
        os.system('color 71')
        # os.system('mode con cols=%d lines=%d' % (_width, _hight))
    os.chdir(Path(__file__).parent)
    cc.clear_console()

    __author__ = 'master by Vint'
    __title__ = '--- Clickermann_bot database ---'
    __version__ = '0.1.4'
    __copyright__ = 'Copyright 2020 (c)  bitbucket.org/Vintets'
    auth_sh.authorship(__author__, __title__, __version__, __copyright__, width=_width)

    db = DB()
    db.create_and_filling()
    db.close_session()


# --------------------------------------------------------------------------------------------------

# cp.cprint(f'12Неправильные данные в файле ^15_{filename}')
