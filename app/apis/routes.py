from app.apis.game_controler import GameControler

class GetDistrict():
    def get(self):
        return GameControler.get_new_district()

