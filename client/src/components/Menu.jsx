import React, { useState, useEffect } from "react";
import "./Menu.css";
import { useGame } from "./GameContext";

function IncrementButton({ onClick }) {
  return (
    <div className="increment-button" onClick={onClick}>
      <button>+</button>
    </div>
  );
}

function DecrementButton({ onClick }) {
  return (
    <div className="decrement-button" onClick={onClick}>
      <button>-</button>
    </div>
  );
}

function Stat({ isConsumed }) {
  const statClassName = isConsumed ? 'stat is-consumed' : 'stat';
  return <div className={statClassName}></div>;
}

function StatsBar({ stats }) {
  return (
    <div className="stats-bar">
      {stats.map((isConsumed, index) => (
        <Stat key={index} isConsumed={isConsumed} />
      ))}
    </div>
  );
}

function IncrementableBar({ attribute, stats, onIncrement, onDecrement, value }) {
  const handleIncrement = () => {
    onIncrement();
  };

  const handleDecrement = () => {
    onDecrement();
  };

  return (
    <div className="incrementable-bars">
      <div className="incrementable-bar-atribute">{attribute}</div>
      <StatsBar stats={stats} />
      <div className="incrementable-value">
        <div className="value-stat">{value}</div>
        <IncrementButton onClick={handleIncrement} />
        <DecrementButton onClick={handleDecrement} />
      </div>
    </div>
  );
} 

function InitGameButton({ isReady, onClick }) {
  const initSimulationButtonClass = isReady ? 'init-simulation-button is-ready' : 'init-simulation-button';
  return <button className={initSimulationButtonClass} onClick={onClick}>Start Simulation</button>;
}

