import React from 'react';
import './WinnerScreen.css';
import { useGame } from "./GameContext";

const WinnerScreen = ({ onViewChange }) => {
    const handleRestartGame = () => {
      onViewChange("menu"); // Llamando a la función proporcionada desde App
    };

    const characters = {
      0: '/board-images/characters/Minotaur_Walking_1.png',
      1: '/board-images/characters/Fallen_Angels_Walking_1.png',
      2: '/board-images/characters/Golem_Walking_1.png',
      3: '/board-images/characters/Goblin_Walking_1.png',
      4: '/board-images/characters/Orc_Walking_1.png',
      5: '/board-images/characters/Reaper_Man_Walking_1.png',
    };

    const { winnerCharacter } = useGame();
  
    return (
      <div className="winner-screen">
        <img src={characters[winnerCharacter]} ></img>
        <button className='button-restart-game' onClick={handleRestartGame}>Restart Game</button>
        <button className='button-save-game' >Save Game</button>
      </div>
    );
  };
  
  export default WinnerScreen;