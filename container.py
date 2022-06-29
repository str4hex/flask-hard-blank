from service.movies import Movie_Service
from dao.movies import MoviesDAO
from dao.genre import GenreDAO
from service.genre import Genre_Service
from dao.director import DirectorDAO
from service.director import Director_Service
from setup_db import db

movie_dao = MoviesDAO(db.session)
movie_service = Movie_Service(movie_dao)
genre_dao = GenreDAO(db.session)
genre_service = Genre_Service(genre_dao)
director_dao = DirectorDAO(db.session)
director_service = Director_Service(director_dao)
