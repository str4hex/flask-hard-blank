from dao.model.movies import MoviesModel


class MoviesDAO:

    def __init__(self, session):
        self.session = session

    def get_movies_all(self):
        return self.session.query(MoviesModel).all()

    def get_movie_id(self, mid):
        return self.session.query(MoviesModel).get(mid)

    def get_director_movies(self, did):
        return self.session.query(MoviesModel).filter_by(director_id=did)

    def get_genre_movies(self, gid):
        return self.session.query(MoviesModel).filter_by(genre_id=gid)

    def get_year_movies(self, yid):
        return self.session.query(MoviesModel).filter_by(year=yid)

    def add_movei(self, data):
        self.session.add(data)
        self.session.commit()
        return {"message": "successfully added movie"}

    def update_movie(self, data):
        id_movie = data.id
        movie = self.session.query(MoviesModel).get(id_movie)
        movie.title = data.title
        movie.description = data.description
        movie.trailer = data.trailer
        movie.year = data.year
        movie.rating = data.rating
        movie.genre_id = data.genre_id
        movie.director_id = data.director_id
        self.session.commit()
        return {"message": "successfully update movie"}

    def delete_movie(self, mid):
        self.session.query(MoviesModel).filter_by(id=mid).delete()
        self.session.commit()
        return {"message": "successfully delete movies"}
