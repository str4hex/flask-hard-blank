from flask import request
from flask_restx import Resource, Namespace
from dao.model.movies import MoviesSchema, MoviesModel
from container import movie_service


movies_ns = Namespace('movies')

movies_shema = MoviesSchema()
movie_shema = MoviesSchema(many=True)


@movies_ns.route('')
class MoviesViews_all(Resource):
    def get(self):
        movies_get_all = movie_service.get_movies_all()
        return movie_shema.dump(movies_get_all), 200

    def post(self):
        data = request.json
        movies_get_bd = MoviesModel(**data)
        return movie_service.add_movie(movies_get_bd)

    def put(self):
        data = request.json
        movies_update_bd = MoviesModel(**data)
        return movie_service.update_movie(movies_update_bd)

@movies_ns.route('/<int:mid>')
class MoviesViews_all(Resource):

    def get(self, mid):
        movies_get_id = movie_service.get_movie_id(mid)
        return movies_shema.dump(movies_get_id)

    def delete(self, mid):
        pass
