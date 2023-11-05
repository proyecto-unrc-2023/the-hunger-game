import React, { useState } from 'react';
import Header from './components/Header.jsx';
import Footer from './components/Footer.jsx';
import Menu from './components/Menu.jsx';
import Game from './components/Game.jsx';
import InitGame from './components/InitGame.jsx';
import WinnerScreen from './components/WinnerScreen.jsx';
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
  };

  const CurrentViewComponent = views[currentView];

  return (
    <div className='app'>
      <CurrentViewComponent onViewChange={handleViewChange} />
    </div>
  );
};

export default App;
