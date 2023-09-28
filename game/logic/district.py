from game.logic.tribute import Tribute

class District:

    # Constructor de clase
    def __init__(self):
        self.number_district = None
        self.cant_tributes = None
        self.tributes = []
    

    # Constructor de clase alternativo. La manera de crear una instancia es: district = District.constructor(1, 4)
    # @classmethod 
    # def constructor(cls, number_district, cant_tributes):
    #     instance = cls()
    #     instance.number_district = number_district
    #     instance.cant_tributes = cant_tributes 
    #     instance.tributes = [] 
    #     return instance

    
    def get_number_district(self):
        return self.number_district
  
  
    def get_cant_tribute(self):
        return self.cant_tributes


    # Metodo para configurar un distrito de tributos, es decir, una lista de instancias.
    def set_config(self, life, force, alliance, number_district, cant_tributes):
        
        if life != 50:
            raise ValueError(f'Life must be 50 points: {life}')
        if force < 5 or force > 10:
            raise ValueError(f'Force must be between 5 and 10 points: {force}')
        if alliance < 1 or alliance > 10:
            raise ValueError(f'Alliance must be between 1 and 10 points: {alliance}')
        if number_district not in [1, 2, 3, 4, 5, 6]:
            raise ValueError(f'Number of district must be between 1 and 6: {number_district}')
        if cant_tributes < 4 or cant_tributes > 6:
            raise ValueError(f'Number of tributes per district must be between 4 and 6: {cant_tributes}')

        self.number_district = number_district # setea el numero del distrito
        self.cant_tributes = cant_tributes # setea la cantidad de tributos en el distrito

        for i in range(self.cant_tributes):
            trib = Tribute()
            trib.life = life # setea la vida
            trib.force = force # setea la fuerza
            trib.alliance = alliance # setea la alianza
            trib.district = number_district # setea el numero del distrito
            self.tributes.append(trib) # se agrega el tributo configurado 

    
# district = District()
# district.set_config(50, 5, 10, 1, 4) # life, force, alliance, num_district, cant_tributes
