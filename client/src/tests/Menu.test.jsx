import React from "react";
import { render } from "@testing-library/react";
import { Menu } from "../components/Menu.jsx";

// Mock del contexto, esto es necesario para crear un menu
jest.mock("../components/GameContext.jsx", () => ({
  __esModule: true,
  useGame: () => ({
    selectedCharacter: 0,
    charactersOrdered: ["/board-images/characters/Minotaur_Walking_1.png", 
                        "/board-images/characters/Fallen_Angels_Walking_1.png",
                        "/board-images/characters/Golem_Walking_1.png",
                        "/board-images/characters/Goblin_Walking_1.png",
                        "/board-images/characters/Orc_Walking_1.png",
                        "/board-images/characters/Reaper_Man_Walking_1.png",
                        "/board-images/characters/Fallen_Angels_Walking_2.png"],
  }),
}));

describe("Menu component", () => {

  it('should render a menu', () => {
    const { container } = render(<Menu onViewChange={'menu'} />);
    const menu = container.querySelector(".menu-container");
    const charactersBar = container.querySelector(".choose-character-container")
    const incrementableBars = container.querySelector(".bars-container");
    expect(menu).toBeInTheDocument();
    expect(incrementableBars).toBeInTheDocument();
    expect(charactersBar).toBeInTheDocument(); 
  });


});
