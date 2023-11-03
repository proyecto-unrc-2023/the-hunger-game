import React, { createContext, useContext, useState } from "react";

const GameContext = createContext();

export const GameProvider = ({ children }) => {
  const [gameID, setGameID] = useState(null);
  const [selectedCharacter, setSelectedCharacter] = useState(null);

  const contextValue = {
    gameID,
    setGameID,
    selectedCharacter,
    setSelectedCharacter,
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
