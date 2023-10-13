# language: es

Característica: Inicio de juego


  Escenario: Se genera el mapa y no hay 2 tributos en la misma celda
    Dado que empezó la simulación
    Cuando se generen los distritos
    Entonces no hay más de un tributo por celda

  Escenario: Correcta inicialización de los tributos de un mismo distrito
	  Dado que la simulación comenzó
	  Cuando dos tributos de un mismo distrito aparecen en el mapa
	  Entonces sus stats deben ser iguales
