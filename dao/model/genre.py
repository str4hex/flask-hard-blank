from setup_db import db
from marshmallow import fields, Schema


class GenreModel(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class GenreShema(Schema):
    id = fields.Integer()
    name = fields.String()
