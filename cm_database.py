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
    main()
    print('Ok')


# --------------------------------------------------------------------------------------------------

# cp.cprint(f'12Неправильные данные в файле ^15_{filename}')

