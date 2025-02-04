import os

SECRET_KEY = '1'
PWD = os.path.abspath(os.curdir)

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://ruben:1@localhost/library_mysql'
SQLALCHEMY_TRACK_MODIFICATIONS = False