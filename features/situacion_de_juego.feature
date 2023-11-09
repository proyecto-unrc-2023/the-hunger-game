# language: es
  Característica: Situacion de juego

    Antecedentes:
      Dado que el juego se ha creado
      Y que la vida inicial de todos los tributos es 50
      Y que la vida maxima por defecto de todos los tributos es 50
      Y que la vida de n0, n1, n2 es 50 y no pertenecen a ningun distrito
      Y que la fuerza de todos los tributos es 5
      Y luego que se muevan todos los tributos en el tablero, se mueven los neutros
      Y todos los tributos que compartan el mismo valor numerico (por ejemplo a1,b1) pertenecen al mismo distrito (Excepcion para la n)


    Esquema del escenario: Enfrentamiento entre 2 tributos
      Dado que el tablero de juego es el siguiente
      |0  |1  |2  |3  |4  |5  |6  |7  |
      |   |   |   |   |   |   |   |   |
      |   |<a>|<b>|   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      Y t0 y t1 no tienen arma
      Cuando se ejecuta una iteracion
      Entonces la vida de <a> es <v0>
      Y la vida de <b> es <v1>
      Ejemplos:
      | a  | v0 | b  | v1 |
      | t0 | 45 | t1 | 45 |


    Esquema del escenario: Enfrentamiento entre un tributo con lanza y otro sin arma
      Dado que el tablero de juego es el siguiente
      |0  |1  |2  |3  |4  |5  |6  |7  |
      |   |   |   |   |   |   |   |   |
      |   |<a>|   |<b>|   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      Y <a> tiene una lanza
      Y la vida de <b> es <v2>
      Y la vida de <a> es <v3>
      Cuando se ejecuta una iteracion
      Entonces <a> tiene vida <v0>
      Y <b> tiene vida <v1>
      Ejemplos:
      |a  |b  |v0 |v1 |v2 |v3 |
      |t0 |t1 |50 |42 |50 |50 |
      |t0 |t1 |50 |0  |8  |50 |


    Esquema del escenario: Enfrentamiento entre un tributo con arco y otro sin arma
      Dado que el tablero de juego es el siguiente
      |0  |1  |2  |3  |4  |5  |6  |7  |
      |   |   |   |   |   |   |   |   |
      |   |<a>|   |   |<b>|   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      Y <a> tiene un arco
      Y la vida de <b> es <v2>
      Y la vida de <a> es <v3>
      Cuando se ejecuta una iteracion
      Entonces <a> tiene vida <v0>
      Y <b> tiene vida <v1>
      Ejemplos:
      |a  |b  |v0 |v1 |v2 |v3 |
      |t0 |t1 |50 |44 |50 |50 |
      |t0 |t1 |50 |0  |6  |50  |


    Esquema del escenario: Un tributo consigue un arma durante un enfrantamiento
      Dado que el tablero de juego es el siguiente
      |0  |1  |2  |3  |4  |5  |6  |7  |
      |   |   |   |   |   |   |   |   |
      |   |<a>|<g>|<b>|   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      Cuando se ejecuta una iteracion
      Entonces <a> tiene vida <v0>
      Y <b> tiene vida <v1>
      Y <a> tiene el arma <g>
      Ejemplos:
      |a |b |v0 |v1 |g  |
      |t0|t1|45 |50 |sp |
      |t0|t1|45 |50 |wo |
      |t0|t1|45 |50 |sw |


    Esquema del escenario: Un tributo con arma se enfrenta a uno sin arma
      Dado que el tablero de juego es el siguiente
      |0  |1  |2  |3  |4  |5  |6  |7  |
      |   |   |   |   |   |   |   |   |
      |   |<a>|<b>|   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      Y <a> tiene el arma <g>
      Y la vida de <b> es <v2>
      Y la vida de <a> es <v3>
      Cuando se ejecuta una iteracion
      Entonces <a> tiene vida <v0>
      Y <b> tiene vida <v1>
      Ejemplos:
      |a |b |v0 |v1 |v2 |v3 |g  |
      |t0|t1|45 |40 |50 |50 |sw |
      |t0|t1|45 |42 |50 |50 |sp |
      |t0|t1|45 |44 |50 |50 |wo |
      |t0|t1|50 |0  |5  |50 |wo |


    Esquema del escenario: Un tributo utiliza o ignora un item
      Dado que el tablero de juego es el siguiente
      |0  |1  |2  |3  |4  |5  |6  |7  |
      |   |   |   |   |   |   |   |   |
      |   |<a>|<i>|   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      Y <a> tiene una vida maxima <mv0>
      Y <a> tiene arma <state>
      Cuando se ejecuta una iteracion
      Entonces <a> tiene vida <v0>
      Y <a> tiene fuerza <f0>
      Y el item <i> tiene un estado <status>
      Ejemplos:
      |a |v0 |mv0 |f0 |i  |status |state |
      |t0|50 |50  |5  |pl |used   |False |
      |t0|60 |60  |5  |pl |used   |False |
      |t0|45 |50  |5  |po |used   |False |
      |t0|50 |50  |10 |pf |used   |False |
      |t0|50 |50  |10 |sw |used   |False |
      |t0|50 |50  |5  |sw |unused |True  |


    Esquema del escenario: Un tributo le propone alianza a un tributo neutro
      Dado que el tablero de juego es el siguiente
      |0  |1  |2  |3  |4  |5  |6  |7  |
      |   |   |   |   |   |   |   |   |
      |   |<b>|<n>|   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      Y <b> tiene un valor de alianza <al1>
      Y <b> le ofrece una alianza a <n>
      Cuando <n> decida el resultado de la alianza con el districto <d1>
      Entonces el resultado es <alliance>
      Y el distrito <d1> tiene <ct> tributos
      Y la cantidad de tributos neutros es <ctn>
      Ejemplos:
      |b |al1|n  |alliance |d1 |ct |ctn |
      |t0|25 |n0 |accept   |0  |2  |0   |
      |t0|1  |n0 |reject   |0  |1  |1   |

    Esquema del escenario: Dos tributos se ignoran
      Dado que el tablero de juego es el siguiente
      |0  |1  |2  |3  |4  |5  |6  |7  |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |<a>|<b>|   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      |   |   |   |   |   |   |   |   |
      Cuando se ejecuta una iteracion
      Entonces <a> tiene vida <v0>
      Y <b> tiene vida <v1>
      Y la posicion de <a> debe ser distinta a (2,1)
      Y la posicion de <b> debe ser distinta a (2,2)
      Ejemplos:
      |a |b |v0|v1|
      |a0|t0|50|50|
      |n0|n1|50|50|

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
      Entonces t1 desaparece del mapa
      Y el distrito 1 tiene un tributo menos


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


    Esquema del escenario: Un tributo es atacado por dos tributos del mismo distrito
      Dado que el tablero de juego es el siguiente
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |a0|  |  |  |  |  |  |
      |  |  |t1|  |  |  |  |  |
      |  |  |b0|  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      Cuando se ejecuta una iteracion
      Entonces <a> tiene en su rango de ataque a <b>
      Y la vida de <a> es <l1>
      Ejemplos:
      | a  | b  | l1 |
      | a0 | t1 | 50 |
      | b0 | t1 | 45 |
      | t1 | b0 | 40 |


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
