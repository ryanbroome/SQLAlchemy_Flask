from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

db = SQLAlchemy()


def connect_db(app):
    db.init_app(app)
    db.app = app
    app.app_context().push()

# MODELS GO BELOW: DEFINE SCHEMA WHAT TABLE AND COLUMNS SHOULD HAVE / LOOK LIKE


class Pet(db.Model):
    """Pet"""
    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(100),
                     nullable=False,
                     unique=True)

    species = db.Column(db.String(30),
                        nullable=True)

    hunger = db.Column(db.Integer,
                       nullable=False,
                       default=20)


class Owner(db.Model):
    """Owners"""
    __tablename__ = "owners"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(100),
                     nullable=False,
                     unique=True)

    species = db.Column(db.String(30),
                        nullable=True)

    hunger = db.Column(db.Integer,
                       nullable=False,
                       default=20)
