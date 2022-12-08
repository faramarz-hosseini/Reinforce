from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

for db_name, db_conf in list(DATABASES.items()):
    DATABASES[db_name]['CONN_MAX_AGE'] = 0