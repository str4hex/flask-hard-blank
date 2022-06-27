from flask_restx import Resource, Namespace

genre_ns = Namespace('genre')

@genre_ns.route('')
class GenreViewe_One(Resource):
    def get(self):
        pass

@genre_ns.route('<int:gid>')
class GenreView_All(Resource):
    def get(self, gid):
        pass