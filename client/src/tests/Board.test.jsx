import React from "react";
import { render } from "@testing-library/react";
import Board from "../components/Board.jsx";
import Cell from "../components/Cell.jsx"

// Mock de un contexto necesario para renderizar el board
jest.mock("../components/GameContext.jsx", () => ({
  __esModule: true,
  useGame: () => ({
    characters: [
      "/board-images/characters/CH1.png",
      "/board-images/characters/CH2.png",
      "/board-images/characters/CH3.png",
      "/board-images/characters/CH4.png",
      "/board-images/characters/CH5.png",
      "/board-images/characters/CH6.png",
      "/board-images/characters/N.png",
    ],
  }),
}));

describe ("Board component", () => {

  const boardSize = 20;

  const emptyBoard = Array.from({ length: boardSize }, () => Array(boardSize).fill('  '));

  const boardState = Array.from({ length: boardSize }, () => Array(boardSize).fill('  '));
  boardState[4][4] = 't0';
  boardState[9][17] = 't1';
  boardState[19][1] = 't2';
  boardState[8][8] = 't3';
  boardState[5][15] = 't4';
  boardState[1][15] = 'pl';
  boardState[7][13] = 'po';
  boardState[14][1] = 'pf';
  boardState[4][5] = 'sw';
  boardState[8][16] = 'sp';
  boardState[18][2] = 'wo';

  it("should render an empty board", () => {
    const { container } = render(<Board size={boardSize} boardState={emptyBoard} />);
    const board = container.querySelector(".board-render");
    const row = board.querySelector(".row");
    const cell = row.querySelector(".cell");
    const water = board.querySelector(".board-water");
    const grass = board.querySelectorAll(".board-free");
    expect(board).toBeInTheDocument();
    expect(row).toBeInTheDocument();
    expect(cell).toBeInTheDocument();
    expect(water).toBeInTheDocument();
    expect(grass).toHaveLength(boardSize*boardSize);
  });

  it("should render a board", () => {
    const { container } = render(<Board size={boardSize} boardState={boardState} />);
    const board = container.querySelector(".board-render");
    const tribute = board.querySelectorAll(".board-tribute");
    const potion = board.querySelectorAll(".board-potion");
    const sword = board.querySelector(".board-sword");
    const spear = board.querySelector(".board-spear");
    const bow = board.querySelector(".board-bow");
    expect(board).toBeInTheDocument();
    expect(tribute).toHaveLength(5);
    expect(potion).toHaveLength(3);
    expect(sword).toBeInTheDocument();
    expect(spear).toBeInTheDocument();
    expect(bow).toBeInTheDocument();
  });

})