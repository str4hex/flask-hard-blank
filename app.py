from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movies import movies_ns
from views.director import diretor_ns
from views.genre import genre_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_exst(app)
    return app


def register_exst(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(diretor_ns)
    api.add_namespace(genre_ns)


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run()
