import React, { useState } from 'react';
import Menu from './components/Menu.jsx';
import Game from './components/Game.jsx';
import InitGame from './components/InitGame.jsx';
import WinnerScreen from './components/WinnerScreen.jsx';
import Register from './components/Register.jsx'
import Rules from './components/Rules.jsx'
import About from './components/About.jsx'
import Login from './components/Login.jsx';
import './App.css';

const App = () => {
  const [currentView, setCurrentView] = useState('init');
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  const handleViewChange = (view) => {
    setCurrentView(view);
  };

  const handleLogin = (status) => {
    setIsLoggedIn(status);
  };

  const views = {
    init: () => <InitGame onViewChange={handleViewChange} isLoggedIn={isLoggedIn} />,
    menu: () => <Menu onViewChange={handleViewChange} />,
    game: () => <Game onViewChange={handleViewChange} />,
    finish: () => <WinnerScreen onViewChange={handleViewChange} />,
    register: () => <Register onViewChange={handleViewChange} />,
    login: () => <Login onLogin={handleLogin} onViewChange={handleViewChange} />,
    rules: () => <Rules onViewChange={handleViewChange} />,
    about: () => <About onViewChange={handleViewChange} />,
  };

  const CurrentViewComponent = views[currentView];

  return (
    <div className='app'>
      <CurrentViewComponent />
    </div>
  );
};

export default App;
