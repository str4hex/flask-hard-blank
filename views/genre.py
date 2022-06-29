from flask_restx import Resource, Namespace
from container import genre_service
from dao.model.genre import GenreShema

genre_ns = Namespace('genre')

genres_shema = GenreShema()
genre_shema = GenreShema(many=True)


@genre_ns.route('')
class GenreViewe_One(Resource):
    def get(self):
        genre_all = genre_service.get_genres_all()
        return genre_shema.dump(genre_all), 200


@genre_ns.route('/<int:gid>')
class GenreView_All(Resource):
    def get(self, gid):
        genre_id = genre_service.get_genre_id(gid)
        return genres_shema.dump(genre_id), 200
