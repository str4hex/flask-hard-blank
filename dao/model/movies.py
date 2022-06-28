from dao.model.director import DirectorModels
from dao.model.genre import GenreModel
from setup_db import db
from marshmallow import fields, Schema


class MoviesModel(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    genre = db.relationship(GenreModel)
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    director = db.relationship(DirectorModels)


class MoviesSchema(Schema):
    id = fields.Integer()
    title = fields.String()
    description = fields.String()
    trailer = fields.String()
    year = fields.Integer()
    rating = fields.Integer()
    genre_id = fields.String()
    director_id = fields.String()
