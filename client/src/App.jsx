import React, { useState } from 'react';
import Menu from './components/Menu.jsx';
import Game from './components/Game.jsx';
import Header from './components/Header.jsx';
import Footer from './components/Footer.jsx';
import InfoPanel from './components/InfoPanel.jsx';
import InitGame from './components/InitGame.jsx';

const App = () => {
  const [gameStarted, setGameStarted] = useState(false);
  const [playGame, setPlayGame] = useState(false);
  // const [selectedCell, setSelectedCell] = useState(null);

  const handleStartGame = () => {
    setGameStarted(true);
  };

  const handlePlayGame = () => {
    setPlayGame(true);
  };

  // const handleCellClick = (cellData) => {
  //   setSelectedCell(cellData);
  // };

  // const handleClosePanel = () => {
  //   setSelectedCell(null);
  // };

  return (
    <div className='app'>
      <Header/>
      {!playGame ? (
        <InitGame onStartGame={handlePlayGame}/>
        ) : (
        !gameStarted ? (
          <Menu onStartGame={handleStartGame} />
        ) : (
          <div className='main'>
            <Game />
            <InfoPanel />
          </div>
        )
        )
      }
      <Footer />
    </div>
  );
};

export default App;
