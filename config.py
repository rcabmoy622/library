import os

SECRET_KEY = '1'
PWD = os.path.abspath(os.curdir)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/bbdd/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False