from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    noteID = db.Column(db.Integer, primary_key=True)
    noteData = db.Column(db.String(10000))
    noteDate = db.Column(db.DateTime(timezone=True), default=func.now())
    

class User(db.Model, UserMixin):
    userID = db.Column(db.Integer, primary_key=True)
    userEmail = db.Column(db.String(150), unique=True)
    userPassword = db.Column(db.String(150))
    userFirstName = db.Column(db.String(150))