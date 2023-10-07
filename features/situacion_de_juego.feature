# language: es
  Característica: Sitauacion de juego

    Antecedentes:
      Dado que la vida de t1 es 50
      Y que la vida de t2 es 50
      Y que la vida de t3 es 50
      Y que la vida de t4 es 50
      Y que la vida de n1 es 50
      Y que la vida de n2 es 50
      Y que la vida de n3 es 50
      Y que la fuerza de t1 es 5
      Y que la fuerza de t2 es 5
      Y que la fuerza de t3 es 5
      Y que la fuerza de t4 es 5
      Y que la fuerza de n1 es 5
      Y que la fuerza de n2 es 5
      Y que la fuerza de n3 es 5
      Y siempre se mueven primero los distritos más cercanos al 0
      Y luego que se muevan todos los tributos en el tablero, se mueven los neutros
      # Si las vidas de dos tributos adyacentes no cambian, entonces se ignoraron (CONSULTAR)
      Y todos los tributos que compartan el mismo valor numerico (a1,b1) pertenecen al mismo distrito (Excepcion para la n)

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
      Y t1 se mueve antes que t2
      Cuando se ejecute un movimiento
      Entonces t1 estara en (2,2)
      Y la vida de t1 se reducirá a 55
      Y la vida de t2 se mantiene igual

    Escenario: Tres tributos luchan
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |t1|t2|  |  |  |  |  |
      |  |t3|  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t1 golpeo a t2
      Y la vida de t2 es 45
      Y t3 tiene en su rango de vision a t1 y t2
      Cuando se ejecuta una iteracion
      Entonces t3 le dara un golpe a t1
      Y la vida de t1 es 45


    Escenario: Dos tributos luchan y llega un aliado
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |a1|t2|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |b1|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y que la vida de a1 es 50
      Y que la vida de b1 es 50
      Cuando se ejecuten 2 iteraciones
      Entonces a1 y b1 seran adyacentes a t2
      Y la vida de a1 será 40
      Y la vida de b1 será 50
      Y la vida de t2 será 35


    Escenario: Enfrentamiento entre 2 tributos
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |t1|t2|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecuta una iteracion
      Entonces la vida de t1 es 45
      Y la vida de t2 es 45

    Escenario: Un tributo se alia con un tributo neutro
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |t1|n0|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t1 tiene un valor de alianza 25
      Y t1 le ofrece una alianza a n0
      Cuando n0 acepte la alianza de t1
      Entonces el tributo n0 forma parte del distrito 1
      Y el distrito 1 tiene un tributo más en su cantidad total
      Y el tributo neutro pertenece al districto 1
      Y el tributo neutro no pertenece más al grupo de los tributos neutros

    Escenario: Un tributo no logra aliarse con un tributo neutro
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |t1|n0|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t1 tiene un valor de alianza 1
      Y t1 le ofrece una alianza a n0
      Cuando n0 rechace la alianza de t1
      Entonces el tributo n0 no forma parte del distrito 1
      Y t1 empieza a pelear con n0

      Escenario: Dos tributos se encuentran en el mapa
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |a1|b1|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecute una iteracion
      Entonces la vida de a1 sera 50
      Y la vida de b1 sera 50
      Y la posicion de n1 debe ser distinta a (2,1)
      Y la posicion de n2 debe ser distinta a (2,2)

    Escenario: Muerte de un tributo en batalla
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |t1|t2|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t2 tiene 5 de vida
      Y t1 tiene 7 de fuerza
      Cuando se ejecuta una iteracion
      Entonces t2 muere
      Y t2 desaparece del mapa
      Y el distrito 2 tiene un tributo menos

    Escenario: Dos tributos neutros se encuentran en el mapa
      Dado que dos tributos son neutros
      Cuando se encuentran en el mapa
      Entonces se ignoran

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
