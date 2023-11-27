import React, { useEffect, useRef } from 'react';
import './WinnerScreen.css';
import "./Common.css";
import { useGame } from "./GameContext";


const WinnerScreen = ({ onViewChange }) => {
    const audioRef = useRef(null);

    const handleRestartGame = () => {
      onViewChange("menu"); // Llamando a la función proporcionada desde App
    };

    const { characters } = useGame();
    const { winnerCharacter } = useGame();
  
    useEffect(() => {
      const audio = audioRef.current;

      if (audio) {
        const isPlaying = audio.currentTime > 0 && !audio.paused && !audio.ended && audio.readySate > 2;
    
        if (!isPlaying) {
          audio.play();
        }

        return () => {
          if (isPlaying) {
            audio.pause();
            audio.currentTime = 0;
          }
        };
      }
    }, []);


    return (
      <div className="winner-screen">
        <div className="winner-container">
          <div className='winner-card'><h2>DISTRICT {winnerCharacter} WON</h2></div>
          <img className = "winner-img" src={characters[winnerCharacter]} ></img>
        </div>
        <div className="restart-save-container">
          <button className='button-restart-game' onClick={handleRestartGame}>Restart Game</button>
          <button className='button-save-game' >Save Game</button>
        </div>
        <audio ref={audioRef} autoPlay>
          <source src="/winner_district.wav" type="audio/wav" />
        </audio>
      </div>
    );
  };
  
  export default WinnerScreen;