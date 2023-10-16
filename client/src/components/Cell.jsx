import React from 'react';

const Cell = ({ state }) => {
  const renderContent = () => {
    switch (state) {
      case 'free':
        return (
          <div className='board-free'>
            <img src="/board-images/tile_0001.png" alt="Free Tile" />
          </div>
        );
      case 'tribute':
        return (
          <div className='board-free'>
            <img src="/board-images/tile_0001.png" alt="Free Tile" />
            <div className='board-tribute'>
              <img src="/board-images/soldier_walk1.png" alt="Tribute Tile" />
            </div>
          </div>
        );
      case 'item':
        return (
          <div className='board-free'>
            <img src="/board-images/tile_0001.png" alt="Free Tile" />
            <div className='board-potion'>
              <img src="/board-images/genericItem_color_102.png" alt="Tribute Tile" />
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
