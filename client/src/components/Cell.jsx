import React from 'react';

const Cell = ({ state }) => {
  const renderContent = () => {
    switch (state) {
      case 'free':
        return null; // Celda vacía
      case 'tribute':
        return 't';
      case 'item':
        return 'i';
      default:
        return null;
    }
  };

  return (
    <div className={`cell ${state}`}>
      {renderContent()}
    </div>
  );
};

export default Cell;
