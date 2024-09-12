from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    userID = db.Column(db.Integer, primary_key=True)
    userEmail = db.Column(db.String(150), unique=True)