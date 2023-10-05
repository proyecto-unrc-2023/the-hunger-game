# language: es

Característica: Movimiento de un tributo
  Antecedentes: juego creado e iniciar un juego
     Dado que un juego fue creado
  Esquema del escenario: Un tributo se mueve por un tablero de 4x4
    Dado que tributo se encuentra en la posición <f> <c>
    Cuando se mueve hacia "<direccion>"
    Entonces tributo se mueve hacia la posición <res1> <res2>
    Ejemplos:
      | f | c |  direccion  |  res1   | res2 |
      | 0 | 3 |   diagonal  |   1     |  3   |
      | 3 | 0 |   diagonal  |   3     |  1   |
      | 0 | 0 |   derecha   |   0     |  1   |
      | 2 | 2 |   derecha   |   2     |  3   |
