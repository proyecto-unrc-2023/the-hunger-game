import React, { useState } from 'react';
import Header from './components/Header.jsx';
import Footer from './components/Footer.jsx';
import Menu from './components/Menu.jsx';
import Game from './components/Game.jsx';
import InitGame from './components/InitGame.jsx';
import WinnerScreen from './components/WinnerScreen.jsx';

const App = () => {
  const [currentView, setCurrentView] = useState('init');
  const [selectedCharacter, setSelectedCharacter] = useState(null);
  
  const handleCharacterSelection = (characterKey) => {
    setSelectedCharacter(characterKey);
  };

  const handleViewChange = (view) => {
    setCurrentView(view);
  };

  const views = {
    init: InitGame,
    menu: () => <Menu onSelect={handleCharacterSelection} onViewChange={handleViewChange}/>,
    game: () => <Game selectedCharacter={selectedCharacter} onViewChange={handleViewChange}/>,
    finish: WinnerScreen,
  };
  

  const CurrentViewComponent = views[currentView];

  return (
    <div className='app'>
      <Header />
      <CurrentViewComponent onViewChange={handleViewChange} />
      <Footer />
    </div>
  );
};

export default App;
