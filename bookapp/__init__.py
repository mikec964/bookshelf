from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bookapp.config import Config 

app = Flask(__name__)
# app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from bookapp import routes
