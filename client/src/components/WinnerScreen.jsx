import React from 'react';
import './WinnerScreen.css';

const WinnerScreen = ({ onViewChange }) => {
    const handleRestartGame = () => {
      onViewChange("menu"); // Llamando a la función proporcionada desde App
    };
  
    return (
      <div className="winner-screen">
        <button className='button-restart-game' onClick={handleRestartGame}>Restart Game</button>
        <button className='button-save-game' >Save Game</button>
      </div>
    );
  };
  
  export default WinnerScreen;