from dao.model.movies import MoviesModel


class MoviesDAO:

    def __init__(self, session):
        self.session = session

    def get_movies_all(self):
        return self.session.query(MoviesModel).all()

    def get_movie_id(self, mid):
        return self.session.query(MoviesModel).get(mid)

    def get_director_movies(self, did):
        return self.session.query(MoviesModel).filter_by(director=did)

    def get_genre_movies(self, gid):
        return self.session.query(MoviesModel).filter_by(genre=gid)

    def get_year_movies(self,yid):
        return self.session.query(MoviesModel).filter_by(year=yid)

    def add_movei(self, data):
        self.session.add(data)
        self.session.commit()
        return {"message": "successfully added movie"}, 200

    def update_movie(self, data):
        id = data.id
        self.session.query(MoviesModel).get(id)
        self.session.commit()
        return {"message": "successfully update movie"}, 200

    def delete_movie(self, mid):
        return self.session.query(MoviesModel).delete(mid)