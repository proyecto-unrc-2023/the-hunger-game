# language: es
  Característica: Sitauacion de juego

    Escenario: Dos tributos luchan y uno de ellos encuentra un item
      Dado que empezo la simulacion
      Y un tributo es adyacente a otr
      Y esta sobre un item
      Cuando se ejecute un paso de iteracion
      Entonces el que no esta sobre el item, golpeara al otro
      Y el otro recoge el item, perdiendo asi una iteracion
      Y luego lucharan

    Escenario: Dos tributos luchan y llega otro tributo
      Dado que empezo la simulacion
      Y dos tributos enemigos son adyacentes
      Y estan luchando
      Cuando otro tributo visualize a los tributos luchando mediante su rango de vision
      Y sea adyacente a ambos
      Entonces le pegara al tributo que tenga mas vida

    Escenario: Dos tributos luchan y llega un aliado
      Dado que empezo la simulacion
      Y dos tributos de distinto distritos son adyacentes
      Y estan luchando
      Cuando  llegue un tributo aliado de algunos de los dos tributos que estan luchando
      Y ambos tributos entran en el rango de vision del aliado
      Entonces el aliado atacara al tributo enemigo

    Escenario: Enfrentamiento entre tributos
      Dado que dos tributos son de distintos distritos
      Y tienen la mismas caracteristicas
      Y tienen la misma cantidad de vida
      Cuando se encuentran y enfrentan en el mapa
      Entonces ambos tributos mueren

    Escenario: Un tributo se alia con un tributo neutro
      Dado que un tributo pertenece a un distrito y otro es neurtro
      Cuando se encuentran en el mapa
      Y el tributo perteneciente al distrito es capaz de aliarse
      Entonces el tributo neutro se convierte en un miembro del tributo que se encontro
      Y adquiere las caracteristicas del distrito al cual corresponde

    Escenario: Un tributo no logra aliarse con un tributo neutro
      Dado un tributo que pertenece a un distrito y otro neutro
      Cuando ambos tributos se encuentran en el mapa
      Y el tributo del distrito NO es capaz de aliarse
      Entonces el tributo del distrito lucha con el tributo neutro

    Escenario: Dos tributos del mismo distrito se encuentran en el mapa
      Dado dos tributos
      Cuando se encuentran en el mapa
      Y ambos pertenecen al mismo distrito
      Entonces se ignoran

    Escenario: Muerte de un tributo en batalla
      Dado que dos tributos son de distinto distrito
      Y tienen distintas estadisticas
      Cuando se encuentran en el mapa
      Y luchan
      Entonces uno de ellos muere

    Escenario: Dos tributos neutros se encuentran en el mapa
      Dado que dos tributos son neutros
      Cuando se encuentran en el mapa
      Entonces se ignoran

    Escenario: Tributo encuentra un item de curacion y lo utiliza
      Dado que un tributo encuentra un item de curacion en el mapa
      Y no tenga la vida al maximo
      Cuando el tributo se encuentra sobre el item
      Entonces su vida incrementa
      Y el item desaparece del mapa

    Escenario: Tributo encuentra un item de curacion y no lo utiliza
      Dado que un tributo encuentra un item de curacion en el mapa
      Y tiene la vida al maximo
      Cuando se encuentra sobre el item
      Entonces lo ignora

    Escenario: Tributo encuentra una espada y la recoge
      Dado que un tributo encuentra una espada en el mapa
      Cuando el tributo no tenga una espada
      Y se escuentre sobre la espada
      Entonces su daño se incrementa
      Y la espada desaparece del mapa

    Escenario: Tributo encuentra una espada y no la recoge
      Dado que un tributo encuentra una espada en el mapa
      Cuando el tributo tenga una espada
      Y se encuentre sobre la espada
      Entonces no la recoge

    Escenario: Tributo con más fuerza inflige más daño a su enemigo
	    Dado que dos tributos son de distinto distrito
	    Cuando se cruzan en el mapa
	    Entonces el tributo con más fuerza inflige más daño

    Escenario: Tributo con menos fuerza inflige menos daño a su enemigo
	    Dado que dos tributos son de distinto distrito
	    Cuando se cruzan en el mapa
	    Entonces el tributo con menos fuerza inflige menos daño
