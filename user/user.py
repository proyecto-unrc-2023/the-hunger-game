from app import db
from marshmallow import Schema, fields


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=False, nullable=False)
    character = db.Column(db.String(50), unique=False, nullable=True)
    
    
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
            'password': self.password,
            'character': self.character
        }
        
    # Method to add an user to the db
    def add_user(self, name, password):
        if name is None or password is None:
            raise ValueError('Name or password is None')
        else:
            new_user = User(username=name, password=password)
            db.session.add(new_user)
            db.session.commit()
    
    # Method to select a character for an user    
    def select_character(self, num_pj):
        self.character = num_pj
        db.session.commit()
        
        
class UserSchema(Schema):
    id = fields.Integer()
    username = fields.Str()
    password = fields.Str()
    character = fields.Str()