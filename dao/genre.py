from model.genre import GenreModel


class GenreDAO:

    def __init__(self, session):
        self.session = session

    def get_genres_all(self):
        return self.session.query(GenreModel).all()

    def get_genre_id(self, gid):
        return self.session.query.get(gid)
