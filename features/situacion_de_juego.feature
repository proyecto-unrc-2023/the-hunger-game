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

    Esquema del escenario: Dos tributos luchan y uno de ellos encuentra un item de curacion
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
      Entonces <a> esta en la posicion <x> <y>
      Y la vida de <a> es <l1>
      Ejemplos:
      | a  | l1 | x | y |
      | t0 | 45 | 2 | 2 |
      | t1 | 50 | 1 | 2 |


    Esquema del escenario: Tres tributos luchan
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
      Y <a> tiene en su rango de ataque a <b>
      Cuando se ejecuta una iteracion
      Entonces la vida de <a> es <l1>
      Ejemplos:
      | a  | b  | l1 |
      | t0 | t2 | 40 |
      | t1 | t0 | 50 |
      | t2 | t0 | 45 |



    Esquema del escenario: : Dos tributos luchan y llega un aliado
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
      Entonces <a> tiene en su rango de ataque a <b>
      Y la vida de <a> es <l1>
      Ejemplos:
      | a  | b  | l1 |
      | a0 | t1 | 50 |
      | b0 | t1 | 40 |
      | t1 | b0 | 35 |

    Esquema del escenario: Enfrentamiento entre 2 tributos
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
      Entonces la vida de <a> es <l1>
      Ejemplos:
      | a  | l1 |
      | t0 | 45 |
      | t1 | 45 |

    Esquema del escenario: Enfrentamiento entre 2 tributos
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
      Cuando se ejecuten 2 iteraciones
      Entonces la vida de <a> es <l1>
      Y <a> tiene un arma con rango <range>
      Ejemplos:
      | a  | l1 | range |
      | t0 | 40 |   1   |
      | t1 | 40 |   0   |
      | t2 | 40 |   0   |
      | t3 | 40 |   0   |
      | t4 | 40 |   0   |
      | t4 | 40 |   0   |

    Esquema del escenario: Enfrentamiento entre 2 tributos
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
      Cuando se ejecuten 2 iteraciones
      Entonces <a> tiene un arma con rango <range>
      Y la vida de <a> es <l1>
      Ejemplos:
      | a  | l1 | range |
      | t0 | 50 |   2   |
      | t1 | 42 |   0   |

    Esquema del escenario: Enfrentamiento entre 2 tributos
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
      Cuando se ejecuten 2 iteraciones
      Entonces la vida de <a> es <l1>
      Y <a> tiene un arma con rango <range>
      Ejemplos:
      | a  | l1 | range |
      | t0 | 50 |   3   |
      | t1 | 44 |   0   |



    Esquema del escenario: Un tributo huye de un combate
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
      Y <a> esta en la posicion <x> <y>
      Ejemplos:
      | a | x | y |
      |t0 | 3 | 0 |


    Esquema del escenario: Tributo con mayor fuerza inflige mayor daño a otro tributo con menor fuerza en combate
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
      Entonces la vida de <a> es <l1>
      Ejemplos:
      | a  | l1 |
      | t0 | 45 |
      | t1 | 40 |

    Esquema del escenario: Se producen dos luchas al mismo tiempo
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
      Y <a> tiene un arma con rango <range>
      Ejemplos:
      | a | range |
      |t0 |   1   |
      |t1 |   0   |
      |t2 |   0   |
      |t3 |   0   |


    Esquema del escenario: Dos tributos luchan a muerte y uno de ellos tiene un arco
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
      Y <a> tiene un arma con rango <range>
      Ejemplos:
      | a | range |
      |t0 |   3   |
      |t1 |   0   |

    Esquema del escenario: Dos tributos luchan a muerte y uno de ellos tiene una lanza
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
      Y <a> tiene un arma con rango <range>
      Ejemplos:
      | a | range |
      |t0 |   2   |
      |t1 |   0   |

    Esquema del escenario: Dos tributos luchan a muerte y uno de ellos tiene una espada
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
      Y <a> tiene un arma con rango <range>
      Ejemplos:
      | a | range |
      |t0 |   1   |
      |t1 |   0   |

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

    Esquema del escenario: Dos tributos en lados contrarios se enfrentan y uno de ellos muere
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
      Y <a> tiene un arma con rango <range>
      Ejemplos:
      | a  | range |
      | t0 |   1   |
      | t1 |   0   |

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

      Esquema del escenario: Dos tributos del mismo distrito se encuentran en el mapa y se ignoran
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |t0|a0|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecuta una iteracion
      Entonces la vida de <a> es <l1>
      Y la posicion de t0 debe ser distinta a (2,1)
      Y la posicion de a0 debe ser distinta a (2,2)
      Ejemplos:
      | a  | l1 |
      | t0 | 50 |
      | a0 | 50 |


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
      Entonces la vida de neutros sigue igual
      Y la posicion de n0 es distinta a (2,1)
      Y la posicion de n1 es distinta a (2,2)


    Esquema del escenario: Tributo encuentra un item de curacion y la utiliza
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
      Entonces <a> esta en la posicion <x> <y>
      Y pl desaparece del mapa
      Y la vida de <a> es <l1>
      Ejemplos:
      | a | x | y | l1 |
      |t0 | 2 | 2 | 60 |

    Esquema del escenario: Tributo encuentra una pocion de curación y no le aplica su efecto
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
      Entonces <a> esta en la posicion <x> <y>
      Y pl desaparece del mapa
      Y la vida de <a> es <l1>
      Ejemplos:
      | a | x | y | l1 |
      |t0 | 2 | 2 | 50 |



    Esquema del escenario: Tributo encuentra una pocion de fuerza y la utiliza
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
      Entonces <a> esta en la posicion <x> <y>
      Y pf desaparece del mapa
      Y la fuerza de t0 es 10
      Ejemplos:
      | a | x | y |
      |t0 | 2 | 2 |

    Esquema del escenario: Tributo encuentra una pocion de veneno y la utiliza
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
      Entonces <a> esta en la posicion <x> <y>
      Y po desaparece del mapa
      Y la vida de <a> es <l1>
      Ejemplos:
      | a | x | y | l1 |
      |t0 | 2 | 2 | 45 |


    Esquema del escenario: Tributo que no tiene arma encuentra una arma y la recoge
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
      Y <a> esta en la posicion <x> <y>
      Ejemplos:
      | a | x | y |
      |t0 | 2 | 3 |

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

    Esquema del escenario: Tributo ignora el arma y pelea con otro tributo
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
      Entonces <a> esta en la posicion <x> <y>
      Y w estara (2,3)
      Y la vida de <a> es <l1>
      Ejemplos:
      | a | x | y | l1 |
      |t0 | 3 | 2 | 45 |
