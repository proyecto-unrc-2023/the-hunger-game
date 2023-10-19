import React from "react";
import "./Board.css";
import Cell from './Cell';

const Board = ({ size, boardState, onCellClick}) => {
  const renderBoard = () => {
    return boardState.map((row, rowIndex) => (
      <div key={rowIndex} className="row">
        {row.map((cellState, columnIndex) => (
          <Cell
            key={`${rowIndex}-${columnIndex}`}
            state={cellState}
            onClick={() => onCellClick(rowIndex, columnIndex)}
          />
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
