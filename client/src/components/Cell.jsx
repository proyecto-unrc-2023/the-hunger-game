import React from 'react';

const Cell = ({ state, onClick }) => {
  
  const GrassImage = "/board-images/grass3.png";
  const Tribute1Walk1 = "/board-images/characters/female_adventurer_walk1.png";
  const Tribute1Walk2 = "/board-images/characters/female_adventurer_walk2.png";
  const Tribute1HoldBow = "/board-images/characters/female_adventurer_hold_bow.png";
  const Tribute1HoldSword = "/board-images/characters/female_adventurer_hold_sword.png";
  const Tribute2Walk1 = "/board-images/characters/male_adventurer_walk1.png";
  const Tribute2Walk2 = "/board-images/characters/male_adventurer_walk2.png";
  const Tribute2HoldBow = "/board-images/characters/male_adventurer_hold_bow.png";
  const Tribute2HoldSword = "/board-images/characters/male_adventurer_hold_sword.png";
  const Tribute3Walk1 = "/board-images/characters/female_person_walk1.png";
  const Tribute3Walk2 = "/board-images/characters/female_person_walk2.png";
  const Tribute3HoldBow = "/board-images/characters/female_person_hold_bow.png";
  const Tribute3HoldSword = "/board-images/characters/female_person_hold_sword.png";
  const Tribute4Walk1 = "/board-images/characters/male_person_walk1.png";
  const Tribute4Walk2 = "/board-images/characters/male_person_walk2.png";
  const Tribute4HoldBow = "/board-images/characters/male_person_hold_bow.png";
  const Tribute4HoldSword = "/board-images/characters/male_person_hold_sword.png";
  const Tribute5Walk1 = "/board-images/characters/robot_walk1.png";
  const Tribute5Walk2 = "/board-images/characters/robot_walk2.png";
  const Tribute5HoldBow = "/board-images/characters/robot_hold_bow.png";
  const Tribute5HoldSword = "/board-images/characters/robot_hold_sword.png";
  const Tribute6Walk1 = "/board-images/characters/zombie_walk1.png";
  const Tribute6Walk2 = "/board-images/characters/zombie_walk2.png";
  const Tribute6HoldBow = "/board-images/characters/zombie_hold_bow.png";
  const Tribute6HoldSword = "/board-images/characters/zombie_hold_sword.png";
  const HealImage = "/board-images/items/heal.png";
  const SwordImage = "/board-images/items/sword.png";
  const BowImage = "/board-images/items/bow.png";

  const renderContent = () => {
    switch (state) {
      case 'free':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
          </div>
        );
      case 'tribute':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-tribute'>
              <img src={Tribute1Walk1} alt="Tribute Tile" />
            </div>
          </div>
        );
      case 'potion':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-potion'>
              <img src={HealImage} alt="Potion Tile" />
            </div>
          </div>
        );
      case 'sword':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-sword'>
              <img src={SwordImage} alt="Sword Tile" />
            </div>
          </div>
        );
      case 'bow':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-bow'>
              <img src={BowImage} alt="Bow Tile" />
            </div>
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <div className={`cell ${state}`} onClick={onClick}>
      {renderContent()}
    </div>
  );
};

export default Cell;
