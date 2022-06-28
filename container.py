from service.movies import Movie_Service
from dao.movies import MoviesDAO
from setup_db import db

movie_dao = MoviesDAO(db.session)
movie_service = Movie_Service(movie_dao)
