import React, { useState, useEffect } from "react";
import "./Menu.css";
import "./Common.css";
import { useGame } from "./GameContext";
import { IncrementableBar, StatsBar } from "./IncrementableBar";
import { act } from 'react-dom/test-utils';

function InitGameButton({ isReady, onClick }) {
  const initSimulationButtonClass = isReady ? 'init-simulation-button is-ready' : 'init-simulation-button';
  return <button className={initSimulationButtonClass} onClick={onClick}>Start Simulation</button>;
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

function BackButton({ onClick }) {
  const backButtonClass = "init-simulation-button is-ready"; // Utiliza la misma clase de estilo que el botón "Start Simulation"
  return (
    <button className={backButtonClass} onClick={onClick}>
      Back
    </button>
  );
}


export default function Menu({ onViewChange }) {
  // Estado de la barra de stats disponibles
  const [statsBar, setStatsBar] = useState(Array(10).fill(true));
  // Estados de las barras incrementables
  const [stats, setStats] = useState({...bars});
  // Estado para regular el inicio de la simulacion
  const [isReady, setIsReady] = useState(!(statsBar.includes(true)));
  // Estado para llevar las configuracion inicial, parcial y final del distrito
  const [menu, setMenu] = useState({});
  // Estado para llevar el personaje seleccionado
  const { selectedCharacter, setSelectedCharacter } = useGame();
  // Seteo el id del juego con la respuesta del POST
  const { setGameID } = useGame();
  // Busco los personajes ordenados para seleccionar el que quiero
  const { charactersOrdered } = useGame();
  
  const Characters = {
    0: charactersOrdered[0],
    1: charactersOrdered[1],
    2: charactersOrdered[2],
    3: charactersOrdered[3],
    4: charactersOrdered[4],
    5: charactersOrdered[5],
  };

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
    if (!isReady) {
      if (selectedCharacter == null) {
        alert("You must select a character before starting the game.");
      } else {
        alert("You must distribute all statistics before starting the game.");
      }
    } else {
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
  const getMenu = async () => {
    try {
      const data = await fetch("http://localhost:5000/game/district");
      const result = await data.json();
      return result;
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };
  
  
  useEffect(() => {
    const updatedStats = {};
    Object.entries(bars).forEach(([key, { attribute, increases, consumes }]) => {
      const filledBar = Array(bars[key].bar.length).fill(false);
      updatedStats[key] = { attribute, bar: filledBar, increases, consumes };
    });
    setStats(updatedStats);

    const fetchData = async () => {
      try {
        const result = await getMenu();
        act(() => {
          setMenu(result); // act asegura que setMenu esté sincronizado y finalizado antes de que la prueba continúe ejecutándose
        });
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };
    
    fetchData();
  }, []);

  // Envio al back las stats configuradas por el usuario
  const sendDataToServer = async () => {
    const dataToSend = {
      ...menu,
    };

    const storedToken = localStorage.getItem('access_token');
      
    if (storedToken) {
      try {
        const response = await fetch("http://localhost:5000/game/district", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${storedToken}`
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
    }
  };

  const handleBackToHome = () => {
    onViewChange('init'); // Cambia "home" al valor correcto para regresar a la página de inicio
  };

  function MenuButtonsContainer({ children }) {
    return <div className="menu-buttons-container">{children}</div>;
  }

  return (
    
    <div className="menu-container">
      <div className="stats-settings-container">
        <div>
        <strong className="available-stats">
             Your Stats:<StatsBar stats={statsBar} />
          </strong> 
        </div>
        <div className="choose-character-container">
        {Object.keys(Characters).map((characterKey) => (
          <CharacterCard
            key={characterKey}
            characterKey={characterKey}
            image={Characters[characterKey]}
            isSelected={selectedCharacter === characterKey}
            onSelect={() =>setSelectedCharacter(characterKey)}
          />
        ))}
      </div>
        <div className="bars-container">
          {Object.entries(stats).map(([key, { attribute, bar, increases, consumes }]) => (
            <IncrementableBar
              key={key}
              attribute={`${attribute}:`}
              stats={bar}
              onDecrement={() => decrementStat(key, increases, consumes)}
              onIncrement={() => incrementStat(key, increases, consumes)}
              value={menu ? menu[key] : 0}
            />
          ))}
        </div>
        
        <MenuButtonsContainer>
          <BackButton onClick={handleBackToHome} />
          <InitGameButton isReady={isReady} onClick={handleStartGame} />
        </MenuButtonsContainer>
      </div>
    </div>
  );
}

export { Menu };