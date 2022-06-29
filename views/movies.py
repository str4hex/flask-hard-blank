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
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        if director_id:
            director_list = movie_service.get_movie_director(director_id)
            return movie_shema.dump(director_list), 200
        if genre_id:
            genre_list = movie_service.get_genre_movies(genre_id)
            return movie_shema.dump(genre_list), 200
        if year:
            year = movie_service.get_year_movies(year)
            return movie_shema.dump(year), 200

        return movie_shema.dump(movies_get_all), 200

    def post(self):
        data = request.json
        movies_get_bd = MoviesModel(**data)
        return movie_service.add_movie(movies_get_bd), 200

    def put(self):
        data = request.json
        movies_update_bd = MoviesModel(**data)
        return movie_service.update_movie(movies_update_bd), 202

@movies_ns.route('/<int:mid>')
class MoviesViews_all(Resource):

    def get(self, mid):
        movies_get_id = movie_service.get_movie_id(mid)
        return movies_shema.dump(movies_get_id), 200

    def delete(self, mid):
        return movie_service.delete_movie(mid), 202
