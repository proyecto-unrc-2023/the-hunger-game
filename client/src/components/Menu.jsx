import React, { useState, useEffect } from "react";
import "./Menu.css";

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

function IncrementableBar({ attribute, stats, onIncrement, onDecrement }) {
  const handleIncrement = () => {
    onIncrement();
  };

  const handleDecrement = () => {
    onDecrement();
  };

  return (
    <div className="incrementable-bars">
      <strong className="incrementable-bar-atribute">{attribute}</strong>
      <StatsBar stats={stats} />
      <IncrementButton onClick={handleIncrement} />
      <DecrementButton onClick={handleDecrement} />
    </div>
  );
} 

function InitGameButton({ isReady, onClick }) {
  const initSimulationButtonClass = isReady ? 'init-simulation-button is-ready' : 'init-simulation-button';
  return <button className={initSimulationButtonClass} onClick={onClick}>Start Simulation</button>;
}

export default function Menu({ onStartGame }) {
  const [statsBar, setStatsBar] = useState(Array(10).fill(true));
  const [lifeStats, setLifeStats] = useState(Array(10).fill(false).map((_, index) => index < 5));
  const [forceStats, setForceStats] = useState(Array(10).fill(false).map((_, index) => index < 2));
  const [allianceStats, setAllianceStats] = useState(Array(10).fill(false).map((_, index) => index < 2));
  const [tributeStats, setTributeStats] = useState(Array(10).fill(false).map((_, index) => index < 4));
  const [isReady, setIsReady] = useState(!(statsBar.includes(true)));

  const incrementLifeStat = () => {
    const indexLife = lifeStats.findIndex(isConsumed => !isConsumed);
    const indexStatsBar = statsBar.slice().reverse().findIndex(isConsumed => isConsumed);
    const life = menu;
    if (indexLife !== -1 && indexStatsBar !== -1) {
      const newStatsBar = [...statsBar];
      const newLifeStats = [...lifeStats];
      const reversedStatsBarIndex = statsBar.length - 1 - indexStatsBar;
      newLifeStats[indexLife] = true; // Consume un stat de vida
      newStatsBar[reversedStatsBarIndex] = false; // Deja de consumir un stat disponible
      setLifeStats(newLifeStats);
      setStatsBar(newStatsBar);
      life.life++;
      setMenu(life);
    }
  };

  const decrementLifeStat = () => {
    const indexLifeStats = lifeStats.slice().reverse().findIndex(isConsumed => isConsumed);
    const indexStatsBar = statsBar.findIndex(isConsumed => !isConsumed);
    const life = menu;
    if (indexLifeStats <= 4 && indexStatsBar !== -1) {
      const newStatsBar = [...statsBar];
      const newLifeStats = [...lifeStats];
      const reversedLifeStatsIndex = lifeStats.length - 1 - indexLifeStats;
      newLifeStats[reversedLifeStatsIndex] = false; // Deja de consumir un stat de vida
      newStatsBar[indexStatsBar] = true; // Devuelve un stat a los disponibles
      setStatsBar(newStatsBar);
      setLifeStats(newLifeStats);
      life.life--;
      setMenu(life);
    }
  };

  const incrementForceStat = () => {
    const indexForce = forceStats.findIndex(isConsumed => !isConsumed);
    const indexStatsBar = statsBar.slice().reverse().findIndex(isConsumed => isConsumed);
    if (indexForce !== -1 && indexStatsBar !== -1) {
      const newStatsBar = [...statsBar];
      const newForceStats = [...forceStats];
      const reversedStatsBarIndex = statsBar.length - 1 - indexStatsBar;
      newForceStats[indexForce] = true; // Consume un stat de fuerza
      newStatsBar[reversedStatsBarIndex] = false; // Deja de consumir un stat disponible
      setForceStats(newForceStats);
      setStatsBar(newStatsBar);
    }
  };

  const decrementForceStat = () => {
    const indexForceStats = forceStats.slice().reverse().findIndex(isConsumed => isConsumed);
    const indexStatsBar = statsBar.findIndex(isConsumed => !isConsumed);
    if (indexForceStats <= 7 && indexStatsBar !== -1) {
      const newStatsBar = [...statsBar];
      const newForceStats = [...forceStats];
      const reversedForceStatsIndex = forceStats.length - 1 - indexForceStats;
      newForceStats[reversedForceStatsIndex] = false; // Deja de consumir un stat de fuerza
      newStatsBar[indexStatsBar] = true; // Devuelve un stat a los disponibles
      setStatsBar(newStatsBar);
      setForceStats(newForceStats);
    }
  };

  const incrementAllianceStat = () => {
    const indexAlliance = allianceStats.findIndex(isConsumed => !isConsumed);
    const indexStatsBar = statsBar.slice().reverse().findIndex(isConsumed => isConsumed);
    if (indexAlliance !== -1 && indexStatsBar !== -1) {
      const newStatsBar = [...statsBar];
      const newAllianceStats = [...allianceStats];
      const reversedStatsBarIndex = statsBar.length - 1 - indexStatsBar;
      newAllianceStats[indexAlliance] = true; // Consume un stat de alianza
      newStatsBar[reversedStatsBarIndex] = false; // Deja de consumir un stat disponible
      setAllianceStats(newAllianceStats);
      setStatsBar(newStatsBar);
    }
  };

  const decrementAllianceStat = () => {
    const indexAllianceStats = allianceStats.slice().reverse().findIndex(isConsumed => isConsumed);
    const indexStatsBar = statsBar.findIndex(isConsumed => !isConsumed);
    if (indexAllianceStats <= 7 && indexStatsBar !== -1) {
      const newStatsBar = [...statsBar];
      const newAllianceStats = [...allianceStats];
      const reversedAllianceStatsIndex = allianceStats.length - 1 - indexAllianceStats;
      newAllianceStats[reversedAllianceStatsIndex] = false; // Deja de consumir un stat de alianza
      newStatsBar[indexStatsBar] = true; // Devuelve un stat a los disponibles
      setStatsBar(newStatsBar);
      setAllianceStats(newAllianceStats);
    }
  };

  const incrementTributeStat = () => {
    const indexTribute = tributeStats.findIndex(isConsumed => !isConsumed);
    const indexStatsBar = statsBar.slice().reverse().findIndex(isConsumed => isConsumed);
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
      }
    }
  };
  

  const decrementTributeStat = () => {
    const indexTributeStats = tributeStats.slice().reverse().findIndex(isConsumed => isConsumed);
    const indexStatsBar = statsBar.findIndex(isConsumed => !isConsumed);
    if (indexTributeStats <= 7 && indexStatsBar !== -1) {
      const newStatsBar = [...statsBar];
      const newTributeStats = [...tributeStats];
      const reversedTributeStatsIndex = tributeStats.length - 1 - indexTributeStats;
      newTributeStats[reversedTributeStatsIndex] = false; // Deja de consumir un stat de tributo
      
      // Verificar que siempre haya al menos 4 elementos true en newTributeStats
      const trueElementsCount = newTributeStats.filter(isConsumed => isConsumed).length;
  
      if (trueElementsCount >= 4) {
        // Devuelve 4 stats a las disponibles
        for (var i = 0; i < 4; i++) {
          const newIndex = indexStatsBar + i;
          newStatsBar[newIndex] = true;
        }
        setTributeStats(newTributeStats);
        setStatsBar(newStatsBar);
      }
    }
  };

  const handleStartGame = () => {
    if (isReady) {
      onStartGame();
    }
  };

  useEffect(() => {
    if (!statsBar.includes(true)) {
      setIsReady(true);
    } else {
      setIsReady(false);
    }
  }, [statsBar]);
  
  const [menu, setMenu] = useState(null);
  
  useEffect(() => {
    const getMenu = async() => {
      const data = await fetch("http://localhost:5000/apis/menu"); 
      const result = await data.json();
      setMenu(result);
    }
    getMenu();
  }, []);
  
  console.log(menu);

  return (
    <div className="menu-container">
      <div className="stats-settings-container">
        <div>
          <strong className="available-stats">Avaible Stats <StatsBar stats={statsBar} /></strong>
        </div>
        <div className="bars-container">
          <IncrementableBar attribute="Life:" stats={lifeStats} setStats={setLifeStats} onIncrement={incrementLifeStat} onDecrement={decrementLifeStat} />
          <IncrementableBar attribute="Force:" stats={forceStats} setStats={setForceStats} onIncrement={incrementForceStat} onDecrement={decrementForceStat} />
          <IncrementableBar attribute="Alliance:" stats={allianceStats} setStats={setAllianceStats} onIncrement={incrementAllianceStat} onDecrement={decrementAllianceStat} />
          <IncrementableBar attribute="Tributes:" stats={tributeStats} setStats={setTributeStats} onIncrement={incrementTributeStat} onDecrement={decrementTributeStat} />
        </div>
        <InitGameButton isReady={isReady} onClick={handleStartGame} />
      </div>
    </div>
  );

}
