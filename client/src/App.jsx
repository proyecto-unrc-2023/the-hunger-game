import React, { useState, useEffect } from 'react';
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

  useEffect(() => {
    const checkAuthentication = async () => {
      const storedToken = localStorage.getItem('access_token');

      if (storedToken) {
        try {
          const response = await fetch('http://localhost:5000/game/login', {
            headers: {
              'Authorization': `Bearer ${storedToken}`
            }
          });

          if (response.ok) {
            setIsLoggedIn(true);
            setCurrentView('init');
          } else {
            setIsLoggedIn(false);
          }
        } catch (error) {
          console.error('Error al verificar la autenticación:', error);
        }
      }
    };

    checkAuthentication();
  }, []);
  
  const views = {
    init: () => <InitGame onViewChange={handleViewChange} isLoggedIn={isLoggedIn} onLogout={handleLogin} />,
    menu: () => <Menu onViewChange={handleViewChange} />,
    game: () => <Game onViewChange={handleViewChange} />,
    finish: () => <WinnerScreen onViewChange={handleViewChange} />,
    register: () => <Register onViewChange={handleViewChange} isLoggedIn={isLoggedIn} />,
    login: () => <Login onLogin={handleLogin} onViewChange={handleViewChange} isLoggedIn={isLoggedIn} />,
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
