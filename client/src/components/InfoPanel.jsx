import React from 'react';
import './InfoPanel.css';

const InfoPanel = ({ selectedCell, onClose }) => {
  // Si no hay celda seleccionada, no mostrar el panel
  const renderCellInfo = () => {
    if (!selectedCell) {
      return null;
    }

    const { type, row, col } = selectedCell;

    return (
      <div className='cell-info'>
        <h3>Información de la celda</h3>
      </div>
    );
  };

  return (
    <div className='info-panel'>
      <div className='top-panel'>
        {/* <button onClick={onClose}>Cerrar</button> */}
      </div>
      <div className='info'>
        {renderCellInfo()}
      </div>
    </div>
  );
};

export default InfoPanel;
