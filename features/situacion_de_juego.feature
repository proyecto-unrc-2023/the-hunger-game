# language: es
  Característica: Sitauacion de juego

    Antecedentes:
      Dado que el juego se ha iniciado
      Y que la vida inicial de todos los tributos es 50
      Y que la vida maxima por defecto de todos los tributos es 50
      Y que la vida de n0, n1, n2 es 50 y no pertenecen a ningun distrito
      Y que la fuerza de t0, t1, t2, t3, n0, n1, n2 es 5
      Y luego que se muevan todos los tributos en el tablero, se mueven los neutros

    Escenario: Dos tributos luchan y uno de ellos encuentra un item
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |t1|  |  |  |  |  |
      |  |t0|p |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y la poción cura 10 de vida
      Y la pocion esta en la posicion (2,2)
      Cuando se ejecuta una iteracion
      Entonces t0 estara en (2,2)
      Y la vida de t0 se reducirá a 45
      Y la vida de t1 se mantiene igual

    Escenario: Tres tributos luchan
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |t0|t1|  |  |  |  |  |
      |  |t2|  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t2 tiene en su rango de ataque a t0
      Y t1 tiene en su rango de ataque a t0
      Y t0 tiene en su rango de ataque a t2
      Cuando se ejecuta una iteracion
      Entonces  la vida de t0 es 40
      Y la vida de t1 es 50
      Y la vida de t2 es 45


    Escenario: Dos tributos luchan y llega un aliado
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |a0|t1|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |b0|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecuten 2 iteraciones
      Entonces a0 y b0 tendrán en su rango de ataque a t1
      Y la vida de a0 será 50
      Y la vida de b0 será 40
      Y la vida de t1 será 35


    Escenario: Enfrentamiento entre 2 tributos
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |t0|t1|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecuta una iteracion
      Entonces la vida de t0 es 45
      Y la vida de t1 es 45

    Escenario: Un tributo se alia con un tributo neutro
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |t0|n0|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t0 tiene un valor de alianza 25
      Y t0 le ofrece una alianza a n0
      Cuando n0 acepte la alianza de t0
      Entonces el tributo n0 forma parte del distrito 0
      Y el distrito 0 tiene un tributo más en su cantidad total
      Y el tributo neutro no pertenece más al grupo de los tributos neutros

    Escenario: Un tributo no logra aliarse con un tributo neutro
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |t0|n0|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t0 tiene un valor de alianza 1
      Y t0 le ofrece una alianza a n0
      Cuando n0 rechace la alianza de t0
      Entonces el tributo n0 no forma parte del distrito 0
      Y t0 empieza a pelear con n0

      Escenario: Dos tributos se encuentran en el mapa
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |a0|b0|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecuta una iteracion
      Entonces la vida de a0 sera 50
      Y la vida de b0 sera 50
      Y la posicion de a0 debe ser distinta a (2,1)
      Y la posicion de b0 debe ser distinta a (2,2)

    Escenario: Muerte de un tributo en batalla
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |t0|t1|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t1 tiene 5 de vida
      Y t0 tiene 7 de fuerza
      Cuando se ejecuta una iteracion
      Entonces t1 muere
      Y t1 desaparece del mapa
      Y el distrito 1 tiene un tributo menos

    Escenario: Dos tributos neutros se encuentran en el mapa
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |n0|n1|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando los neutrales iteren
      Entonces la vida de n1 y n0 es 50
      Y la posicion de n0 es distinta a (2,1)
      Y la posicion de n1 es distinta a (2,2)


    Escenario: Tributo encuentra un item de curacion y lo utiliza
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |t0|p |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y la vida maxima de t0 es 60
      Cuando se ejecuta una iteracion
      Entonces t0 estara en (2,2)
      Y p desaparece del mapa
      Y la vida de t0 sera 55

    Escenario: Tributo encuentra un item de curación y no lo utiliza
      Dado que el tablero de juego es el siguiente
        |0 |1 |2 |3 |4 |5 |6 |7 |
        |  |  |  |  |  |  |  |  |
        |  |  |t0|  |  |  |  |  |
        |  |  |p |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
      Y la vida maxima de t0 es 50
      Cuando se ejecuta una iteracion
      Entonces t0 estara en (2,2)
      Y p desaparece del mapa
      Y la vida de t0 sera 50

    Escenario: Tributo encuentra una espada y la recoge
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |t0|w |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecuta una iteracion
      Entonces la fuerza de t0 sera 10
      Y w desaparece del mapa
      Y t0 estara en (2,3)


    Escenario: Tributo encuentra una espada y no la recoge
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |t0|w |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t0 tiene un arma
      Cuando se ejecuta una iteracion
      Entonces la posicion de t0 debe ser distinta a (2,2) y a (2,3)
      Y w estara (2,3)

    Escenario: Tributo ignora la espada y pelea
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |t0|w |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |t1|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t0 tiene un arma
      Y t1 tiene un arma
      Cuando se ejecutan dos iteraciones
      Entonces la posicion de t0 debe ser distinta a (2,2) y a (2,3)
      Y w estara (2,3)
      #Y la vida de t1 sera 45


    Escenario: Tributo con mayor fuerza inflige mayor daño a otro tributo con menor fuerza en combate
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |t0|  |  |  |  |
      |  |  |t1|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y la fuerza de t0 es 10
      Cuando se ejecuta una iteracion
      Entonces la vida de t1 sera 40
      Y vida de t0 sera 45
