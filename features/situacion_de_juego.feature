# language: es
  Característica: Sitauacion de juego

    Escenario: Dos tributos luchan y uno de ellos encuentra un item
      Dado que tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |t2|  |  |  |  |  |
      |  |t1|p |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y la vida de t1 es de 50
      Y la vida de t2 es de 50
      Y la poción cura 10 de vida
      Y la fuerza de t2 es de 5
      Y la pocion esta en la posicion (2,2)
      Y t1 se mueve antes que t2
      Cuando se ejecute un movimiento
      Entonces t1 estara en (2,2)
      Y la vida de t1 se reducirá a 55
      Y la vida de t2 se mantiene igual

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

    Escenario: Enfrentamiento entre 2 tributos
      Dado que t0 pertenece al distrito 0
      Y t0 tiene una vida de 50
      Y t0 tiene una fuerza de 10
      Y t1 pertenece al distrito 1
      Y t1 tiene una vida de 50
      Y t1 tiene una fuerza de 10
      Y t0 esta en la posicion (0,0)
      Y t1 esta en la posicion (0,1)
      Cuando se ejecute una iteracion del juego
      Entonces la vida de t0 es 40
      Y la vida de t1 es 40

    Escenario: Un tributo se alia con un tributo neutro
      Dado que existe un t1 y un t
      Y t1 pertenece al distrito 0
      Y t1 tiene un valor de alianza 25
      Y t es un tribruto neutro
      Y el estado del tablero es el siguiente
        |0 |1 |2 |3 |
        |  |  |  |  |
        |  |  |  |  |
        |  |t1|t |  |
        |  |  |  |  |
      Cuando t acepte la alianza de t1
      Entonces el tributo t forma parte del distrito 0
      Y el distrito 0 tiene un tributo más en su cantidad total
      Y el tributo neutro pertenece al districto 0
      Y el tributo neutro no pertenece más al grupo de los neutros


    Escenario: Un tributo no logra aliarse con un tributo neutro
      Dado que existe un t1 y un t
      Y t1 pertenece al distrito 0

      Y t1 tiene un valor de alianza 1
      Y t es un tribruto neutro
      Y el estado del tablero es el siguiente
        |0 |1 |2 |3 |
        |  |  |  |  |
        |  |  |  |  |
        |  |t1|t |  |
        |  |  |  |  |
      Cuando t rechaze la alianza de t1
      Entonces el tributo t empieza a pelear con t1

      #Dado un tributo que pertenece a un distrito y otro neutro
      #Cuando ambos tributos se encuentran en el mapa
      #Y el tributo del distrito NO es capaz de aliarse
      #Entonces el tributo del distrito lucha con el tributo neutro

    Escenario: Dos tributos del mismo distrito se encuentran en el mapa
      Dado dos tributos
      Cuando se encuentran en el mapa
      Y ambos pertenecen al mismo distrito
      Entonces se ignoran

    Escenario: Muerte de un tributo en batalla
      Dado t1 en la posición (0,2)
      Y t2 en la posición (1,2)
      Y ambos son de distinto distrito
      Y t2 tiene 5 de vida
      Y t1 tiene 7 de fuerza
      Cuando t1 le pega a t2
      Entonces la vida de t2 se reduce en 7 puntos
      Y la vida de t2 es de 0 o menos
      Y t2 muere
#""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""2
      Escenario: Dos tributos neutros se encuentran en el mapa
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |n1|n2|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecuten una iteracion
      Entonces la vida de n1 sera 50
      Y la vida de n2 sera 50
      Y la posicion de n1 debe ser distinta a (2,1)
      Y la posicion de n2 debe ser distinta a (2,2)

    Escenario: Tributo encuentra un item de curacion y lo utiliza
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |t1|  |  |  |  |  |
      |  |  |p |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecute una iteracion
      Entonces t1 estara en (2,2)
      Y p desaparece del mapa
      Y la vida de t1 sera 55

    Escenario: Tributo encuentra un item de curación y no lo utiliza
      Dado que el tablero de juego es el siguiente
        |0 |1 |2 |3 |4 |5 |6 |7 |
        |  |  |  |  |  |  |  |  |
        |  |  |t1|  |  |  |  |  |
        |  |  |p |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
      Cuando se ejecute una iteracion
      Entonces t1 estara en (2,2)
      Y p desaparece del mapa
      Y la vida de t1 sera 50

    Escenario: Tributo encuentra una espada y la recoge
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |t1|w |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecuta una iteracion
      Entonces la fuerza de t1 sera 10
      Y w desaparece del mapa
      Y t1 estara en (2,3)


    Escenario: Tributo encuentra una espada y no la recoge
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |t1|w |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y la fuerza de t1 es 10
      Cuando se ejecuta una iteracion
      Y la posicion de t1 debe ser distinta a (2,2)
      Y w estara (2,3)

    Escenario: Tributo con mayor fuerza inflige mayor daño a otro tributo con menor fuerza en combate
	    Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |t1|  |  |  |  |
      |  |  |t2|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y la fuerza de t1 es 10
	    Cuando se ejecuta una iteracion
	    Entonces la vida de t2 sera 40
      Y vida de t1 sera 45
