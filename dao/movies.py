from dao.model.movies import MoviesModel
from setup_db import db


class MoviesDAO:
    def get_all_movies(self):
        return MoviesModel.query.all()