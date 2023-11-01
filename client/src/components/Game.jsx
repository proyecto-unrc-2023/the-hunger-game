import React, { useState, useEffect, memo } from 'react';
import {
  TransformWrapper,
  TransformComponent,
  useControls
} from "react-zoom-pan-pinch";
import Board from "./Board.jsx";
// import InfoPanel from './components/InfoPanel.jsx';

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

const Game = ({onViewChange}) => {

  //Tamaño del tablero
  const [boardSize, setBoardSize] = useState(20);

  //Estado del tablero
  const [boardState, setBoardState] = useState([]);

  //Estado de la simulación
  const [isPaused, setPaused] = useState(true);
  
  //Estado ganador
  // const [winner, setWinner] = useState(null);

  // Pone pausa o reanuda la simulación
  const handlePause = () => {
    setPaused(!isPaused);
  };

  const [gameInitialized, setGameInitialized] = useState(false)

  const handleFinish = () => {
    //debe devolver el ganador
    //setWinner
    onViewChange("finish");
  }
  
  const [gameID, setGameID] = useState(0);

  const getLastId = async () => {
    try {
      const response = await fetch(`http://localhost:5000/game/last_id`, {
        method: 'GET',
      });
  
      if (response.ok) {
        const data = await response.json();
        setGameID(data.game_id);
      } else {
        console.error('Error al obtener el último game_id');
      }
    } catch (error) {
      console.error('Error en la solicitud de getLastId:', error);
    }
  };
  
  // Tablero vacío
  const emptyBoard = Array.from({ length: boardSize }, () => Array(boardSize).fill('  '));
  
  
  const initialBoard = async () => {
    getLastId();
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
    } else {
      console.error('Error al finalizar el juego');
    }
    setGameInitialized(true);
    setPaused(true);
  };
 

  useEffect(() => {
    if (!gameInitialized) {
      initialBoard();
    }
    const fetchGameInfo = async () => {
      try {
        const response = await fetch(`http://localhost:5000/game/${gameID}`, {
          method: 'GET',
        });
        if (response.ok) {
          const data = await response.json();
          const gameData = Object.values(data)[0];
          setBoardState(gameData.board.board);
          setBoardSize(gameData.board.rows)
        } else {
          // Manejar errores de la solicitud, si es necesario
        }
      } catch (error) {
        console.error("Error fetching game information:", error);
      }
    };

    // Actualizar la información del juego cada 500 ms si no está pausado
    const time = setInterval(() => {
      if (!isPaused) {
        fetchGameInfo();
      }
    }, 500);

    // Limpiar el intervalo cuando el componente se desmonta o el juego se pausa
    return () => clearInterval(time);

  }, [gameID, isPaused, gameInitialized]);
  

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
  
  
  return (
    <main className="game">
      <TransformWrapper minScale={0.5}>
        <div className='button-section'><ControlsZoom /></div>
        <TransformComponent>
          <section className='board'>
            {!gameInitialized ? (
              <Board boardSize={boardSize} boardState={emptyBoard} />
              ) : ( <Board size={boardSize} boardState={boardState} />
              )}
          </section>
        </TransformComponent>
      </TransformWrapper>
      <div className="button-section">
        <ControlsAdvance onPause={handlePause}  onFinish={handleFinish}/>
      </div>
    </main>
  );
};
export default Game;
