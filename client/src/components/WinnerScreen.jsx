import React from 'react';
import './WinnerScreen.css';
import "./Common.css";
import { useGame } from "./GameContext";

const WinnerScreen = ({ onViewChange }) => {
    const handleRestartGame = () => {
      onViewChange("menu"); // Llamando a la función proporcionada desde App
    };

    const { characters } = useGame();

    const { winnerCharacter } = useGame();
  
    return (
      <div className="winner-screen">
        <div className="winner-container">
          <div className='winner-card'><h2>DISTRICT {winnerCharacter} WON</h2></div>
          <img className = "winner-img" src={characters[winnerCharacter]} ></img>
        </div>
        <div className="restart-save-container">
          <button className='button-restart-game' onClick={handleRestartGame}>Restart Game</button>
          <button className='button-save-game' >Save Game</button>
        </div>
      </div>
    );
  };
  
  export default WinnerScreen;