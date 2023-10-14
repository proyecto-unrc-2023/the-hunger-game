import React from 'react';
import tileImage from './tile_0001.png';
import tributeImage from './soldier_walk1.png';
import potionImage from './genericItem_color_102.png';

const Cell = ({ state }) => {
  const renderContent = () => {
    switch (state) {
      case 'free':
        return (
          <div className='board-free'>
            <img src={tileImage} alt="Free Tile" />
          </div>
        );
      case 'tribute':
        return (
          <div className='board-free'>
            <img src={tileImage} alt="Free Tile" />
            <div className='board-tribute'>
              <img src={tributeImage} alt="Tribute Tile" />
            </div>
          </div>
        );
      case 'item':
        return (
          <div className='board-free'>
            <img src={tileImage} alt="Free Tile" />
            <div className='board-potion'>
              <img src={potionImage} alt="Tribute Tile" />
            </div>
          </div>
        );
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
