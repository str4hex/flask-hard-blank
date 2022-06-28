from model.director import DirectorModels


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_director_all(self):
        return self.session.query.all()

    def get_director_id(self, did):
        return self.session.query(DirectorModels).get(did)
