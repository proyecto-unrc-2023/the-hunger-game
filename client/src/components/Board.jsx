// Board.js
import React from "react";
import "./Board.css";
import { Square } from './Square.jsx'
import Cell from './Cell';

const Board = ({ size, boardState }) => {
  const renderBoard = () => {
    return boardState.map((row, rowIndex) => (
      <div key={rowIndex} className="row">
        {row.map((cellState, columnIndex) => (
          <Cell key={`${rowIndex}-${columnIndex}`} state={cellState} />
        ))}
      </div>
    ));
  };

  return (
    <div className="board">
      {renderBoard()}
    </div>
  );
};
export default Board;
