from dao.movies import MoviesDAO


class Movie_Service:

    def __init__(self, dao: MoviesDAO):
        self.dao = dao

    def get_movies_all(self):
        return self.dao.get_movies_all()

    def get_movie_id(self, mid):
        return self.dao.get_movie_id(mid)

    def get_movie_director(self, did):
        return self.dao.get_director_movies(did)

    def get_genre_movies(self, gid):
        return self.dao.get_genre_movies(gid)

    def add_movie(self, data):
        return self.dao.add_movei(data)

    def get_year_movies(self, yid):
        return self.dao.get_year_movies(yid)

    def update_movie(self,data):
        return self.dao.update_movie(data)

    def delete_movie(self, mid):
        return self.dao.delete_movie(mid)