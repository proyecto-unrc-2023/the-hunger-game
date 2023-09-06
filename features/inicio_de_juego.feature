# language: es

Característica: Inicio de juego

  Escenario: El usuario entra a jugar
    Dado que ingresó a jugar
    Cuando da un click en el botón “Jugar”
    Entonces accede a la configuración de su distrito

  Escenario: Inicio de juego
    Dado que mi distrito está listo
    Cuando doy click al botón “Comienzo de simulación”
    Entonces empieza la simulación
	  Y aparecen todos los tributos en el tablero
	  Y aparecen los items en el tablero

  Escenario: Se genera el mapa y no hay 2 tributos en la misma celda
    Dado que empezó la simulación
    Cuando se generen los distritos
    Entonces no hay más de un tributo por celda

  Escenario: Correcta inicialización de los tributos de un mismo distrito
	  Dado que la simulación comenzó
	  Cuando dos tributos de un mismo distrito aparecen en el mapa
	  Entonces sus stats deben ser iguales
