#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker
from configs.config import DATABASE
from cm_db_models import Base, Partitions, Elements, Users, LogRequests, create_db
from sqlalchemy.exc import IntegrityError
from data_help.partitions import DATA_PARTITIONS
from data_help.elements import DATA_ELEMENTS


def filling_db(session):
    for partition in DATA_PARTITIONS:
        new_partition = Partitions(**partition)
        session.add(new_partition)

    for element in DATA_ELEMENTS:
        new_element = Elements(**element)
        session.add(new_element)
    
    try:
        session.commit()
    except IntegrityError:
        print('Дубль уникальных значений')

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
    print('Ok')


# --------------------------------------------------------------------------------------------------


