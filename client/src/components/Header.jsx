import React from 'react';
import './Header.css';

const Header = ({ districtChosed, districtsLive }) => {

  const handleLogoClick = () => {
    // Redirige a la página de inicio (recarga la página)
    window.location.href = '/';
  };

  return (
    <header className='header'>
      <a href="/" onClick={handleLogoClick} className='a-logo'>
        <img src='./11-2-the-hunger-games-picture.png' className='logo-img' alt='logo'></img>
      </a>
      <div className='top-header'>
      <section className="game-title">
        <div className="top">The Hunger Games</div>
        <div className="bottom" aria-hidden="true">The Hunger Games</div>
      </section>
        {districtChosed && (
        <div className='districts-info'>
          <div className='district-chosed'>{`District: ${districtChosed}`}</div>
          <div className='districts-live'>{`Districts live: ${districtsLive}`}</div>
        </div>
        )}
      </div>
      <div className='login'>
        <button className="cssbuttons-io-button">
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
