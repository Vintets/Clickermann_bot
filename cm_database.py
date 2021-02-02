#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy import Table, Column, Integer, String, Text, DateTime, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.orm import sessionmaker
from configs.config import DATABASE
from cm_db_models import Base, Partitions, Elements, Users, LogRequests, create_db


# Base = declarative_base()


def filling_db(session):
    new_partition = Partitions(name='Введение')
    session.add(new_partition)
    new_element = Elements(
                    header='математические операции',
                    parent_id=1,
                    description=(
                                'Операция                Приоритет Пример\n'
                                'Скобки приоритета "( )" 1         $var = (1 + 2) * 2\n'
                                'Умножение "*"           2         $var = 1 * 2\n'
                                'Деление "/"             2         $var = 1 / 2\n'
                                'Сложение "+"            3         $var = 1 + 2\n'
                                'Вычитание "-"           3         $var = 1 - 2\n'
                                ),
                    keywords='математические операции, математика, скобки, умножение, деление, сложение, вычитание, скобка, плюс, минус, умножить, разделить',
                    version_cm_major=3,
                    version_cm_minor=2,
                    version_cm_build=0,
                    version_cm_releaselevel='beta',
                    )
    session.add(new_element)
    session.commit()


def main():
    engine  = create_engine(URL(**DATABASE), echo = True)

    # создает таблицы в БД
    create_db(engine)

    # Создаем фабрику Session для создания экземпляров
    Session = sessionmaker(bind=engine)
    # Создаем объект сессии из вышесозданной фабрики Session
    session = Session()

    filling_db(session)


if __name__ == '__main__':
    main()


# --------------------------------------------------------------------------------------------------


