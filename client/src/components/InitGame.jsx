import React from 'react';
import "./InitGame.css";

const InitGame = ({ onViewChange }) => {
  const handlePlayGame = () => {
    onViewChange("menu"); // Llamando a la función proporcionada desde App
  };

  return (
    <div className="init-render">
      <div className="video">
        <video width="auto" height="646" autoPlay muted loop playsInline>
          <source src="/video.mp4" type="video/mp4"/>
        </video>
      </div>
      <button className='button-play-game' onClick={handlePlayGame}>PLAY GAME</button>
    </div>
  );
};

export default InitGame;
