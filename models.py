"""Models for Blogly."""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


default = 'https://thecontemporarypet.com/wp-content/themes/contemporarypet/images/default.png'


class Pet(db.Model):
    __tablename__ = 'pet'

    def __repr__(self):
        p = self
        return '<Pet: {p.id} name: {p.name} species: {p.species} photo_url: {p.photo_url} age: {p.age} notes: {p.notes} available: {p.available}>'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)
    photo_url = db.Column(db.String, nullable=False, default=default)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.String, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)
