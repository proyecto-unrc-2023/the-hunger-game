// App.jsx
import React, { useState } from "react";
import Menu from "./components/Menu.jsx";
import Game from "./components/Game.jsx";
import Header from "./components/Header.jsx";

const App = () => {
  const [gameStarted, setGameStarted] = useState(false);

  const handleStartGame = () => {
    setGameStarted(true);
  };

  return (
    <div className="parent">
      <Header districtChosed={1} districtsLive={4} />
      {!gameStarted ? (
        <Menu onStartGame={handleStartGame} />
      ) : (
        <Game />
      )}
    </div>
  );
};

export default App;
