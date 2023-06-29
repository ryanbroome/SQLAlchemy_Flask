from flask import Flask, current_app, render_template, request, redirect, session
from models import db
from models import connect_db
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql import text
from models import Pet

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_shop_db"

app.config['SECRET_KEY'] = 'chickenzarecool21837'

app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

app.config["SQLALCHEMY_ECHO"] = True

# app.config["SQLALchemy_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def list_pets():
    """show home page"""
    pets = Pet.query.all()
    return render_template('list.html', pets=pets)


@app.route('/', methods=["POST"])
def create_pet():
    name = request.form["name"]
    species = request.form["species"]
    hunger = request.form["hunger"]
    hunger = int(hunger) if hunger else None

    new_pet = Pet(name=name, species=species, hunger=hunger)

    db.session.add(new_pet)
    db.session.commit()

    return redirect(f"/{new_pet.id}")


@app.route('/<int:pet_id>')
def show_pet(pet_id):
    """Show details about a single pet"""
# this get_or_404 comes from sql alchemy, get or if None respond 404
    pet = Pet.query.get_or_404(pet_id)
    # our original method was this, so the above is similar just helps if the id doesn't exist in db
    # pet = Pet.query.get(pet_id)
    return render_template("details.html", pet=pet)


@app.route("/species/<species_id>")
def show_pets_by_species(species_id):
    pets = Pet.get_by_species(species_id)
    return render_template("species.html", pets=pets, species=species_id)
