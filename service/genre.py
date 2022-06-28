from dao.genre import GenreDAO


class Genre_Service():

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_genres_all(self):
        return self.dao.get_genres_all()

    def get_genre_id(self, gid):
        return self.dao.get_genre_id(gid)