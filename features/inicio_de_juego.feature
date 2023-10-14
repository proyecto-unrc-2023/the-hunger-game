# language: es

Característica: Inicio de juego


  Escenario: Se genera el mapa y no hay 2 tributos en la misma celda
    Dado que el juego se creo
    Cuando esta por comenzar la simulacion
    Entonces no hay más de un tributo por celda

  Escenario: Correcta inicialización de los tributos de un mismo distrito
    Dado que el juego se creo
    Cuando esta por comenzar la simulacion
    Entonces dos tributos del mismo distrito deben tener las mismas caracteristicas

  Escenario: Se genera el mapa y todos los distritos tienen tributos
    Dado que el juego se creo
    Cuando esta por comenzar la simulacion
    Entonces todos los distritos tienen al menos un tributo