import React, { useState, useEffect, memo, useRef } from 'react';
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

  //Tamaño del tablero
  const [boardSize, setBoardSize] = useState(20);

  //Estado del tablero
  const [boardState, setBoardState] = useState([]);

  //Estado de la simulación
  const [isPaused, setPaused] = useState(true);

  //Estado ganador
  const [winner, setWinner] = useState(null);

  // Pone pausa o reanuda la simulación
  const handlePause = () => {
    setPaused(!isPaused);
  };

  const [gameID, setGameID] = useState(123);

  const handleFinish = async () => {
    const response = await fetch(`http://localhost:5000/game/${gameID}`, {
      method: 'PUT',
    });

    if (response.ok) {
      const data = await response.json();
      const gameData = Object.values(data)[0];
      if (gameData && gameData.board) {
        setBoardState(gameData.board.board);
        setBoardSize(gameData.board.rows); 
      } else {
        console.error('La estructura de datos es incorrecta:', data);
      }
      // setWinner(data.winner);
    } else {
      console.error('Error al finalizar el juego');
    }
    
    setPaused(true);
  };

  useEffect(() => {
    // Realizar el PUT al principio
    
    const fetchGameInfo = async () => {
      try {
        const response = await fetch(`http://localhost:5000/game/${gameID}/next_iteration`);
        if (response.ok) {
          const data = await response.json();
          const gameData = Object.values(data)[0];
          setBoardState(gameData.board.board);
        } else {
          // Manejar errores de la solicitud, si es necesario
        }
      } catch (error) {
        console.error("Error fetching game information:", error);
      }
    };

    // Actualizar la información del juego cada 500 ms si no está pausado
    const intervalId = setInterval(() => {
      if (!isPaused) {
        fetchGameInfo();
      }
    }, 500);

    // Limpiar el intervalo cuando el componente se desmonta o el juego se pausa
    return () => clearInterval(intervalId);

  }, [gameID, isPaused]);

  // const [selectedCell, setSelectedCell] = useState(null);

  // Función para manejar clics en las celdas
  // const handleCellClick = (row, col) => {
  //   const clickedCell = boardState[row][col];
  //   setSelectedCell({
  //     row,
  //     col,
  //     type: clickedCell,
  //     // Puedes agregar más información aquí según sea necesario
  //   });
  // };  

  // Tablero de prueba 1
  const testBoardState = Array.from({ length: boardSize }, () => Array(boardSize).fill('  '));
  // Probando posiciones iniciales
  testBoardState[4][4] = 't0';
  testBoardState[9][17] = 't1';
  testBoardState[19][1] = 't2';
  testBoardState[8][8] = 'pl';
  testBoardState[5][15] = 'pp';
  testBoardState[1][15] = 'ow';
  testBoardState[7][13] = 'sw';
  testBoardState[14][1] = 'sp';

  // Tablero de prueba 2
  const test2BoardState = Array.from({ length: boardSize }, () => Array(boardSize).fill('  '));
  test2BoardState[4][5]  = 't0';
  test2BoardState[8][16] = 't1';
  test2BoardState[18][2] = 't2';
  test2BoardState[8][8]  = 'pl';
  test2BoardState[5][15] = 'pp';
  test2BoardState[1][15] = 'ow';
  test2BoardState[7][13] = 'sw';
  test2BoardState[14][1] = 'sp';

  console.log('boardState:', boardState);
  // Tablero vacío
  const emptyBoard = Array.from({ length: boardSize }, () => Array(boardSize).fill('free'));
  return (
    <main className="game">
      <TransformWrapper minScale={0.5}>
        <div className='button-section'><ControlsZoom /></div>
        <TransformComponent>
          <section className='board'>
            {winner ? (
              <div className="winner-message">Ha ganado el {winner}
              <Board boardSize={boardSize} boardState={emptyBoard} /></div>
            ) : ( <Board boardSize={boardSize} boardState={test2BoardState}/>
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
