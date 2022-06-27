from flask_restx import Resource, Namespace


diretor_ns = Namespace('director')


@diretor_ns.route('')
class DirectorViews_One(Resource):
    def get(self):
        pass

@diretor_ns.route('<int:did>')
class DirecrorViews_all(Resource):
    def get(self, did):
        pass