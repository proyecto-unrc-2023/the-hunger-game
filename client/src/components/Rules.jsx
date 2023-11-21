import React from 'react';
import "./Rules.css";
import rulesInfo from './rulesInfo.json';

const Rules = ({ onViewChange }) => {
  const { title, content } = rulesInfo;

  const handleGoToInitGame = () => {
    onViewChange('init');
  };

  return (
    <div className="about-container-wrapper">
      <div className="background"></div>
      <div className="rules-container">
        <h2>{title}</h2>
        {content.map((paragraph, index) => (
          <p key={index}>{paragraph}</p>
        ))}
        <button className="custom-button" onClick={handleGoToInitGame}>
          Back to menu
        </button>
      </div>
    </div>
  );
};

export default Rules;
