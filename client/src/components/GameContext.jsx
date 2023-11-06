import React, { createContext, useContext, useState } from "react";

const GameContext = createContext();

export const GameProvider = ({ children }) => {
  const [gameID, setGameID] = useState(null);
  const [selectedCharacter, setSelectedCharacter] = useState(null);
  const [winnerCharacter, setWinnerCharacter] = useState(null);

  const contextValue = {
    gameID,
    setGameID,
    selectedCharacter,
    setSelectedCharacter,
    winnerCharacter,
    setWinnerCharacter
  };

  return (
    <GameContext.Provider value={contextValue}>
      {children}
    </GameContext.Provider>
  );
};


export const useGame = () => {
  return useContext(GameContext);
};
