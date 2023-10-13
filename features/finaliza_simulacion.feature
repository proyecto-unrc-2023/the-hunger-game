# language: es

Característica: Finalización de la simulación

  Escenario: Termina la simulación
    Dado que hay dos distritos con sus respectivos tributos en el mapa
    Cuando solo quedan tributos de un distrito
    Entonces el distrito sobreviviente gana

  Escenario: Finalizar la simulación intencionalmente
    Dado que la simulación ha comenzado
    Cuando hago clic en "Finalizar simulación"
    Entonces la simulación termina
    Y se muestra el distrito ganador
    Y se muestra la pantalla de inicio