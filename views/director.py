from flask_restx import Resource, Namespace
from container import director_service
from dao.model.director import DirectorShema

diretor_ns = Namespace('director')
director_shema = DirectorShema(many=True)
directors_shema = DirectorShema()

@diretor_ns.route('')
class DirectorViews_All(Resource):
    def get(self):
        directors_all = director_service.get_director_all()
        return director_shema.dump(directors_all), 200

@diretor_ns.route('/<int:did>')
class DirecrorViews_Id(Resource):
    def get(self, did):
        director_id = director_service.get_director_id(did)
        return directors_shema.dump(director_id), 200
