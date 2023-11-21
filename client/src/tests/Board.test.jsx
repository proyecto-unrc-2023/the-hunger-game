import React from "react";
import { render } from "@testing-library/react";
import Board from "../components/Board.jsx";
import Cell from "../components/Cell.jsx"

// Mock de un contexto necesario para renderizar el board
jest.mock("../components/GameContext.jsx", () => ({
  __esModule: true,
  useGame: () => ({
    characters: [
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

describe ("Board component", () => {

  const boardSize = 20;
  const emptyBoard = Array.from({ length: boardSize }, () => Array(boardSize).fill('  '));

  it("should render an empty board", () => {
    const { container } = render(<Board size={boardSize} boardState={emptyBoard} />);
    const board = container.querySelector(".board-render");
    const row = board.querySelector(".row");
    const cell = row.querySelector(".cell");
    const water = container.querySelector(".board-water");
    const grass = container.querySelectorAll(".board-free");
    const border = container.querySelector("border")
    expect(board).toBeInTheDocument();
    expect(row).toBeInTheDocument();
    expect(cell).toBeInTheDocument();
    expect(water).toBeInTheDocument();
    expect(grass).toHaveLength(boardSize*boardSize);
  });

})