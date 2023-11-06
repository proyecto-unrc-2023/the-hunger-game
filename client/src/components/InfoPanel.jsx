import React from 'react';
import './InfoPanel.css';




const InfoPanel = ({ isPaused }) => {
  
    if(isPaused){
    //  fetchGamePaused();

      
    }


    return (
      <div className='cell-info'>
        <h3>Información de la celda</h3>
      </div>
    );
  };


export default InfoPanel;
