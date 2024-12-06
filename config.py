import os

secret_key = '1'
PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/bbdd/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False