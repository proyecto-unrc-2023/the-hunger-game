import React, {useEffect} from 'react';
import { useGame } from "./GameContext";

const Tribute0Walk1 = "/board-images/characters/Minotaur_Walking_1.png";
// const Tribute0Walk2 = "/board-images/characters/female_adventurer_walk2.png";
// const Tribute0HoldBow = "/board-images/characters/female_adventurer_hold_bow.png";
// const Tribute0HoldSword = "/board-images/characters/female_adventurer_hold_sword.png";
const Tribute1Walk1 = "/board-images/characters/Fallen_Angels_Walking_1.png";
// const Tribute1Walk2 = "/board-images/characters/male_adventurer_walk2.png";
// const Tribute1HoldBow = "/board-images/characters/male_adventurer_hold_bow.png";
// const Tribute1HoldSword = "/board-images/characters/male_adventurer_hold_sword.png";
const Tribute2Walk1 = "/board-images/characters/Golem_Walking_1.png";
// const Tribute2Walk2 = "/board-images/characters/female_person_walk2.png";
// const Tribute2HoldBow = "/board-images/characters/female_person_hold_bow.png";
// const Tribute2HoldSword = "/board-images/characters/female_person_hold_sword.png";
const Tribute3Walk1 = "/board-images/characters/Goblin_Walking_1.png";
// const Tribute3Walk2 = "/board-images/characters/male_person_walk2.png";
// const Tribute3HoldBow = "/board-images/characters/male_person_hold_bow.png";
// const Tribute3HoldSword = "/board-images/characters/male_person_hold_sword.png";
const Tribute4Walk1 = "/board-images/characters/Orc_Walking_1.png";
// const Tribute4Walk2 = "/board-images/characters/robot_walk2.png";
// const Tribute4HoldBow = "/board-images/characters/robot_hold_bow.png";
// const Tribute4HoldSword = "/board-images/characters/robot_hold_sword.png";
const Tribute5Walk1 = "/board-images/characters/Reaper_Man_Walking_1.png";
// const Tribute5Walk2 = "/board-images/characters/zombie_walk2.png";
// const Tribute5HoldBow = "/board-images/characters/zombie_hold_bow.png";
// const Tribute5HoldSword = "/board-images/characters/zombie_hold_sword.png";
const TributeNWalk1 = "/board-images/characters/Fallen_Angels_Walking_2.png";
// const TributeNWalk2 = "/board-images/characters/neutral_walk2.png";
// const TributeNHoldBow = "/board-images/characters/neutral_hold_bow.png";
// const TributeNHoldSword = "/board-images/characters/neutral_hold_sword.png";

const CharacterImages = [
    Tribute0Walk1,
    Tribute1Walk1,
    Tribute2Walk1,
    Tribute3Walk1,
    Tribute4Walk1,
    Tribute5Walk1
]
const renderTributeImage = (selectedTribute, characters) => {  
    const result = [];
    for (let i = 0; i < characters.length; i++) {
      result.push(characters[(parseInt(selectedTribute) + i) % characters.length]);
    }
    return result;
  };

const Characters = () => {
    const { selectedCharacter, setCharacters, setNeutralCharacter, setCharactersOrdered} = useGame();
  
    useEffect(() => {
      const tributeImages = renderTributeImage(selectedCharacter, CharacterImages)
      setCharacters(tributeImages);
      setNeutralCharacter(TributeNWalk1);
      setCharactersOrdered(CharacterImages);
    }, [selectedCharacter, setCharacters, setNeutralCharacter, setCharactersOrdered]);
  
    // No necesitas renderizar nada en este componente, ya que su propósito es actualizar el contexto.
    return null;
  };

export default Characters;
