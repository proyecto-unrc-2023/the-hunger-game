from marshmallow import Schema, fields
from app import db #traigo instancia db
import json

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    
    # Constructor of User, values can take None or specified value.
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password
  
    # Representation of username to string.  
    def __repr__(self):
        return "<User %r>" % self.username
    
    # Return dicctionary of columns
    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }

#Crear Userschema?