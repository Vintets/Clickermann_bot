#!/usr/bin/env python
# -*- coding: utf-8 -*-

CLICKERMANN_HELP_BOT_TOKEN = 'token'
DBNAME = 'cm_bot'

ECHO_SQL = False

# db mysql
# engine = create_engine(f'mysql+mysqlconnector://user:pwd@localhost/{DBNAME}', echo = True)
# DATABASE = {
    # 'drivername': 'mysql+mysqlconnector',
    # 'host': 'localhost',
    # 'port': '3306',
    # 'username': 'username',
    # 'password': 'password',
    # 'database': DBNAME
# }

# db sqlite
# engine = create_engine(f'sqlite:///{DBNAME}.db', echo = True)
DATABASE = {
    'drivername': 'sqlite',
    'database': f'{DBNAME}.db'
}
