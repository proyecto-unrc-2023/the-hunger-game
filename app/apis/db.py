from app.apis.config_bp import GameControler
from game.logic.game_logic import GameLogic

class GetDistrict():
    def get(self):
        return GameControler.get_new_district()
from app import db


class ConfigDistrict(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_district = db.Column(db.Integer)
    cant_tributes = db.Column(db.Integer)
    tributes = db.Column()


'''Class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.Enum ,nullable=False)
    board = db.Column(db.Text)
    districts = db.Column(db.List) 
    neutrals = db.Column(db.List) 
   
    def __init__(self, rows,columns):  
        self = GameLogic(rows,columns)  
    
    def __repr__(self):
        return self.id 
    
    def json(self):
        return self.to_string() 
    '''
 
        

