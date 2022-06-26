from flask import Flask


class Config(object):
    DEBUG = True
    SECRET_HERE = '249y823r9v8238r9u'
    SQLALCHEMY_DATABASE_URI = 'SQLITE:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False