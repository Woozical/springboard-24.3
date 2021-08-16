"""Flask app for Cupcakes"""

from flask import Flask
from models import db, connect_db, Cupcake

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_KEY_HERE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)