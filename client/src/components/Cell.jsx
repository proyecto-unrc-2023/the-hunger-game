import React from 'react';

const Cell = ({ state, onClick, selectedCharacter}) => {
  
  const renderTributeImage = (character) => {
    // Lógica para determinar qué imagen mostrar según selectedCharacter
    switch (character) {
      case 'characterOne':
        return Tribute0Walk1;
      case 'characterTwo':
        return Tribute1Walk1;
      case 'characterThree':
        return Tribute2Walk1;
      case 'characterFour':
        return Tribute3Walk1;
      case 'characterFive':
        return Tribute4Walk1;
      case 'characterSix':
        return Tribute5Walk1;
      default:
        return Tribute0Walk1; // Imagen predeterminada si no hay coincidencia
    }
  };
  const Pointer = "/board-images/characters/pointer.png";
  const GrassImage = "/board-images/grass3.png";
  const BorderRImage = "/board-images/border-r.png";
  const BorderLImage = "/board-images/border-l.png";
  const BorderDImage = "/board-images/border-d.png";
  const BorderDLImage = "/board-images/border-dl.png";
  const BorderDRImage = "/board-images/border-dr.png";
  const BorderUImage = "/board-images/border-u.png";
  const BorderULImage = "/board-images/border-ul.png";
  const BorderURImage = "/board-images/border-ur.png";
  const WaterImage = "/board-images/water.png";
  const Tribute0Walk1 = "/board-images/characters/female_adventurer_walk1.png";
  // const Tribute0Walk2 = "/board-images/characters/female_adventurer_walk2.png";
  // const Tribute0HoldBow = "/board-images/characters/female_adventurer_hold_bow.png";
  // const Tribute0HoldSword = "/board-images/characters/female_adventurer_hold_sword.png";
  const Tribute1Walk1 = "/board-images/characters/male_adventurer_walk1.png";
  // const Tribute1Walk2 = "/board-images/characters/male_adventurer_walk2.png";
  // const Tribute1HoldBow = "/board-images/characters/male_adventurer_hold_bow.png";
  // const Tribute1HoldSword = "/board-images/characters/male_adventurer_hold_sword.png";
  const Tribute2Walk1 = "/board-images/characters/female_person_walk1.png";
  // const Tribute2Walk2 = "/board-images/characters/female_person_walk2.png";
  // const Tribute2HoldBow = "/board-images/characters/female_person_hold_bow.png";
  // const Tribute2HoldSword = "/board-images/characters/female_person_hold_sword.png";
  const Tribute3Walk1 = "/board-images/characters/male_person_walk1.png";
  // const Tribute3Walk2 = "/board-images/characters/male_person_walk2.png";
  // const Tribute3HoldBow = "/board-images/characters/male_person_hold_bow.png";
  // const Tribute3HoldSword = "/board-images/characters/male_person_hold_sword.png";
  const Tribute4Walk1 = "/board-images/characters/robot_walk1.png";
  // const Tribute4Walk2 = "/board-images/characters/robot_walk2.png";
  // const Tribute4HoldBow = "/board-images/characters/robot_hold_bow.png";
  // const Tribute4HoldSword = "/board-images/characters/robot_hold_sword.png";
  const Tribute5Walk1 = "/board-images/characters/zombie_walk1.png";
  // const Tribute5Walk2 = "/board-images/characters/zombie_walk2.png";
  // const Tribute5HoldBow = "/board-images/characters/zombie_hold_bow.png";
  // const Tribute5HoldSword = "/board-images/characters/zombie_hold_sword.png";
  const TributeNWalk1 = "/board-images/characters/neutral_walk1.png";
  // const TributeNWalk2 = "/board-images/characters/neutral_walk2.png";
  // const TributeNHoldBow = "/board-images/characters/neutral_hold_bow.png";
  // const TributeNHoldSword = "/board-images/characters/neutral_hold_sword.png";
  const SwordImage = "/board-images/items/sword.png";
  const BowImage = "/board-images/items/bow.png";
  const SpearImage = "/board-images/items/spear.png";
  const HealImage = "/board-images/items/heal.png";
  const PoisonImage = "/board-images/items/poison.png";
  const ForceImage = "/board-images/items/force.png";

  const renderContent = () => {
    switch (state) {
      case '  ':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
          </div>
        );
      case 'border-r':
        return (
          <div className='board-border-r'>
            <img src={BorderRImage} alt="Right Border Tile" />
          </div>
        );
      case 'border-l':
        return (
          <div className='board-border-l'>
            <img src={BorderLImage} alt="Left Border Tile" />
          </div>
        );
      case 'border-u':
        return (
          <div className='board-border-u'>
            <img src={BorderUImage} alt="Upper Border Tile" />
          </div>
        );
      case 'border-d':
        return (
          <div className='board-border-d'>
            <img src={BorderDImage} alt="Down Border Tile" />
          </div>
        );
      case 'border-dl':
        return (
          <div className='board-border-dl'>
            <img src={BorderDLImage} alt="Down Left Border Tile" />
          </div>
        );
      case 'border-dr':
        return (
          <div className='board-border-dr'>
            <img src={BorderDRImage} alt="Down Right Border Tile" />
          </div>
        );
      case 'border-ul':
        return (
          <div className='board-border-ul'>
            <img src={BorderULImage} alt="Upper Left Border Tile" />
          </div>
        );
      case 'border-ur':
        return (
          <div className='board-border-ur'>
            <img src={BorderURImage} alt="Upper Right Border Tile" />
          </div>
        );
      case 'water':
        return (
          <div className='board-water'>
            <img src={WaterImage} alt="Water Tile" />
          </div>
        );
      case 't0':
      case 'a0':
      case 'b0':
      case 'c0':
      case 'd0':
      case 'e0':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-tribute'>
              <div className='pointer'><img src={Pointer} alt='Pointer' /></div>
              <img src={renderTributeImage(selectedCharacter)} alt="Tribute 0 Tile" />
            </div>
          </div>
        );
      case 't1':
      case 'a1':
      case 'b1':
      case 'c1':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-tribute'>
              <img src={Tribute1Walk1} alt="Tribute 1 Tile" />
            </div>
          </div>
        );
      case 't2':
      case 'a2':
      case 'b2':
      case 'c2':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-tribute'>
              <img src={Tribute2Walk1} alt="Tribute 2 Tile" />
            </div>
          </div>
        );
      case 't3':
      case 'a3':
      case 'b3':
      case 'c3':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-tribute'>
              <img src={Tribute3Walk1} alt="Tribute 3 Tile" />
            </div>
          </div>
        );
      case 't4':
      case 'a4':
      case 'b4':
      case 'c4':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-tribute'>
              <img src={Tribute4Walk1} alt="Tribute 4 Tile" />
            </div>
          </div>
        );
      case 't5':
      case 'a5':
      case 'b5':
      case 'c5':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-tribute'>
              <img src={Tribute5Walk1} alt="Tribute 5 Tile" />
            </div>
          </div>
        );
      case 'n0':
      case 'n1':
      case 'n2':
      case 'n3':
      case 'n4':
      case 'n5':
      case 'n6':
      case 'n7':
      case 'n8':
      case 'n9':
      return (
        <div className='board-free'>
          <img src={GrassImage} alt="Free Tile" />
          <div className='board-tribute-n'>
            <img src={TributeNWalk1} alt="Neutral Tribute Tile" />
          </div>
        </div>
      );
      case 'pl':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-potion'>
              <img src={HealImage} alt="Life Potion Tile" />
            </div>
          </div>
        );
      case 'po':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-potion'>
              <img src={PoisonImage} alt="Poison Potion Tile" />
            </div>
          </div>
        );
      case 'pf':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-potion'>
              <img src={ForceImage} alt="Force Potion Tile" />
            </div>
          </div>
        );
      case 'sw':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-sword'>
              <img src={SwordImage} alt="Sword Tile" />
            </div>
          </div>
        );
      case 'sp':
        return (
          <div className='board-free'>
            <img src={GrassImage} alt="Free Tile" />
            <div className='board-spear'>
              <img src={SpearImage} alt="Spear Tile" />
            </div>
          </div>
        );
      case 'wo':
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
    <div className={`cell ${state}`}>
      {renderContent()}
    </div>
  );
};

export default Cell;
