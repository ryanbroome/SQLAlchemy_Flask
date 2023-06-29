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

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(100), nullable=False, unique=True)

    species = db.Column(db.String(30), nullable=True)

    hunger = db.Column(db.Integer, nullable=False, default=20)

    @classmethod
    def get_by_species(cls, species):
        return cls.query.filter_by(species=species).all()

    @classmethod
    def get_all_hungry(cls):
        return cls.query.filter(Pet.hunger > 20).all()

    def __repr__(self):
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} hunger={p.hunger}>"

    def greet(self):
        """return greeting of each Pet"""
        return f"Hi, I am the {self.name} the {self.species}"

    def feed(self, amt=20):
        """Update hunger based off of amt"""
        self.hunger -= amt
        self.hunger = max(self.hunger, 0)

        # if trying to make updates to a table like adding a column, go to postgres and DROP TABLE, it will not create a table if the same table already exists in the db
