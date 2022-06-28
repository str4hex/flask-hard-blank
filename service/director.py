from dao.director import DirectorDAO


class Director_Service:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_director_all(self):
        return self.dao.get_director_all()

    def get_director_id(self, did):
        return self.dao.get_director_id(did)
