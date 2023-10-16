import './App.css';
import React from "react";
import StatsSettings from "./components/Menu.jsx"
import Game from "./components/Game.jsx";
import Header from "./components/Header.jsx";

function App() {
  return (
    <div className="parent">
      <Header districtChosed={1} districtsLive={4}/>
      <StatsSettings />
    </div>
  );
}

export default App;