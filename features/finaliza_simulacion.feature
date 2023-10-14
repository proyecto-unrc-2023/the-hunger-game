# language: es

Característica: Finalización de la simulación

  Escenario: Termina la simulación
    Dado que el tablero se encuentra en el siguiente estado
      |0 |1 |2 |3 |4 |5 |6 |7 |
      |  |  |  |  |  |  |  |  |
      |  |  |a0|  |  |  |  |  |
      |  |t0|  |  |  |  |c0|  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |  |  |  |  |  |
      |  |  |  |b0|  |  |  |  |
      |  |  |  |  |  |  |  |  |
    Cuando se ejecute la ultima iteracion
    Entonces el unico distrito sobreviviente gana la partida