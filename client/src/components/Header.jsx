import React, { useState, useRef } from 'react';
import './Header.css';

const Header = ({ onViewChange }) => {
  
  const handleLogoClick = () => {
    // Redirige a la página de inicio (recarga la página)
    window.location.href = '/';
  };

  const [volume, setVolume] = useState(0.2); 
  const audioRef = useRef(new Audio('/audio.mp3'));
  const [isVolumeVisible, setIsVolumeVisible] = useState(false);
  const volVisble = isVolumeVisible ? 'volume-button-on' : 'volume-button-off';

  const handleToggleVolume = () => {
    setIsVolumeVisible(!isVolumeVisible);
  };

  const handleVolumeChange = (event) => {
    const newVolume = parseFloat(event.target.value);
    audioRef.current.volume = newVolume;
    setVolume(newVolume);
  };

  const handleLoginClick = () => {
    onViewChange("login");
  };

  return (
    <header className='header'>
      <a href="/" onClick={handleLogoClick} className='a-logo'>
        <img src='./11-2-the-hunger-games-picture.png' className='logo-img' alt='logo'></img>
      </a>
      <div className='audio-container'>
        <audio ref={audioRef} autoPlay loop>
          <source src='/audio.mp3' type="audio/mp3" />
        </audio>
        <button 
          className={volVisble}
          onClick={handleToggleVolume}
        >🔊
        </button>
        {isVolumeVisible && (
          <input
            type="range"
            min="0"
            max="1"
            step="0.01"
            value={volume}
            onChange={handleVolumeChange}
            className={`volume-slider ${isVolumeVisible ? 'active' : ''}`}
          />
        )}
      </div>
      <div className='top-header'>
        <section className="game-title">
          <div className="top">The Hunger Games</div>
          <div className="bottom" aria-hidden="true">The Hunger Games</div>
        </section>
      </div>
      <div className='container-login-button'>
        <button className="login-button" onClick={() => handleLoginClick()}>
          Login
          <div className="icon">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">
              <path fill="none" d="M0 0h24v24H0z"></path><path fill="currentColor" d="M16.172 11l-5.364-5.364 1.414-1.414L20 12l-7.778 7.778-1.414-1.414L16.172 13H4v-2z"></path></svg>
          </div>
        </button>
      </div>
    </header>
  );
};

export default Header;
