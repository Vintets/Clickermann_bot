#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from sqlalchemy import create_engine, MetaData
from sqlalchemy.engine.url import URL
from sqlalchemy import Table, Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.functions import current_timestamp
# from sqlalchemy.dialects.mysql import INTEGER, DATETIME
# from sqlalchemy.dialects.mysql import MEDIUMTEXT
# UnsignedInt = db.Integer()
# UnsignedInt = UnsignedInt.with_variant(INTEGER(unsigned=True), 'mysql')
from configs.config import DBNAME, DATABASE


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    # created_at = Column(TIMESTAMP, nullable=False)
    # updated_at = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return '<{0.__class__.__name__}(id={0.id!r})>'.format(self)


class Partitions(BaseModel):
    __tablename__ = 'partitions'
    header = Column(String(255), nullable=False)
    visible = Column(Integer, nullable=False, default=1, server_default=1)
    parent = Column(Integer, nullable=False, default=0, server_default=0)
    description = Column(Text)


class Elements(BaseModel):
    __tablename__ = 'elements'
    header = Column(String(255), nullable=False)
    visible = Column(Integer, nullable=False, default='1', server_default='1')
    # parent_id = Column(Integer, nullable=False, default='0', server_default='0', index=True)
    parent_id = Column(Integer, ForeignKey('partitions.id', ondelete='CASCADE'), nullable=False, default='0', server_default='0', index=True)
    description = Column(Text)
    syntax = Column(String(255), nullable=False)
    parameters = Column(Text)
    example = Column(Text)
    notes = Column(Text)
    keywords = Column(String(255), index=True)
    version_cm_major = Column(Integer, nullable=False, default='4', server_default='4')
    version_cm_minor = Column(Integer, nullable=False, default='13', server_default='13')
    version_cm_build = Column(Integer, nullable=False, default='0', server_default='0')
    version_cm_releaselevel = Column(String(16), nullable=True, default=None, server_default=None)

    # def __unicode__(self):
        # return self.header

    # def __repr__(self):
        # return 'Element: {}'.format(self.header)


class Users(BaseModel):
    __tablename__ = 'users'
    chat_id = Column(String(32), nullable=False, unique=True)
    # created = Column(TIMESTAMP, nullable=False)
    created = Column(DateTime, nullable=False, default=current_timestamp(), server_default='2000-01-01 00:00:00')
    last_update = Column(DateTime, nullable=False, default=datetime(2000, 1, 1, 0, 0, 0), server_default='2000-01-01 00:00:00')


class LogRequests(BaseModel):
    __tablename__ = 'log_requests'
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    request = Column(String(64), nullable=False)
    rtime = Column(DateTime, nullable=False, default=current_timestamp(), server_default='2000-01-01 00:00:00')


def main():
    engine  = create_engine(URL(**DATABASE), echo = True)

    # создает таблицы в БД
    Base.metadata.create_all(engine)

    # Создаем фабрику Session для создания экземпляров
    Session = sessionmaker(bind=engine)
    # Создаем объект сессии из вышесозданной фабрики Session
    session = Session()


if __name__ == '__main__':
    main()


# --------------------------------------------------------------------------------------------------

# autoincrement=True
# primary_key=True
# unique=True
# nullable=False
# default=
# server_default =


'''
import models
from app import db

db.create_all()
p = Post(title='First post', body='First post body')
db.session.add(p)
db.session.commit()
'''

'''
opt_managers_bind = db.Table('opt_managers_bind',
            db.Column('opt_user_id', INTEGER(unsigned=True), db.ForeignKey('opt_users.id'), nullable=False),
            db.Column('opt_manager_id', INTEGER(unsigned=True), db.ForeignKey('opt_managers.id'), nullable=False)
            )

post_tags = db.Table('post_tags',
            db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
            db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
            )

tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))
'''

