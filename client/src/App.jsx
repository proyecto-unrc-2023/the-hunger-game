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
 
  const handleViewChange = (view) => {
    setCurrentView(view);
  };

  const views = {
    init: InitGame,
    menu: Menu,
    game: Game,
    finish: WinnerScreen,
    register: Register,
    login: Login,
    rules: Rules,
    about: About,
  };

  const CurrentViewComponent = views[currentView];

  return (
    <div className='app'>
      <CurrentViewComponent onViewChange={handleViewChange} />
    </div>
  );
};

export default App;
