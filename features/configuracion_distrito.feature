# language: es

Característica: Configuración del distrito

  Escenario: El usuario incrementa en un punto de estadistica
    Dado que un usuario aumenta una stat a su distrito
    Cuando da click en el botón + da la estadistica X
    Y tiene puntos disponibles para consumir
    Entonces se incrementa un punto la estadística X
    Y se decrementa un punto a la cantidad de puntos disponibles


  Escenario: El usuario decrementa en un punto una estadística
    Dado  que un usuario decrementa una stat a su distrito
   	Cuando da click en el botón - de una estadística X
   	Y X fue incrementada al menos una vez
   	Entonces decrementa un punto la estadística  X
   	Y se incrementa un punto a la cantidad de puntos disponibles

  Escenario: El usuario comienza la simulación
    	Dado que un usuario termina de configura su distrito
    	Y no hay más puntos disponibles para aumentar las estadísticas
    	Cuando el usuario hace click en Comenzar
    	Entonces se inicializa el tablero y comienza la simulación

