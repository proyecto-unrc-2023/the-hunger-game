import React, { useState, useEffect, memo } from 'react';
import {
  TransformWrapper,
  TransformComponent,
  useControls
} from "react-zoom-pan-pinch";
import Board from "./Board.jsx";
import { useGame } from "./GameContext";

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
  const [winner, setWinner] = useState(null);
  
  //Estado del juego
  const [gameInitialized, setGameInitialized] = useState(false);

  //Estado para regular el fetch
  const [fetchGameData, setFetchGameData] = useState(true);

  //Estado para obtener el id del juego actual, se obtiene de un contexto
  const { gameID } = useGame();

  // Pone pausa o reanuda la simulación
  const handlePause = () => {
    setPaused(!isPaused);
  };

  const handleFinish = () => {
    //debe devolver el ganador
    onViewChange("finish");
  }

  // Tablero vacío
  const emptyBoard = Array.from({ length: boardSize }, () => Array(boardSize).fill('  '));
  
  // Crea un juego
  const initialBoard = async () => {
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
  }

  // Actualiza el juego creado 
  const fetchGameInfo = async () => {
    try {
      if (fetchGameData && winner === null) {
        const response = await fetch(`http://localhost:5000/game/${gameID}`, {
          method: 'GET',
        });
        if (response.ok) {
          const data = await response.json();
          const gameData = Object.values(data)[0];
          setBoardState(gameData.board.board);
          setBoardSize(gameData.board.rows);
          
          if (gameData.winner !== null) {
            setFetchGameData(false);
            setWinner(gameData.winner);
          }
        }
      }
    } catch (error) {
      console.error("Error fetching game information:", error);
    }
  };
 
  // Crea un juego si es necesario y se encarga de actualizarlo cada cierto intervalo
  useEffect(() => {
    if (gameID !== null){
      if (!gameInitialized) {
        initialBoard();
      }
    }
    
    const time = setInterval(() => {
      if (!isPaused) {
        fetchGameInfo();
      }
    }, 500);

    // Limpiar el intervalo cuando el componente se desmonta o el juego se pausa
    return () => clearInterval(time);
  
  }, [gameID, isPaused, gameInitialized, winner]);

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