export default function Menu({ onViewChange }) {
  // Estado de la barra de stats disponibles
  const [statsBar, setStatsBar] = useState(Array(10).fill(true));

  // Estados de las barras incrementables
  const [lifeStats, setLifeStats] = useState(Array(10).fill(false));
  const [forceStats, setForceStats] = useState(Array(10).fill(false));
  const [allianceStats, setAllianceStats] = useState(Array(7).fill(false));
  const [cowardiceStats, setCowardiceStats] = useState(Array(5).fill(false));
  const [tributeStats, setTributeStats] = useState(Array(10).fill(false));

  // Estado para regular el inicio de la simulacion
  const [isReady, setIsReady] = useState(!(statsBar.includes(true)));
  
  // Estado para llevar las configuracion inicial, parcial y final del distrito
  const [menu, setMenu] = useState(null);

  // Seteo el id del juego con la respuesta del POST
  const { setGameID } = useGame();

  const incrementStat = (statArray, setStatArray, statKey, menu, setMenu, value) => {
    const indexStat = statArray.findIndex((isConsumed) => !isConsumed);
    const indexStatsBar = statsBar.slice().reverse().findIndex((isConsumed) => isConsumed);
    if (indexStat !== -1 && indexStatsBar !== -1) {
      const newStatsBar = [...statsBar];
      const newStat = [...statArray];
      const reversedStatsBarIndex = statsBar.length - 1 - indexStatsBar;
      newStat[indexStat] = true; // Consume un stat
      newStatsBar[reversedStatsBarIndex] = false; // Deja de consumir un stat disponible

      // Incrementamos el valor de la estadística en el diccionario
      const updatedMenu = { ...menu, [statKey]: menu[statKey] + value };

      setStatArray(newStat);
      setStatsBar(newStatsBar);
      setMenu(updatedMenu); 
    }
  };

  const decrementStat = (statArray, setStatArray, statKey, menu, setMenu, value) => {
    const indexStat = statArray.slice().reverse().findIndex((isConsumed) => isConsumed);
    const indexStatsBar = statsBar.findIndex((isConsumed) => !isConsumed);
    if (indexStat !== -1 && indexStatsBar !== -1) {
      const newStatsBar = [...statsBar];
      const newStat = [...statArray];
      const reversedStatIndex = statArray.length - 1 - indexStat;
      newStat[reversedStatIndex] = false; // Deja de consumir un stat
      newStatsBar[indexStatsBar] = true; // Devuelve un stat a los disponibles

      // Decrementamos el valor de la estadística en el diccionario
      const updatedMenu = { ...menu, [statKey]: menu[statKey] - value };

      setStatArray(newStat);
      setStatsBar(newStatsBar);
      setMenu(updatedMenu); 
    }
  };

  const incrementTributeStat = () => {
    const indexTribute = tributeStats.findIndex(isConsumed => !isConsumed);
    const indexStatsBar = statsBar.slice().reverse().findIndex(isConsumed => isConsumed);
    const cant_tributes = menu;
    if (indexTribute !== -1 && indexStatsBar !== -1) {
      const newStatsBar = [...statsBar];
      const newTributeStats = [...tributeStats];
      const reversedStatsBarIndex = statsBar.length - 1 - indexStatsBar;
      newTributeStats[indexTribute] = true; // Consume un stat de tributo
  
      // Verificar si hay al menos 4 elementos true en newStatsBar
      const trueElementsCount = newStatsBar.filter(isConsumed => isConsumed).length;
  
      if (trueElementsCount >= 4) {
        // Deja de consumir 4 stats disponibles
        for (var i = 0; i < 4; i++) {
          const newIndex = reversedStatsBarIndex - i;
          newStatsBar[newIndex] = false;
        }
        setTributeStats(newTributeStats);
        setStatsBar(newStatsBar);
        cant_tributes.cant_tributes++;
        setMenu(cant_tributes);
      }
    }
  };
  
  const decrementTributeStat = () => {
    const indexTributeStats = tributeStats.slice().reverse().findIndex(isConsumed => isConsumed);
    const indexStatsBar = statsBar.findIndex(isConsumed => !isConsumed);
    const cant_tributes = menu;
    if (indexTributeStats !== -1 && indexStatsBar !== -1) {
      const newStatsBar = [...statsBar];
      const newTributeStats = [...tributeStats];
      const reversedTributeStatsIndex = tributeStats.length - 1 - indexTributeStats;
      newTributeStats[reversedTributeStatsIndex] = false; // Deja de consumir un stat de tributo
      
      // Verificar que siempre haya al menos 4 elementos true en newTributeStats
      const trueElementsCount = newTributeStats.filter(isConsumed => isConsumed).length;
  
      if (trueElementsCount >= 0) {
        // Devuelve 4 stats a las disponibles
        for (var i = 0; i < 4; i++) {
          const newIndex = indexStatsBar + i;
          newStatsBar[newIndex] = true;
        }
        setTributeStats(newTributeStats);
        setStatsBar(newStatsBar);
        cant_tributes.cant_tributes--;
        setMenu(cant_tributes);
      }
    }
  };

  // Al darle click al boton de start simulation
  const handleStartGame = () => {
    if (isReady) {
      onViewChange("game");
      sendDataToServer();
    }
  };

  // Regula que todas las stats disponibles sean distribuidas
  useEffect(() => {
    if (!statsBar.includes(true)) {
      setIsReady(true);
    } else {
      setIsReady(false);
    }
  }, [statsBar]);
  
  // Hago un fetch para obtener configuraciones iniciales
  useEffect(() => {
    const getMenu = async() => {
      const data = await fetch("http://localhost:5000/game/district"); 
      const result = await data.json();
      setMenu(result);
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
      <div className="stats-settings-container">
        <div>
          <strong className="available-stats">Available Stats <StatsBar stats={statsBar} /></strong>
        </div>
        <div className="bars-container">
          <IncrementableBar attribute="Life:" stats={lifeStats} onIncrement={() => incrementStat(lifeStats, setLifeStats, 'life', menu, setMenu, 5)} onDecrement={() => decrementStat(lifeStats, setLifeStats, 'life', menu, setMenu, 5)} value={menu ? menu.life : 0}/>
          <IncrementableBar attribute="Force:" stats={forceStats} onIncrement={() => incrementStat(forceStats, setForceStats, 'force', menu, setMenu, 2)} onDecrement={() => decrementStat(forceStats, setForceStats, 'force', menu, setMenu, 2)} value={menu ? menu.force : 0}/>
          <IncrementableBar attribute="Alliance:" stats={allianceStats} onIncrement={() => incrementStat(allianceStats, setAllianceStats, 'alliance', menu, setMenu, 1)} onDecrement={() => decrementStat(allianceStats, setAllianceStats, 'alliance', menu, setMenu, 1)} value={menu ? menu.alliance : 0}/>
          <IncrementableBar attribute="Cowardice:" stats={cowardiceStats} onIncrement={() => incrementStat(cowardiceStats, setCowardiceStats, 'cowardice', menu, setMenu, 1)} onDecrement={() => decrementStat(cowardiceStats, setCowardiceStats, 'cowardice', menu, setMenu, 1)} value={menu ? menu.cowardice : 0}/>
          <IncrementableBar attribute="Tributes:" stats={tributeStats} setStats={setTributeStats} onIncrement={incrementTributeStat} onDecrement={decrementTributeStat} value={menu ? menu.cant_tributes : 0}/>
        </div>
        <InitGameButton isReady={isReady} onClick={handleStartGame} />
    </div>
    </div>
  );

}
