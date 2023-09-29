from game.logic.tribute import Tribute

class District:

    # Constructor de clase
    def __init__(self):
        self.number_district = None
        self.cant_tributes = None
        self.tributes = []
    

    def get_number_district(self):
        return self.number_district
  
  
    def get_cant_tribute(self):
        return self.cant_tributes


    # Metodo para configurar un distrito de tributos, es decir, una lista de instancias.
    def set_config(self, life, force, alliance, number_district, cant_tributes):
        
        if force < 5 or force > 10:
            raise ValueError(f'Force must be between 5 and 10 points: {force}')
        if alliance < 1 or alliance > 10:
            raise ValueError(f'Alliance must be between 1 and 10 points: {alliance}')
        
        self.number_district = number_district # setea el numero del distrito
        self.cant_tributes = cant_tributes # setea la cantidad de tributos en el distrito

        for i in range(self.cant_tributes):
            trib = Tribute()
            trib.life = life # setea la vida
            trib.force = force # setea la fuerza
            trib.alliance = alliance # setea la alianza
            trib.district = number_district # setea el numero del distrito
            self.tributes.append(trib) # se agrega el tributo configurado 

    
    # Metodo donde agregar una instancia de Tributo a una lista tributes.
    def add_tribute(self, tribute):
        if not isinstance(tribute, Tribute):
            raise ValueError(f'Is not an instance of Tribute: {tribute}')
         
        self.tributes.append(tribute) # agrega un tributo a la lista de tributos
    