import React, { useState, useEffect, memo } from 'react';
import {
  TransformWrapper,
  TransformComponent,
  useControls
} from "react-zoom-pan-pinch";
import Board from "./Board.jsx";

const ControlsZoom = () => {
  const { zoomIn, zoomOut, resetTransform } = useControls();
  return (
    <>
      <button onClick={() => zoomIn()}>🔍+</button>
      <button onClick={() => zoomOut()}>🔍-</button>
      <button onClick={() => resetTransform()}>↩️</button>
    </>
  );
};

const ControlsAdvance = memo(({ onPause, onFinish }) => {
  return (
    <>
      <button onClick={onPause}>Pause⏯️</button>
      <button onClick={onFinish}>Finish</button>
    </>
  );
});

const Game = () => {
  const size = 20;
  // Tablero de prueba 1
  const testBoardState = Array.from({ length: size }, () => Array(size).fill('free'));
  // Probando posiciones iniciales
  testBoardState[4][4] = 'tribute';
  testBoardState[9][17] = 'tribute';
  testBoardState[19][1] = 'tribute';
  testBoardState[8][8] = 'potion';
  testBoardState[5][15] = 'potion';
  testBoardState[1][15] = 'bow';
  testBoardState[7][13] = 'sword';
  testBoardState[14][1] = 'sword';

  // Tablero de prueba 2
  const test2BoardState = Array.from({ length: size }, () => Array(size).fill('free'));
  test2BoardState[4][5] = 'tribute';
  test2BoardState[8][16] = 'tribute';
  test2BoardState[18][2] = 'tribute';
  test2BoardState[8][8] = 'potion';
  test2BoardState[5][15] = 'potion';
  test2BoardState[1][15] = 'bow';
  test2BoardState[7][13] = 'sword';
  test2BoardState[14][1] = 'sword';

  // Tablero vacío
  const emptyBoard = Array.from({ length: size }, () => Array(size).fill('free'));

  //Estado del tablero
  const [boardState, setBoardState] = useState(testBoardState);

  //Estado de la simulación
  const [isPaused, setPaused] = useState(true);

  //Estado ganador
  const [winner, setWinner] = useState(null);

  // Pone pausa o reanuda la simulación
  const handlePause = () => {
    setPaused(!isPaused);
  };

  const handleFinish = () => {
    const winningDistrict = Math.random() < 0.5 ? 'Distrito 1' : 'Distrito 2';
    setWinner(winningDistrict);
    // Pausa para que no quede iterando
    setPaused(true);
    // Finaliza la simulación, deja el último tablero y da al ganador
  };

  const [selectedCell, setSelectedCell] = useState(null);

  // Función para manejar clics en las celdas
  const handleCellClick = (row, col) => {
    const clickedCell = boardState[row][col];
    setSelectedCell({
      row,
      col,
      type: clickedCell,
      // Puedes agregar más información aquí según sea necesario
    });
  };

  // Configuración de tiempo y estados para la actualización de los tableros
  useEffect(() => {
    let time;
  
    // Función para alternar entre estados del tablero
    const toggleBoardState = () => {
      setBoardState((prevBoardState) =>
        prevBoardState === testBoardState ? test2BoardState : testBoardState
      );
    };
  
    // Iniciar tiempo para alternar el tablero cada 500 ms
    if (!isPaused) {
      time = setInterval(toggleBoardState, 500);
    }
  
    // Limpiar el tiempo cuando el juego se pausa
    return () => clearInterval(time);
    // esto para que no joda el warning jaja
    // eslint-disable-next-line react-hooks/exhaustive-deps 
  }, [isPaused]);

  return (
    <main className="game">
      <TransformWrapper minScale={0.5}>
        <div className='button-section'><ControlsZoom /></div>
        <TransformComponent>
          <section className='board'>
            {winner ? (
              <div className="winner-message">Ha ganado el {winner}
              <Board size={size} boardState={emptyBoard} /></div>
            ) : ( <Board size={size} boardState={boardState} onCellClick={handleCellClick}/>
            )}
          </section>
        </TransformComponent>
      </TransformWrapper>
      <div className="button-section">
        <ControlsAdvance onPause={handlePause} onFinish={handleFinish} />
      </div>
    </main>
  );
};
export default Game;
