import React from 'react';
import './About.css';
import gameInfo from './gameInfo.json';

const About = ({ onViewChange }) => {
  const { title, content } = gameInfo;

  const images = [
    { url: '/board-images/items/heal.png', alt: 'potionlife', description: 'Life' },
    { url: '/board-images/items/poison.png', alt: 'potionpoison', description: 'Poison' },
    { url: '/board-images/items/force.png', alt: 'potionforce', description: 'Force' },
    { url: '/board-images/items/spear.png', alt: 'weaponspear', description: 'Spear' },
    { url: '/board-images/items/sword.png', alt: 'weaponsword', description: 'Sword' },
    { url: '/board-images/items/bow.png', alt: 'weaponbow', description: 'Bow' },
  ];

  const handleGoToInitGame = () => {
    onViewChange('init');
  };

  return (
    <div className="about-container-wrapper">
      <div className="background"></div>
      <div className="about-container">
        <h2>{title}</h2>
        {content.map((paragraph, index) => (
          <p key={index}>{paragraph}</p>
        ))}
        <div className="image-container">
          {images.map((image, index) => (
            <div key={index} className="image-item">
              <h3>ITEMS</h3>
              <img src={image.url} alt={image.alt} />
              <p>{image.description}</p>
            </div>
          ))}
        </div>
        <button className="custom-button" onClick={handleGoToInitGame}>
        Back to menu
          </button>
      </div>
    </div>
  );
};

export default About;
