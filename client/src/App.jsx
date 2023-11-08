import React, { useState } from 'react';
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
