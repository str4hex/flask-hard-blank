from marshmallow import Schema, fields

from setup_db import db


class DirectorModels(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class DirectorShema(Schema):
    id = fields.Integer()
    name = fields.String()
