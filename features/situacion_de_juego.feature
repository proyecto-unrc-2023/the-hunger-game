# language: es
  Característica: Sitauacion de juego

    Antecedentes:
      Dado que el juego se ha creado
      Y que la vida inicial de todos los tributos es 50
      Y que la vida maxima por defecto de todos los tributos es 50
      Y que la vida de n0, n1, n2 es 50 y no pertenecen a ningun distrito
      Y que la fuerza de todos los tributos es 5
      Y luego que se muevan todos los tributos en el tablero, se mueven los neutros
      Y todos los tributos que compartan el mismo valor numerico (por ejemplo a1,b1) pertenecen al mismo distrito (Excepcion para la n)

    Escenario: Dos tributos luchan y uno de ellos encuentra un item de curacion
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |t1|  |  |  |  |  |
      |  |t0|pl|  |  |  |  |  |
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
      Y la vida de a0 es 50
      Y la vida de b0 es 40
      Y la vida de t1 es 35


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
      Y t0 y t1 no tienen arma
      Cuando se ejecuta una iteracion
      Entonces la vida de t0 es 45
      Y la vida de t1 es 45

    Escenario: Enfrentamiento entre 2 tributos
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |t0|sw|t1|  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |t2|t3|  |  |  |  |t4|t5|
      Y t1 no tiene arma
      Cuando se ejecuten 2 iteraciones
      Entonces la vida de t0 es 40
      Y t0 tiene una espada
      Y la vida de t1 es 40


    Escenario: Enfrentamiento entre 2 tributos
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |t0|sp|  |  |t1|  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t1 no tiene arma
      Cuando se ejecuten 2 iteraciones
      Entonces t0 tiene una lanza
      Y  la vida de t0 es 50
      Y la vida de t1 es 42


    Escenario: Enfrentamiento entre 2 tributos
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |t0|wo|  |  |t1|  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t1 no tiene arma
      Cuando se ejecuten 2 iteraciones
      Entonces la vida de t0 es 50
      Y t0 tiene un arco
      Y la vida de t1 es 44



    Escenario: Un tributo huye de un combate
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |t0|  |  |t1|  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y t0 tiene un punto de cobardia disponible
      Cuando se ejecuta una iteracion
      Entonces t0 usará medio punto de cobardia
      Y la pocision de t0 es (3, 0)

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
      Entonces la vida de t1 es 40
      Y la vida de t0 es 45

    Escenario: Se producen dos luchas al mismo tiempo
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |t0|sw|t1|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |po|  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |t2|t3|
      Cuando se ejecute el juego
      Entonces el distrito 0 es el ganador
      Y t0 tiene una espada


    Escenario: Dos tributos luchan a muerte y uno de ellos tiene un arco
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |t0|wo|  |  |t1|  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y la vida de t1 es 5
      Cuando se ejecuten 2 iteraciones
      Entonces t1 esta muerto
      Y t0 tiene un arco

    Escenario: Dos tributos luchan a muerte y uno de ellos tiene una lanza
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |t0|sp|  |t1|  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y la vida de t1 es 5
      Cuando se ejecuten 2 iteraciones
      Entonces t1 esta muerto
      Y t0 tiene una lanza

    Escenario: Dos tributos luchan a muerte y uno de ellos tiene una espada
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |t0|sw|t1|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y la vida de t1 es 5
      Cuando se ejecuten 2 iteraciones
      Entonces t1 esta muerto
      Y t0 tiene una espada

    Escenario: Un tributo muere por el efecto de la posion de veneno
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |t0|po|  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y la vida de t0 es 5
      Cuando se ejecuta una iteracion
      Entonces t0 esta muerto

    Escenario: Un tributo no logra aliarse con un tributo neutro y el tributo muere
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
      Y la vida de t0 es 5
      Cuando n0 rechace la alianza de t0
      Y se ejecuta una iteracion
      Entonces el tributo n0 no forma parte del distrito 0
      Y t0 esta muerto

    Escenario: Dos tributos en lados contrarios se enfrentan y uno de ellos muere
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |t0|sw|  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |t1|
      Cuando se ejecute el juego
      Entonces el distrito 0 es el ganador
      Y t0 tiene una espada

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

    Escenario: Un tributo NO logra aliarse con un tributo neutro
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

      Escenario: Dos tributos del mismo distrito se encuentran en el mapa y se ignoran
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
      Entonces la vida de a0 es 50
      Y la vida de b0 es 50
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

    Escenario: Dos tributos neutros se encuentran en el mapa y se ignoran
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


    Escenario: Tributo encuentra un item de curacion y la utiliza
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |t0|pl|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Y la vida maxima de t0 es 60
      Cuando se ejecuta una iteracion
      Entonces t0 estara en (2,2)
      Y pl desaparece del mapa
      Y la vida de t0 es 60

    Escenario: Tributo encuentra una pocion de curación y no le aplica su efecto
      Dado que el tablero de juego es el siguiente
        |0 |1 |2 |3 |4 |5 |6 |7 |
        |  |  |  |  |  |  |  |  |
        |  |  |t0|  |  |  |  |  |
        |  |  |pl|  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
        |  |  |  |  |  |  |  |  |
      Y la vida maxima de t0 es 50
      Cuando se ejecuta una iteracion
      Entonces t0 estara en (2,2)
      Y pl desaparece del mapa
      Y la vida de t0 es 50

    Escenario: Tributo encuentra una pocion de fuerza y la utiliza
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |t0|pf|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecuta una iteracion
      Entonces t0 estara en (2,2)
      Y pf desaparece del mapa
      Y la fuerza de t0 es 10

    Escenario: Tributo encuentra una pocion de veneno y la utiliza
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |t0|po|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecuta una iteracion
      Entonces t0 estara en (2,2)
      Y po desaparece del mapa
      Y la vida de t0 es 45



    Escenario: Tributo que no tiene arma encuentra una arma y la recoge
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
      Entonces la fuerza de t0 es 10
      Y w desaparece del mapa
      Y t0 estara en (2,3)


    Escenario: Tributo que tiene arma encuentra una arma y NO la recoge
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

    Escenario: Tributo ignora el arma y pelea con otro tributo
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
      Cuando se ejecuta una iteracion
      Entonces la posicion de t0 es (3,2)
      Y w estara (2,3)
      Y la vida de t0 es 45
