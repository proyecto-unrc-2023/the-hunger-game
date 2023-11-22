import React, {useEffect} from 'react';
import { useGame } from "./GameContext";

const Tribute0Walk1 = "/board-images/characters/CH1.png";
const Tribute1Walk1 = "/board-images/characters/CH2.png";
const Tribute2Walk1 = "/board-images/characters/CH3.png";
const Tribute3Walk1 = "/board-images/characters/CH4.png";
const Tribute4Walk1 = "/board-images/characters/CH5.png";
const Tribute5Walk1 = "/board-images/characters/CH6.png";
const TributeNWalk1 = "/board-images/characters/N.png";

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
