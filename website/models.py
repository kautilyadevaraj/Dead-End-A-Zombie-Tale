from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(10) , unique=True)
    text = db.Column(db.String(10000))
    question = db.Column(db.String(10000))
    choices = db.Column(db.String(10000))
    location = db.Column(db.String(50))
    next_level = db.Column(db.String(50))
    item = db.Column(db.String(50))
    use = db.Column(db.String(50))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150) , unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(100) , unique=True)
    first_name = db.Column(db.String(150))
    level = db.Column(db.String(10))
    inventory = db.Column(db.String(1000))
    
class Stats(db.Model):
    username = db.Column(db.String(100) , primary_key=True)
    levels_cleared = db.Column(db.Integer)
    coins = db.Column(db.Integer)
    deaths = db.Column(db.Integer)
    
class ShopItem(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  description = db.Column(db.String(200))
  cost = db.Column(db.Integer, nullable=False)
    