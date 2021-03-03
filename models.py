from server import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)
class User(db.Model):

    id=db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable = False, unique=True)
    password = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(50), nullable = False)

