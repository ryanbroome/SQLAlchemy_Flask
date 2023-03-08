from flask import Flask, current_app, render_template
from models import db, connect_db
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.sql import text


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///pet_shop_db"
app.config['SECRET_KEY'] = 'chickenzarecool21837'
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_ECHO"] = True
# app.config["SQLALchemy_TRACK_MODIFICATIONS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def home_page():
    """show home page"""
    return render_template('home.html')


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String, unique=True, nullable=False)


# kyle = Pet(name="Kyle the chicken", species="Chicken")
# kyle.name = "rooster"


# * PYTHON COMMANDS USE ORMS TO USE PYTHON TO
# * DEFINE A MODEL / CLASS FOR SQL COMMANDS
# * SAME AS WRITING THESE BELOW COMMANDS IN SQL BUT  INSTEAD AS A CLASS IN PYTHON
# * SEE ~USF/PRACTICE/ARCHIVE/FIRSTFLASKAPP/MODELS.PY

# * INSERT INTO pets(name, species) VALUES('kyle', 'chicken')

# * CREATE TABLE pets(
# *     id INTEGER,
# *     name NOT NULL UNIQUE,
# *     species NOT NULL,
# * )
