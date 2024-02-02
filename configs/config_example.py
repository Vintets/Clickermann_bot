from pathlib import Path


CLICKERMANN_HELP_BOT_TOKEN = 'token'
DBNAME = 'cm_bot'
IDADMIN = '00000000'

ECHO_SQL = False
PARSE_MODE = 'MARKDOWN'

THUMB_URL = 'https://i.ibb.co/dpWYP66/Clickermann-v4-MAINICON.jpg'

"""
db mysql
engine = create_engine(f'mysql+mysqlconnector://user:pwd@localhost/{DBNAME}', echo = True)
DATABASE = {
    'drivername': 'mysql+mysqlconnector',
    'host': 'localhost',
    'port': '3306',
    'username': 'username',
    'password': 'password',
    'database': DBNAME
}
"""

# db sqlite
# engine = create_engine(f'sqlite:///{DBNAME}.db', echo = True)
DATABASE = {
    'drivername': 'sqlite',
    'database': str(Path(__file__).parent / f'{DBNAME}.db')
}
