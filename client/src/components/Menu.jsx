import React, { useState, useEffect } from "react";
import "./Menu.css";
import { useGame } from "./GameContext";
import { IncrementableBar, StatsBar } from "./IncrementableBar";

function InitGameButton({ isReady, onClick }) {
  const initSimulationButtonClass = isReady ? 'init-simulation-button is-ready' : 'init-simulation-button';
  return <button className={initSimulationButtonClass} onClick={onClick}>Start Simulation</button>;
};

const characters = {
  characterOne: '/board-images/characters/female_adventurer_walk1.png',
  characterTwo: '/board-images/characters/female_person_walk1.png',
  characterThree: '/board-images/characters/male_person_walk1.png',
  characterFour: '/board-images/characters/male_adventurer_walk1.png',
  characterFive: '/board-images/characters/robot_walk1.png',
  characterSix: '/board-images/characters/zombie_walk1.png',
};

function CharacterCard({ characterKey, image, isSelected, onSelect }) {
  return (
    <article
      className={`card ${isSelected ? 'selected' : ''}`}
      onClick={() => onSelect(characterKey)}
      >
      <img src={image} className="image" alt={`Character ${characterKey}`} />
    </article>
  );
};

// Barras en el menú
const bars = {
  life:{
    attribute: 'Life',
    bar: Array(10).fill(false),
    increases: 5,
    consumes: 1
  },
  force:{
    attribute: 'Force',
    bar: Array(10).fill(false),
    increases: 2,
    consumes: 1
  },
  alliance:{
    attribute: 'Alliance',
    bar: Array(7).fill(false),
    increases: 1,
    consumes: 1
  },
  cowardice:{
    attribute: 'Cowardice',
    bar: Array(5).fill(false),
    increases: 1,
    consumes: 1
  },
  cant_tributes:{
    attribute: 'Tributes',
    bar: Array(2).fill(false),
    increases: 1,
    consumes: 4
  }
};

export default function Menu({ onViewChange }) {
  // Estado de la barra de stats disponibles
  const [statsBar, setStatsBar] = useState(Array(10).fill(true));
  // Estados de las barras incrementables
  const [stats, setStats] = useState({...bars});
  // Estado para regular el inicio de la simulacion
  const [isReady, setIsReady] = useState(!(statsBar.includes(true)));
  // Estado para llevar las configuracion inicial, parcial y final del distrito
  const [menu, setMenu] = useState(null);
  // Estado para llevar el personaje seleccionado
  const [selectedCharacter, setSelectedCharacter] = useState(null);
  // Seteo el id del juego con la respuesta del POST
  const { setGameID } = useGame();

  const incrementStat = (statKey, increases, consumes) => {
    const indexStat = stats[statKey].bar.findIndex(isConsumed => !isConsumed);
    const indexStatsBar = statsBar.slice().reverse().findIndex(isConsumed => isConsumed);
    if (indexStat !== -1 && indexStatsBar !== -1) {
      const newStats = { ...stats };
      const newStatsBar = [...statsBar];
      const reversedStatsBarIndex = statsBar.length - 1 - indexStatsBar;
      // Verificar si hay suficientes stats disponibles antes de incrementar
      if (reversedStatsBarIndex >= consumes - 1) {
        newStats[statKey].bar[indexStat] = true;
        for (let i = 0; i < consumes; i++) {
          const newIndexStatsBar = reversedStatsBarIndex - i;
          newStatsBar[newIndexStatsBar] = false;
        }
        const updatedMenu = { ...menu, [statKey]: menu[statKey] + increases };
        setStats(newStats);
        setStatsBar(newStatsBar);
        setMenu(updatedMenu);
      }
    }
  };
  
  
  const decrementStat = (statKey, increases, consumes) => {
    const indexStat = stats[statKey].bar.slice().reverse().findIndex(isConsumed => isConsumed);
    const indexStatsBar = statsBar.findIndex(isConsumed => !isConsumed);
    if (indexStat !== -1 && indexStatsBar !== -1) {
      const newStats = { ...stats };
      const newStatsBar = [...statsBar];
      const reversedStatsIndex = newStats[statKey].bar.length - 1 - indexStat;
      newStats[statKey].bar[reversedStatsIndex] = false;
      for (let i = 0; i < consumes; i++) {
        const newIndexStatsBar = indexStatsBar + i;
        newStatsBar[newIndexStatsBar] = true;
      }
      const updatedMenu = { ...menu, [statKey]: menu[statKey] - increases };
      setStats(newStats);
      setStatsBar(newStatsBar);
      setMenu(updatedMenu);
    }
  };

  // Al darle click al boton de start simulation
  const handleStartGame = () => {
    if (isReady && selectedCharacter != null) {
      sendDataToServer();
      onViewChange('game'); 
    }
  };

  // Regula que todas las stats disponibles sean distribuidas y que se elija un personaje
  useEffect(() => {
    if (!statsBar.includes(true) && selectedCharacter != null) {
      setIsReady(true);
    } else {
      setIsReady(false);
    }
  }, [statsBar, selectedCharacter]);
  
  // Hago un fetch para obtener configuraciones iniciales
  useEffect(() => {
    const getMenu = async() => {
      const data = await fetch("http://localhost:5000/game/district"); 
      const result = await data.json();
      // Asegurarse de que las barras se inicialicen vacías
      const updatedStats = {};
      Object.entries(bars).forEach(([key, { attribute, increases, consumes }]) => {
        const filledBar = Array(bars[key].bar.length).fill(false);
        updatedStats[key] = { attribute, bar: filledBar, increases, consumes };
      });
      setMenu(result);
      setStats(updatedStats);
    }
    getMenu();
  }, []);

  // Envio al back las stats configuradas por el usuario
  const sendDataToServer = async () => {
    const dataToSend = {
      ...menu,
    };
  
    try {
      const response = await fetch("http://localhost:5000/game/district", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend),
      });
  
      if (response.ok) {
        const data = await response.json();
        const gameIdFromResponse = data.game_id;
        setGameID(gameIdFromResponse); // Establecer el game_id en el contexto
      } else {
        console.error("Post request failed");
      }
    } catch (error) {
      console.error("An error occurred:", error);
    }
  };

  return (
    <div className="menu-container">
      <div className="choose-character-container">
        {Object.keys(characters).map((characterKey) => (
          <CharacterCard
            key={characterKey}
            characterKey={characterKey}
            image={characters[characterKey]}
            isSelected={selectedCharacter === characterKey}
            onSelect={() =>setSelectedCharacter(characterKey)}
          />
        ))}
      </div>
      <div className="stats-settings-container">
        <div>
        <strong className="available-stats">
            Available Stats <StatsBar stats={statsBar} />
          </strong>
        </div>
        <div className="bars-container">
          {Object.entries(stats).map(([key, { attribute, bar, increases, consumes }]) => (
            <IncrementableBar
              key={key}
              attribute={`${attribute}:`}
              stats={bar}
              onIncrement={() => incrementStat(key, increases, consumes)}
              onDecrement={() => decrementStat(key, increases, consumes)}
              value={menu ? menu[key] : 0}
            />
          ))}
        </div>
        <InitGameButton isReady={isReady} onClick={handleStartGame} />
      </div>
    </div>
  );
}
