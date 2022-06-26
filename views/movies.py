from flask_restx import Resource, Namespace
from flask import request

movies_ns = Namespace('movies')


@movies_ns.route('')
class MoviesViews_all(Resource):
    def get(self):
        pass


@movies_ns.route('/<int:mid>')
class MoviesViews_all(Resource):
    def get(self, mid):
        pass

    def post(self, mid):
        pass

    def put(self, mid):
        pass

    def delete(self, mid):
        pass