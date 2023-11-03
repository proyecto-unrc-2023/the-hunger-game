import React, { useState, useEffect } from "react";
import "./Menu.css";
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
  const [statsBar, setStatsBar] = useState(Array(10).fill(true));
  const [stats, setStats] = useState(bars);
  const [isReady, setIsReady] = useState(!(statsBar.includes(true)));
  const [menu, setMenu] = useState(null);
  const [selectedCharacter, setSelectedCharacter] = useState(null);

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
        // Asegurarse de no exceder el rango permitido al decrementar statsBar
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
        console.log('barra index al decre: ', newIndexStatsBar);
        console.log('barra avS al decre: ',newStatsBar);
      }
      const updatedMenu = { ...menu, [statKey]: menu[statKey] - increases };
      console.log('barra al decre: ',newStats[statKey].bar)
      setStats(newStats);
      setStatsBar(newStatsBar);
      setMenu(updatedMenu);
    }
  };
  

  const handleStartGame = () => {
    if (onViewChange && selectedCharacter != null) {
      sendDataToServer();
      onViewChange('game'); 
    } else {
      console.error('Erroraso');
    }
  };

  useEffect(() => {
    if (!statsBar.includes(true)) {
      setIsReady(true);
    } else {
      setIsReady(false);
    }
  }, [statsBar]);
  
  useEffect(() => {
    const getMenu = async() => {
      const data = await fetch("http://localhost:5000/game/district"); 
      const result = await data.json();
      setMenu(result);
    }
    getMenu();
  }, []);

  const sendDataToServer = async () => {
    const dataToSend = {
      ...menu,
    };
  
    const response = await fetch("http://localhost:5000/game/district", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json', // Con esto nos aseguramos que los datos se envíen como JSON
      },
      body: JSON.stringify(dataToSend), // Convierte los datos en una cadena JSON
    });

    if (response.ok) {
      console.log("Post request succeeded");
    } else {
      console.error("Post request failed");
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
