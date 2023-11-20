import React from 'react';
import "./InitGame.css";
import Header from './Header.jsx';
import Footer from './Footer.jsx';
const InitGame = ({ onViewChange, isLoggedIn }) => {
  const handlePlayGame = () => {
    onViewChange("menu"); // Llamando a la función proporcionada desde App
  };

  const handleViewRules = () => {
    onViewChange("rules");
  };

  const handleViewAbout = () => {
    onViewChange("about");
  };

  return (
    <div className="init-render">
      <Header onViewChange={onViewChange} /> 
      <div className="video">      
        <video className='video-init' autoPlay muted loop playsInline>
          <source src="/video.mp4" type="video/mp4"/>
        </video>
      </div> 
      <button className='button-play-game' onClick={handleViewRules}>GAME RULES</button>
      <button
        className={`button-play-game ${isLoggedIn ? '' : 'disabled'}`}
        onClick={handlePlayGame}
        disabled={!isLoggedIn}
      >
        PLAY GAME
      </button>
      <button className='button-play-game' onClick={handleViewAbout}>ABOUT GAME</button>
      <Footer onViewChange={onViewChange} /> 
    </div>
  );
};

export default InitGame;
