# language: es

Característica: Movimiento de un tributo
  
  Escenario: Un tributo se mueve hacia abajo porque se localiza en la posición superior derecha del tablero   
    Dado que un tributo se encuentra en la posición (0, 3)
      |   |   |   | t |
      |   |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
    Cuando el tributo tenga que moverse
    Entonces se moverá hacia abajo a la posición (1, 3)
      |   |   |   |   |
      |   |   |   | t |
      |   |   |   |   |
      |   |   |   |   |

  # escenario 2
  Escenario: Un tributo se mueve hacia la derecha porque se localiza en la posición inferior izquierda del tablero
    Dado que un tributo se encuentra en la posición (3, 0)
      |   |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
      | t |   |   |   |
    Cuando el tributo se mueva
    Entonces se moverá hacia la derecha a la posición (3, 1)
      |   |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
      |   | t |   |   |

  # escenario 3
  Escenario: Un tributo se mueve en diagonal porque se localiza en la posición superior izquierda del tablero
    Dado que un tributo se encuentra en la posición (0, 0)
      | t |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
    Cuando el tributo tenga que avanzar
    Entonces avanzará en diagonal hacia la posición (1, 1)
      |   |   |   |   |
      |   | t |   |   |
      |   |   |   |   |
      |   |   |   |   |

  # escenario 4
  Escenario: Un tributo se mueve hacia arriba porque se localiza en el borde inferior del tablero
    Dado que un tributo se encuentra en la posición (3, 2)
      |   |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
      |   |   | t |   |
    Cuando el tributo avance
    Entonces avanzará hacia arriba a la posición (2, 2)
      |   |   |   |   |
      |   |   |   |   |
      |   |   | t |   |
      |   |   |   |   |

  # escenario 5
  Escenario: Un tributo se mueve hacia la izquierda porque se localiza en el borde superior del tablero
    Dado que un tributo se encuentra en la posición (0, 2)
      |   |   | t |   |
      |   |   |   |   |
      |   |   |   |   |
      |   |   |   |   |
    Cuando cuando realice un movimiento
    Entonces se moverá hacia la izquierda a la posición (0, 1)
      |   | t |   |   |
      |   |   |   |   |
      |   |   |   |   |
      |   |   |   |   |

  # escenario 6
  Escenario: Un tributo se mueve sin estar en los límites del tablero
    Dado que un tributo se encuentre en la posición (2, 1) 
    Y no es adyacente a otro tributo
    Y no se encuentra en la misma celda que un ítem
      |    |    |    |    |
      |    |    |    | t2 |
      |    | t1 |    |    |
      |    |    |    |  i |
    Cuando se ejecute un paso de iteración
    Entonces se moverá a una celda adyacente disponible (1, 1)
      |    |    |    |    |
      |    | t1 |    | t2 |
      |    |    |    |    |
      |    |    |    |  i |
