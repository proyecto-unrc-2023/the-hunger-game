import React from "react";
import { render, fireEvent, screen, act } from "@testing-library/react";
import { Menu } from "../components/Menu.jsx";

// Mock de un contexto necesario para renderizar el menu
jest.mock("../components/GameContext.jsx", () => ({
  __esModule: true,
  useGame: () => ({
    selectedCharacter: 0,
    charactersOrdered: [
      "/board-images/characters/Minotaur_Walking_1.png",
      "/board-images/characters/Fallen_Angels_Walking_1.png",
      "/board-images/characters/Golem_Walking_1.png",
      "/board-images/characters/Goblin_Walking_1.png",
      "/board-images/characters/Orc_Walking_1.png",
      "/board-images/characters/Reaper_Man_Walking_1.png",
      "/board-images/characters/Fallen_Angels_Walking_2.png",
    ],
  }),
}));

global.fetch = jest.fn(); // Para hacer el fetch usamos funciones proporcionadas por jest

describe("Menu component", () => {

  beforeEach(() => {
    // CREO que simula una solicitud 
    fetch.mockResolvedValue({
      json: async () => ({
        alliance: 3,
        cant_tributes: 4,
        cowardice: 0,
        force: 5,
        life: 50,
      }),
    });
  });

  it("should render a menu", () => {
    const { container } = render(<Menu onViewChange={"menu"} />);
    const menu = container.querySelector(".menu-container");
    const charactersBar = container.querySelector(".choose-character-container");
    const incrementableBars = container.querySelector(".bars-container");
    expect(menu).toBeInTheDocument();
    expect(incrementableBars).toBeInTheDocument();
    expect(charactersBar).toBeInTheDocument();
  });

  it("should increment 'Life' stat correctly", async () => {
    await act(async () => {
      render(<Menu onViewChange={"menu"} />);
    });

    const lifeBar = screen.getByText("Life:", { selector: ".incrementable-bar-atribute" }).closest(".incrementable-bars");
    const initialLifeValue = lifeBar.querySelector(".incrementable-value .value-stat").textContent;
    console.log("Valor inicial: " + initialLifeValue);
  
    fireEvent.click(lifeBar.querySelector(".incrementable-value .increment-button"));
  
    const updatedLifeValue = lifeBar.querySelector(".incrementable-value .value-stat").textContent;
    console.log("Valor incrementado: " + updatedLifeValue);
    
    expect(Number(updatedLifeValue)).toBeGreaterThan(Number(initialLifeValue));
      
  });

  it("shouldn't decrement 'Life' stat with the initial value", async () => {
    await act(async () => {
      render(<Menu onViewChange={"menu"} />);
    });

    const lifeBar = screen.getByText("Life:", { selector: ".incrementable-bar-atribute" }).closest(".incrementable-bars");
    const initialLifeValue = lifeBar.querySelector(".incrementable-value .value-stat").textContent;
    console.log("Valor inicial: " + initialLifeValue);
  
    fireEvent.click(lifeBar.querySelector(".incrementable-value .decrement-button"));
  
    const updatedLifeValue = lifeBar.querySelector(".incrementable-value .value-stat").textContent;
    console.log("Valor decrementado: " + updatedLifeValue);

    expect(Number(updatedLifeValue)).toBe(Number(initialLifeValue));
      
  });

  it("should decrement 'Life' stat correctly", async () => {
    await act(async () => {
      render(<Menu onViewChange={"menu"} />);
    });

    const lifeBar = screen.getByText("Life:", { selector: ".incrementable-bar-atribute" }).closest(".incrementable-bars");
  
    fireEvent.click(lifeBar.querySelector(".incrementable-value .increment-button"));
    const initialLifeValue = lifeBar.querySelector(".incrementable-value .value-stat").textContent;
    console.log("Valor inicial: " + initialLifeValue);

    fireEvent.click(lifeBar.querySelector(".incrementable-value .decrement-button"));
    const updatedLifeValue = lifeBar.querySelector(".incrementable-value .value-stat").textContent;
    console.log("Valor decrementado: " + updatedLifeValue);

    expect(Number(updatedLifeValue)).toBeLessThan(Number(initialLifeValue));
      
  });

});
